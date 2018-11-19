"""
Mimick the stdout process of shipping
"""


from datetime import datetime
from time import sleep
import random
import sys


class It(object):
	def __init__(self):
		sys.stdout.write("Pushing silly phrases into containers...")
		self.spin()
		with open("Text/SC4LoadingPhrases.txt", "r") as phrases:
			self.random_phrases = list(map(lambda x: x.replace('\n', ''),
				phrases.readlines()))
		sys.stdout.write("\n\t")
		sys.stdout.write("Loading...")
		self.spin()
		sys.stdout.write("\n")


	def bore_me(self):
		spin = self.spinner()
		with open('Text/atotc.txt', 'r') as atotc:
			lines = atotc.readlines()
		for _ in lines:
			print(f"\t{_}")
			sleep(3)


	def spinner(self):
		while True:
			for _ in '|/-\\':
				yield _

	def spin(self, wait=10, load_rate=random.randint(1, 4)/10):
		now = datetime.now()
		calc_time = lambda now_time: (datetime.now() - now_time).total_seconds()
		spin = self.spinner()
		while calc_time(now) < wait:
			sys.stdout.write(next(spin))
			sys.stdout.flush()
			sleep(load_rate)
			sys.stdout.write('\b')

	def RunRandomProcess(self, wait=10):
		position_choice = random.randint(0, len(self.random_phrases))
		subprocess = random.choice([0, 0, 0, 1])
		phrase = self.random_phrases.pop(position_choice)
		if subprocess:
			sys.stdout.write(f"\t\t{phrase}...")
		else:
			sys.stdout.write(f"\t{phrase}...")
		self.spin(wait=wait)
		sys.stdout.write("\n")


	def entertain_me(self):
		num_processes = random.randint(10, 20)
		for _ in range(num_processes):
			wait_time = random.randint(0, 10)
			self.RunRandomProcess(wait_time)


	def run(self):
		self.entertain_me()
		self.bore_me()
			
			


if __name__ == '__main__':
	# Test it out
	it = It()
	it.run()