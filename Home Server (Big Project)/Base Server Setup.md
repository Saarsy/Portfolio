# Contents
- [Why I Built It](#why-i-built-it)
- [What I Did](#what-i-did)
- [Learnings](#what-i-learned)
- [Results](#results)
- [What's Next](#what's-next)
# Why I Built It
Growing up, all my stuff revolved around the cloud, all my pictures, all my files, literally everything, and the price for those just kept going up. How much money would I allow myself and my family to spend on monthly subscriptions? I knew the answer to this: a home server. But I always hesitated to actually get started, as this was an entirely new field for me, in which I had no prior experience. But then, this was my time to build experience, so I took on the daunting task of researching and making a home server. This turned out to be a way bigger system of other apps and density than I initially thought it would be.
# What I Did
First, I had to pick what hardware to use and what platforms I was going to use to build this. After looking at YouTube videos, reading articles, and asking the Reddit community for suggestions, I had found the path I was going to take:
For the Hardware I was going to use:
- A old but capable windows laptop
- 2TB SSD
- 2TB HDD

![Poster](/Home%20Server%20(Big%20Project)/Images/Server.jpeg)

For the Software I was going to run:
- Ubuntu Server
- Casa OS
To code it Im going to use SSH so I can configure/program via my Mac

![Poster](/Home%20Server%20(Big%20Project)/Images/SS1.jpeg) ![Poster](/Home%20Server%20(Big%20Project)/Images/SS2.jpeg)

(Updated right after taking SS)

Why I chose them:
- The laptop has more then enough processing power to power my servers needs
- The 2TB SSD is the primary high speed storage
- The 2TB HDD is for backups that run weekly at night
- Ubuntu server was just what I found on many servers and what my researching concluded to
- Casa OS is a web based OS that can manage my apps and other stuff cleanly so my server stays organized, for me staying organized is one of the biggest things to understanding and succeeding
- SSH just allows me to sit at my main setup and cleanly configure/program my server
# What I Learned
## Take Your Time
This is the single thing I messed up on the most. I rushed through things and didn't fine-tune stuff, so later I had to redo stuff. Installing software and skipping over setup instructions led to  conflicts, messy file trees, and dependencies that had to be cleaned up later. When something is the foundation of something else, you have to take extra time to make it extra stable and workable. 
## Understanding How It Works
A key part of building a Home server for me was deeply understanding the concepts going on instead of passive terminal commands, even though sometimes you don't understand, trying your best to understand makes the biggest difference and can take you from blind trial/error testing to advanced troubleshooting.
## Verify First
Engineering with AI, I made a stable workflow that leverages AI as a learning tool. I fed official documentations and repositories into the model to break down complex vocabulary and configurations. Maintaining a solid cross-reference between AI explanations and official documents verified accuracy and prevented mistakes. Reading the explanations and then the official documents helps develop vocabulary and a solid understanding on the topic.
# Results
In the end of this section, I ended up with a solid foundation to add software to, a organized place to build my server off of. Casa OS running beautifully with all the failsafes so that this server will get back online after whatever it gets hit with. 
# What's Next
The next steps for me included:
- Setting up Immich for photos: [Immich Documentation](/Home%20Server%20(Big%20Project)/Immich%20Setup.md)
- Setting up Home Assistant for my smart home: [Home Assistant Documentation](/Home%20Server%20(Big%20Project)/Home%20Assistant%20Setup.md)
- Making a Server Laptop holder to mount the server to the wall: [Laptop Wall Mount Documentation](/Home%20Server%20(Big%20Project)/Laptop%20Wall%20Mount%20Documentation.md)
- Allow access to the server from outside local network: [Tailscale Setup](/Home%20Server%20(Big%20Project)/Tailscale%20Setup.md)
