from time import sleep
from salmon import Salmon

# Misc. thread
class Chum(Salmon):
	def run(self):
		while not self.done:
			if not self.downstream.empty():
				# Process commands from parent
				pass
			# Do any further processing
			# place info on output_queue
			if self.parent.done:
				self.done = True
			else:
				sleep(.5) # This value can be changed to work
						  # as fast as needs to be done
		self.die()

	def die(self):
		pass