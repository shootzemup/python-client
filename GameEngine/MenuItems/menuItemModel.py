# -*- coding: utf8 -*-

import logging
import pygame


class MenuItemModel(object):
	"""
        Handle the data of a default menu item
	"""
	def __init__(self, imageLink, initPos, initSize, absolute, name):
		"""
		Initialize the model of the menu item
		initPos -- the initial position of the item
		initSize -- the initial size of the item.
		absolute -- if set to `True`, the position and the size will be used as
					stated. If no, the size and the position will be computed
					from the size of the parent at render time
		"""
		super(MenuItemModel, self).__init__()
		self._position = initPos
		self._size = initSize
		self._absolute = absolute
		self._surface = pygame.image.load(imageLink)
		self._itemName = name
		self._rect = self._surface.get_rect()

	@property
	def itemName(self):
	    return self._itemName
	@itemName.setter
	def itemName(self, value):
	    self._itemName = value
	

	@property
	def position(self):
	    return self._position
	@position.setter
	def position(self, value):
	    self._position = value

	@property
	def size(self):
	    return self._size
	@size.setter
	def size(self, value):
	    self._size = value

	@property
	def absolute(self):
	    return self._absolute

	# if the menu position is not absolute, realPosition will
	# contain the real position in pixel the item uses on the scren.
	# note that this property is not valid before the first
	@property
	def realPosition(self):
	    return self._rect.center
	@realPosition.setter
	def realPosition(self, value):
	    self._rect.center = value

	@property
	def realSize(self):
		return self._rect.size
	@realSize.setter
	def realSize(self, value):
		self._rect.size = value
	

	@property
	def rect(self):
	    return self._rect

	@property
	def surface(self):
	    return self._surface
	@surface.setter
	def surface(self, value):
	    self._surface = value
	
	
	

	
	

