'''
Created on Mar 19, 2012

@author: mpetyx
'''


from sleekxmpp.thirdparty.suelta.sasl import Mechanism, register_mechanism


class EXTERNAL(Mechanism):

    def __init__(self, sasl, name):
        super(EXTERNAL, self).__init__(sasl, name)

    def process(self, challenge=None):
        return ''

    def okay(self):
        return True

                                                                                                                                                                                     
register_mechanism('EXTERNAL', 90, EXTERNAL, use_hashes=False)

