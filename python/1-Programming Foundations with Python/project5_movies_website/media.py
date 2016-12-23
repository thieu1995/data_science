# https://google.github.io/styleguide/pyguide.html 	--> Style 
# https://docs.python.org/2/library/urllib.html		--> Thu vien
# http://www2.lib.uchicago.edu/keith/courses/python/	--> Book

import webbrowser

class Movie():

	""" This class provides a way to store movie related information """			# declare __doc__

	VALID_RATINGS = ["G", "PG", "PG-13", "R"]			# static variable, class variable

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline				# self = this 
		self.poster_image_url = poster_image			# properties 
		self.trailer_youtube_url = trailer_youtube
		
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)	
		

