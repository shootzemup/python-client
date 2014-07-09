# -*- coding: utf8 -*-

import logging

import pygame
from pygame.font import Font

from conf import conf
from GameEngine.MenuItems.menuItemModel import MenuItemModel


class LabelItemModel(MenuItemModel):
	"""
	Represents the model of a label
	"""
	def __init__(self, text, **kwargs):
		"""
		Initialize a new model for a label item
		text -- the text to be displayed
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
		image = self._write(text)
		super(LabelItemModel, self).__init__(image=image, **kwargs)
		self._text = text

	def _write(self, text):
		myFont = Font(conf['resources']['font']['default'],
					  conf['resources']['font']['default_size'])
		surface = myFont.render(text, True, (0, 0, 0))
		return surface
		
	@property
	def text(self):
	    return self._text
	