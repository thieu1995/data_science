import urllib

def read_text():
	myFile = open("./curse_word.txt")
	contents_of_file = myFile.read()
	print(contents_of_file)
	myFile.close()
	
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
	output = connection.read()
	connection.close()
	
	if "false" in output:
		print("No curse word")
	elif "true" in output:
		print("Found curse word!")
	else: 
		print("Could not scan this document!")
	
	


read_text()
