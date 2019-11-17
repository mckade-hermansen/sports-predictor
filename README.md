# Sports Predictor
scripts used to predict scores of upcoming games

# Running The Script
## Setup
- Make sure python 2.7 is installed.
    - instillation can be found [here](https://www.python.org/download/releases/2.7/)
- Download script from git
    - If running on windows machine download the git shell first [here](https://gitforwindows.org/)
```
git clone https://github.com/mckade-hermansen/sports-predictor
```

## Arguments
To see a list of arguments run
```
python main.py -h
```
- `-d` DVOA CSV file to get statistics from
- `-t` the home team, should be abrievation from the csv file, (e.g., KC)
- `-a` the away team, should be abrievation from the csv file, (e.g., KC)

## Example
```
python main.py -d dvoa.csv -t SF -a SEA
```