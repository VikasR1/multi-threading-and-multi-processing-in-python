# Now let’s assume we want to run this function twice, as illustrated below:


# Task1 : A CPU-bound task without multiprocessing 
import random

def append_to_list(lst, num_items):
	"""
	Appends num_items integers within the range [0-20000000) to the input lst
	"""
	for n in random.sample(range(20000000), num_items):
		lst.append(n)

if __name__ == "__main__":
    for i in range(2):
        append_to_list([], 10000000)

'''
And let’s `time` this execution and inspect the results.

we can verify it by running "time python mp1.py" command in terminal

results :- 

$ time python mp1.py

real    0m23.465s
user    0m0.000s 
sys     0m0.015s 
'''