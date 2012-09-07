#!/usr/bin/python

#
# get-artist-image-url.py
# 
# Gets The Echo Nest's URLs to pictures/images of artist from given input string (or list of strings from file), representing artist's name.
# Poweredy by: The Echo Nest API
#
# 2012, Daniel Portwood (http://portwd.com)
# daniel [AT] portwd [DOT] com
#

from pyechonest import artist
import sys
import getopt

def get_echonest_images(artist_name):
	try:
		echonest_artist_params = artist.Artist(artist_name)
		for echonest_images in echonest_artist_params.images[:3]:
			print "%s;%s" % (artist_name,echonest_images["url"])
	except:
		print "Artist %s - NOT_FOUND" % artist_name

def print_help():
	print "\t Usage: ./get-artist-image-url.py [OPTIONS]"
	print "\t\t Gets URLs to pictures/images of artist from given input string (or list of strings from file), representing artist's name.\n"
	print '\t -a | --artist :: name of the artist, e.g. ("Iron Maiden")'
	print "\t -f | --file :: list of artists from a *.txt file"

try:
	options, remainder = getopt.getopt(sys.argv[1:], 'a:f:', ['artist=', 'file=',])
	if len(sys.argv) > 1:
		for opt, arg in options:
			if opt in ('-a', '--artist'):
				artist_name = arg
				get_echonest_images(artist_name)
			elif opt in ('-f', '--file'):
				artist_file = file(arg).read().split('\n')
				for artist_name in artist_file:
					get_echonest_images(artist_name)
	else:
		print_help()
except:
	print_help()
