from unittest import TestCase
from bowling.score import score_throw, score_throws, find_strikes

class ScoringTest(TestCase):
  def test_x_is_ten(self):
    self.assertEqual(score_throw('X'), 10)

  def test_spare_is_ten(self):
    self.assertEqual(score_throw('/'), 10)

  def test_miss_is_zero(self):
    self.assertEqual(score_throw('-'), 0)

  def test_other_is_value(self):
    self.assertEqual(score_throw('9'), 9)
    self.assertEqual(score_throw('5'), 5)

  def test_multiple_throws(self):
    self.assertEqual(score_throws('9876'), 30)
    self.assertEqual(score_throws('----'), 0)
    self.assertEqual(score_throws('9--6'), 15)

  def test_find_strike(self):
    self.assertEqual(list(find_strikes('X12')), [0])
    self.assertEqual(list(find_strikes('X1X11')), [0, 2])

  def test_multiple_throws_strike(self):
    self.assertEqual(score_throws('X12'), 16)
