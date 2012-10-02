#!/usr/bin/python

#
# get-artist-genres_echonest.py
# 
# Gets The Echo Nest artist genres from given input string (or list of strings from file), representing artist's name.
# Powered by: The Echo Nest API
#
# 2012, Daniel Portwood (http://portwd.com)
# daniel [AT] portwd [DOT] com
# 

from pyechonest import artist
import sys
import getopt

def get_echonest_artist_genres(artist_name):
	try:
		echonest_artist_params = artist.Artist(artist_name)
		echonest_artist_genres = echonest_artist_params.terms
		echonest_genre = echonest_artist_genres[0]["name"]
		print ("%s;%s") % (artist_name, echonest_genre)
	except:
		print "%s;NOT_FOUND" % artist_name

def print_help():
	print "\t Usage: ./get-artist-genres_echonest.py [OPTIONS]"
	print "\t\t Gets The Echo Nest artist genres from given input string (or list of strings from file), representing artist's name.\n"
	print '\t -a | --artist :: name of the artist, e.g. ("Iron Maiden")'
	print "\t -f | --file :: list of artists from a *.txt file"

try:
	options, remainder = getopt.getopt(sys.argv[1:], 'a:f:', ['artist=', 'file=',])
	if len(sys.argv) > 1:
		for opt, arg in options:
			if opt in ('-a', '--artist'):
				artist_name = arg
				get_echonest_artist_genres(artist_name)
			elif opt in ('-f', '--file'):
				artist_file = file(arg).read().split('\n')
				for artist_name in artist_file:
					get_echonest_artist_genres(artist_name)
	else:
		print_help()
except:
	print_help()
