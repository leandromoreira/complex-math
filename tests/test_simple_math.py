from mock import Mock
import sure

from cmath.simple_math import add, add_remotely

def test_simple_math():
  add(1, 3).should.be.equals(4)

#Stubing
def test_simple_math_remotely():
  server = Mock()
  server.computes_add = Mock(return_value=3)

  add_remotely(1, 2, server).should.be.equals(3)


