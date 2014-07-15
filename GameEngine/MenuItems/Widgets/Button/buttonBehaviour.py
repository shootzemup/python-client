# -*- coding: utf8 -*-

import logging

import pygame
from pygame.font import Font, SysFont

from conf import conf
from GameEngine.MenuItems.menuItemBehaviour import MenuItemBehaviour
from EventsManager import eventsManager


class ButtonBehaviour(MenuItemBehaviour):
	"""Represents the behaviour of a button"""
	def __init__(self, model):
		super(ButtonBehaviour, self).__init__(model)
	
		eventsManager.registerEvent(
			'onButtonHover-' + self._model.itemName,
			(pygame.MOUSEMOTION),
			self.onButtonHover)
		eventsManager.registerEvent(
			'onButtonClick-' + self._model.itemName,
			(pygame.MOUSEBUTTONDOWN),
			self.onButtonClick)
		eventsManager.registerEvent(
			'onButtonUnClick-' + self._model.itemName,
			(pygame.MOUSEBUTTONUP),
			self.onButtonUnClick)
		eventsManager.registerEvent(
			'onButtonEnter-' + self._model.itemName,
			(pygame.KEYUP, pygame.K_RETURN),
			self.onButtonEnterPull)
		eventsManager.registerEvent(
			'onButtonSpace-' + self._model.itemName,
			(pygame.KEYUP, pygame.K_SPACE),
			self.onButtonEnterPull)
		eventsManager.registerEvent(
			'onButtonEnterPush-' + self._model.itemName,
			(pygame.KEYDOWN, pygame.K_RETURN),
			self.onButtonEnterPush)
		eventsManager.registerEvent(
			'onButtonSpacePush-' + self._model.itemName,
			(pygame.KEYUP, pygame.K_SPACE),
			self.onButtonEnterPull)

	def focus(self):
		if self._model.focusable and not self._model.isPressed():
			self._model.focus()
			self._model.useSurface(self._model.FOCUSED_SURFACE)
		return self._model.focusable

	def unfocus(self):
		if self._model.hasFocus:
			self._model.unfocus()
			self._model.useSurface(self._model.UNFOCUSED_SURFACE)
		if self._model.isPressed():
			self._model.release()

	def press(self):
		self._model.press()

	def release(self):
		if self._model.isPressed():
			self._model.release()
			for cb in self._model.get_pressedCb():
				cb()

	def onButtonHover(self, pos):
		if self._model.intersect(pos):
			self.focus()
		else:
			self.unfocus()

	def onButtonClick(self, button, pos):
		if button == 1 or button == 3:
			if self._model.intersect(pos):
				self.press()

	def onButtonUnClick(self, button, pos):
		if button == 1 or button == 3:
			if self._model.intersect(pos):
				self.release()
			else:
				self._model.release()

	def onButtonEnterPush(self):
		if self._model.hasFocus:
			logging.info("Pushing button")
			self.press()
		else:
			logging.info("Not focused")

	def onButtonEnterPull(self):
		if self._model.hasFocus:
			self.release()

