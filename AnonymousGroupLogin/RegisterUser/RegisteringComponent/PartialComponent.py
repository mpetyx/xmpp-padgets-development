'''
Created on Mar 16, 2012

@author: mpetyx
'''

import sleekxmpp.componentxmpp


class Example(sleekxmpp.componentxmpp.ComponentXMPP):

    def __init__(self, jid, password):
        sleekxmpp.componentxmpp.ComponentXMPP.__init__(self, jid, password, '147.102.6.34', 5060)

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

#if __name__ == '__main__':
#    #parse command line arguements   

print "yo"
local = Example("mpetyx@gic","emp")#.connect("publishsubscribe@facebooknode")
iq = """<iq to="gic" type="set" id="1"><query xmlns="jabber:iq:register"><username>epukouklaki@gic</username><password>baraki</password></query></iq>"""

local.reg(iq)

#    xmpp = sleekxmpp.componentxmpp.ComponentXMPP("publishsubscribe@facebooknode", "test2xm", "147.102.6.34", "5060")
#
#    if xmpp.connect():
#        xmpp.process(threaded=False)
#        #xmpp.disconnect()        
#        #sys.exit(retCode)
#    else:
#        print "skatoulia"