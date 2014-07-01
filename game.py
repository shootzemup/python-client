# -*- coding: utf8 -*-

# from __future__ import unicode_literals
import time
import sys
import logging
import pygame

from conf import conf
from GameEngine.GameStates.stateManager import StateManager
from Graphx import graphx

DONE = False

class Game(object):
	"""Handle the main loop of the game"""
	def __init__(self):
		super(Game, self).__init__()
		logging.log(1, "Trace: Game.__init__()")
		graphx.init()
		self._init_time = time.time()
		self._rendering_time = 0
		self._updating_time = 0
		self._nb_updates = 0
		self._nb_renders = 0
		self._state_manager = StateManager()

	# Statistics
	@property
	def init_time(self):
	    return self._init_time
	@init_time.setter
	def init_time(self, value):
	    self._init_time = value
	@property
	def nb_updates(self):
	    return self._nb_updates
	@nb_updates.setter
	def nb_updates(self, value):
	    self._nb_updates = value
	@property
	def nb_renders(self):
	    return self._nb_renders
	@nb_renders.setter
	def nb_renders(self, value):
	    self._nb_renders = value
	def getAverageRenderingTime(self):
		return not self._nb_renders or self._rendering_time / self._nb_renders
	def getAverageUpdatingTime(self):
		return not self._nb_updates or self._updating_time / self._nb_updates
	
		
	# Run the main game loop.
	# It updates the game with a fixed time step but can update multiple time
	# the game if it needs to catch up the lag introduce by rendering on a 
	# slow hardware.
	# See: [http://gameprogrammingpatterns.com/game-loop.html],
	# [http://www.koonsolo.com/news/dewitters-gameloop/] for more info about
	# how and why this game loop works well and avoid lots of synchronization
	# problems.
	def run (self):
		logging.log(1, "Trace: Game.run()")
		global DONE
		previous = time.time()
		lag = 0
		while not DONE:
			# compute the elapsed time since previous rendering
			current = time.time()
			elapsed = current - previous
			previous = current

			# handle events
			self.handleEvents()
			# handle pressed keys
			self.handlePressed()

			# add the elapsed time to the lag. That allow to know whether 
			# we need to update once or more on very slow hardware
			lag += elapsed

			# catch up the lag
			while lag >= conf['game_engine']['update_time_step']:
				t = time.time()  # used for statistics
				self.update()
				updating_time = time.time() - t
				self._updating_time += updating_time  # used for statistics
				self._nb_updates += 1
				lag -= conf['game_engine']['update_time_step']

			t = time.time()  # used for statistics
			self.render(lag / conf['game_engine']['update_time_step'])
			self._rendering_time += time.time() - t  # used for statistics
			self._nb_renders += 1  # used for statistics

	# handle a single event from the event queue
	def handleEvents(self):
		global DONE
		logging.log(1, 'Trace: Game.handleEvent()')
		for event in pygame.event.get():
			logging.debug('Event: %s', event)
			self._state_manager.handleEvent(event)
			if event.type == pygame.QUIT: 
				DONE = True
				time.sleep(10000)
				sys.exit()
			if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
				DONE = True

	# handle the keyboard and the mouse state
	def handlePressed(self):
		logging.log(1, 'Trace: Game.handlePressed()')
		kbs = pygame.key.get_pressed()
		ms = pygame.mouse.get_pressed()
		self._state_manager.handlePressed(kbs, ms)

	# Update the game for one fixed-time step
	def update(self):
		logging.log(1, "Trace: ========> Game.update()")
		self._state_manager.update()

	# render the game objects.
	# If some objects are moving from one position to another, it should
	# linearly interpolate the real drawing position between the previous and 
	# the current position of the object using the given interpolation factor.
	# Note: to let the `render` step be as focused as possible on the actual 
	# drawing, this interpolation computation should be done in the models of 
	# the game objects.
	def render(self, interpolation):
		logging.log(1, "Trace: ========> Game.render(%.5f)" % interpolation)
		time.sleep(conf['game_engine']['simulate_hardware_lag']);
		self._state_manager.render(interpolation)
		graphx.update()
