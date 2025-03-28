#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from io import open

AUTHOR = u'Adil Moujahid'
SITENAME = u'Adil Moujahid'
TAGLINE = u'Bridging Tech and Art'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


#MENUITEMS = [('Posts', 'posts'), ('Projects', 'projects'), ('Notes', 'notes'), ('About', 'about')]
MENUITEMS = [('Posts', 'posts'), ('Projects', 'projects'), ('About', 'about')]

#('Archive', 'archives.html')



PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'

#COVER_IMG_URL = '/images/cover-img.jpg'
COVER_IMG_URL = '/images/banner.png'


# Social widget
SOCIAL = (('twitter', 'https://twitter.com/AdilMouja'),
          ('linkedin', 'https://www.linkedin.com/in/adilmoujahid/'),
          ('github', 'https://github.com/adilmoujahid'),)

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

#Set Disqus sitename
DISQUS_SITENAME = "adilmoujahid"
GOOGLE_ANALYTICS = "G-24GHYVXZ5F"
ADDTHIS_PROFILE = "ra-54c667f5423e719f"
# Formatting for urls

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

# Generate yearly archive
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Show most recent posts first
NEWEST_FIRST_ARCHIVES = False

# Static paths will be copied without parsing their contents
STATIC_PATHS = ['images', 'extra', 'files']


# Ipython setting
NOTEBOOK_DIR = 'notebooks'
EXTRA_HEADER = open('_nb_header.html', encoding='utf-8').read()
IPYNB_STOP_SUMMARY_TAGS = [('div', ('class', 'input')), ('div', ('class', 'output'))]


# Shift the installed location of a file
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

DEFAULT_PAGINATION = 10

# Show most recent posts first
NEWEST_FIRST_ARCHIVES = False

# Specify theme
THEME = "theme/pure"

# Plugins
PLUGIN_PATHS = ['./plugins']
MARKUP = ('md', 'ipynb')


PLUGINS = ['gravatar', 'pelican_gist', 'pelican-page-hierarchy', 'pelican.plugins.liquid_tags', 'pelican_javascript']
LIQUID_TAGS = ["img", "youtube",  "notebook"]

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


