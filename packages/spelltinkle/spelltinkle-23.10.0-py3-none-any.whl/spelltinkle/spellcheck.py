import argparse
import sys
from pathlib import Path
import re

import enchant


def check(word: str) -> list[str]:
    d = enchant.Dict('en_US')
    if d.check(word):
        return []
    return d.suggest(word)


def find_words(text, kind: str) -> list[tuple[int, str]]:
    """Find words in text.

    Here is a typo: Pyton.
    """
    parts = []
    if kind == 'py':
        # Python code
        for m in re.finditer(r'  # ', text):
            i = m.end()
            parts.append((i, text[i:].split('\n', 1)[0]))
        for m in re.finditer(r'""".*?"""', text, re.DOTALL):
            i, j = m.span()
            parts.append((i + 3, text[i + 3:j - 3]))

    words = []
    for i, part in parts:
        for m in re.finditer(r'\w+', part):
            words.append((i + m.start(), m[0]))
    words.sort()
    w = 0
    i1 = 0
    for y, line in enumerate(text.splitlines()):
        i2 = i1 + len(line) + 1
        while w < len(words):
            i, word = words[w]
            if i1 <= i < i2:
                yield y, i - i1, word
                w += 1
            else:
                break
        i1 = i2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', default='-')
    args = parser.parse_args()
    if args.filename == '-':
        text = sys.stdin.read()
        kind = 'txt'
    else:
        text = Path(args.filename).read_text()
        kind = args.filename.rsplit('.')[-1]

    words = find_words(text, kind)
    for y, x, word in words:
        suggestions = check(word)
        if suggestions:
            print(y + 1, x + 1, word, ','.join(suggestions))


if __name__ == '__main__':
    main()
