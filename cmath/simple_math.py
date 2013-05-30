import mailer

def add(x, y):
  return x + y

def add_remotely(x, y, server):
  return server.computes_add(x, y)

def add_and_sends_email(x, y):
  z = x + y
  mailer.send(to='master@math.com', subject='Complex addition', body=('The result was %s' % z))
  return z

