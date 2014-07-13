# -*- coding: utf8 -*-

import logging

import pygame

from Graphx import graphx
from conf import conf
from menuItemBehaviour import MenuItemBehaviour


class ContainerBehaviour(MenuItemBehaviour):
	"""
	Represents the behaviour of an container
	"""

	def computeSize(self, parentPos=None, parentSize=None):
		# the first container of the tree has the screen as a parent
		if parentSize is None:
			parentSize = graphx.getScreenSize()
		if parentPos is None:
			parentPos = (graphx.getScreenSize()[0] / 2,
						 graphx.getScreenSize()[1] / 2)

		super(ContainerBehaviour, self).computeSize(parentPos, parentSize)

		for item in self._model.menuItems:
			item.computeSize(self._model.realPosition, self._model.realSize)

	def update(self, stateManager):
		super(ContainerBehaviour, self).update(stateManager)

		# successively update all the children items
		for item in self._model.menuItems:
			item.update(stateManager)