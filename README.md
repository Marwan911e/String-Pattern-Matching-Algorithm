# 🔍 Naive String Pattern Matching Algorithm

> Implementation of a naive string pattern matching algorithm for finding all occurrences of a pattern in a text.

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Algorithm](https://img.shields.io/badge/Algorithm-Naive-orange.svg)]()
[![Status](https://img.shields.io/badge/Status-Educational-yellow.svg)]()

## Overview

This implementation demonstrates the naive approach to string pattern matching, which searches for all occurrences of a pattern within a given text by checking every possible position in the text.

### Key Features

- **Complete Detection**: Finds all pattern occurrences in the text
- **Simple Implementation**: Easy to understand algorithm logic
- **No Dependencies**: Pure Python implementation with no external libraries
- **Educational**: Well-documented code with clear explanations

## Quick Start

```bash
git clone https://github.com/yourusername/String-Pattern-Matching-Algorithm.git
cd String-Pattern-Matching-Algorithm
python naive.py
```

## Algorithm Details

**Naive String Matching**

- Time Complexity: O(n\*m) where n is text length and m is pattern length
- Space Complexity: O(1)
- Checks every position in the text by comparing characters with the pattern
- Returns a list of all starting indices where pattern is found

## How It Works

1. The algorithm iterates through each possible starting position in the text
2. For each position, it compares the pattern with the corresponding text segment
3. If a complete match is found, the position is recorded
4. The process continues until the entire text has been examined
5. Finally, all matching positions are reported

## Usage Example

The program provides a simple command-line interface:

```
Naive String Matching Algorithm
-------------------------------
Enter the text: ABABDABACDABABCABAB
Enter the pattern: ABABC

Searching for pattern in text...
Pattern found at 1 position(s):
  Index 10: 'ABABC'
```

## Code Structure

```python
def naive_string_matching(text, pattern):
    """
    Implements the naive string matching algorithm

    Args:
        text (str): The text to search in
        pattern (str): The pattern to search for

    Returns:
        list: List of starting indices where pattern is found
    """
    # Implementation details...

def main():
    """Main function to handle user input and display results"""
    # User interaction code...

if __name__ == "__main__":
    main()
```

## Limitations

- The naive approach has O(n\*m) time complexity, which is not optimal for large texts
- Performance degrades significantly with longer texts and patterns
- More efficient algorithms (like KMP, Boyer-Moore, or Rabin-Karp) are recommended for production use

## Educational Purpose

This implementation is primarily for educational purposes to understand:

- The basic concept of string pattern matching
- How a brute force approach works
- The foundation upon which more efficient algorithms are built

## Requirements

- Python 3.7 or higher
- No external dependencies
- Cross-platform support (Windows, macOS, Linux)

---

**Created as a course assignment for Algorithms (Term 6)**
