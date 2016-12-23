# project 1 from course : https://classroom.udacity.com/courses/ud036/lessons/993460168/concepts/10175186730923

import time
import webbrowser

url = 'https://www.youtube.com/watch?v=7gphiFVVtUI'
# Open URL in a new tab, if a browser window is already open.
# webbrowser.open_new_tab(url)
# Open URL in new window, raising the window if possible.
# webbrowser.open_new(url)

total_breaks = 3
break_count = 0

print("This program started on: " + time.ctime())
while break_count < total_breaks:
	time.sleep(2*60*60)
	webbrowser.open_new_tab(url)
	break_count += 1

