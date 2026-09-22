# Contents - Medium Size Project
- [The Problem](#the-problem--why-i-built-it)
- [What It Does](#what-it-does)
- [The Hard Parts](#the-hard-parts)
- [Results](#Results)
- [Whats Next](#Whats-Next)



# The Problem / Why I Built It
Using a computer for many years, I found that the volume control was way too hard. I had to stretch my finger across the keyboard to press FN + F2 or F3, to control my volume. I realized it wasn't fast, and I just didn't like it. I knew I could make it more satisfying, more interactive, and way faster, so I could control the volume without thinking about it. That’s when it hit me: I had to design and create my own product that solves this issue I had, using the materials and tools I already had. After thinking about it, I realized that I could create a media controller that could control the volume, along with any media that I'm playing or watching.

# What It Does
After thinking about it for a while, I created a list of things I wanted it to do:
- Volume up and down
- Play/Pause media
- Swipe through songs

After finishing the build it had incorporated 3 more things tied to me:
- Turn on/off all the lights in my room
- Set my room to a colorful scene

# The Hard Parts 

## Linking DialZero with Home Assistant
After a while of using it, I knew that it could do more. I had three more combinations:
- Touch + Encoder press
- Encoder press and hold
- Encoder double press

So after thinking about it for a while, I thought of an idea: What if I link the DialZero to my smart home? This was my biggest breakthrough yet. I already had a home server running Home Assistant, which had all my smart devices, and it would make controlling the lights and other smart home things seamless for me. So first I searched it up, if it was even possible, and Google said that it was in fact possible. Doing more research, I found that I could have the DialZero output special keys that weren't found on a normal keyboard, like F13, F14 and F15, after it output this, I could have Apple Shortcuts read these special keys and send messages to my Home Assistant app on my Mac. This allowed me to use those three combinations on the DialZero that I had left to control my smart home, and to this day I use these every day.

## The Design
I probably spent the most time on this, as I wanted it to look really clean and modern, just fitting on my desk along with my keyboard and mouse. I wanted something minimalistic but also functional. After brainstorming for a while, I landed on a circular design: the middle of the circle would have the encoder with a textured knob, giving it a high-quality feel, and the side would have a textured place that reveals the location of the touch sensor, so you could use the touch sensor without looking. In the front would be an RGB LED that responds to whatever you do.

# Results
I had a working product that could control all my media, and using it was as seamless as clicking space bar on your keyboard between every word. 

I also had a strong Etsy listing that I have just recently made and already had a custom order for DialZero. On my Etsy shop, looking at the stats, I see that this product gets the most views too averaging around 30 per week.
Link to listing: https://makrix.etsy.com/listing/4556098632

# What's Next
- Vial/QMK for easier config
- Another touch sensor for even more combinations 
- Grow my sales for this product
