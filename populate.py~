import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tuber.settings')
import django
import csv
django.setup()
from videos.models import Video, Flipbook, Actor
from taggit.models import Tag

def populate():
	print("In the populator now....")
	
	try:
		with open('ebony.csv') as csvfile:
			csvreader = csv.reader(csvfile, delimiter='|')
			for row in csvreader:
				embed = row[0]
				url = row[1]
				categories = row[2]
				rating = row[3]
				channel = row[4]
				title = row[5]
				tags = row[6]
				views = row[7]
				actors = row[8]
				thumbnail = row[9]
				flipbook = row[10]
				
				Tags = tags.split(";")
				Categories = categories.split(";")
				Actors = actors.split(";")
				Slideshow = flipbook.split(";")
				
				splice, link = url.split('=')
				ID = link

				print("-----------------------------------------------------------------")
				v = Video()
				v = Video.objects.get_or_create(id = ID, embedded = embed, url = url, rating = rating, channel = channel, title = title, views = views, thumbnail = thumbnail)[0]	
				v.save()
				#print("Video added")

				vid = Video.objects.get(id = ID)				
				for tag in Categories:
					vid.tags.add(tag)
					vid.save()
				#print("Tags added")	
				
				for slide in Slideshow:
					t = Flipbook()
					t = Flipbook.objects.get_or_create(video_id = ID, images = slide)[0]
					t.save()
				#print("Slidrz added")
				'''
				for item in Categories:
					ca = Category()
					ca = Category.objects.get_or_create(name = item)[0]
					ca.save()
				'''
				#print("Categories added")
					
				a = Actor()
				a = Actor.objects.get_or_create(video_id = ID, actors = Actors)[0]
				a.save()
				#print("Actors added")
                
				print(ID + "----------------------Added Successfully---------------------")
	except IOError:
		print('The datafile does not exist')
	
# Start execution here!
if __name__ == '__main__':
	print("Starting engine population script...")
	populate()
	print("Finishing engine population script...")
