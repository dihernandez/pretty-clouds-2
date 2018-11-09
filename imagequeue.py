import urllib.request

#may only load one image at a time
class ImageQueue:
	def __init__(self):
		self.isPopulated = False
		self.content = ""

	def isPopulated(self):
		return self.isPopulated
	
	def clearImage(self):
		self.isPopulated = False
		self.content = ""
	
	def pushImage(self, image_url):
		if (not self.isPopulated):
			self.content = image_url
			image_holder = open("image_holder.jpg",'wb')
			#print(image_url)
			image_data = urllib.request.urlopen("http://"+image_url[4:])
			#print(image_url, "  ", image_data)
			image_holder.write(image_data.read())
			image_holder.close()
			self.isPopulated = True
		else:
			raise Exception("image already loaded")
