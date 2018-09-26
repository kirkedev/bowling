import sys
from bowling.score import score_game

game = sys.argv[1]

if not game:
  exit("Enter a string of bowling throws to score. Example: bin/bowling XXXXXXXXXXXX")

print(list(score_game(game)))
