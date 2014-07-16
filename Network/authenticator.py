# -*- coding: utf8 -*-

import socket
import logging
import hashlib

from conf import conf


def default_callback(err, data):
	if err:
		logging.error("An error occured: %s" % err)
		return
	logging.info("Default callback called with data: %s" % data)


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
		
	def authenticate(self, username, password, callback=None):
		"""
		Send an authentication query to the authentication server.
		username -- name of the user
		password -- password of the user
		callback -- a function (err, data) that will be called when the answer 
					of the server is fully received.
					err -- string containing the error message
					data -- {server_name: string, server_ip: string}
							where server_name is the unique name of the server
							and server_ip is the ip of the server to connect to.
		"""
		logging.info("Authenticating user: %s with password: %s" 
					 % (username, password))
		if callback is None:
			callback = default_callback
		s = socket.socket()
		s.connect((self._host, self._port))
		hash_pass = hashlib.new(self._hash_algo)
		hash_pass.update(password)
		s.send('user/authent/%s/%s' % (username, hash_pass.hexdigest()))

		response = ''
		end_msg = False
		while not end_msg:
			buf = s.recv(128)
			end_msg = len(buf) == 0 or '\n' in buf
			logging.log(1, "Received: %s" % buf)
			response += buf
		logging.debug("Response got: %s" % response)

		data = response.split('/')
		access = data[0]  # should contains 'Access'
		status = data[1]
		if status == 'Restricted':
			return callback('Restricted access!', None)
		server_name = data[2]
		server_ip = data[3]
		logging.info("Will access to server: %s using ip: %s" 
					 % (server_name, server_ip))
		callback(None, {
			'server_name': server_name,
			'server_ip': server_ip
		})

	def createAccount(self, username, password, callback=None):
		"""
		Create a new account on the server
		username -- name of the user
		password -- password of the user
		"""
		logging.info("Creating account for user: %s with password: %s" 
					 % (username, password))
		if callback is None:
			callback = default_callback
		s = socket.socket()
		s.connect((self._host, self._port))
		hash_pass = hashlib.new(self._hash_algo)
		hash_pass.update(password)
		s.send('user/authent/%s/%s' % (username, hash_pass.hexdigest()))

		response = ''
		end_msg = False
		while not end_msg:
			buf = s.recv(128)
			end_msg = len(buf) == 0 or '\n' in buf
			logging.log(1, "Received: %s" % buf)
			response += buf
		logging.debug("Response got: %s" % response)
		callback(None, response)

