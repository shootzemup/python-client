# -*- coding: utf8 -*-

import pygame
from pygame.locals import *
import logging
from functools import wraps

instance = None

def singletonize(method):
	@wraps(method)
	def wrapper(*args, **kwargs):
		return method(instance, *args, **kwargs)
	return wrapper

def init():
	global instance
	instance = EventsManager()

class EventsManager(object):
	"""
	Manage events and allow to register functions to be called when an
	event is fired.
	"""
	def __init__(self):
		super(EventsManager, self).__init__()
		logging.log(1, "Trace: EventManager.__init__()")
		# registered allow to get all the callbacks related to an event
		self._registered = {}
		# names allow to get an event from the name
		self._names = {}

		# list of event types that will not generate a warning when they are
		# fired and not handled
		self._ignored_events = []

		# list of registered combinations
		self._registered_combinations = {}

	def _call_callbacks(self, event, event_value=None):
		logging.log(1, "Trace: EventManager._call_callbacks(%s, %s)"
						% (event, event_value))
		for cb_name in self._registered[event]:
			logging.debug("Event callback '%s' called." % cb_name)
			if event_value:
				self._registered[event][cb_name](event_value)
			else:
				self._registered[event][cb_name]()

	def handleEvent(self, event):
		logging.log(1, "Trace: EventManager.handleEvent(%s)" % event)
		# construct the event if it is valid
		if event.type == KEYDOWN or event.type == KEYUP:
			reg_ev = (event.type, event.key)
		elif event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
			reg_ev = (event.type, event.button)
		elif event.type == MOUSEMOTION:
			reg_ev = (event.type, event.pos)
		elif event.type == QUIT:
			reg_ev = (event.type, None)
		elif not event.type in self._ignored_events:
			logging.warning("Unexpected event: %s" % event)
			return;

		# check if the event is registered
		if reg_ev in self._registered:
			# import pdb
			# pdb.set_trace()
			# if it is, call all the callback registered
			self._call_callbacks(reg_ev)

		# now do the same without the value, the value will be given to the
		# callback
		if (event.type) in self._registered:
			if event.type == KEYDOWN or event.type == KEYUP:
				self._call_callbacks(self, (event.type), event.key)
			elif event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
				self._call_callbacks(self, (event.type), event.button)
			elif event.type == MOUSEMOTION:
				self._call_callbacks(self, (event.type), event.pos)
			elif event.type == QUIT:
				self._call_callbacks(self, (event.type), None)
			elif not event.type in self._ignored_events:
				logging.warning("Unexpected event: %s" % event)

	def handlePressed(self, kbs, ms):
		logging.log(1, "Trace: EventManager.handlePressed(%s, %s)" 
						% (kbs, ms))
		# allow to check key combination, that can be used for shortcuts
		for combin in self._registered_combinations:
			# activate is true if combination contains either keycode or 
			# mousebutton list
			activate = len(combit['keycodes']) > 0 or \
				len(combin['mousebuttons']) > 0
			# and all the keys presence in kbs of the registered keycode.
			# if one is not true in the kbs list, activate will be false
			for key in combin['keycodes']:
				activate = activate and kbs[key]
			# idem for the mouse buttons
			for but in combin['mousebuttons']:
				activate = activate and ms[but]
			if activate:
				self._registered_combinations['callback']()

	def registerCombination(self, name, keycodes, mousebuttons, callback):
		"""
		Register a new callback to be called when the given key combination
		is pressed at the same time
		name -- the unique name of the combination
		keycodes -- list<keycode>: list of key to be pressed to have the 
					callback called
		mousebuttons -- list<mousebutton>: list of mouse buttons to be pressed
						to have th callback called
		callback -- callback to be called when both listed keycodes and 
					mousebuttons are pressed at the same time
		"""
		logging.log(1, "Trace: EventManager.registerCombination(%s, %s, %s, %s)" 
						% (name, keycodes, mousebuttons, callback))
		logging.debug("Registering combination %s on callback: %s"
						% (name, callback))
		self._registered_combinations[name] = {
			'keycodes': keycodes,
			'mousebuttons': mousebuttons,
			'callback': callback
		}

	def unregisterCombination(self, name):
		logging.log(1, "Trace: EventManager.unregisterCombination(%s)" % name)
		del self._registered_combinations[name]

	def registerEvent(self, name, event, callback):
		"""
		Register a new callback to be caled when an event is fired
		name -- the unique name of the event
		event -- the tuple (type, value) that correspond to the event that will
				 make the callback to be called. 
				 Note: If the value is not specified, if will be given to the 
				 callback
		callback -- the callback that will be called when the given event is
					fired
		"""
		logging.log(1, "Trace: EventManager.registerEvent(%s, %s, %s)" 
						% (name, event, callback))
		logging.debug("Registering event %s on callback: %s" % (name, callback))
		# create or add the the dict of callbacks 
		# related to the event
		if event in self._registered:
			self._registered[event][name] = callback
		else:
			self._registered[event] = {'name': callback}
		# save that the name matching this event
		self._names[name] = event

	def unregisterEvent(self, name):
		#retrieve the event from the name, then delete the callback
		# that is registered under this name
		logging.log(1, "Trace: EventManager.registerEvent(%s)" % name)

		del self._registered[self._names[name]][name]


handleEvent = singletonize(EventsManager.handleEvent)
handlePressed = singletonize(EventsManager.handlePressed)
registerCombination = singletonize(EventsManager.registerCombination)
unregisterCombination = singletonize(EventsManager.unregisterCombination)
registerEvent = singletonize(EventsManager.registerEvent)
unregisterEvent = singletonize(EventsManager.unregisterEvent)