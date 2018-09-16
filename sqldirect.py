# -*- coding: utf-8 -*-
import os
#import sys
import csv
import sqlite3


#.setdefaultencoding('UTF8')
#connection establish
connection = sqlite3.connect('******.sqlite3')
print("Connected to Database", connection)
#pick the data
try:
	with open('FILE.csv') as csvfile:
		csvreader = csv.reader(csvfile, delimiter='|')
		for row in csvreader:
			embed = row[0]
			url = row[1]
			Tags = row[2]
			rating = row[3]
			channel = row[4]
			title = row[5]
			Categories = row[6]
			views = row[7]
			Actors = row[8]
			thumbnail = row[9]
			Flipbook = row[10]
			
			tags = Tags.split(";")
			categories = Categories.split(";")
			actors = Actors.split(";")
			slideshow = Flipbook.split(";")
			
			splice, link = url.split('=')
			ID = link

            #show the cursor
			cursor = connection.cursor()
				
			cursor.execute('INSERT INTO searchengine_video(id, embedded, url, rating, channel, title, views, thumbnail, IsActive) VALUES(?,?,?,?,?,?,?,?,?)', (ID, embed, url, rating, channel, title, views, thumbnail, 1))
			connection.commit()
			
			for slide in slideshow:					
				cursor.execute('INSERT INTO searchengine_flipbook( video_id, images) VALUES(?,?)', (ID, slide))
				connection.commit()
				#print(slide)

			for tag in tags:
				cursor.execute('INSERT INTO searchengine_tag( video_id, tags) VALUES(?,?)', (ID, tag))
				connection.commit()
				#print(tag)

			for item in categories:
				cursor.execute('INSERT INTO searchengine_category( video_id, categories) VALUES(?,?)', (ID, item))
				connection.commit()
				#print(item)
		
			if(actors):
				for person in actors:
					cursor.execute('INSERT INTO searchengine_actor( video_id, actors) VALUES(?,?)', (ID, person))
					connection.commit()
					#print(person)
			else:
				pass
					
			print(ID, " Done ")
			print("_______________________________________________________________________________")
except IOError:
	print('The datafile does not exist')	
#create a cursor pointer