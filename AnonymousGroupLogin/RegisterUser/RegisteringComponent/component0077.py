'''
Created on Mar 15, 2012

@author: mpetyx
'''

import sleekxmpp.componentxmpp
from optparse import OptionParser
import os
import sys
import logging
import logging.handlers

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

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
        
if __name__ == '__main__':
    #parse command line arguements

    optp = OptionParser()
    optp.add_option('--daemon', action="store_true", dest='daemonize', help="run as daemon")
    optp.add_option('-q','--quiet', help='set logging to ERROR', action='store_const', dest='loglevel', const=logging.ERROR, default=None)
    optp.add_option('-d','--debug', help='set logging to DEBUG', action='store_const', dest='loglevel', const=logging.DEBUG, default=None)
    optp.add_option('-v','--verbose', help='set logging to COMM', action='store_const', dest='loglevel', const=5, default=None)
    optp.add_option("-c","--config", dest="configfile", default="config.ini", help="set config file to use")
    opts,args = optp.parse_args()
    
    config = configparser.RawConfigParser()
    config.read(opts.configfile)
    
    xmpp = sleekxmpp.componentxmpp.ComponentXMPP(config.get('pubsub', 'host'), config.get('pubsub', 'secret'), config.get('pubsub', 'server'), config.getint('pubsub', 'port'))
    
    #load config
    settings = {
            'node_creation': config.get('settings', 'node_creation'),
            #'addtorosteraddtonode': config.getboolean('settings', 'addtorosteraddtonode'),
            'eventsfromsubscribedjid': config.getboolean('settings', 'eventsfromsubscribedjid'),
            'eachjiduserisnode': config.getboolean('settings', 'eachjiduserisnode'),
            }

    rest = {
            'enabled': config.getboolean('rest', 'enabled'),
            'server': config.get('rest', 'server'),
            'port': config.getint('rest', 'port'),
            'user': config.get('rest', 'user'),
            'passwd': config.get('rest', 'passwd'),
            'userasjid':config.get('rest', 'userasjid'),
            }
    
    
    overridedefault = {}
    for option in config.options('defaultnodeconfig'):
        overridedefault[option] = config.get('defaultnodeconfig', option)

    pubsub = Example(xmpp, config.get('pubsub', 'dbfile'), settings, rest, overridedefault)
  
    if xmpp.connect():
        xmpp.process(threaded=False)
        #xmpp.disconnect()        
        logging.info("Saving...")
        pubsub.save() 
        #sys.exit(retCode)
    else:
        logging.log(logging.CRITICAL, "Unable to connect.")
    