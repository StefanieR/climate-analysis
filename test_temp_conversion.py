#testing temperature conversion code

from temp_conversion import fahr_to_kelvin
from nose.tools import *

def test_random():
   assert fahr_to_kelvin(20.0)==266.48333333

def test_zero():
   assert fahr_to_kelvin(0.)==255.372222

@raises(TypeError)
def test_temp_string():
   assert fahr_to_kelvin("Sometemperature")

@raises(TypeError)
def test_null_temp():
   assert fahr_to_kelvin()
