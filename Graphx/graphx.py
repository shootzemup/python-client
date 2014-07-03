# -*- coding: utf8 -*-
import pygame
import logging

from conf import conf
from videoPlayer import VideoPlayer

# This module intends to provide a proxy to the pygame library,
# also providing a Camera object.

instance = None

def update():
	global instance
	instance.update()

def init():
	global instance
	instance = Graphx()

def getScreen():
	return instance._screen

def draw(surface, position=(0, 0)):
	instance.draw(surface, position)

def playVideo(link, on_video_end):
	instance.playVideo(link, on_video_end)

def handleEvent(event):
	instance.handleEvent(event)

def handlePressed(kbs, ms):
	instance.handlePressed(kbs, ms)

def getScreenSize():
	return instance._screen_size


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

	def draw(self, surface, position):
		logging.log(1, "Trace: Graphx.draw(%s, %s)" % (surface, position))
		self._screen.blit(surface, position)


		