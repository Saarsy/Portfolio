import serial
import time
import threading
import requests

# --- CONFIG ---
ARDUINO_PORT = '/dev/ttyACM2'
BAUD = 9600
HA_URL = "http://192.168.1.43:8123"
HA_TOKEN = "long lived token put here"
BLIND_TRAVEL_TIME = 48

# State tracking
is_running_command = False
blind_state = "unknown"

HEADERS = {
    "Authorization": f"Bearer {HA_TOKEN}",
    "Content-Type": "application/json"
}

def send_ha_state(state):
    try:
        requests.post(
            f"{HA_URL}/api/states/sensor.blinds_state",
            headers=HEADERS,
            json={
                "state": state,
                "attributes": {"friendly_name": "Blinds State"}
            },
            timeout=5
        )
        print(f"[HA] Blinds state updated: {state}")
    except Exception as e:
        print(f"[HA] Failed: {e}")

def get_last_triggered(entity_id):
    """Get the last triggered timestamp of a button."""
    try:
        res = requests.get(
            f"{HA_URL}/api/states/{entity_id}",
            headers=HEADERS,
            timeout=5
        )
        if res.status_code == 200:
            return res.json().get("state", "")
    except Exception as e:
        print(f"[HA] Error getting {entity_id}: {e}")
    return ""

def run_blind(ser, direction):
    global is_running_command, blind_state

    # Block if already in that position
    if direction == "open" and blind_state == "open":
        print("[BLIND] Already open, ignoring.")
        is_running_command = False
        return
    if direction == "close" and blind_state == "closed":
        print("[BLIND] Already closed, ignoring.")
        is_running_command = False
        return

    is_running_command = True

    if direction == "open":
        print("[BLIND] Opening...")
        send_ha_state("opening")
        ser.write(b'O')
        time.sleep(BLIND_TRAVEL_TIME)
        ser.write(b'S')
        blind_state = "open"
        send_ha_state("open")
        print("[BLIND] Fully open.")

    elif direction == "close":
        print("[BLIND] Closing...")
        send_ha_state("closing")
        ser.write(b'C')
        time.sleep(BLIND_TRAVEL_TIME)
        ser.write(b'S')
        blind_state = "closed"
        send_ha_state("closed")
        print("[BLIND] Fully closed.")

    is_running_command = False

def poll_ha(ser):
    global is_running_command

    # Get initial timestamps on startup to avoid triggering old presses
    last_open_ts = get_last_triggered("input_button.open_blinds")
    last_close_ts = get_last_triggered("input_button.close_blinds")

    print("[HA] Polling for blind commands...")
    while True:
        try:
            open_ts = get_last_triggered("input_button.open_blinds")
            close_ts = get_last_triggered("input_button.close_blinds")

            if not is_running_command:
                if open_ts and open_ts != last_open_ts:
                    last_open_ts = open_ts
                    last_close_ts = close_ts  # Flush close presses too
                    threading.Thread(
                        target=run_blind,
                        args=(ser, "open"),
                        daemon=True
                    ).start()

                elif close_ts and close_ts != last_close_ts:
                    last_close_ts = close_ts
                    last_open_ts = open_ts  # Flush open presses too
                    threading.Thread(
                        target=run_blind,
                        args=(ser, "close"),
                        daemon=True
                    ).start()
            else:
                # While running, flush all presses so they don't queue up
                last_open_ts = open_ts
                last_close_ts = close_ts

        except Exception as e:
            print(f"[HA] Poll error: {e}")

        time.sleep(2)

def main():
    print("[SERIAL] Connecting to Arduino...")
    try:
        ser = serial.Serial(ARDUINO_PORT, BAUD, timeout=1)
        time.sleep(2)
        ser.reset_input_buffer()
        print(f"[SERIAL] Connected on {ARDUINO_PORT}")
    except Exception as e:
        print(f"[ERROR] Serial: {e}")
        return

    send_ha_state("unknown")
    poll_ha(ser)

if __name__ == "__main__":
    main()
