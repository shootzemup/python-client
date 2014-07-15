# -*- coding: utf8 -*-

import socket
import logging
import hashlib

from conf import conf


class Authenticator(object):
	"""Manage the connection with the authentication server"""
	def __init__(self):
		"""
		Initialize the authenticator that is able to send request to the
		authenticator server
		host -- host adress of the authenticator server
		port -- listening port of the authenticator server 
		"""
		super(Authenticator, self).__init__()
		self._host = conf['net']['authenticator']['host']
		self._port = conf['net']['authenticator']['port']
		self._hash_algo = None
		for algo in conf['net']['authenticator']['hash']:
			if algo in hashlib.algorithms:
				self._hash_algo = algo
		if self._hash_algo is None:
			logging.error("Unable to find any hash algorithm in: %s" 
						  % hashlib.algorithms)
			exit(1)
		self._authenticated = False

		
	def authenticate(self, username, password):
		"""
		Send an authentication query to the authentication server.
		username -- name of the user
		password -- password of the user
		"""
		logging.info("Authenticating user: %s with password: %s" 
					 % (username, password))
		s = socket.socket()
		s.connect((self._host, self._port))
		hash_pass = hashlib.new(self._hash_algo)
		hash_pass.update(password)
		s.send('user/authent/%s/%s' % (username, hash_pass.hexdigest()))

		response = ''
		while (buf = s.recv(128)):
			logging.log(1, "Received: %s" % buf)
			response += buf
		logging.debug("Response got: %s" % response)

		data = response.split('/')
		access = data[0]  # should contains 'Access'
		server_name = data[1]
		server_ip = data[2]
		logging.info("Will access to server: %s using ip: %s" 
					 % (server_name, server_ip))

	def createAccount(self, username, password):
		"""
		Create a new account on the server
		username -- name of the user
		password -- password of the user
		"""
		logging.info("Creating account for user: %s with password: %s" 
					 % (username, password))
		s = socket.socket()
		s.connect((self._host, self._port))
		hash_pass = hashlib.new(self._hash_algo)
		hash_pass.update(password)
		s.send('user/authent/%s/%s' % (username, hash_pass.hexdigest()))

		response = ''
		while (buf = s.recv(128)):
			logging.log(1, "Received: %s" % buf)
			response += buf
		logging.debug("Response got: %s" % response)

