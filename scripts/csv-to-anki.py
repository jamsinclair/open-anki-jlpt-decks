import csv
import genanki
import os

def fileToStr(path):
  with open(path, 'r') as myfile:
    data = myfile.read()
  return data

qfmt = fileToStr('src/templates/question.html')
afmt = fileToStr('src/templates/answer.html')
css = fileToStr('src/templates/styles.css')

decks = [{
  'id': 1116267102,
  'name': 'Open Anki JPLT N5 Deck',
  'csv': 'src/n5.csv'
}, {
  'id': 2097673790,
  'name': 'Open Anki JPLT N4 Deck',
  'csv': 'src/n4.csv'
}, {
  'id': 1859281248,
  'name': 'Open Anki JPLT N3 Deck',
  'csv': 'src/n3.csv'
}, {
  'id': 1482466869,
  'name': 'Open Anki JPLT N2 Deck',
  'csv': 'src/n2.csv'
}, {
  'id': 1626470530,
  'name': 'Open Anki JPLT N1 Deck',
  'csv': 'src/n1.csv'
}]

deckDescription = """Open source and updatable JPLT Anki Decks to help you learn Japanese.

                     Checkout https://github.com/jamsinclair/open-anki-jplt-decks for more information"""
model = genanki.Model(
  2000494194, 'Open Anki JPLT Vocab',
  fields=[{'name': 'expression'}, {'name': 'reading'}, {'name': 'meaning'}],
  templates=[
    {
      'name': 'JPLT Expressions',
      'qfmt': qfmt,
      'afmt': afmt
    },
  ],
  css=css
)

def toKebabCase(str):
  return str.lower().replace(' ', '-')

def createDeckFromCsv(id, name, description, csvPath):
  deck = genanki.Deck(id, name, description)
  with open(csvPath, mode='r') as csvFile:
    reader = csv.reader(csvFile)
    lineCount = 0
    for row in reader:
        if lineCount > 0:
          note = genanki.Note(model=model, fields=row[0:3], tags=row[3].split())
          deck.add_note(note)
        lineCount += 1
  genanki.Package(deck).write_to_file('decks/{}.apkg'.format(toKebabCase(name)))

def generateDecks():
  if not os.path.exists('decks'):
      os.makedirs('decks')

  for deck in decks:
    createDeckFromCsv(deck['id'], deck['name'], deckDescription, deck['csv'])

generateDecks()
