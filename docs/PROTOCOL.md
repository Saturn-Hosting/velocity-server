# Protocol Commands
**Authentication**
```
c2s registering
REGISTER username password

s2c too few args
ERR_NEEDMOREPARAMS

s2c too many args
ERR_TOOMANYPARAMS

s2c username in use
ERR_ALREADYREGISTRED

s2c register confirm
CONFIRM_REGISTER

c2s logging in
LOGIN username password

s2c incorrect login
ERR_INVALIDCREDENTIALS

s2c login confirm
CONFIRM_LOGIN
```

**Connection**
```
s2c ping
PING 912389

c2s ping
PONG 912389
```

**Messaging**
```
c2s sending a message
MSG :hello world

s2c not logged in
ERR_NOAUTH

s2c receiving message
MSG username :hello world

c2s sending a dm
PRIVMSG username :hello world

s2c user not online
ERR_NOSUCHUSER

s2c receiving a dm
PRIVMSG sender :hello world

c2s fetching 10 messages from the index 50
FETCH 50

s2c receiving a fetched message
FETCH timestamp username :message
```

**Images**
```
c2s sending a image
IMAGE link

s2c receiving a image
IMAGE username link
```