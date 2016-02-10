from pink import Pink
from chum import Chum
from Queue import Queue
from sockeye import Sockeye
from time import sleep

class Chinook:
	done = False
	upstream = Queue()
	tasks = []

	def __init__(self):
		self.motor = Pink(Queue(), self.upstream, self)
		self.vision = Sockeye(Queue(), self.upstream, self)
		self.misc = Chum(Queue(), self.upstream, self)

	def start(self):
		# Setup task list
		
		self.motor.start()
		self.vision.start()
		self.misc.start()
		self.run()

	def run(self):
		while not self.done:
			if not self.upstream.empty():
				pass # Process data here
			# Make any decisions and send data to threads
			sleep(1)