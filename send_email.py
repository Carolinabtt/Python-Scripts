import socket
import socks # PySocks
import smtplib
from smtplib import SMTP
import sys

sys_profile = sys.getprofile()
sys.path
sys.platform
sys.prefix

# secure_smtplib - secure SMTP classes from mercurial
#
# Copyright 2006 Matt Mackall <mpm@selenic.com>
#
# This software may be used and distributed according to the terms of the
# GNU General Public License version 3 or any later version.

import smtplib
import socket
import ssl
import sys

class STARTTLS(smtplib.SMTP):
    '''Derived class to verify the peer certificate for STARTTLS.

    This class allows to pass any keyword arguments to SSL socket creation.
    '''
    def __init__(self, sslkwargs, **kwargs):
        smtplib.SMTP.__init__(self, **kwargs)
        self._sslkwargs = sslkwargs

    def starttls(self, keyfile=None, certfile=None):
        self.ehlo_or_helo_if_needed()
        if not self.has_extn("starttls"):
            msg = "STARTTLS extension not supported by server"
            raise smtplib.SMTPException(msg)
        (resp, reply) = self.docmd("STARTTLS")
        if resp == 220:
            self.sock = ssl.wrap_socket(
                self.sock,
                keyfile,
                certfile,
                **self._sslkwargs
            )
            if not hasattr(self.sock, "read"):
                # using httplib.FakeSocket with Python 2.5.x or earlier
                self.sock.read = self.sock.recv
            self.file = smtplib.SSLFakeFile(self.sock)
            self.helo_resp = None
            self.ehlo_resp = None
            self.esmtp_features = {}
            self.does_esmtp = 0
        return (resp, reply)

if hasattr(smtplib.SMTP, '_get_socket'):
    class SMTPS(smtplib.SMTP):
        '''Derived class to verify the peer certificate for SMTPS.

        This class allows to pass any keyword arguments to SSL socket creation.
        '''
        def __init__(self, sslkwargs, keyfile=None, certfile=None, **kwargs):
            self.keyfile = keyfile
            self.certfile = certfile
            smtplib.SMTP.__init__(self, **kwargs)
            self.default_port = smtplib.SMTP_SSL_PORT
            self._sslkwargs = sslkwargs

        def _get_socket(self, host, port, timeout):
            if self.debuglevel > 0:
                print >> sys.stderr, 'connect:', (host, port)
            new_socket = socket.create_connection((host, port), timeout)
            new_socket = ssl.ssl_wrap_socket(
                new_socket,
                self.keyfile,
                self.certfile,
                **self._sslkwargs
            )
            self.file = smtplib.SSLFakeFile(new_socket)
            return new_socket

#--- Send Email
remitente = "Desde gnucita <ebahit@member.fsf.org>"
destinatario = "Carolina Battaglia <carolina.battaglia@gmail.com>"
asunto = "E-mal HTML enviado desde Python"
mensaje = """Hola!<br/> <br/>
Este es un <b>e-mail</b> enviando desde <b>Python</b>
"""
email = """From: %s
To: %s
MIME-Version: 1.0
Content-type: text/html
Subject: %s

%s
""" % (remitente, destinatario, asunto, mensaje)
try:
    smtp = smtplib.SMTP('localhost', port=8080)
    smtp.sendmail(remitente, destinatario, email)
    print ("Correo enviado")
except:
    print ("""Error: el mensaje no pudo enviarse.
    Compruebe que sendmail se encuentra instalado en su sistema""")


address = 'carolina.battaglia@gmail.com'
user = 'carolina.battaglia@gmail.com'
password = 'Tash2945'

servername = 'smtps.gmail.com'
server = SMTP.connect(host=servername, port=0)
SMTP.login(self='',user='carolina', password='ooo', initial_response_ok=True)
#AttributeError: 'str' object has no attribute 'ehlo_or_helo_if_needed'
server = smtplib.SMTP('localhost', port=8080)
server = smtplib.SMTP('localhost')
server = smtplib.SMTP()
server.connect(host=servername, port=8080)
server.sendmail(remitente, destinatario, email)

socket.getaddrinfo('localhost', 8080)
SMTP.helo(name='')
#SMTP.verify(address='carolina.battaglia@gmail.com',self='')
self.debuglevel
