"""
Mimick the stdout process of shipping
"""


from datetime import datetime
from time import sleep
import random
import sys


class It(object):
		
	with open("SC4LoadingPhrases.txt", "r") as phrases:
		random_phrases = list(map(lambda x: x.replace('\n', ''),
			phrases.readlines()))


	def spinner(self):
		while True:
			for _ in '|/-\\':
				yield _

	def spin(self, wait=10):
		now = datetime.now()
		calc_time = lambda now_time: (datetime.now() - now_time).total_seconds()
		spin = self.spinner()
		load_rate = random.randint(1, 4)/10
		while calc_time(now) < wait:
			sys.stdout.write(next(spin))
			sys.stdout.flush()
			sleep(load_rate)
			sys.stdout.write('\b')

	def RunRandomProcess(self, wait=10):
		position_choice = random.randint(0, len(self.random_phrases))
		phrase = self.random_phrases.pop(position_choice)
		sys.stdout.write(f"\t{phrase}...")
		self.spin(wait=wait)
		sys.stdout.write("\n")


	def run(self):
		num_processes = random.randint(10, 20)
		for _ in range(num_processes):
			wait_time = random.randint(0, 10)
			self.RunRandomProcess(wait_time)


if __name__ == '__main__':
	# Test it out
	it = It()
	it.run()