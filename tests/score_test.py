from unittest import TestCase
from bowling.score import score_throw, score_throws, score_game, split_frames

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

  # def test_multiple_throws_strike(self):
  #   self.assertEqual(score_game('X12'), 16)

  # def test_multiple_throws_spare(self):
  #   self.assertEqual(score_game('4/12'), 14)
  #   self.assertEqual(score_game('5/5/5/5/5/5/5/5/5/5/5'), 150)

  def test_split_frame(self):
    self.assertEqual(list(split_frames('9-XX')), ['9-', 'XX', 'X'])

  def test_split_frames_with_tenth(self):
    self.assertEqual(list(split_frames('XXXXXXXXXXXX')),
      ['XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX', 'XXX'])

    self.assertEqual(list(split_frames('5/5/5/5/5/5/5/5/5/5/5')),
      ['5/5', '5/5', '5/5', '5/5', '5/5', '5/5', '5/5', '5/5', '5/5', '5/5'])

  # def test_score_tenth(self):
  #   self.assertEqual(score_throws('5/5'), 15)
