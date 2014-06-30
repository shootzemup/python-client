#!/usr/local/bin/python
# -*- coding: utf8 -*-

# from __future__ import unicode_literals
import time

from conf import conf


DONE = False

print "test"

class Game(object):
	"""Handle the main loop of the game"""
	def __init__(self):
		super(Game, self).__init__()
		
	# Run the main game loop.
	# It updates the game with a fixed time step but can update multiple time
	# the game if it needs to catch up the lag introduce by rendering on a 
	# slow hardware.
	# See: [http://gameprogrammingpatterns.com/game-loop.html],
	# [http://www.koonsolo.com/news/dewitters-gameloop/] for more info about
	# how and why this game loop works well and avoid lots of synchronization
	# problems.
	def run (self):
		print "running"
		global DONE
		previous = time.time()
		lag = 0
		while not DONE:
			# compute the elapsed time since previous rendering
			current = time.time()
			elapsed = current - previous
			previous = current

			# add the elapsed time to the lag. That allow to know whether 
			# we need to update once or more on very slow hardware
			lag += elapsed

			# catch up the lag
			while lag >= conf['game_engine']['update_time_step']:
				self.update()
				lag -= conf['game_engine']['update_time_step']

			self.render(lag / conf['game_engine']['update_time_step'])

	# Update the game for one fixed-time step
	def update(self):
		print "update"
		pass

	# render the game objects.
	# If some objects are moving from one position to another, it should
	# linearly interpolate the real drawing position between the previous and 
	# the current position of the object using the given interpolation factor.
	# Note: to let the `render` step be as focused as possible on the actual 
	# drawing, this interpolation computation should be done in the models of 
	# the game objects.
	def render(self, interpolation):
		print "render(%.5f)", interpolation
		time.sleep(conf['game_engine']['simulate_hardware_lag']);
		pass


if __name__ == "__main__":
	print "Game is starting..."
	Game().run()