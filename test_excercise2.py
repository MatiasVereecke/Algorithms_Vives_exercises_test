from exercise2 import luc, lucasRow, sumOfEvenLucasNumbers

def test_generateLucas():
  assert(3 == luc(2))
  assert(4 == luc(3))

def test_sumOfLucas():
  assert(2 == lucasRow(3))

def test_generateSumOfEvenLucasNumbers():
  assert(6 == sumOfEvenLucasNumbers(4))
  assert(24 == sumOfEvenLucasNumbers(7))
