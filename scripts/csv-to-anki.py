#!/usr/bin/env python3
import csv
import genanki
import os
import sys


def fileToStr(path):
    with open(path, "r") as myfile:
        data = myfile.read()
    return data


qfmt = fileToStr("src/templates/question.html")
afmt = fileToStr("src/templates/answer.html")
css = fileToStr("src/templates/styles.css")

deckInfos = [
    {"id": 1116267102, "name": "Open Anki JLPT N5 Deck", "csv": "src/n5.csv"},
    {"id": 2097673790, "name": "Open Anki JLPT N4 Deck", "csv": "src/n4.csv"},
    {"id": 1859281248, "name": "Open Anki JLPT N3 Deck", "csv": "src/n3.csv"},
    {"id": 1482466869, "name": "Open Anki JLPT N2 Deck", "csv": "src/n2.csv"},
    {"id": 1626470530, "name": "Open Anki JLPT N1 Deck", "csv": "src/n1.csv"},
]

deckDescription = """Open source and updatable JLPT Anki Decks to help you learn Japanese.

                     Visit <a href="https://github.com/jamsinclair/open-anki-jlpt-decks">https://github.com/jamsinclair/open-anki-jlpt-decks</a> for more information"""
model = genanki.Model(
    2000494194,
    "Open Anki JLPT Vocab",
    fields=[{"name": "expression"}, {"name": "reading"}, {"name": "meaning"}],
    templates=[{"name": "JLPT Expressions", "qfmt": qfmt, "afmt": afmt},],
    css=css,
)


def toKebabCase(str):
    return str.lower().replace(" ", "-")


def createDeckFromCsv(id, name, description, csvPath):
    deck = genanki.Deck(id, name, description)
    with open(csvPath, mode="r") as csvFile:
        reader = csv.reader(csvFile)
        lineCount = 0
        for row in reader:
            if lineCount > 0:
                note = genanki.Note(model=model, fields=row[0:3], tags=row[3].split())
                deck.add_note(note)
            lineCount += 1
    return genanki.Package(deck)


def generateDecks(tag=""):
    if not os.path.exists("decks"):
        os.makedirs("decks")

    for deckInfo in deckInfos:
        deck = createDeckFromCsv(
            deckInfo["id"], deckInfo["name"], deckDescription, deckInfo["csv"]
        )
        fileName = toKebabCase(deckInfo["name"])
        if tag:
            fileName += "-" + tag
        deck.write_to_file("decks/{}.apkg".format(fileName))


if __name__ == "__main__":
    tag = sys.argv[1] if len(sys.argv) > 1 else ""
    generateDecks(tag)
