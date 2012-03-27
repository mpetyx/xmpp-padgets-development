'''
Created on Mar 15, 2012

@author: mpetyx
'''

from xep_0077 import Registration
from sleekxmpp.xmlstream import ElementBase, register_stanza_plugin
from sleekxmpp import Iq
from sleekxmpp.xmlstream import XMLStream

server = "147.102.6.34"

stream = XMLStream(host=server, port=5222)

register_stanza_plugin(Iq, Registration)

iq = Iq(stream=stream, stype='set')

iq['register']['username'] = 'epukouklaki@gic'
iq['register']['password'] = 'baraki'
iq['to'] = "gic"

print iq

#iq.send()
