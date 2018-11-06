import requests
import time
import json
from bs4 import BeautifulSoup
import copy
import imagequeue as imQ
import imgurpython as imgP


client_id = 'eaa798b45a9adeb'
client_secret = 'a788992ea533c67d9a2d75921aa39148e39c9c29'
cloud_gallery_key = 'https://imgur.com/search?q=clouds'
client = imgP.ImgurClient(client_id, client_secret)

# Example request


class ImageStream:
	def __init__(self):
		self.image_urls = client.gallery()
		self.image_queue = imQ.ImageQueue()
		self.num_page_updates = 0
		try:
			page_json = json.loads(requests.get(gallery_url.format(page_number = self.num_page_updates)))
		except:
			page_json = {}

	def updatePageUrl(self):
		self.num_page_updates +=1
		updated_url = gallery_url
		updated_url.format(page_number = self.num_page_updates)
		self.page_json = json.loads(requests.get())
	
	def getImageLinks(self):
		headers = requests.utils.default_headers()
		headers.update({
    		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
		})

		page = requests.get(cloud_gallery_key)
		content = BeautifulSoup(page.content, features="html.parser")
		url_container = content.select('img')

		for reference in url_container:
			extracted_url = reference['src']
			if "gif" not in extracted_url:
				self.image_urls.append(extracted_url)
				print(extracted_url)
		return self.image_urls

	def populateQueue(self, image_url):
		try:
			self.image_queue.pushImage(image_url)
		except:
			#give time for processing to finish
			time.sleep(5)
			#now force next one through
			self.image_queue.clearImage()
			self.image_queue.pushImage(image_url)


