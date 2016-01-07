#!/usr/bin/env python

import pushbullet
import urllib

# open the file containing my pushbullet api key and get the key
keyFile = open('./key', 'r')
key = keyFile.readline()
keyFile.close()

# strip the trailing newline
pb = pushbullet.Pushbullet(key.rstrip())

# connect to the motion api to tell it to take a snapshot
url = urllib.URLopener()
url.retrieve('http://192.168.1.98:8080/0/action/snapshot')

# get the snapshot taken
pic = open('/var/motion/lastsnap.jpg', 'rb')

# to send a pic via pushbullet you have to upload it first then send it
picdata = pb.upload_file(pic, 'visitor.jpg')
pb.push_file(**picdata)


