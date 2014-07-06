# -*- coding: utf8 -*-

import pygame
import logging

import graphx
from conf import conf
from EventsManager import eventsManager


class VideoPlayer(object):
	"""Allow to easily play a video"""
	def __init__(self):
		super(VideoPlayer, self).__init__()
		logging.log(1, "Trace: VideoPlayer.__init__")
		self._clock = pygame.time.Clock()
		self._movie_screen = None
		self._movie_screen_resized = None
		self._movie = None
		self._on_video_end = None
		self._playing = False
		self._movie_length = 0


	def play(self, video_link, on_video_end):
		logging.log(1, "Trace: VideoPlayer.play(%s, %s)"
						% (video_link, on_video_end))
		self._movie = pygame.movie.Movie(video_link)
		self._movie_screen = pygame.Surface(self._movie.get_size()).convert()
		self._movie_screen_resized = pygame.Surface(graphx.getScreenSize())
		self._movie.set_display(self._movie_screen)
		self._on_video_end = on_video_end
		self._movie_length = self._movie.get_length()
		self._movie.play()
		self._playing = True
		# register events
		eventsManager.registerEvent('skipVideoUsingSpace', 
			(pygame.KEYDOWN, pygame.K_ESCAPE), self.stop)
		eventsManager.registerEvent('skipVideoUsingEnter',
			(pygame.KEYDOWN, pygame.K_RETURN), self.stop)
		eventsManager.registerEvent('skipVideoUsingEscape',
			(pygame.KEYDOWN, pygame.K_SPACE), self.stop)

	def stop(self):
		logging.log(1, "Trace: VideoPlayer.stop()")
		if not self._playing:
			return
		self._movie.stop()
		self._playing = False
		self._on_video_end()

	def render(self):
		logging.log(1, "Trace: VideoPlayer.render()")
		if self._playing and self._movie.get_time() > self._movie_length - 0.1:
			logging.info("Video ended!")
			self.stop()
		elif self._playing:
			logging.debug("Playing video... %.2f/%.2f" 
						  % (self._movie.get_time(), self._movie_length))
			pygame.transform.scale(
				self._movie_screen, graphx.getScreenSize(),
				self._movie_screen_resized)
			graphx.draw(self._movie_screen_resized)
			self._clock.tick(conf['graphx']['video_player']['max_fps'])


