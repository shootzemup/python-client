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

#cl: Game: Manage the game loop
class Game(object):
	"""Handle the main loop of the game"""
	def __init__(self):
		super(Game, self).__init__()
		logging.log(1, "Trace: Game.__init__()")
		graphx.init()
		#a: _init_time: allow to compute some running statistics
		self._init_time = time.time()
		#a: _rendering_time: contains the total time spent for rendering
		self._rendering_time = 0
		#a: _updating_time: contains the total time spent for updating
		self._updating_time = 0
		#a: _nb_updated: contains the total number of updates made by the game
		self._nb_updates = 0
		#a: _nb_renders: contains the total number of renders
		self._nb_renders = 0
		#a: _state_manager: allow to manage the state stack
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
	def getAverageFPS(self):
		return not self._nb_renders or (time.time() - self._init_time) / self._nb_renders

	#m: run: Run the main game loop.
	#c: It updates the game with a fixed time step but can update multiple time
	#c: the game if it needs to catch up the lag introduce by rendering on a
	#c: slow hardware.
	#c: See: [http://gameprogrammingpatterns.com/game-loop.html],
	#c: [http://www.koonsolo.com/news/dewitters-gameloop/] for more info about
	#c: how and why this game loop works well and avoid lots of synchronization
	#c: problems.
	def run (self):
		logging.log(1, "Trace: Game.run()")
		global DONE
		previous = time.time()
		lag = 0
		while not DONE:
			#c: compute the elapsed time since previous rendering
			current = time.time()
			elapsed = current - previous
			previous = current

			# handle events
			self.handleEvents()
			# handle pressed keys
			self.handlePressed()

			#c: add the elapsed time to the lag. That allow to know whether
			#c: we need to update once or more on very slow hardware
			lag += elapsed

			#c: catch up the lag
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

	#m: handleEvents: handle a single event from the event queue
	def handleEvents(self):
		global DONE
		logging.log(1, 'Trace: Game.handleEvents()')
		for event in pygame.event.get():
			logging.debug('Event: %s', event)
			self._state_manager.handleEvent(event)
			if event.type == pygame.QUIT:
				DONE = True
				time.sleep(10000)
				sys.exit()
			if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
				DONE = True
			graphx.handleEvent(event)

	#m: handlePressed: handle the keyboard and the mouse state
	def handlePressed(self):
		logging.log(1, 'Trace: Game.handlePressed()')
		kbs = pygame.key.get_pressed()
		ms = pygame.mouse.get_pressed()
		self._state_manager.handlePressed(kbs, ms)
		graphx.handlePressed(kbs, ms)

	#m: update: Update the game for one fixed-time step
	def update(self):
		logging.log(1, "Trace: ========> Game.update()")
		self._state_manager.update()

	#m: render: render the game objects.
	#c: If some objects are moving from one position to another, it should
	#c: linearly interpolate the real drawing position between the previous and
	#c: the current position of the object using the given interpolation factor.
	#c: Note: to let the `render` step be as focused as possible on the actual
	#c: drawing, this interpolation computation should be done in the models of
	#c: the game objects.
	def render(self, interpolation):
		#p: interpolation: float[0,1]: interpolation factor between current and next frame
		logging.log(1, "Trace: ========> Game.render(%.5f)" % interpolation)
		time.sleep(conf['game_engine']['simulate_hardware_lag']);
		self._state_manager.render(interpolation)
		graphx.update()
