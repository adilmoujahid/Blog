#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Adil Moujahid'
SITENAME = u'Adil Moujahid'
TAGLINE = u'Data Analytics and more'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


MENUITEMS = [('Archive', 'archives.html'), ('About', 'pages/about.html'), ]

STATIC_PATHS = ['images', 'pdfs']

COVER_IMG_URL = '/images/cover-img.jpg'

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/AdilMouja'),
          ('linkedin', 'https://www.linkedin.com/pub/adil-moujahid/65/51/83a'),
          ('github', 'https://github.com/adilmoujahid'),)

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)


# Static paths will be copied without parsing their contents
STATIC_PATHS = ['images', 'extra']

# Shift the installed location of a file
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

DEFAULT_PAGINATION = 10

# Show most recent posts first
NEWEST_FIRST_ARCHIVES = False

# Specify theme
THEME = "theme/pure"

# Plugins
PLUGIN_PATH = 'plugins'
PLUGINS = ['gravatar']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
