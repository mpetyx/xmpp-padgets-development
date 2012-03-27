'''
Created on Mar 16, 2012

@author: mpetyx
'''
import sleekxmpp

client = sleekxmpp.ClientXMPP(None, None, ssl=True)#S,resource='OptionalResource')
client.connect(('147.102.6.34', 5222))