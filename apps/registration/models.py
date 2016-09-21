from __future__ import unicode_literals
from django.shortcuts import redirect
import re, bcrypt
from django.db import models


class UserManager(models.Manager):
	def register(self, first_name, last_name, email_address, pwhash, pwcheck):
		errors = []
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		namecheck = re.compile(r"[0-9]+")

		if re.search(namecheck, first_name):
			errors.append('First name cannot contain numbers')
		elif len(first_name) < 1:
			errors.append('Please fill out first name')
		if re.search(namecheck, last_name):
			errors.append('Last name cannot contain numbers')
		elif len(last_name) < 1:
			errors.append('Please fill out last name')
		if len(email_address) < 1:
			errors.append('Please fill out email')
		elif not EMAIL_REGEX.match(email_address):
			errors.append('Not valid email')
		if len(pwhash) < 8:
			errors.append('Password must be longer than 8 characters')
		if pwhash != pwcheck:
			errors.append("PASSWORDS DON'T MATCH")

		response = {}
		if errors: #Not empty list returns True
			response['created'] = False
			response['errors'] = errors
		else:
			pw_hash = bcrypt.hashpw(pwhash.encode(), bcrypt.gensalt())
			dmail = User.userManager.create(first_name = first_name, last_name = last_name, email_address = email_address, pwhash = pw_hash)
			response['created'] = True
			response['newuser'] = dmail
			response['id'] = dmail.id
		return response

	def login(request, data):
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		errors = []
		loginresponse = {} 
		
		dmail = User.userManager.filter(email_address = data['loginemail'])
		password = data['loginpw'].encode()

		if not dmail:
			errors.append('Email does not exist in database')
		else:
			if bcrypt.hashpw(password, dmail[0].pwhash.encode()) == dmail[0].pwhash:
				loginresponse['created'] = True
				loginresponse['user'] = dmail[0]
				loginresponse['id'] = dmail[0].id
			else:
				errors.append('Password does not work with provided email')
		
		if errors:
			loginresponse['created'] = False
			loginresponse['errors'] = errors
	
		return loginresponse

class User(models.Model):
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	email_address = models.CharField(max_length = 100)
	pwhash = models.CharField(max_length = 100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	userManager = UserManager()

