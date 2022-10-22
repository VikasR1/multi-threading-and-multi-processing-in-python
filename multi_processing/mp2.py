'''
Now let’s refact our code a little bit and now use two different processes 
so that each call to the function is executed in its own process:
'''
# Task2  : Multi-processing with a CPU-bound task

import random
import multiprocessing


NUM_PROC = 2


def append_to_list(lst, num_items):
	"""
	Appends num_items integers within the range [0-20000000) to the input lst
	"""
	for n in random.sample(range(20000000), num_items):
		lst.append(n)


if __name__ == "__main__":
	jobs = []

	for i in range(NUM_PROC):
		process = multiprocessing.Process(
			target=append_to_list, 
		    args=([], 10000000)
		)
		jobs.append(process)

	for j in jobs:
		j.start()

	for j in jobs:
		j.join()

'''
And finally let’s `time` and execution and inspect results:

$ time python mp2.py

real    0m14.493s
user    0m0.000s 
sys     0m0.030s
'''
# Note: 

"""
We can clearly see that (even though user and sys times remained approximately the same), 
the real time has dropped by a factor even greater than two (and this is expected since 
we essentially distributed the load to two distinct processes so that they can run in parallel).
"""