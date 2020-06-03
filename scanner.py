#!/bin/python
from pynada import Pynada
import pyfiglet
import time

def list_users(user_file):
	with open(user_file, 'r') as content_file:
		content = content_file.readlines()
		content = [x.strip() for x in content]
		return content

def list_keywords(keywords_file):
	with open(keywords_file, 'r') as content_file:
		content = content_file.readlines()
		content = [x.strip() for x in content]
		return content

def scanner(user, keywords):
	nada = Pynada()
	for domain in nada.get_domains():
		email = user +"@"+domain
		try:
			for email_log in nada.inbox(email).get_emails():
				for keyword in keywords:
					if keyword.lower() in email_log.subject.lower():
						email_contents = email_log.get_contents()
						print email + " - " + email_log.from_email + " - " +email_log.subject 
						#If you want to see the contents of the emails uncomment the line below, Warning: Its very messy.
						#print "Contents: \n" + email_log.get_contents() 
						time.sleep(0.5)
		except:
			continue


users =list_users('users.txt')
keywords = list_keywords('keywords.txt')
nada_banner = pyfiglet.figlet_format("NADA Scanner")
pr3r00t_banner =  pyfiglet.figlet_format("@PR3R00T")

print(nada_banner)
print(pr3r00t_banner)

print "Nada Email Account - Recpt Address - Subject Name \n"
for user in users:
	scanner(user, keywords)


