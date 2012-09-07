#!/usr/bin/python

#
# get-users-friends-of-friends_lastfm.py 
# 
# Gets list of friends and friends of their friends from given input string (or list of strings from file), representing user's last.fm username.
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

user_friends_of_friends = []

def lastfm_friends_inception(init_user):
	try:
		lastfm_user = api.get_user(init_user)
		user_friends = lastfm_user.friends
	except:
		pass
	friends_of_friends = []
	
	for user_friend in user_friends:
		print "%s;%s" % (init_user,user_friend.name)
		try:
			other_user = api.get_user(user_friend.name)
			other_user_friends = other_user.friends
		except:
			pass
		for other_user_friend in other_user_friends:
			friends_of_friends.append(other_user_friend.name)
			#print other_user_friend.name
	
	friends_of_friends = list(set(friends_of_friends))
	for friend_of_friends in friends_of_friends:
		if type(friend_of_friends) is int:
			friend_of_friends = str(friend_of_friends)
		elif type(friend_of_friends) is None:
			friend_of_friends = str("none_type")
		print "%s;%s" % (init_user,friend_of_friends)

def print_help():
	print "\t Usage: ./get-users-friends-of-friends_lastfm.py [OPTIONS]"
	print "\t\t Get's list of friends and friends of their friends from given input string (or list of strings from file), representing user's last.fm username.\n"
	print '\t -u | --user :: last.fm username'
	print "\t -f | --file :: list of artists from a *.txt file"

try:
	options, remainder = getopt.getopt(sys.argv[1:], 'u:f:', ['user=', 'file=',])
	if len(sys.argv) > 1:
		for opt, arg in options:
			if opt in ('-u', '--user'):
				init_user = arg
				lastfm_friends_inception(init_user)
			elif opt in ('-f', '--file'):
				init_users = file(arg).read().split('\n')
				for init_user in init_users:
					lastfm_friends_inception(init_user)
	else:
		print_help()
except:
	print_help()
