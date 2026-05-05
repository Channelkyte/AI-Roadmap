# TextCleaner

A Python text preprocessing tool built using OOP principles.
Cleans raw text for NLP pipelines and AI applications.

---

## What it does

- Converts text to lowercase
- Removes punctuation, numbers, and extra spaces
- Removes common stopwords (the, is, a, and...)
- Tokenizes text into individual words
- Returns summary statistics (word count, unique words, top 5 words)
- Detects the language of the text using a free public API

---

## How to run it

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/textcleaner.git
cd textcleaner

# 2. Install dependencies
pip install requests python-dotenv

# 3. Add your text to input.txt

# 4. Run the program
python main.py
```

---

## Example output

```
TextCleaner — NLP Text Preprocessor
------------------------------------
Read 847 characters from input.txt
Created: TextCleaner(words=142, chars=847)
Cleaning complete.

========================================
         TEXT SUMMARY
========================================
  Word count    : 98
  Char count    : 612
  Unique words  : 76
  Avg word len  : 6.24 chars
  Top 5 words   :
    'learning' — 4x
    'text' — 3x
    'language' — 3x
    'data' — 2x
    'ai' — 2x
========================================

Detecting language: English (confidence: 99%)

Cleaned text saved to 'output.txt'
```

---

## Project structure

```
textcleaner/
├── cleaner.py     # TextCleaner class
├── main.py        # entry point
├── input.txt      # raw text input
├── .env           # API keys (not committed)
├── .gitignore
└── README.md
```

---

## Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `.lowercase()` | self | Convert to lowercase |
| `.remove_punctuation()` | self | Strip punctuation |
| `.remove_extra_spaces()` | self | Collapse whitespace |
| `.remove_numbers()` | self | Strip digits |
| `.remove_stopwords()` | self | Remove common words |
| `.tokenize()` | list | Split into words |
| `.word_count()` | int | Total word count |
| `.most_common(n)` | list | Top n frequent words |
| `.get_summary()` | dict | Full text statistics |
| `.detect_language()` | str | Language via API |
| `.clean_all()` | self | Run all steps at once |
| `.reset()` | self | Restore original text |

---

## What I learned

- Object-oriented programming: classes, `__init__`, `__repr__`, `__len__`, magic methods
- Method chaining by returning `self`
- File I/O with proper error handling
- Making HTTP API calls with the `requests` library
- Handling API errors gracefully (timeout, connection error, HTTP errors)

---

## Author

**Carl Joshua M. Coloma**
Computer Science — Software Engineering
AI Engineering Track | Phase 1 Project