# How to contribute

Thank you for reading this and helping improve the project! We all have the power to make Japanese learning more accessible, achievable and free.

Here are some important resources:

  * [Ankiweb documentation](https://docs.ankiweb.net) is great for both general Anki information and use of the web app
  * [Anki-Android's Database Structure](https://github.com/ankidroid/Anki-Android/wiki/Database-Structure), the best explanation of the Anki database structure
  * [Genanki documenation](https://github.com/kerrickstaley/genanki), the library used to generate our decks

Improvements for the code, card templates and japanese notes are all welcome.

Please see our [Guiding Principles](./README.md#guiding-principles) to help inform your changes.

## Setup

### Prerequisites:
- Python 3+
- Node.js 12+

### Installation

To install python dependencies:
```shell
pip install -r requirements.txt
# Or pip3 install -r requirements.txt
```

To install Node.js dependencies:
```shell
npm install
```

## Making Changes

### CSV Format

The CSV schema contains the following fields
- `expression` - The text of how the vocablurary would appear in a JLPT test
- `reading` - The reading of the text, usually expressed in hiragana or katakana
- `meaning` - The english meaning of the expression
- `tags` - Metadata for the note that could be used by various Anki apps for advanced customisation. The existing data are relics from the previous deck that the project was sourced from.
- `guid` - The “Globally Unique Identifier” used by Anki to keep a stable reference of notes. For new entries we can ignore adding this and the project should autogenerate a new guid. Changing this field would result in losing existing progress or history within your Anki app.

### Building

To build Anki `apkg` files from the CSVs run the script `scripts/generate-decks.py`.

To update screenshots of the templates run the command `npm run generate-screenshots`.

## Submitting changes

Please send a [GitHub Pull Request to open-anki-jlpt-decks](https://github.com/jamsinclair/open-anki-jlpt-decks/pull/new/master) and follow the Pull Request template.

## Coding conventions

* Python code is linted and formatted with [black](https://github.com/psf/black).
  
  After [installing](#installation) python dependencies, run from your terminal `black scripts` to format your code.
* JavaScript code is linted and formatted with [prettier-standard](https://github.com/sheerun/prettier-standard).
  
  After [installing](#installation) the node.js dependencies, run from your terminal `npm run format` to format your code.

Thanks!
