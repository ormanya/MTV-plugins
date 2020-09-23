###
# Copyright (c) 2020, liriel
# All rights reserved.
#
#
###

from supybot import conf, registry
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('MTVauth')
except:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified themself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('MTVauth', True)


MTVauth = conf.registerPlugin('MTVauth')
# This is where your configuration variables (if any) should go.  For example:
# conf.registerGlobalValue(MTVauth, 'someConfigVariableName',
#     registry.Boolean(False, _("""Help for someConfigVariableName.""")))
conf.registerGlobalValue(MTVauth,'urlBase',
    registry.String('https://www.morethantv.me/user/checkirckey',"""Base URL for IRC authorization check endpoint""", private=True))

conf.registerGlobalValue(MTVauth,'groupsrvNick',
    registry.String('GroupServ',"""The nick to use for GroupServ""", private=True))

conf.registerGlobalValue(MTVauth,'groupsrvString',
    registry.String('FLAGS !mtv-users {} +cv',"""String to send to GroupSrv for authorization""", private=True))

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
