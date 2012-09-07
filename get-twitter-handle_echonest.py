#!/usr/bin/python

#
# get-twitter-handle.py 
# 
# Gets Twitter handle from given input string (or list of strings from file), representing artist's name.
# Powered by: The Echo Nest API
#
# 2012, Daniel Portwood (http://portwd.com)
# daniel [AT] portwd [DOT] com
#

from pyechonest import artist
import sys
import getopt

def get_twitter_handle(artist_name):
	try:
		echonest_artist_params = artist.Artist(artist_name)
		twitter_handle = echonest_artist_params.get_twitter_id()
		print "%s;@%s" % (artist_name,twitter_handle)
	except:
		print "Artist: %s - NOT_FOUND" % artist_name

def print_help():
	print "\t Usage: ./get-twitter-handle.py [OPTIONS]"
	print "\t\t Gets Twitter handle from given input string (or list of strings from file), representing artist's name.\n"
	print '\t -a | --artist :: name of the artist, e.g. ("Iron Maiden")'
	print "\t -f | --file :: list of artists from a *.txt file"

try:
	options, remainder = getopt.getopt(sys.argv[1:], 'a:f:', ['artist=', 'file=',])
	if len(sys.argv) > 1:
		for opt, arg in options:
			if opt in ('-a', '--artist'):
				artist_name = arg
				get_twitter_handle(artist_name)
			elif opt in ('-f', '--file'):
				artist_file = file(arg).read().split('\n')
				for artist_name in artist_file:
					get_twitter_handle(artist_name)
	else:
		print_help()
except:
	print_help()
