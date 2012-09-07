#!/usr/bin/python

#
# get-artist-image-url_lastfm.py
# 
# Gets Last.fm's URLs to pictures/images of artist and it's similars from given input string (or list of strings from file), representing artist's name.
# Poweredy by: Last.fm API
#
# 2012, Daniel Portwood (http://portwd.com)
# daniel [AT] portwd [DOT] com
# 

import urllib2
import sys
import getopt

from xml.dom.minidom import parse

def print_help():
	print "\t Usage: ./get-artist-image-url_lastfm.py [OPTIONS]"
	print "\t\t Gets Last.fm's URLs to pictures/images of artist and it's similars from given input string (or list of strings from file), representing artist's name.\n"
	print '\t -a | --artist :: name of the artist, e.g. ("Iron Maiden")'
	print "\t -f | --file :: list of artists from a *.txt file"

def get_lastfm_images(artist_name):
	try:
		artist_name = artist_name.rstrip()
		artist_name = artist_name.replace (" ", "+")
		lastfm_api_url = "http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=%s&api_key=b25b959554ed76058ac220b7b2e0a026" % (artist_name)
		file = urllib2.urlopen(lastfm_api_url)
		data = parse(file)
		lastfm_artists = data.getElementsByTagName("artist")
	
		for artist in lastfm_artists:
			obj = artist.getElementsByTagName("image")[4].firstChild.data
			print obj
	except:
		print "Artist %s - NOT_FOUND" % artist_name

try:
	options, remainder = getopt.getopt(sys.argv[1:], 'a:f:', ['artist=', 'file=',])
	if len(sys.argv) > 1:
		for opt, arg in options:
			if opt in ('-a', '--artist'):
				artist_name = arg
				get_lastfm_images(artist_name)
			elif opt in ('-f', '--file'):
				artist_file = file(arg).read().split('\n')
				for artist_name in artist_file:
					get_lastfm_images(artist_name)
	else:
		print_help()
except:
	print_help()
