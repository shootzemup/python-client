# -*- coding: utf8 -*-

import logging

import pygame
from pygame.font import Font

from conf import conf
from GameEngine.MenuItems.menuItemModel import MenuItemModel

class InputItemModel(MenuItemModel):
	"""
	Represents the model of an input, which is a specialized menu item
	where the user can type some text
	"""
	def __init__(self, defaultText=None, placeHolder="", precision=None,
				 color=(255, 255, 255), **kwargs):
		"""
		Initialize a new model for an input item
		defaultText -- the text to be displayed, that the user can edit
		placeHolder -- the text to be displayed when no text is inputed yet
		precision -- the precision of the drawing of the text
		color -- the tuple (r, g, b) of the color of the text
		**kwargs -- other arguments will be given to the MenuItemModel
		"""
		if not 'image' in kwargs:
			kwargs['image'] = conf['resources']['menu']['input']['default_background']
		super(InputItemModel, self).__init__(**kwargs)
		logging.log(1, "Trace: InputItemModel.__init__(%s, %s, %s)"
						% (defaultText, placeHolder, kwargs))
		self._defaultText = defaultText
		self._placeHolder = placeHolder
		self._hasFocus = False
		self._textSurface = None
		self._textSurfaceRect = None
		self._text = defaultText if defaultText else ''
		self._color = color
		self._textChanged = True
		self._precision = precision or conf['resources']['font']['default_precision']
		self._empty = len(self._text) == 0
		
	@property
	def precision(self):
	    return self._precision
	@precision.setter
	def precision(self, value):
	    self._precision = value
	
	@property
	def hasFocus(self):
	    return self._hasFocus
	
	def focus(self):
		logging.info("InputItem %s - focus" % self.itemName)
		self._hasFocus = True
	def unfocus(self):
		logging.info("InputItem %s - unfocus" % self.itemName)
		self._hasFocus = False

	@property
	def textChanged(self):
	    return self._textChanged
	@textChanged.setter
	def textChanged(self, value):
		self._textChanged = value

	@property
	def text(self):
	    return self._text
	@text.setter
	def text(self, value):
		logging.info("Text changed to: %s" % self._text)
		self._textChanged = True
		self._text = value
		self._empty = len(self._text) == 0
	
	@property
	def textSurface(self):
	    return self._textSurface if self._textSurface else self.surface
	@textSurface.setter
	def textSurface(self, value):
	    self._textSurface = value
	    self._textSurfaceRect = self._textSurface.get_rect()
		
	@property
	def textSurfaceSize(self):
	    return self._textSurfaceRect.size if self._textSurfaceRect else (0, 0)

	@property
	def color(self):
	    return self._color
	@color.setter
	def color(self, value):
	    self._color = value

	@property
	def empty(self):
	    return self._empty

	@property
	def placeHolder(self):
	    return self._placeHolder
