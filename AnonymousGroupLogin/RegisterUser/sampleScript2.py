'''
Created on Mar 15, 2012

@author: mpetyx
'''

from xep_0077 import Registration 
from sleekxmpp.xmlstream import ElementBase, register_stanza_plugin 
from sleekxmpp import Iq 
from sleekxmpp.xmlstream import XMLStream 
import logging 

log = logging.getLogger('sleekxmpp') 
log.setLevel(logging.DEBUG) 
ch = logging.StreamHandler() 
ch.setLevel(logging.DEBUG) 
formatter = logging.Formatter('%(message)s') 
ch.setFormatter(formatter) 
log.addHandler(ch) 


def bbb(*args): 
    def __init__(self): 
        print(args) 

stream = XMLStream() 
stream.response_timeout = 15 

stream.connect(host = '147.102.6.34', port = 5222) 
print(stream.new_id()) 

register_stanza_plugin(Iq, Registration) 


iq = Iq(stream=stream, stype='set') 

iq['to'] = 'gic' 
iq['register']['username'] = 'epukouklaki@gic' 
iq['register']['password'] = 'bar' 


print('iq.send = ' + str(iq.send())) 