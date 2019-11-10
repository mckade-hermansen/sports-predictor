import csv

def parse_dvoa(dvoa_file):
  """
  parses dvoa files with the following format
  [team, wei dvoa, off dvoa, deff dvoa, s.t. dvoa]

  the first row of the array stores the weights

  returns hash where the key is the team name that maps
  to an array of values
  """
  dvoa_data = {}

  with open(dvoa_file) as csv_file:
    file_data = csv.reader(csv_file, delimiter=',')
    for row in file_data:
      if row[1] != 'TEAM':
        dvoa_data[row[1]] = parse_dvoa_row(row)

  print_csv_data(dvoa_data)
  return dvoa_data

def parse_dvoa_row(row):
  """ remove percent signs from dvoa row """
  row_data = [s.strip('%') for s in row]
  return [
    float(row_data[4]), # weighted dvoa
    float(row_data[7]), # off dvoa
    float(row_data[9]) * -1, # deff dvoa but data is negative
    float(row_data[11])] # S.T. dvoa

def print_csv_data(csv_data):
  print("CSV Data:")
  for data in csv_data:
    print(data, csv_data[data])
