# -*- coding: utf8 -*-

import logging
import pygame
from pprint import pformat

from Graphx import graphx


class MenuItemView(object):
	"""
    View of the menu item. It handles the drawing of a menu item
	"""
	def __init__(self, model):
		super(MenuItemView, self).__init__()
		self._model = model

	def _computeRealSize(self, parentSize):
		logging.log(1, "Trace: MenuItemView._computeRealSize(%s)" 
						% str(parentSize))
		logging.debug("%s, realSize = %s * %s" 
					  % (self._model.itemName,
					  	 str(parentSize), str(self._model.size)))

		realSize = (parentSize[0] * self._model.size[0], 
					parentSize[1] * self._model.size[1])
		logging.debug("%s MenuItem Real Size: %s" 
						% (self._model.itemName, str(realSize)))
		# do not resize if the size is the same as it will involve useless
		# copy
		if self._model.realSize[0] != realSize[0] or \
				self._model.realSize[1] != realSize[1]:
			self._model.realSize = realSize
			self._model.surface = pygame.transform.scale(
				self._model.surface, self._model.realSize)


	def _computeRealPos(self, parentPos, parentSize):
		logging.log(1, "Trace: MenuItemView._computeRealPos(%s, %s)" % 
					(parentPos, parentSize))
		logging.debug("%s realPos = %s + %s * %s - %s / 2" 
					  	% (self._model.itemName, str(parentPos), 
					  		str(self._model.position), str(parentSize),
					  		str(self._model.realSize)))
		# we cannot be sure that nothing changed since last frame
		# if self._model.absolute:
		logging.debug("%s realPos = %s + %s * %s" 
					  	% (self._model.itemName, str(parentPos), 
					  		str(self._model.position), str(parentSize)))
		self._model.realPosition = \
			(parentPos[0] + self._model.position[0] * parentSize[0] / 2,
			 parentPos[1] + self._model.position[1] * parentSize[1] / 2)

		logging.debug("%s MenuItem Real Position: %s" 
						% (self._model.itemName, str(self._model.realPosition)))

	def render(self, interpolation, parentPos, parentSize):
		logging.log(1, "Trace: MenuItemView.render(%.5f, %s, %s)" % 
					(interpolation, parentPos, parentSize))
		logging.debug("Rendering using model: %s" % self._model)
		if self._model.absolute:  # the model contains the real positions
			# position is the position of the center pixel 
			# size is a multiple of pixels
			self._computeRealSize((1, 1))
			self._computeRealPos((0, 0), (1, 1))
		else:  # the model contains relative positions/size
			# compute size first as it will be used bu the position computation
			self._computeRealSize(parentSize)
			self._computeRealPos(parentPos, parentSize)
		graphx.draw(self._model.surface, self._model.rect)



