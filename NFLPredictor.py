from CSVParser import parse_dvoa

class NFLPredictor:

  def __init__(self, file_name):
    self.dvoa_data = parse_dvoa(file_name)
  
  def getWinningPercentages(self, home, away):
    if home not in self.dvoa_data:
      print(home + ' data not found in csv')
    if away not in self.dvoa_data:
      print(away + ' data not found in csv')

    home_perc = sum(self.dvoa_data[home])
    away_perc = sum(self.dvoa_data[away])
    home_perc *= 1.025 # home advantage bumps total dvoa by 2.5%
    total_perc = home_perc + away_perc
    
    home_perc = home_perc / total_perc * 100
    away_perc = away_perc / total_perc * 100

    return str(home_perc), str(away_perc)
