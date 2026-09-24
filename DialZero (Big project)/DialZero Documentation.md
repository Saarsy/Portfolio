# Contents
- [The Problem](#the-problem--why-i-built-it)
- [What It Does](#what-it-does)
- [Technical Overview](#technical-overview)
- [The Hard Parts](#the-hard-parts)
- [Results](#Results)
- [Whats Next](#Whats-Next)

![Poster](/DialZero%20(Big%20project)/Images/Poster%20Hero%20Shot.jpeg)

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
# Technical Overview
Now, for the one of the hard parts. Actually, thinking about how it's gonna work. I opened my closet and took out a box with a lot of sensors and microchips. In there I stumbled across:
- Encoder
- Touch sensor
- RP2040-zero (Microchip)
- RGB LED (Visual feedback)

Visualizing it, I could see a design that incorporated the touch sensor and encoder to make combinations that could make me achieve the list of things that I wanted it to do. I mapped out my thoughts and assigned a combination for the things on my list.
- Encoder spin = Volume control
- Touch + Encoder spin = skip through song tracks
- Encoder press = Pause/Play volume
- Double touch = RGB LED on/off

![Poster](/DialZero%20(Big%20project)/Images/Wiring.jpeg)


# The Hard Parts 
## Linking DialZero with Home Assistant
After a while of using it, I knew that it could do more. I had three more combinations:
- Touch + Encoder press
- Encoder press and hold
- Encoder double press

So after thinking about it for a while, I thought of an idea: What if I link the DialZero to my smart home? This was my biggest breakthrough yet. I already had a home server running Home Assistant, which had all my smart devices, and it would make controlling the lights and other smart home things seamless for me. So first I searched it up, if it was even possible, and Google said that it was in fact possible. Doing more research, I found that I could have the DialZero output special keys that weren't found on a normal keyboard, like F13, F14 and F15, after it output this, I could have Apple Shortcuts read these special keys and send messages to my Home Assistant app on my Mac. This allowed me to use those three combinations on the DialZero that I had left to control my smart home, and to this day I use these every day.

![Poster](/DialZero%20(Big%20project)/Images/SS1.jpeg)![Poster](/DialZero%20(Big%20project)/Images/SS2.jpeg)

## The Design
I probably spent the most time on this, as I wanted it to look really clean and modern, just fitting on my desk along with my keyboard and mouse. I wanted something minimalistic but also functional. After brainstorming for a while, I landed on a circular design: the middle of the circle would have the encoder with a textured knob, giving it a high-quality feel, and the side would have a textured place that reveals the location of the touch sensor, so you could use the touch sensor without looking. In the front would be an RGB LED that responds to whatever you do.
![Poster](/DialZero%20(Big%20project)/Images/Drawing.jpeg)

## Code / Customer Config
After designing it, I knew that I wanted to sell this as a product on Etsy, so I needed to make this as customer-friendly as possible. So I experimented with Vial and QMK configurations, but in the end I wasn't able to do these. Next, I tried to create a website on GitHub that could be opened on any browser and could easily configure the DialZero to whatever the user wanted. But mysteriously, it only worked every second time you plugged in DialZero, which was really frustrating and after spending a few hours on it, I knew that it wasn't gonna work out. I resorted to a CircuitPython script that could be edited by the customer. This was extremely time consuming, as I had to put support for Windows and Mac and make shortcuts so that the customer could easily set their DialZero to do whatever they wanted it to. Code file that I ended up on: [DialZero.py](/DialZero%20(Big%20project)/DialZero.py)

# Results
I had a working product that could control all my media, and using it was as seamless as clicking space bar on your keyboard between every word. 

I also had a strong Etsy listing that I have just recently made and already had a custom order for DialZero. On my Etsy shop, looking at the stats, I see that this product gets the most views too averaging around 30 per week.
Link to listing: https://makrix.etsy.com/listing/4556098632

![Poster](/DialZero%20(Big%20project)/Images/SS3.jpeg)

# What's Next
- Vial/QMK for easier config
- Another touch sensor for even more combinations 
- Grow my sales for this product
