# What Is Immich
Immich is a self-hosted photo and video manager. It is something like Google Photos or Apple Photos but is self-hosted so your in full control of your data.
# Why I Chose Immich
The reason I chose Immich boils down to a few reasons:
- Immich had the best UI I had seen, it was clean and organized and could compete with the UI of something like Google Photos
- It supported advanced facial recognization and OCR which made my photos always sorted and it way easy to find any photo you had in mind
- It is self-hosted so I am in full control of my data, at anytime I can add more storage and have no monthly subscription for that extra storage. For example for the 2TB I wanted to utilize on my home server would of costed around 10 dollars per month, which really stacks up over time.
- It had awesome support with my current home server setup as it was on the Casa OS app store and easy to download, manage, and use.
# Problems I Faced
I faced many problems along my journey of setting up immich, here were some that I can recall:
## Backup
### Problem
For some reason, whenever I tried to set up a backup schedule to back up all my data from my 2tb ssd to a 2TB HDD, it always reset or returned an error; something was just not working in Immich and wasn't allowing me to set up a backup.
### Mistakes
At first, I tried to use another server software called Duplicati, which would provide a UI for me to navigate so I could see the backups, but I quickly ran into errors like the destination path not working. Even when I directed it to the folders inside the HDD and SDD, it was duplicating the files to the laptop’s internal storage, which was just too small to keep the images and videos. I also faced issues with false UI indications, permission issues, and database corruptions.
### Solution
Sometimes the best solution is the simplest. Even though I didn't like not seeing my backups, I solved this by setting up the backup externally through the terminal. I used a simple terminal command called rsync, which allowed the server to duplicate the files from one drive to another. I also set up a cron job that kept 4 weeks of backups, with 3 of them being what changed week from week and one of them being the full backup. 
## Video Transcoding
### Problem
This was a frustrating and annoying problem: whenever I opened my videos, the audio played, but the video returned a black screen. Only when I clicked “ play original video” did it play properly. At first, this gave me a mini heart attack, as I thought all my files had gotten corrupted, but it turns out it was a false alarm.
### What Was Wrong
It didn't take me a while to figure out what was wrong; I realized that the videos were just not transcoded. A transcoded video is a low-quality version of the video so that it has less buffer time when viewing; it allows for a faster experience.
### Solution
It was a really simple solution: I just had to go to my administration tab and go to the jobs section, where I could run the server job of transcoding all my videos. 

## Family sharing
### Problem
So when showing this self-hosted thing to my parents, they liked everything about it but brought up a good point: they didn't have any personal storage. At the moment, everything was one big shared account in which all of the family members could upload photos and videos; all of it was organized into one big timeline. Now, this was good in some situations but bad in others, like when they wanted to just dump their camera roll to the server; no one wants to see your family’s unorganized junk that they haven't sorted through. They needed personal storage.
### Realization
Now this was a complex problem. Immich did support multiple accounts, but didn't support multi-user shared albums. A person could have a shared timeline with another person but couldn't have it with more than one user. So the only option was having personal storage but having to re-upload the family photos using another account which had all the family photos timeline access. This is still a problem I am trying to come up with a solution to, but it seems to be that I can’t do anything until Immich officially makes the update to support multiple accounts in a timeline/album.

# Conclusion
In all, this is a solid tool to have to look at all our family photos (more then 300gb of photos/videos). It is a massive upgrade from the manually sorted photos we had before, even though it failed to FULLY replace the workflow as it didn't support multi-user album sharing. It is great to just have a place to put your 10-minute, zip lining videos.
![Poster](/Home%20Server%20(Big%20Project)/Images/SS4.jpeg)
![Poster](/Home%20Server%20(Big%20Project)/Images/SS3.jpeg)