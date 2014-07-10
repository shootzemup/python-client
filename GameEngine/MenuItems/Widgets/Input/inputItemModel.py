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
	def __init__(self, defaultText=None, placeHolder="", color=(255, 255, 255), **kwargs):
		"""
		Initialize a new model for an input item
		defaultText -- the text to be displayed, that the user can edit
		placeHolder -- the text to be displayed when no text is inputed yet
		initPos -- the initial position of the item to set as the center of the 
				   surface. If `absolute` is `False` (default), the
				   position will be a percentage of the size of
				   the object, starting from the center.
				   eg: (1, -1) will be the upper left
		initSize -- the initial size of the item.
		absolute -- if set to `True`, the position and the size will be used as
					stated. If no, the size and the position will be computed
					from the size of the parent at render time
		itemName -- used only for debugging identification
		"""
		if not 'image' in kwargs:
			kwargs['image'] = conf['resources']['menu']['input']['default_background']
		super(InputItemModel, self).__init__(**kwargs)
		logging.log(1, "Trace: InputItemModel.__init__(%s, %s, %s)"
						% (defaultText, placeHolder, kwargs))
		self._defaultText = defaultText
		self._placeHolder = placeHolder
		self._hasFocus = True
		self._textSurfaceRect = None
		self._text = defaultText if defaultText else placeHolder
		self._color = color
		self._textChanged = True
		
	@property
	def hasFocus(self):
	    return self._hasFocus
	@hasFocus.setter
	def hasFocus(self, value):
	    self._hasFocus = value

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
	
	# override the getter/setter of the _surface member to make a fresh copy
	# when it gets resized
	@property
	def surface(self):
	    return self._surface
	@surface.setter
	def surface(self, value):
	    self._surface = value
	    self._rect = self._surface.get_rect()

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
	