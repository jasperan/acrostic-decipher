# acrostic-decipher
Decipher acrostic ciphers given any text or file

# How it works
The file in `data/words.txt` contains the top 25 nouns in English. It uses these words and tries to find them in sentences using the pattern described in the Acrostic Cipher. Sometimes jail inmates use this method to communicate. However, there is not an automatized process to detect these kind of messages. 

## Installation

<!-- one-command-install -->
> **One-command install** — clone, configure, and run in a single step:
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
> # See below for setup instructions
> ```
> </details>


## Word and lemma dataset
By default, the words that the program tries to find are included in a dataset that contains the top 60,000 lemmas + word forms (100,000+ forms) in English.

# Credits

Thank you to GitHub user [dwyl](https://github.com/dwyl) for providing a list of all alpha words (words that only have letters, no numbers or symbols). From [this repository](https://github.com/dwyl/english-words). You can use this list if you are interested in expanding the functionality of this repository.

Also, credits to [worldfrequency](https://worldfrequency.info) for providing with a list of the most common English words.