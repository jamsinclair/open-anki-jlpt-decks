# open-anki-jlpt-decks
[![CI workflow](https://github.com/jamsinclair/open-anki-jlpt-decks/actions/workflows/ci.yml/badge.svg)](https://github.com/jamsinclair/open-anki-jlpt-decks/actions/workflows/ci.yml)

> Open source and updatable JLPT vocabulary Anki decks.

This project contains the notes for vocabulary used in JLPT (Japanese-Language Proficiency Test) tests from N1 to N5. Flashcard decks, for the spaced repetition software [Anki](https://apps.ankiweb.net/), are generated from the notes.

The notes are stored in csv files to allow easy editing and reviewing of changes. Newer decks will be generated from any changes.

You can see the notes for each test level:
- [**N1 Vocabulary List**](src/n1.csv)
- [**N2 Vocabulary List**](src/n2.csv)
- [**N3 Vocabulary List**](src/n3.csv)
- [**N4 Vocabulary List**](src/n4.csv)
- [**N5 Vocabulary List**](src/n5.csv)

This project aims to solve many problems with existing anki decks that grow stale. This project gives **you** the **power** to help everyone.
- Notice a mistake? Easy you can fix it 💪
- Missing relevant JLPT vocab? Send us a reputable source and let's add it 🤓
- Ideas for improving the design and look of cards? Help us design it 👩‍🎨

For any improvements or suggestions please [create an issue](https://github.com/jamsinclair/open-anki-jlpt-decks/issues/new/choose).

| Question Template | Answer Template |
| :---: | :---: |
| <img alt="Question Template" src="screenshots/jp-question.png" width="320"> | <img alt="Answer Template" src="screenshots/jp-answer.png" width="320"> |
| <img alt="Question Template" src="screenshots/en-question.png" width="320"> | <img alt="Answer Template" src="screenshots/en-answer.png" width="320"> |

## Installation

### Ankiweb

The shared decks can be found on [Ankiweb's shared decks.](https://ankiweb.net/shared/decks/Open%20Anki%20JLPT)

Use the search term _"Open Anki JLPT"_ for best search result.

The downloaded file can then be imported into your Anki app of choice (Anki Desktop, Ankidroid etc.).

### Manual download

The `apkg` files can be downloaded directly from the [latest release page](https://github.com/jamsinclair/open-anki-jlpt-decks/releases/latest) and imported into your Anki app of choice.


## Guiding Principles

Use these principles to help guide changes to the project.

1. Card [questions and answers are as atomic as possible](http://augmentingcognition.com/ltm.html). Expressing one idea.
1. Card design is minimal and does not distract from the information
1. Only content relevant for active recall is present on the card

## How to contribute to the project?

Feel free to [create an issue](https://github.com/jamsinclair/open-anki-jlpt-decks/issues/new/choose) to let us know of any mistakes, improvements or other suggestions.

For those who feel comfortable changing CSV files or any code see the [contributing document](CONTRIBUTING.md) for more information.

## Acknowledgements
Original deck data was taken from https://github.com/chyyran/jlpt-anki-decks,
which were based on decks from tanos.co.uk
