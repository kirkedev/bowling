import sys
from bowling.score import score_game

if len(sys.argv) < 2:
  print("Enter a string of bowling throws to score, where 'X' is a strike, '/' is a spare, and '-' is a gutter.")
  print("Example: bin/bowling XXXXXXXXXXXX")
  exit(1)

print(list(score_game(sys.argv[1])))
