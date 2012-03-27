'''
Created on Mar 16, 2012

@author: mpetyx
'''

import logging
from CheshiR.SimpleBackend import SimpleBackend
from CheshiR.HTTPFrontend import HTTPFrontend
from CheshiR.Bot import Bot
from component0077 import Example

# Uncomment the following line to turn on debugging
#logging.basicConfig(level=logging.DEBUG, format='%(levelname)-8s %(message)s')

def main() :
    backend = SimpleBackend()
    bot = Bot("bot@cheshir.lit", "mypass", backend, "http://cheshir.lit")
    bot.start()
    httpFrontend = HTTPFrontend(8080, backend)
    httpFrontend.start()

if __name__ == '__main__' :
    main()
