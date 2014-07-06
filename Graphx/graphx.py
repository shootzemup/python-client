# -*- coding: utf8 -*-
import pygame
import logging
from functools import wraps

from conf import conf
from videoPlayer import VideoPlayer

# This module intends to provide a proxy to the pygame library,
# also providing a Camera object.

instance = None

def singletonize(method):
	@wraps(method)
	def wrapper(*args, **kwargs):
		logging.debug("Trace: wrapper(%s, %s)" % (args, kwargs))
		logging.debug("Calling: %s(%s, %s, %s)" % (method.__name__, instance, args, kwargs))
		return method(instance, *args, **kwargs)
	return wrapper

def init():
	global instance
	instance = Graphx()

class Graphx(object):
	"""Represent the graphx engine"""
	def __init__(self):
		super(Graphx, self).__init__()
		logging.log(1, "Trace: Graphx.__init__()")
		self._screen_size = conf['graphx']['screen_size']
		self._screen = pygame.display.set_mode(self._screen_size)
		self._video_player = VideoPlayer()

	def handleEvent(self, event):
		logging.log(1, "Trace: Graphx.handleEvent(%s)" % event)
		self._video_player.handleEvent(event)

	def handlePressed(self, kbs, ms):
		logging.log(1, "Trace: Graphx.handlePressed(...)")
		self._video_player.handlePressed(kbs, ms)

	def playVideo(self, link, on_video_end):
		self._video_player.play(link, on_video_end)

	# Flip the screen and erase the drawing surface.
	# This function should be called once after all the game rendering
	def update(self):
		logging.log(1, "Trace: Graphx.update()")
		self._video_player.render()
		pygame.display.flip()
		self._screen.fill(conf['graphx']['screen_base_color'])

	def draw(self, surface, position=(0, 0)):
		logging.log(1, "Trace: Graphx.draw(%s, %s)" % (surface, position))
		self._screen.blit(surface, position)


	def getScreen(self):
		return self._screen

	def getScreenSize(self):
		print "Screen size: ", self._screen_size
		return self._screen_size

draw = singletonize(Graphx.draw)
update = singletonize(Graphx.update)
playVideo = singletonize(Graphx.playVideo)
handleEvent = singletonize(Graphx.handleEvent)
handlePressed = singletonize(Graphx.handlePressed)
getScreen = singletonize(Graphx.getScreen)
getScreenSize = singletonize(Graphx.getScreenSize)