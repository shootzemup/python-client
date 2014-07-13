# -*- coding: utf8 -*-

import logging

import pygame

from Graphx import graphx
from conf import conf
from menuItemBehaviour import MenuItemBehaviour
from EventsManager import eventsManager



class ContainerBehaviour(MenuItemBehaviour):
	"""
	Represents the behaviour of an container
	"""
	def __init__(self, model):
		super(ContainerBehaviour, self).__init__(model)
		eventsManager.registerEvent(
			'onContainerTab-' + self._model.itemName, 
			(pygame.KEYDOWN, pygame.K_TAB), 
			self.onTabPressed)
		eventsManager.registerCombination(
			'onContainerTabShift-' + self._model.itemName,
			[pygame.K_TAB, pygame.K_LSHIFT], [],
			self.onShiftTabPressed)

	def onTabPressed(self):
		# if the current item the cointainer think is focus is not, find the
		# focused one
		if not self._model.get_menuItem(self._model.focusedItem).hasFocus():
			focused = None
			for i, item in enumerate(self._model.menuItems):
				if item.hasFocus():
					focused = i
			if focused is None:
				self._model.focusedItem = -1
			else:
				self._model.focusedItem = focused
		
		#unfocus the current item
		self._model.get_menuItem(self._model.focusedItem).unfocus()
		# focus the next one focusable
		for x in xrange(len(self._model.menuItems)):
			
			self._model.focusedItem = \
				(self._model.focusedItem + 1) % len(self._model.menuItems)
			if self._model.get_menuItem(self._model.focusedItem).focus():
				break

	def onShiftTabPressed(self):
		# if the current item the cointainer think is focus is not, find the
		# focused one
		if not self._model.get_menuItem(self._model.focusedItem).hasFocus():
			focused = None
			for i, item in enumerate(self._model.menuItems):
				if item.hasFocus():
					focused = i
			if focused is None:
				self._model.focusedItem = -1
			else:
				self._model.focusedItem = focused
		
		#unfocus the current item
		self._model.get_menuItem(self._model.focusedItem).unfocus()
		# focus the next one focusable
		for x in xrange(len(self._model.menuItems)):
			
			self._model.focusedItem = \
				(self._model.focusedItem - 1) % len(self._model.menuItems)
			if self._model.get_menuItem(self._model.focusedItem).focus():
				break

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