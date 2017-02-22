import socket
from datetime import datetime


HOST = "irc.twitch.tv"
PORT = 6667
NICK = "paul7373"
PASS = 'oauth:lcxkpx9uwv22ncqh1fcy8qqcle87zl'
CHAN = 'roger9527'

def send_message(message):
    s.send(bytes("PRIVMSG #" + NICK + " :" + message + "\r\n", "UTF-8"))


s = socket.socket()
s.connect((HOST, PORT))
s.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))
s.send(bytes("NICK " + NICK + "\r\n", "UTF-8"))
s.send(bytes("JOIN #" + CHAN + " \r\n", "UTF-8"))


while True:
    line = str(s.recv(1024))
    if "End of /NAMES list" in line:
        break

while True:
    for source in s.recv(1024).decode('UTF-8').split('\\r\\n'):
        if len(source.split(':')) < 3:
            continue
        #print (source)
        username = source.split('.tmi.twitch.tv PRIVMSG')[0].split('@')[1]
        message = source.split('.tmi.twitch.tv PRIVMSG')[1].split('#' + CHAN + ' :')[1]
        line = u'<' + username + u'> ' + message
        print (datetime.now().strftime('[%H:%M:%S %Y-%m-%d]'), line[:-1])
