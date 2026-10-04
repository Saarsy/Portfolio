# Contents
- [What Is HA](#What-Is-Home-Assistant-(HA))
- [iPad Integration](#iPad-Integration)
- [The Hard Parts](#the-hard-parts)
- [Results](#Results)
# What Is Home Assistant (HA)
Home Assistant, abbreviated to HA is a self-hosted software that allows you to connect all your smart devices to one place. Here are its advantages:
- Usually, the average person has an app for Feit Electric, one for Wiz, one for Govee, etc., but with HA you can have all of those smart devices in one place. This allows the smart devices to rely on each other and can make your "Smart home” actually smart.
- You have way more control. Most manufacturers actually don't even use all the things that your Smart device can do; HA makes it so that there are no hidden features, just pure functionality. 
- The UI is smooth, organized, and highly customizable.
- All the bullet points above also mean it can execute HIGHLY complex and specific tasks. For example, "If my calendar shows a meeting before 8am tomorrow, and the temperature overnight outside drops below 30F, then turn on my electric car charger (So it preconditions), but only if the car is plugged in and is below 80% battery level." No other software could even compare to HA's functionality.

It basically has no disadvantages aside from the fact that it requires time to set up and program.
# iPad Integration
With so many devices came a problem of how to control all of them. Of course, you could just open Home Assistant on your phone, but that was way too inconvenient, especially when I had a slightly cracked iPad lying around.

When thinking about this idea, I knew that I needed to mount it to the wall, so I CADed some 2-piece mounts to mount this iPad to the wall and printed them out, and they fit on the first try! I configured the iPad to stay on 24/7 at 70% brightness and stay on the Home Assistant app, so now there’s an iPad on top of my main living room switches, to control my smart home quickly.

![Poster](/Home%20Server%20(Big%20Project)/Images/Front%20iPad.jpeg)
![Poster](/Home%20Server%20(Big%20Project)/Images/SS7.png)
# The Hard Parts 
This was supposed to be a quick project but turned out to be the single biggest thing I use the home server for, with this came hard parts (those I can remember at least): 
## Feit Electric
Now mostly all devices were supported by HA, but the ones that weren't were harder to add than the others. For example, Feit Electric wasn't supported fully by the Feit Electric app, so to add the smart plug I had to first connect it via Tuya Smart or Smart Life on my phone and then use some developer mode on one of them to connect them to HA.
## NFC Tags
So I had a control center in the middle of my living room, but what if I wanted to control my lights from my room? Here is where NFC tags come in handy; these allow me to just tap my phone on the tag and activate whatever automation I want. One tag can close my blinds, one can turn off all the lights, one can set the volume of the tv to a low level. These still required a phone but were way faster as you only had to tap your phone to the NFC tag and it executed the automation rather than opening the app and then running the automation; over time, this makes the smart home experience more seamless.

![Poster](/Home%20Server%20(Big%20Project)/Images/NFC.jpeg)
## Connecting to Immich outside of home network
I have a separate section to how I made it so that I could access the home server outside of my local network: [Taiscale Setup](/Home%20Server%20(Big%20Project)/Tailscale%20Setup.md)
## Raspberry Pi
Since these are big topics in which I also did a lot of work on (automated my blinds and door), I have separate documentations for them too: [Automating Blinds](/Automating%20Blinds%20(Pi)/Automating%20Blinds%20Documentation.md) - [Door Sentry](/Door%20Sentry%20(Pi)/Door%20Sentry%20Documentation.md)
# Results
Home Assistant was now the center of my whole home, It was the single thing that kept all my smart devices alive, honestly this has grown to be so important that I cant even imagine how much more I would have to do manually if HA even stopped for one day. 

![Poster](/Home%20Server%20(Big%20Project)/Images/SS8.jpeg)
