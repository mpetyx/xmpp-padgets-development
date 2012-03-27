'''
Created on Mar 20, 2012

@author: mpetyx
'''

class admin:
    
    def __init__(self):
        """
        
        """
        self.server  = "147.102.6.34"
        self.port = 5222
        self.domain = "gic"
        
    def RegisterUser(self, jid, password):
        """
        This method is for registering new user to the xmpp server we use
        """
        from inServer.register_account2 import RegisterBot
        import ssl
        
        if self.domain not in jid:
            jid = jid + "@"+self.domain
        
        xmpp = RegisterBot(jid, password)
        xmpp.register_plugin('xep_0030') # Service Discovery
        xmpp.register_plugin('xep_0004') # Data forms
        xmpp.register_plugin('xep_0066') # Out-of-band Data
        xmpp.register_plugin('xep_0077') # In-band Registration
    
        # If you are working with an OpenFire server, you may need
        # to adjust the SSL version used:
        xmpp.ssl_version = ssl.PROTOCOL_SSLv3
    
        # If you want to verify the SSL certificates offered by a server:
        # xmpp.ca_certs = "path/to/ca/cert"
    
        # Connect to the XMPP server and start processing XMPP stanzas.
        if xmpp.connect((self.server,self.port)):
            # If you do not have the dnspython library installed, you will need
            # to manually specify the name of the server if it does not match
            # the one in the JID. For example, to use Google Talk you would
            # need to use:
            #
            # if xmpp.connect(('talk.google.com', 5222)):
            #     ...
            xmpp.process(block=True)
            print("Done")
        else:
            print("Unable to connect.")
        
        
    def RemoveUser(self):
        """
        We remove a user from the system given a specified jid ( or a nickname, full name of the user )
        """
        
    def RegisterAnonymous(self):
        """
        
        """
        
    def KickAnonymous(self):
        """
        
        """
        
    def AddToGroup(self):
        """
        
        """
        
    def RemoveFromGroup(self):
        """
        
        """
        
#admin = admin()
#admin.RegisterUser("otaspaw@gic", "1234")