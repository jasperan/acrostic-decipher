# Acrostic Decipher

Detect hidden acrostic messages in any text. Takes the first letter of each word in a sentence, concatenates them, and checks whether known English words appear in the resulting string.

Originally built to detect covert communication (e.g., inmates encoding messages in seemingly normal text). There's no widely available automated tool for this, so here's one.

## How It Works

1. Split the input text into sentences (on `. `)
2. For each sentence, take the first letter of every word to form an "acrostic string"
3. Search that string against a dictionary of 60,000+ English lemmas and word forms
4. Report any matches longer than 2 characters

## Prerequisites

- Python 3.8+
- No external dependencies (stdlib only)

## Installation

<!-- one-command-install -->
> **One-command install**: clone, configure, and run in a single step:
>
> ```bash
> curl -fsSL https://raw.githubusercontent.com/jasperan/acrostic-decipher/main/install.sh | bash
> ```
>
> <details><summary>Advanced options</summary>
>
> Override install location:
> ```bash
> PROJECT_DIR=/opt/myapp curl -fsSL https://raw.githubusercontent.com/jasperan/acrostic-decipher/main/install.sh | bash
> ```
>
> Or install manually:
> ```bash
> git clone https://github.com/jasperan/acrostic-decipher.git
> cd acrostic-decipher
> ```
> </details>

## Usage

```bash
# Run against the included sample text
python src/main.py
```

The script loads `data/lemmas_and_words.txt` (word dictionary) and `data/text.txt` (sample text to analyze), then prints any acrostic matches it finds:

```
Loaded words OK
Loaded text OK
had -> DmtmdbhtmrewmAlfbfiswcgdhadsfg ||| Full sentence: Divide morning them moved...
way -> Wayvoomw ||| Full sentence: Way a year very over own multiply winged
```

To analyze your own text, replace `data/text.txt` with your content, or modify `main()` in `src/main.py` to point at a different file.

## Word Dataset

The default dictionary (`data/lemmas_and_words.txt`) contains the top 60,000 lemmas plus word forms (100,000+ total). Swap this file for a domain-specific word list to detect different kinds of hidden messages.

## Project Structure

```
acrostic-decipher/
  src/main.py                  # Entry point and cipher detection logic
  data/
    lemmas_and_words.txt       # Default word dictionary (100K+ forms)
    text.txt                   # Sample text for analysis
    additional_datasets/       # Extra word lists
  docs/                        # Documentation
```

## Credits

- [dwyl](https://github.com/dwyl) for the [english-words](https://github.com/dwyl/english-words) alpha word list
- [worldfrequency.info](https://worldfrequency.info) for the most common English words dataset

## License

MIT