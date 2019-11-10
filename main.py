import argparse
from NFLPredictor import NFLPredictor

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dvoa", help="dvoa statistic CSV file", required=True)
parser.add_argument("-t", "--home", help="home team", required=True)
parser.add_argument("-a", "--away", help="away team", required=True)

if __name__== "__main__":
  args = parser.parse_args()
  nfl_predictor = NFLPredictor(args.dvoa)
  home_perc, away_perc = nfl_predictor.getWinningPercentages(args.home, args.away)
  print("Winning Percentages:")
  print(args.home + ": " + home_perc)
  print(args.away + ": " + away_perc)
