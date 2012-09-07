#!/usr/bin/python

#
# get-top-artists-chart_lastfm.py
# 
# Get's Top Chart of Last.fm artists: http://www.last.fm/charts/artists/top
# Powered by: Last.fm API
#
# 2012, Daniel Portwood (http://portwd.com)
# daniel [AT] portwd [DOT] com
#

import urllib2
from xml.dom.minidom import parse

file = urllib2.urlopen('http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key=b25b959554ed76058ac220b7b2e0a026')
data = parse(file) 
file.close()

artists = data.getElementsByTagName("artist")
result = []
for artist in artists:
	obj = artist.getElementsByTagName("name")[0].firstChild.data
	print "%s" % (obj)
