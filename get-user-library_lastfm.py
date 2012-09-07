#!/usr/bin/python

#
# get-user-library_lastfm.py
# Gets the entire list of scrobbled artists from given input string (or list of strings from file), representing user's last.fm username.
# Powered by: Last.fm API
#
# 2012, Daniel Portwood (http://portwd.com)
# daniel [AT] portwd [DOT] com
#

import lastfm
import sys
import getopt

api_key = 'b25b959554ed76058ac220b7b2e0a026'
api = lastfm.Api(api_key)

def get_lastfm_library(init_user):
	try:
		lastfm_user = api.get_user(init_user)
		user_library = lastfm_user.library
		library_artists = user_library.artists
		for library_artist in library_artists:
			print "%s;%s" % (init_user,library_artist.name)
	except:
		pass

def print_help():
  print "\t Usage: ./get-user-library_lastfm.py [OPTIONS]"
  print "\t\t Gets the entire list of scrobbled artists from given input string (or list of strings from file), representing user's last.fm username.\n"
  print '\t -u | --user :: last.fm username'
  print "\t -f | --file :: list of artists from a *.txt file"

try:
	options, remainder = getopt.getopt(sys.argv[1:], 'u:f:', ['user=', 'file=',])
	if len(sys.argv) > 1:
		for opt, arg in options:
			if opt in ('-u', '--user'):
				init_user = arg
				get_lastfm_library(init_user)
			elif opt in ('-f', '--file'):
				init_users = file(arg).read().split('\n')
				for init_user in init_users:
					get_lastfm_library(init_user)
	else:
		print_help()
except:
	print_help()
