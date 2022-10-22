# Multi-processing in Python
''' 
if we want to take advantage of multi-core systems and eventually
run tasks in a truly parallelised context, we need to perform multi-processing instead 
of multi-threading.

In Python, multi-processing can be implemented using the "multiprocessing" module 
(or concurrent.futures.ProcessPoolExecutor) that can be used in order to spawn multiple OS processes.

multiprocessing is a package that supports spawning processes using an API
similar to the threading module.
'''

"""
Now let’s consider a "CPU-bound operation" that involves a function 
which appends multiple random integers to a list.
"""

import random

# Task0 : A CPU-bound task

def append_to_list(lst, num_items):
	"""
	Appends num_items integers within the range [0-20000000) to the input lst
	"""
	for n in random.sample(range(20000000), num_items):
		lst.append(n)