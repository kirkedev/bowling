from unittest import TestCase
from bowling.score import score_throw

class ScoringTest(TestCase):
  def test_x_is_ten(self):
    self.assertEqual(score_throw('X'), 10)
