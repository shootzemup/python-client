# -*- coding: utf8 -*-

import logging

import pygame


class MenuItemBehaviour(object):
	"""
        Handle the behaviour of a default menu item
	"""
	def __init__(self, model):
		"""
		Initialize the behaviour of the menu item
		model -- the model of the menu item
		"""
		super(MenuItemBehaviour, self).__init__()
		logging.log(1, "Trace: MenuItemBehaviour.__init__(%s)" % model)
		self._model = model

	def _computeRealSize(self, parentSize):
		logging.debug("MenuItem %s: realSize = %s * %s"
					  % (self._model.itemName, parentSize, self._model.size))
		realSize = (parentSize[0] * self._model.size[0], 
					parentSize[1] * self._model.size[1])
		logging.debug("MenuItem %s: Resizing from: %s to %s"
					  % (self._model.itemName, self._model.size, realSize))
		# do not resize if the size is the same as it will involve useless
		# copy
		if self._model.realSize[0] != realSize[0] or \
				self._model.realSize[1] != realSize[1]:
			self._model.realSize = realSize
			self._model.resizeSurface(self._model.realSize)


	def _computeRealPos(self, parentPos, parentSize):
		# we cannot be sure that nothing changed since last frame
		# if self._model.absolute:
		logging.debug("MenuItem %s: realPos = %s + %s * %s" 
					  	% (self._model.itemName, str(parentPos), 
					  		str(self._model.position), str(parentSize)))
		realPosition = \
			(parentPos[0] + self._model.position[0] * parentSize[0] / 2,
			 parentPos[1] + self._model.position[1] * parentSize[1] / 2)

		logging.debug("MenuItem %s: old pos: %s, real pos: %s"
					% (self._model.itemName, self._model.position, realPosition))

		self._model.realPosition = realPosition

	def computeSize(self, parentPos, parentSize):
		logging.debug("MenuItem %s: Parent position: %s, parent size: %s" 
					  % (self._model.itemName, parentPos, parentSize))
		if self._model.absoluteSize:  # model contains the real size
			# size is a multiple of pixels
			self._computeRealSize((1, 1))
		else:
			# compute size first as it will be used bu the position computation
			self._computeRealSize(parentSize)

		if self._model.absolutePos:  # the model contains the real positions
			# position is the position of the center pixel 
			self._computeRealPos((0, 0), (1, 1))
		else:  # the model contains relative positions/size
			self._computeRealPos(parentPos, parentSize)


	def update(self, stateManager):
		pass
