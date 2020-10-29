"""

:mod:`Tor2Web`
=====================================================

.. automodule:: Tor2Web
   :synopsis: [GLOBALEAKS_MODULE_DESCRIPTION]

.. moduleauthor:: Arturo Filasto' <art@globaleaks.org>
.. moduleauthor:: Giovanni Pellerano <evilaliv3@globaleaks.org>

"""

# -*- coding: utf-8 -*-

import re
import socket

from twisted.protocols import tls


def listenTCPonExistingFD(reactor, fd, factory):
    return reactor.adoptStreamPort(fd, socket.AF_INET, factory)


def listenSSLonExistingFD(reactor, fd, factory, contextFactory):

    tlsFactory = tls.TLSMemoryBIOFactory(contextFactory, False, factory)
    port = listenTCPonExistingFD(reactor, fd, tlsFactory)
    port._type = 'TLS'
    return port


def re_sub(pattern, replacement, string):
    return re.sub(pattern, replacement, string)


def is_onion(hostname):
    """
    Check to see if the address is a .onion.
    returns the onion address as a string if True else returns False
    """
    pattern = re.compile('^([a-z0-9]){16,56}.onion$')
    return pattern.match(hostname) is not None
