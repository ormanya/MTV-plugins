###
# Copyright (c) 2020, liriel
# All rights reserved.
#
#
###

from supybot import utils, plugins, ircutils, callbacks, ircmsgs
from supybot.commands import *
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('MTVauth')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x

import requests, sys

class WebParser():
	"""Contains functions for getting and parsing web data"""

	def getWebData(self, irc, url):
		# Site returns bot error without headers - these could be added to a configuration variable
		headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'}
		try:
			content = requests.get(url, headers=headers)
			return content.json()
		except:
			irc.reply("Error: Couldn't connect to "+url)
			sys.exit()

class MTVauth(callbacks.Plugin):
	"""Authing users in MTV irc"""
	threaded = True

	def authCheck(self, irc, msg, args, site_nick, irc_key):
		"""<site_nick> <irc_key>
		Authorizes user with GroupServ, based on sitenick and IRC key.
		IRC key can be set at https://www.morethantv.me/user/security
		"""

		url = '{}/{}/{}'.format(self.registryValue('urlBase'), site_nick, irc_key)
		
		valid_user = WebParser().getWebData(irc,url)

		if valid_user: # == 'True':
			irc.sendMsg(ircmsgs.privmsg(self.registryValue('groupsrvNick'), self.registryValue('groupsrvString').format(site_nick)))
			irc.reply('Authorization successful')
		else:
			irc.reply('Authorization failed')

	auth = wrap(authCheck, ['anything', 'anything'])


Class = MTVauth


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
