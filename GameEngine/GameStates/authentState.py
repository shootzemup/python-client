# -*- coding: utf8 -*-

import logging
from state import State
from GameEngine.MenuItems.container import Container
from GameEngine.MenuItems.Widgets.Input.inputItem import InputItem
from GameEngine.MenuItems.Widgets.Label.labelItem import LabelItem


class AuthentState(State):
	"""
	Represent the main authentification page of the game.
	The purpose of this state is to display the authentication menu
	and allow the user to connect
	"""
	def __init__(self):
		super(AuthentState, self).__init__()
		self._page = Container(initSize=(1.0, 1.0), initPos=(0, 0), 
							   itemName="Container")

		userNameLabel = LabelItem(
			text="Login",
			initSize=(0.1, 0.05),
			initPos=(0, -0.2),
			itemName="UserNameLabel")
		inputUserName = InputItem(
			placeHolder="User name", 
			initSize=(0.25, 0.025),
			initPos=(0, -0.1),
			itemName="UserName")
		passwordLabel = LabelItem(
			text="Password",
			initSize=(0.1, 0.05),
			initPos=(0, 0),
			itemName="passwordLabel")
		inputPassword = InputItem(
			placeHolder="Password", 
			initSize=(0.25, 0.025),
			initPos=(0, 0.1),
			itemName="Password")
		self._page.addMenuItem(userNameLabel)
		self._page.addMenuItem(inputUserName)
		self._page.addMenuItem(passwordLabel)
		self._page.addMenuItem(inputPassword)

	def update(self, stateManager):
		self._page.update(stateManager)

	def render(self, interpolation):
		self._page.render(interpolation)
		import sys
		# sys.exit()
		