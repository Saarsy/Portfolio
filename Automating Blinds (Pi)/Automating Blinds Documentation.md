# The Problem
# Contents
- [The Problem](#the-problem--why-i-built-it)
- [What It Does](#what-it-does)
- [Technical Overview](#technical-overview)
- [The Hard Parts](#the-hard-parts)
- [Results](#Results)
- [Whats Next](#Whats-Next)
# The Problem / Why I Built It
Every day, before going to sleep and after waking up, I always manually opened and closed the blinds. It was a simple thing to most people, but I was different. I saw how the blinds could be used, their potential. For example, every day when I have to wake up for school at 7, I always struggle to wake up. I’ve always naturally woken up to light, as I can’t sleep with even a little light in the room, so I knew that making my room light up right before I had to wake up would be a much more natural, gentler way to wake up. But how would I do this? Automating my lights to turn on at a certain time would be too bright and abrupt; when I finally woke up, I would be staring into the bright light, and it would be uncomfortable. The solution was natural light! By automating my blinds to open at a certain time, I could catch the natural light flooding into my room slowly, waking me up gently and nicely.
# What It Does
To achieve fully automated blinds, I had to use motors to mechanically open/close the blinds, and for accessibility also connect it to a brain (Home Assistant) that actually tells the blinds to open/close at the times selected.
# Technical Overview
For this projects I utilized materials I already had:
- Raspberry Pi 5
- Arduino Uno R3
- Arduino Uno Motor Shield
- N20 Gear Reduction Motor
- 3D Printed Gears and Housing

The way this was going to work in my mind was the Raspberry Pi 5 was going to receive the signal from HA and send a message to the Arduino Uno. The Arduino would then utilize the motor shield on it to send electrical current to the motors in the direction that was said in HA. I cannot do this without the motor shield because the Arduino alone can only send current in one way and cannot switch the direction without manual intervention.
# The Hard Parts 
## The Design
After a while of using it, I knew that it could do more. I had three more combinations:
- Touch + Encoder press
- Encoder press and hold
- Encoder double press

So after thinking about it for a while, I thought of an idea: What if I link the DialZero to my smart home? This was my biggest breakthrough yet. I already had a home server running Home Assistant, which had all my smart devices, and it would make controlling the lights and other smart home things seamless for me. So first I searched it up, if it was even possible, and Google said that it was in fact possible. Doing more research, I found that I could have the DialZero output special keys that weren't found on a normal keyboard, like F13, F14 and F15, after it output this, I could have Apple Shortcuts read these special keys and send messages to my Home Assistant app on my Mac. This allowed me to use those three combinations on the DialZero that I had left to control my smart home, and to this day I use these every day.
## The Design
I probably spent the most time on this, as I wanted it to look really clean and modern, just fitting on my desk along with my keyboard and mouse. I wanted something minimalistic but also functional. After brainstorming for a while, I landed on a circular design: the middle of the circle would have the encoder with a textured knob, giving it a high-quality feel, and the side would have a textured place that reveals the location of the touch sensor, so you could use the touch sensor without looking. In the front would be an RGB LED that responds to whatever you do.

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
