# -*- coding: utf8 -*-

import logging
from state import State
from GameEngine.MenuItems.container import Container
from GameEngine.MenuItems.Widgets.Input.inputItem import InputItem
from GameEngine.MenuItems.Widgets.Label.labelItem import LabelItem
from GameEngine.MenuItems.Widgets.Button.button import Button


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

		self._userNameLabel = LabelItem(
			text="Login",
			initPos=(0, -0.2),
			itemName="UserNameLabel",
			absoluteSize=True)
		self._inputUserName = InputItem(
			placeHolder="User name",
			initPos=(0, -0.1),
			itemName="UserName",
			absoluteSize=True)
		self._passwordLabel = LabelItem(
			text="Password",
			initPos=(0, 0),
			itemName="passwordLabel",
			absoluteSize=True)
		self._inputPassword = InputItem(
			placeHolder="Password",
			initPos=(0, 0.1),
			itemName="Password",
			absoluteSize=True,
			inputType='password')
		self._validateButton = Button(
			initPos=(0, 0.2),
			itemName="Validate",
			absoluteSize=True)
		self._validateButton.onPressed(self.submit)
		self._page.addMenuItem(self._userNameLabel)
		self._page.addMenuItem(self._inputUserName)
		self._page.addMenuItem(self._passwordLabel)
		self._page.addMenuItem(self._inputPassword)
		self._page.addMenuItem(self._validateButton)
		self._page.computeSize()

	def submit(self):
		username = self._inputUserName.value()
		password = self._inputPassword.value()
		logging.info("Submitting authentication request: \
Username=%s, Password=%s" % (username, password))

	def update(self, stateManager):
		self._page.update(stateManager)

	def render(self, interpolation):
		self._page.render(interpolation)
		import sys
		# sys.exit()
		