import sys
from bowling.score import score_game

if len(sys.argv) < 2:
  exit("Enter a string of bowling throws to score. Example: bin/bowling XXXXXXXXXXXX")

print(list(score_game(sys.argv[1])))
