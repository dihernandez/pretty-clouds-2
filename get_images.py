import requests
import time
import json
from bs4 import BeautifulSoup
import copy
import imagequeue as imQ
import imgurpython as imgP


client_id = 'eaa798b45a9adeb'
client_secret = 'a788992ea533c67d9a2d75921aa39148e39c9c29'
gallery_url = 'https://imgur.com/search?q=clouds'
gallery_key = "GALLERY" 
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

		page = requests.get(gallery_url)
		content = BeautifulSoup(page.content)
		thumbnail_container = content.select('a.thumbnail')		

		for reference in thumbnail_container:
			extracted_url = reference['href']
			self.image_urls.append(extracted_url)
		return self.image_urls


	''' extract urls from imgur gallery 
		adapted from Tankor Smash's Blog post http://blog.tankorsmash.com/?p=266
	'''
	def getImageLinksFromImgurGallery(self):
		IMAGE_NAME_KEY = 'hash'		
		IMAGE_EXTENSION_KEY = 'ext'
		BASE_URL = r'http://imgur.com/{name}{ext}'
		image_list = self.page_json[GALLERY_KEY]
		
		for image in image_list:
			image_name = image[IMAGE_NAME_KEY]
			image_ext = image[IMAGE_EXTENSION_KEY]
			image_url = BASE_URL.format(name=name, ext=ext)
			self.image_urls.append(image_url)
		return copy.copy(self.image_urls)

	def populateQueue(self, image_url):
		try:
			self.image_queue.pushImage(image_url)
		except:
			#give time for processing to finish
			time.sleep(5)
			#now force next one through
			self.image_queue.clearImage()
			self.image_queue.pushImage(image_url)


