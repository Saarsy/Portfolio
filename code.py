# ==========================================
# 🛠️ DIALZERO CUSTOMER CONFIGURATION 🛠️
# ==========================================
# Just type what you want in plain text! Use a plus sign (+) for combos.
# Note: Double-tapping the touch sensor is hardcoded to toggle the RGB lights.
# FULL DICTIONARY DOWN AROUND LINE 50
# REMEMBER TO HIT ctrl + s / cmd + s TO SAVE 

# --- 1. KNOB SPIN RIGHT ---
SPIN_RIGHT = "vol up"
# --- 2. KNOB SPIN LEFT ---
SPIN_LEFT = "vol down"

# --- 3. KNOB SPIN RIGHT + SIDE TOUCH ---
SPIN_RIGHT_TOUCH = "next"
# --- 3. KNOB SPIN LEFT + SIDE TOUCH ---
SPIN_LEFT_TOUCH = "prev"

# --- 4. KNOB PUSH ---
KNOB_PUSH = "play"

# --- 5. DOUBLE KNOB PUSH ---
DOUBLE_KNOB_PUSH = "" 

# --- 6. TOUCH + KNOB PUSH ---
TOUCH_KNOB_PUSH = "mute" 

# --- 7. HOLD KNOB ---
KNOB_HOLD = "esc"         
KNOB_HOLD_TIME = 0.5     # Seconds to hold before it triggers


# ==========================================
# 🎨 RGB LED CONFIGURATION (GP2, GP3, GP4)
# ==========================================
BASE_COLOR  = (0, 0, 255) # Default resting color (Blue)
FLASH_COLOR = (255, 255, 255)  # Flash color on press (White)
BRIGHTNESS  = 0.3              # Brightness limit (0.1 = dim, 1.0 = BRIGHT)

# Red          = (255, 0, 0)
# Green        = (0, 255, 0)
# Blue         = (0, 0, 255)
# White        = (255, 200, 255)
# Black / Off  = (0, 0, 0)
# Yellow       = (255, 40, 0)
# Cyan / Teal  = (0, 255, 255)
# Orange       = (255, 10, 0)
# Purple       = (128, 0, 128)
#
# ==========================================
# 📚 COMPLETE KEYCODE REFERENCE
# ==========================================
#
# REMEMBER TO HIT ctrl + s / cmd + s TO SAVE 
#
# EXAMPLES:
#   "a" → types 'a'
#   "shift + a" → types 'A'
#   "ctrl + c" → Copy
#   "ctrl + v" → Paste
#   "cmd + shift + 4" → Mac screenshot
#   "cmd + space" → Mac Spotlight
#   "f13" → F13 key (custom shortcuts in apps)
#   "alt + tab" → Switch windows (Windows)
#   "cmd + tab" → Switch apps (Mac)
#
# LETTERS: a-z (just type them)
# NUMBERS: 0-9 (just type them)
#
# MODIFIERS (use with +):
#   ctrl, control, shift, alt, option, cmd, command, win, windows, mac
#
# SPECIAL KEYS:
#   esc, escape, space, enter, return, backspace, tab, delete, insert,
#   home, end, page up, pageup, page down, pagedown
#
# ARROWS: up, down, left, right
#
# FUNCTION KEYS: f1-f24 (f1, f2, f3, ... f24)
#
# NUMPAD: numpad 0-9, numpad +, numpad -, numpad *, numpad /, numpad .
#
# SYMBOLS: [ ] { } ` - ; ' , . / \ = 
#
# MEDIA KEYS:
#   vol up, vol down, mute, play, play/pause, pause,
#   next, next track, prev, previous, prev track
#
# OTHER:
#   printscreen, prtsc, pause, scroll lock, num lock


























































































# ==========================================
# ⚙️ SYSTEM FIRMWARE (DO NOT EDIT BELOW)
# ==========================================
import time
import board
import digitalio
import rotaryio
import pwmio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode as K
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode as Media

kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

# PWM LED Setup
pwm_r = pwmio.PWMOut(board.GP2, frequency=5000, duty_cycle=0)
pwm_g = pwmio.PWMOut(board.GP3, frequency=5000, duty_cycle=0)
pwm_b = pwmio.PWMOut(board.GP4, frequency=5000, duty_cycle=0)

led_on = True

def set_rgb(color):
    if not led_on:
        pwm_r.duty_cycle = 0
        pwm_g.duty_cycle = 0
        pwm_b.duty_cycle = 0
        return
        
    r, g, b = color
    pwm_r.duty_cycle = int((r / 255.0) * BRIGHTNESS * 65535)
    pwm_g.duty_cycle = int((g / 255.0) * BRIGHTNESS * 65535)
    pwm_b.duty_cycle = int((b / 255.0) * BRIGHTNESS * 65535)

set_rgb(BASE_COLOR)

# Build the key map ONCE at startup (not every keypress) with correct
# Adafruit Keycode names. Wrapped so one bad entry can never crash the board.
KEY_MAP = {}
def _safe_add(name, keycode_attr):
    try:
        KEY_MAP[name] = getattr(K, keycode_attr)
    except AttributeError:
        print("WARNING: keycode", keycode_attr, "does not exist, skipping")

# Modifiers
_safe_add("ctrl", "CONTROL"); _safe_add("control", "CONTROL")
_safe_add("shift", "SHIFT")
_safe_add("alt", "ALT"); _safe_add("option", "ALT")
_safe_add("cmd", "GUI"); _safe_add("command", "GUI")
_safe_add("win", "GUI"); _safe_add("windows", "GUI"); _safe_add("mac", "GUI")

# Navigation & Editing
_safe_add("esc", "ESCAPE"); _safe_add("escape", "ESCAPE")
_safe_add("space", "SPACE")
_safe_add("enter", "ENTER"); _safe_add("return", "ENTER")
_safe_add("backspace", "BACKSPACE"); _safe_add("back", "BACKSPACE")
_safe_add("tab", "TAB")
_safe_add("delete", "DELETE"); _safe_add("del", "DELETE")
_safe_add("insert", "INSERT"); _safe_add("ins", "INSERT")
_safe_add("home", "HOME")
_safe_add("end", "END")
_safe_add("page up", "PAGE_UP"); _safe_add("pageup", "PAGE_UP")
_safe_add("page down", "PAGE_DOWN"); _safe_add("pagedown", "PAGE_DOWN")

# Arrows
_safe_add("up", "UP_ARROW")
_safe_add("down", "DOWN_ARROW")
_safe_add("left", "LEFT_ARROW")
_safe_add("right", "RIGHT_ARROW")

# Numpad
_safe_add("numpad 0", "KEYPAD_ZERO"); _safe_add("numpad 1", "KEYPAD_ONE")
_safe_add("numpad 2", "KEYPAD_TWO"); _safe_add("numpad 3", "KEYPAD_THREE")
_safe_add("numpad 4", "KEYPAD_FOUR"); _safe_add("numpad 5", "KEYPAD_FIVE")
_safe_add("numpad 6", "KEYPAD_SIX"); _safe_add("numpad 7", "KEYPAD_SEVEN")
_safe_add("numpad 8", "KEYPAD_EIGHT"); _safe_add("numpad 9", "KEYPAD_NINE")
_safe_add("numpad +", "KEYPAD_PLUS"); _safe_add("numpad -", "KEYPAD_MINUS")
_safe_add("numpad *", "KEYPAD_ASTERISK"); _safe_add("numpad /", "KEYPAD_FORWARD_SLASH")
_safe_add("numpad .", "KEYPAD_PERIOD"); _safe_add("numpad enter", "KEYPAD_ENTER")

# Symbols & Punctuation (verified against real Adafruit Keycode names)
_safe_add("[", "LEFT_BRACKET"); _safe_add("left bracket", "LEFT_BRACKET")
_safe_add("]", "RIGHT_BRACKET"); _safe_add("right bracket", "RIGHT_BRACKET")
_safe_add("`", "GRAVE_ACCENT"); _safe_add("backtick", "GRAVE_ACCENT"); _safe_add("tilde", "GRAVE_ACCENT"); _safe_add("~", "GRAVE_ACCENT")
_safe_add("=", "EQUALS"); _safe_add("equal", "EQUALS"); _safe_add("equals", "EQUALS")
_safe_add("-", "MINUS"); _safe_add("minus", "MINUS"); _safe_add("dash", "MINUS"); _safe_add("hyphen", "MINUS")
_safe_add(";", "SEMICOLON"); _safe_add("semicolon", "SEMICOLON")
_safe_add("'", "QUOTE"); _safe_add("quote", "QUOTE"); _safe_add("apostrophe", "QUOTE")
_safe_add(",", "COMMA"); _safe_add("comma", "COMMA")
_safe_add(".", "PERIOD"); _safe_add("period", "PERIOD"); _safe_add("dot", "PERIOD")
_safe_add("/", "FORWARD_SLASH"); _safe_add("slash", "FORWARD_SLASH"); _safe_add("forwardslash", "FORWARD_SLASH")
_safe_add("\\", "BACKSLASH"); _safe_add("backslash", "BACKSLASH")

# Function Keys F1-F24
for _i in range(1, 25):
    _safe_add("f" + str(_i), "F" + str(_i))

# System & Lock Keys
_safe_add("print", "PRINT_SCREEN"); _safe_add("printscreen", "PRINT_SCREEN"); _safe_add("prtsc", "PRINT_SCREEN")
_safe_add("pause", "PAUSE")
_safe_add("scroll lock", "SCROLL_LOCK"); _safe_add("scrolllock", "SCROLL_LOCK")
_safe_add("caps lock", "CAPS_LOCK"); _safe_add("capslock", "CAPS_LOCK")
_safe_add("num lock", "KEYPAD_NUMLOCK"); _safe_add("numlock", "KEYPAD_NUMLOCK")

def fire(action_str):
    """Parses plain text strings like 'shift + a' into Adafruit HID commands"""
    if not action_str: return
    
    set_rgb(FLASH_COLOR)
    
    action_str = action_str.lower().strip()
    
    # Media keys dictionary
    media_map = {
        "vol up": Media.VOLUME_INCREMENT,
        "vol down": Media.VOLUME_DECREMENT,
        "mute": Media.MUTE,
        "play": Media.PLAY_PAUSE,
        "play/pause": Media.PLAY_PAUSE,
        "pause": Media.PLAY_PAUSE,
        "next": Media.SCAN_NEXT_TRACK,
        "next track": Media.SCAN_NEXT_TRACK,
        "prev": Media.SCAN_PREVIOUS_TRACK,
        "previous": Media.SCAN_PREVIOUS_TRACK,
        "prev track": Media.SCAN_PREVIOUS_TRACK,
    }
    
    if action_str in media_map:
        cc.send(media_map[action_str])
    else:
        # Split by '+' and press all keys in the combo
        parts = [p.strip() for p in action_str.split('+')]
        keys_to_press = []
        
        for part in parts:
            if part in KEY_MAP:
                keys_to_press.append(KEY_MAP[part])
            else:
                try:
                    # Dynamically grab the key from Adafruit's Keycode list (e.g. "a" -> K.A)
                    keys_to_press.append(getattr(K, part.upper()))
                except AttributeError:
                    print("WARNING: unknown key '" + part + "' in config.py, ignoring")
                    
        if keys_to_press:
            try:
                kbd.press(*keys_to_press)
                kbd.release_all()
            except Exception as e:
                print("KEY PRESS ERROR:", e)
            
    time.sleep(0.05) 
    set_rgb(BASE_COLOR)

# Hardware Setup 
touch_pin = digitalio.DigitalInOut(board.GP0)
touch_pin.direction = digitalio.Direction.INPUT

btn_pin = digitalio.DigitalInOut(board.GP29)
btn_pin.direction = digitalio.Direction.INPUT
btn_pin.pull = digitalio.Pull.UP

encoder = rotaryio.IncrementalEncoder(board.GP27, board.GP28)

last_position = encoder.position
last_btn = True
last_click_time = 0
pending_click = False

last_touch = False
touch_time = 0
pending_touch = False

btn_press_time = 0
hold_triggered = False

while True:
    now = time.monotonic()
    is_touching = touch_pin.value

    # 1. ENCODER SPIN LOGIC
    current_position = encoder.position
    if current_position != last_position:
        diff = current_position - last_position
        if diff < 0: # Reversed
            fire(SPIN_RIGHT_TOUCH if is_touching else SPIN_RIGHT)
        elif diff > 0:
            fire(SPIN_LEFT_TOUCH if is_touching else SPIN_LEFT)
        last_position = current_position
        if is_touching: pending_touch = False

    # 2. ENCODER PUSH & HOLD LOGIC
    btn_pressed = not btn_pin.value
    if btn_pressed and not last_btn:
        btn_press_time = now
        hold_triggered = False
        
    if btn_pressed:
        if not hold_triggered and (now - btn_press_time >= KNOB_HOLD_TIME):
            fire(KNOB_HOLD)
            hold_triggered = True
            pending_click = False 
            if is_touching: pending_touch = False

    if not btn_pressed and last_btn:
        if not hold_triggered:
            if is_touching:
                fire(TOUCH_KNOB_PUSH)
                pending_click = False 
                pending_touch = False 
            else:
                if pending_click and (now - last_click_time < 0.4):
                    fire(DOUBLE_KNOB_PUSH)
                    pending_click = False
                else:
                    pending_click = True
                    last_click_time = now
        time.sleep(0.05) 
    last_btn = btn_pressed

    # 3. ENCODER SINGLE PRESS TIMEOUT
    if pending_click and (now - last_click_time > 0.4):
        fire(KNOB_PUSH)
        pending_click = False

    # 4. TOUCH LOGIC (Hardcoded to Toggle LED)
    if is_touching and not last_touch:
        if pending_touch and (now - touch_time < 0.4): 
            led_on = not led_on
            set_rgb(BASE_COLOR)
            pending_touch = False
        else:
            pending_touch = True
            touch_time = now
    last_touch = is_touching

    if pending_touch and not is_touching and (now - touch_time >= 0.4):
        pending_touch = False

    time.sleep(0.005)