# What It Is
The door century was is a experimental project that links the opening of my door to home assistant and my JBL speaker. 
# Why I Made It
I made this because of a few reasons:
- I wanted to experiment with the capabilities of my Raspberry Pi, RP2040–ZERO, and a rotary encoder
- I wanted to be alerted when someone entered my room, as my desk faced the opposite side of my door
- I wanted to prank my sibling, as I could connect my speaker to the door, and the speaker could play a loud sound. There were many other possibilities to this as well, like linking a water gun to the door, or connecting lights using automations in HA
# Design
## Mechanical
The first step to achieving this was the design. I had to make something mechanical that sensed the position of my door and sent it to a microcontroller. So after brainstorming for a while, I landed on an encoder based design. This would simply attach to the door hinge and sense the door angle in real time. Stability was a big issue for this, as my door opened and closed several times each day: I did not want this part to be constantly falling off, affecting the accuracy as well. To do this, I decided to leverage the door hinge and use it as a guide so that the encoder would stay centered where the door rotates. 
![Poster](/Door%20Sentry/Images/Close.jpeg)
![Poster](/Door%20Sentry/Images/Drawing.png)
## Technical
The technical part of this combines many aspects. The way this was gonna work was the rotary encoder sent a value to the RP2040-zero and that then sent another value to the Raspberry Pi, which then gave it to Home or Assistant or played something on the speaker, depending on the value the RP2040-zero gave. You may ask why I even included the RP2040-zero and I did that because the Raspberry Pi wasn't that great with receiving real-time information from the encoder as the RP2040-Zero did. It also provided nanosecond precision and made organization within the system neat.
![Poster](/Door%20Sentry/Images/RP2040%20Exposed.jpeg)
![Poster](/Door%20Sentry/Images/RP2040.jpeg)
![Poster](/Door%20Sentry/Images/Pi.jpeg)
# What's Next
- Connect my water gun to HA
- Facial Recognization?

![Poster](/Door%20Sentry/Images/SS.png)
![Poster](/Door%20Sentry/Images/Wide.jpeg)