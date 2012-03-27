'''
Created on Mar 15, 2012

@author: mpetyx
'''

import sleekxmpp.componentxmpp

class Example(sleekxmpp.componentxmpp.ComponentXMPP):

    def __init__(self, jid, password):
        sleekxmpp.componentxmpp.ComponentXMPP.__init__(self, jid, password, 'localhost', 8888)

        self.registerPlugin('xep_0030')
        self.registerPlugin('xep_0077')
        self.plugin['xep_0077'].setForm('username', 'password')

        self.add_event_handler("registered_user", self.reg)
        self.add_event_handler("unregistered_user", self.unreg)

    def reg(self, iq):
        msg = "Welcome! %s" % iq['register']['username']
        self.sendMessage(iq['from'], msg, mfrom=self.fulljid)

    def unreg(self, iq):
        msg = "Bye! %s" % iq['register']['username']
        self.sendMessage(iq['from'], msg, mfrom=self.fulljid)