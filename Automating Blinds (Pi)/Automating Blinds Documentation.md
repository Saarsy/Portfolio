# Contents
- [The Problem](#the-problem--why-i-built-it)
- [What It Does](#what-it-does)
- [Technical Overview](#technical-overview)
- [The Hard Parts](#the-hard-parts)
- [Results](#results)
- [What's Next](#what's-next)
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

![Poster](/Automating%20Blinds%20(Pi)/Image/Tech.jpeg)

# The Hard Parts 
## CADing The Design
This was the steepest learning curve for me, as I had to design and make gears that would work for my blinds. The concept of a gear is simple for me, but actually creating it and learning about the different variables that are needed to create a gear was the harder part for me. Eventually, I settled on a gear generator and generated some gears that fit perfectly (in around 7 tries). All the rest of the housing was easy as it was basic CAD. 

![Poster](/Automating%20Blinds%20(Pi)/Image/Mech.jpeg)

## Code
After designing, printing, and fitting it to my blinds, I came to the daunting task of figuring out how to code it so it seamlessly worked every day. I used Claude to generate the base code for me, then I tried to understand it at a high level so I at least knew what was going on. After I understood most of the code, I sent it out to the Raspberry Pi and Arduino. One thing I still haven't gotten to is the fact that whenever the Raspberry Pi restarts, the digital port somehow changes for the Arduino. For example, the Arduino was first found at /dev/ttyACM1 on the Pi, but after it restarted, the Arduino was found at /dev/ttyACM2 on the Pi. Even with this minor problem, the code was working! You can see the code in here: [Arduino Code](/Automating%20Blinds%20(Pi)/Code/Arduino_code.cpp) - [Raspberry Pi Code](/Automating%20Blinds%20(Pi)/Code/Pi_code.py)
# Results
The results were amazing! Even though it took around 40 seconds to fully open the blinds, and it made a decent amount of noise, it still felt like magic that when I woke up the blinds were open and when I went to sleep they were already closed. Now I could peacefully and naturally wake up to the beautiful sunrise sky.
# What's Next
- Increase motor quality for improved speed
- Include rotary encoder for more precise movements
- Make wires less visible
- Make housing smaller for aesthetics
