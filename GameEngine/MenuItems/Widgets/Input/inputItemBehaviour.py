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
		eventsManager.registerEvent(
			'onInputClick-' + self._model.itemName, (pygame.MOUSEBUTTONDOWN),
			 self.onInputClick)
		eventsManager.registerEvent(
			'onKeyPressed-' + self._model.itemName, (pygame.KEYDOWN),
			self.onKeyPressed)

	def onInputClick(self, button, pos):
		logging.info("InputItem received event: (%s, %s)" % (button, pos))

	def onKeyPressed(self, key, ascii):
		logging.info("InputItem received event: %s" % key)
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
		logging.log(1, "Trace: MenuItemBehaviour.update(%s, %s, %s)" % 
					(stateManager, parentPos, parentSize))
		logging.debug("Updating using model: %s", self._model)
		if self._model.textChanged:
			self.write(
				self._model.text if not self._model.empty else self._model.placeHolder,
				self._model.color if not self._model.empty else 
					(self._model.color[0] / 2, self._model.color[1] / 2, self._model.color[2] / 2))
