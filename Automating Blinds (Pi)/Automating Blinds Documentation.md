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
## CADing The Design
This was the steepest learning curve for me, as I had to design and make gears that would work for my blinds. The concept of a gear is simple for me, but actually creating it and learning about the different variables that are needed to create a gear was the harder part for me. Eventually, I settled on a gear generator and generated some gears that fit perfectly (in around 7 tries). All the rest of the housing was easy as it was basic CAD. 
## Code
After designing, printing, and fitting it to my blinds, I came with the daunting task of figuring out how to code it so it seamlessly worked. 

# Results
I had a working product that could control all my media, and using it was as seamless as clicking space bar on your keyboard between every word. 

I also had a strong Etsy listing that I have just recently made and already had a custom order for DialZero. On my Etsy shop, looking at the stats, I see that this product gets the most views too averaging around 30 per week.
Link to listing: https://makrix.etsy.com/listing/4556098632

![Poster](/DialZero%20(Big%20project)/Images/SS3.jpeg)

# What's Next
- Vial/QMK for easier config
- Another touch sensor for even more combinations 
- Grow my sales for this product
