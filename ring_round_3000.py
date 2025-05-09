import csv
import json
import ui_automator

def read_csv():
  people = []
  with open('test.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
      if(row[1]):
        people.append(person(row[0], row[1], row[2], row[3]))
  return people


def read_credentials():
  with open('credentials.json', 'r') as f:
    return json.load(f)


class person:
  def __init__(self, name, answered, meaningful_interaction, notes):
    self.name = name
    self.answered = answered
    self.meaningful_interaction = meaningful_interaction
    self.notes = notes

  def format_notes(self, date):

    message = f"Contacted during ring-round on {date}"

    if self.notes:
      message += f"\n \n Notes: {self.notes}"

    return message

if __name__ == "__main__":
    people = read_csv()
    ring_round_date = "29-Mar-2025"

    credentials = read_credentials()
    automator = ui_automator.ui_automator()
    automator.open_and_login(credentials['username'], credentials['password'])


    for p in people:
        try:
            automator.update_person(p, ring_round_date)
        except Exception as e:
            print(f"Error updating {p.name}. Error: {e}. Please update manually")

    # automator.close_browser()
    print("All done!")