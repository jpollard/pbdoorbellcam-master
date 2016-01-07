Home Security Camera Project
============================

Doorbell snapshot
-----------------

####Background####
This is a small subset of security cam related projects i've been working recently. The premise is simple, but needs a bit of explaination on why things are set up the way they are. Firstly, my brother had given me a raspberry pi for christmas that had been sitting around for a while. At first I had used it as a retropi setup, which was fun but only lasted a week. Secondly, I found an old usb webcam that I hadnt used for a long time. Thirdly, my neighbor across the street was broken into. 

So I decided to create a security cam setup with the pi, webcam, and motion. The camera is situated over the front door, looking down on to the porch. The pi is right inside the front door with the web cam connected to it. It is accessible through a wifi dongle that is on the pi. I can now see a live feed of the front porch and have videos saved whenever motion is detected.


But then I thought of something else. I'd like to see who was at the door whenever someone rang the doorbell. My first thought was to get a small lcd and attach it to the pi and have that next to the door too. Then I thought maybe the pi could "sense" that the doorbell had been pushed, and send me a push via pushbullet. My doorbell is one of those wireless ones and I didnt want to drill a hole through the wall to connect some wires to the doorbell and the pi...

####Setup####

So the plan is;
- Connect an arduino with a bluetooth shield to the doorbell unit in the house. I plan on using the change in current to the speaker to trigger the arduino.

- Connect a bluetooth dongle to the pi and have the pi connect to the arduino, which i might have send out "heartbeats" so the pi knows its still connected and can reestablish the connection if needed.

- When the arduino senses the doorbell, tell the pi, then have the pi send a pushbullet to my phone, or a channel so my roommates can get it too.

####Files####

- pushPic.py
A python script that tells motion to take a screenshot, which is dated, timed, etc., but conviently is linked to lashsnap.jpg in the motion storage directory.

- master.py
A python script that sets up a "master" bluetooth connection to the arduino.



