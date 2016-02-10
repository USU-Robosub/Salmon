from threading import Thread

# Parent thread
class Salmon(Thread):
	done = False
	def __init__(self, output_queue, input_queue, parent):
		Thread.__init__(self)
		self.downstream = output_queue
		self.upstream = input_queue
		self.parent = parent