# What Is Tailscale
Tail scale is a virtual private network (VPN) that you can install and put on your devices. It links all the devices on it to a single private network. It basically allows for my phone to have a tunneled connection to my server outside my local home network, which is secure and fast. 
# How I Set It Up
My memory is still a little foggy, but here is what I can recall myself doing to set up Tailscale. I first signed into Tailscale using my Gmail account, and then linked it to my home server using terminal commands. After that, I also downloaded Tailscale on my phone and signed into my account, then I added that device to Tailscale as well. So now, using the home servers IP address in Tailscale, I could connect to Home Assistant and Immich from outside my local home network. For example:
- My home Immich address is: http://192.168.1.43:2283 (On my home network)
- My outside Immich address is: http://100.111.47.121:2283 (Using Tailscale outside)

# Results
I could now access whatever I put on my home server from anywhere in the world, with a fast and secure connection. 