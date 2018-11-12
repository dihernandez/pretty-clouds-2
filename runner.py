import subprocess
import get_images
import cv2
import numpy

''' here I will call the scraper (pull highly ranked pics with keyword cloud from imgur)
	and pass on to initialize metadata assignments
	run learning algorithms
	and based on their output populate criteria for picture generation
	The scraper/learning stuff will run depending on a switch (boolean var)
	afterwards output will generate image
'''

def resizePicture():
	img = cv2.imread('image_holder.jpg', cv2.IMREAD_UNCHANGED)
	 
	print('Original Dimensions : ',img.shape)
	 
	dim = (600, 400)
	# resize image
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	 
	print('Resized Dimensions : ',resized.shape)
	 
	cv2.imshow("Resized image", resized)
	cv2.waitKey(1000)
	cv2.destroyAllWindows()
	return resized



class Runner:
	def __init__(self, WIDTH = 600, HEIGHT = 400):
		self.image_stream = get_images.ImageStream()
		self.images_to_process = self.image_stream.getImageLinks()
		self.WIDTH = 600
		self.HEIGHT = 400
		self.num_picutres_analyzed = 0
		self.num_pixels = self.WIDTH * self.HEIGHT
		self.output = numpy.zeros([self.HEIGHT, self.WIDTH, 3])


	def extractColor(self, img):
		self.num_picutres_analyzed += 1

		for w in range(self.WIDTH - 1):
			for h in range(self.HEIGHT - 1):
				self.output[h, w, 0] += img[h, w, 0]
				self.output[h, w, 1] += img[h, w, 1]
				self.output[h, w, 2] += img[h, w, 2]
	
	def averageOutput(self):
		for w in range(self.WIDTH - 1):
			for h in range(self.HEIGHT - 1):
				self.output[h, w, 0] = self.output[h, w, 0]/self.num_picutres_analyzed
				self.output[h, w, 1] = self.output[h, w, 1]/self.num_picutres_analyzed
				self.output[h, w, 2] = self.output[h, w, 2]/self.num_picutres_analyzed

	def trainingMain(self):
		def retrieveNextImage():
			if (not self.images_to_process):
				self.image_stream.updatePageUrl();
				self.images_to_process = self.image_stream.getImageLinks()
			return self.images_to_process.pop()		

		# def callAnalyzer():
		# 	analyzer = subprocess.Popen('./pictureAnalyzerMain.py', shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
		# 	print(analyzer.stdout.read())
		# 	analyzer.wait()


		max_images=2
		image_cnt=0
		while (self.images_to_process and image_cnt<max_images):
			next_image = retrieveNextImage()
			self.image_stream.populateQueue(next_image)
			img = resizePicture()
			self.extractColor(img)
			image_cnt+=1

		self.averageOutput()
		cv2.imwrite("image_output.jpg", self.output)


runner = Runner()
runner.trainingMain()
