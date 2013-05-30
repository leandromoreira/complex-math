from mock import Mock, patch
import sure

from cmath.simple_math import add, add_remotely, add_and_sends_email

def test_simple_math():
  add(1, 3).should.be.equals(4)

#Stubing
def test_simple_math_remotely_stubed():
  server = Mock()
  server.computes_add = Mock(return_value=3)

  add_remotely(1, 2, server).should.be.equals(3)

#Mocking
def test_simple_math_remotely_mocked():
  server = Mock()

  add_remotely(1, 2, server)

  server.computes_add.assert_called_once_with(1, 2)

#Mocking an internal dependency
@patch('mailer.send')
def test_simple_math_that_sends_email(mailer_mock):
  add_and_sends_email(3, 9)

  mailer_mock.assert_called_once_with(to='master@math.com', subject='Complex addition', body='The result was 12')

