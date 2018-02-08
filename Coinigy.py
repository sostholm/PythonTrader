import logging
from socketclusterclient import Sockercluster

logging.basicConfig(format ="%s(levelname)s:%(message)s", level=logging.DEBUG)

import json

api_credentials = json loads('{}')
api_credentials["apiKey"] = "6bc0738a92f985678777b5f2b90d2ce0"
api_credentials["apiSecret"] = "cc94c0a1e151a30f55588c8d917f01c9"

def starting(socket):
    ##sub code
    socket.subscribe('TICKER')

    def channelmessage(key, data):
        print("\n\n\n Got data " +json.dumps(data, sort_keys=True)+ "from channel "+key)

    socket.onchannel('TICKER', channelmessage)

    def ach(eventname, error, data):
        print('\n\n\nGot ach data ' + json.dumps(data, sort_keys=True) + ' and eventname is ' +eventname)

    socket.emitack('exhanges', None, ack)
    socket.emotack('exchanges', None, ack)

def onconnect(socket):
    logging.info('on connect got called')

def ondisconnect(socket):
    logging.info('on disconnect got called')

def onConnectError(socket, error):
    logging.info('On connect error got called')

def onSetAuthentication(socket, token):
    logging.info('Token recieved ' +token)
    socket.setAuthtoken(token)

def onAuthentication(socket, isauthenticated):
    logging.info('Authenticated is ' + str(isauthenticated))
    def ack(eventname, error, data):
        print('token is ' + json.dumps(data, sort_keys=True))
        starting(socket);

    socket.emitack('auth', api_credentials, ack)

if __name__ == "__main__":
    socket = Socketcluster.socket("wss://sc-02.coinigy.com/socketcluster/")
    socket.setBasicListener(onconnect, ondisconnect, onConnectError)
    socket.setAuthenticationListener(onSetAuthentication, onAuthentication)
    socket.setreconnection(false)
    socket.connect()
