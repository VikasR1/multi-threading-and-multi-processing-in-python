'''
special Note :- In fact, a Python process cannot run threads in parallel but it can run them 
concurrently through context switching during I/O bound operations.
'''

'''
 let's optimize our code by taking advantage of threads 
(don’t forget that downloading -multiple- images is a I/O-bound task).
'''
#Task2 - Download images from Unsplash with threading

import requests
from queue import Queue
from threading import Thread

NUM_THREADS = 5
q = Queue()

def download_img():
	"""
	Download image from img_url in curent directory
	"""
	global q

	while True:
		img_url = q.get()

		res = requests.get(img_url, stream=True)
		filename = f"{img_url.split('/')[-1]}.jpg"

		with open(filename, 'wb') as f:
			for block in res.iter_content(1024):
				f.write(block)
		q.task_done()


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
    
    for img_url in images * 5:
        q.put(img_url)

    for t in range(NUM_THREADS):

        worker = Thread(target=download_img)
        worker.daemon = True
        worker.start()

    q.join()


'''
To recap, threading in Python allows multiple threads to be created within a single process, 
but due to GIL, none of them will ever run at the exact same time. 
Threading is still a very good option when it comes to running multiple I/O bound tasks concurrently.
'''


# special note
'''
You should also note that threading comes with the overhead associated with 
managing the threads and therefore you should avoid using them for basic tasks. 
Additionally, they also increase the complexity of the program which means that debugging may 
become a little bit tricky. Therefore, use threading only wherever there’s a clear value when doing so.
'''