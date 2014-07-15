# -*- coding: utf8 -*-

import logging

import pygame
from pygame.font import Font

from conf import conf
from GameEngine.MenuItems.menuItemModel import MenuItemModel


class ButtonModel(MenuItemModel):
	UNFOCUSED_SURFACE = 0
	FOCUSED_SURFACE = 1
	PRESSED_SURFACE = 2
	"""Represents the model of a button"""
	def __init__(self, image=None, **kwargs):
		"""
		Initialize a new button
		image -- a list of three surface or links [unfocused, focused, pressed]
				 each surface corresponding to a state
		**kwargs -- all the others arguments will be given to the MenuItemModel.
		"""
		# default parameters
		if image is None:
			image = []
		if type(image) is not list:
			image = [image]
		if len(image) < 1:
			image.append(conf['resources']['menu']['button']['default_background'])
		if len(image) < 2:
			image.append(conf['resources']['menu']['button']['focused_default_background'])
		if len(image) < 3:
			image.append(conf['resources']['menu']['button']['pressed_default_background'])
		super(ButtonModel, self).__init__(image=image, **kwargs)
		self._on_pressed_cb = []
		self._pressed = False

	def onPressed(self, callback):
		""" add a callback to be called when the button is pressed """
		self._on_pressed_cb.append(callback)

	def offPressed(self):
		""" Remove all the callback registered """
		del self._on_pressed_cb[:]

	def get_pressedCb(self):
		return self._on_pressed_cb
		
	def press(self):
		self._pressed = True
		self.useSurface(self.PRESSED_SURFACE)
	def release(self):
		self._pressed = False
		if self.hasFocus:
			self.useSurface(self.FOCUSED_SURFACE)
		else:
			self.useSurface(self.UNFOCUSED_SURFACE)

	def isPressed(self):
		return self._pressed
