# refrence : https://towardsdatascience.com/multithreading-multiprocessing-python-180d0975ab29
''' 
In Python, threads can be implemented with the use of threading module. 
Now let’s consider a function that is used to download an image — this is clearly a I/O-bound task
'''

#Task 0 - Example CPU-bound function

import requests

def download_img(img_url: str):
	"""
	Download image from img_url in curent directory
	"""
	res = requests.get(img_url, stream=True)
	filename = f"{img_url.split('/')[-1]}.jpg"

	with open(filename, 'wb') as f:
		for block in res.iter_content(1024):
			f.write(block)