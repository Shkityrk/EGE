#import socks, socket, urllib
#
#url = "http://hss3uro2hsxfogfq.onion"
#
#def create_connection(address, timeout=None, source_address=None):
#    sock = socks.socksocket()
#    sock.connect(address)
#    return sock
#
#socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150, True)
#socket.socket = socks.socksocket
#socket.create_connection = create_connection
#
#contents = urllib.urlopen(url).read()
#print contents