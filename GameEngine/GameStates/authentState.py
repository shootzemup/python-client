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
			initPos=(0, -0.2),
			itemName="UserNameLabel",
			absoluteSize=True)
		inputUserName = InputItem(
			placeHolder="User name",
			initPos=(0, -0.1),
			itemName="UserName",
			absoluteSize=True)
		passwordLabel = LabelItem(
			text="Password",
			initPos=(0, 0),
			itemName="passwordLabel",
			absoluteSize=True)
		inputPassword = InputItem(
			placeHolder="Password",
			initPos=(0, 0.1),
			itemName="Password",
			absoluteSize=True,
			inputType='password')
		self._page.addMenuItem(userNameLabel)
		self._page.addMenuItem(inputUserName)
		self._page.addMenuItem(passwordLabel)
		self._page.addMenuItem(inputPassword)

		self._page.computeSize()

	def update(self, stateManager):
		self._page.update(stateManager)

	def render(self, interpolation):
		self._page.render(interpolation)
		import sys
		# sys.exit()
		