from mock import Mock, patch
import sure

from cmath.simple_math import add, add_remotely, add_and_sends_email, add_and_sum_with_rnd

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

#Stubing an internal dependency
@patch('cmath.nasa.random')
def test_simple_math_with_randon_generated_by_nasa(nasa_random_generator):
  nasa_random_generator.configure_mock(return_value=42)

  add_and_sum_with_rnd(3, 9).should.be.equals(54)

#Mocking an internal dependency
@patch('mailer.send')
def test_simple_math_that_sends_email(mailer_mock):
  add_and_sends_email(3, 9)

  mailer_mock.assert_called_once_with(to='master@math.com', subject='Complex addition', body='The result was 12')

