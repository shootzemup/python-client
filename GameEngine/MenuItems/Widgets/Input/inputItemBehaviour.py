# -*- coding: utf8 -*-

import logging

import pygame
from pygame.font import Font, SysFont

from conf import conf
from GameEngine.MenuItems.menuItemBehaviour import MenuItemBehaviour
from EventsManager import eventsManager


class InputItemBehaviour(MenuItemBehaviour):
	"""
	Represents the behaviour of an input item
	"""
	def __init__(self, model):
		"""
		Initializes a new input item behaviour.
		model -- requires a input item model 
		"""
		super(InputItemBehaviour, self).__init__(model)
		logging.log(1, "Trace: InputItemBehaviour(%s)" % model)
		# self._register_events()
		eventsManager.registerEvent(
			'onInputClick-' + self._model.itemName, (pygame.MOUSEBUTTONDOWN),
			 self.onInputClick)

	def _register_events(self):
		logging.info("Registering events for item %s" % self._model.itemName)
		eventsManager.registerEvent(
			'onKeyPressed-' + self._model.itemName, (pygame.KEYDOWN),
			self.onKeyPressed)

	def _unregister_events(self):
		eventsManager.unregisterEvent(
			'onKeyPressed-' + self._model.itemName)

	def onInputClick(self, button, pos):
		logging.info("InputItem %s received event: (%s, %s)"
					 % (self._model.itemName, button, pos))
		if button == 1 or button == 3:
			if self._model.intersect(pos):
				if not self._model.hasFocus:
					self._model.focus()
					self._register_events()
			elif self._model.hasFocus:
				self._model.unfocus()
				self._unregister_events()


	def onKeyPressed(self, key, ascii):
		logging.info("InputItem %s received event: %s" 
					 % (self._model.itemName, key))
		if self._model.hasFocus:
			if key >= 32:
				self._model.text += ascii
			if key == pygame.K_BACKSPACE:
				self._model.text = self._model.text[:-1]

	def write(self, text, color=None):
		self._model.textChanged = False
		if conf['resources']['font']['use_system']:
			myFont = SysFont(conf['resources']['font']['system'], 
							self._model.precision)
		else:
			myFont = Font(conf['resources']['font']['default'],
						  self._model.precision)
		fontSurface = myFont.render(text, True, color or self._model.color)
		# resize to fit the size of the background. 
		self._model.textSurface = pygame.transform.scale(
			fontSurface,
			(fontSurface.get_rect().size[0] * (self._model.realSize[1] - 2 *  conf['resources']['menu']['input']['margins'][1]) / fontSurface.get_rect().size[1],
			 self._model.realSize[1] - 2 *  conf['resources']['menu']['input']['margins'][1]))

	def update(self, stateManager, parentPos, parentSize):
		super(InputItemBehaviour, self).update(stateManager, parentPos, parentSize)
		if self._model.textChanged:
			self.write(
				self._model.text if not self._model.empty else self._model.placeHolder,
				self._model.color if not self._model.empty else 
					(self._model.color[0] / 2, self._model.color[1] / 2, self._model.color[2] / 2))
