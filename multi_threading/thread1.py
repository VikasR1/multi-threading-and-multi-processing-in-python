'''Then let’s try to download a few images from Unsplash using the code snippet below. 
Note that for to demonstrate the effect of threading more clearly, 
we intentionally attempt to download these images 5 times (see the for loop):'''

#Task1 - Downloading images from Unsplash with Python (I/O bound task) 

import requests

# Example CPU-bound function
def download_img(img_url: str):
	"""
	Download image from img_url in curent directory
	"""
	res = requests.get(img_url, stream=True)
	filename = f"{img_url.split('/')[-1]}.jpg"

	with open(filename, 'wb') as f:
		for block in res.iter_content(1024):
			f.write(block)

#Downloading images from Unsplash with Python (I/O bound task) 

if __name__ == '__main__':
    images = [
    	# Photo credits: https://unsplash.com/photos/IKUYGCFmfw4 
    	'https://images.unsplash.com/photo-1509718443690-d8e2fb3474b7',

    	# Photo credits: https://unsplash.com/photos/vpOeXr5wmR4
    	'https://images.unsplash.com/photo-1587620962725-abab7fe55159',

    	# Photo credits: https://unsplash.com/photos/iacpoKgpBAM
    	'https://images.unsplash.com/photo-1493119508027-2b584f234d6c',

    	# Photo credits: https://unsplash.com/photos/b18TRXc8UPQ
    	'https://images.unsplash.com/photo-1482062364825-616fd23b8fc1',

    	# Photo credits: https://unsplash.com/photos/XMFZqrGyV-Q
    	'https://images.unsplash.com/photo-1521185496955-15097b20c5fe',

    	# Photo credits: https://unsplash.com/photos/9SoCnyQmkzI
    	'https://images.unsplash.com/photo-1510915228340-29c85a43dcfe',

    ]

    for img in images * 5:
        download_img(img)


'''
special Note :- In fact, a Python process cannot run threads in parallel but it can run them 
concurrently through context switching during I/O bound operations.
'''