# project 2 from course : https://classroom.udacity.com/courses/ud036/lessons/993460168/concepts/10175186730923


import os 

def rename_files():
	# (1): Get file name in the folder 
	file_list = os.listdir(r"./prank")
	print(file_list)
	
	save_path = os.getcwd()
	print("Current working directory is: " + save_path)
	os.chdir(r"./prank")
	
	# (2): Rename file name for each file
	for file_name in file_list:
		print("Old filename is: " + file_name)
		print("New filename is: " + file_name.translate(None, "0123456789")) 
		os.rename(file_name, file_name.translate(None, "0123456789"))
	
	print("Current working directory is: " + os.getcwd())
	os.chdir(r"../")
	print("Back to first directory: " + os.getcwd())
	
rename_files()	
