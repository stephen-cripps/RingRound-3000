# I need to:
# Read test.csv
# Login to nationbuilder
# Loop over the rows in test.csv
# Find Person
# Log contact

# Print errors to add manually

import csv
import json
import UiAutomator

def read_csv():
  people = []
  with open('test.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
      people.append(person(row[0], row[1], row[2]))
  return people


def read_credentials():
  with open('credentials.json', 'r') as f:
    return json.load(f)


class person:
  def __init__(self, name, answered, notes):
    self.name = name
    self.answered = answered
    self.notes = notes


people = read_csv()
credentials = read_credentials()

UiAutomator.open_and_login(credentials['username'], credentials['password'])
