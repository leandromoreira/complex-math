from mock import Mock
import sure

from cmath.simple_math import add, add_remotely

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

