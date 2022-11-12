from functools import reduce
from typing import Dict, Generator, Iterable


def remove_noalpha(input: str) -> str:
    return "".join([c for c in input if c.isalnum()])


def words(sentence: str) -> Generator[str, None, None]:
    return (word for word in sentence.lower().split())


def words_alphnum(sentence: Iterable[str]) -> Generator[str, None, None]:
    return (remove_noalpha(word) for word in sentence)


# Soluzione 1
def words_count(sentence: Iterable[str]) -> Dict[str, int]:
    collected = list(sentence)
    unique = set(collected)

    return {
        word_key: len([word for word in collected if word == word_key])
        for word_key in unique
    }


# Soluzione 2
def words_count_reduce(sentence: Iterable[str]) -> Dict[str, int]:
    return reduce(
        lambda frequencies, word: {
            **frequencies,
            **{word: 1 + frequencies.get(word, 0)},
        },
        sentence,
        {},
    )


if __name__ == "__main__":
    input = "How much wood would a woodchuck chuck if a woodchuck would chuck wood? A woodchuck would chuck how much a woodchuck would chuck if a woodchuck would chuck wood?"
    expected = {
        "a": 5,
        "chuck": 5,
        "how": 2,
        "if": 2,
        "much": 2,
        "wood": 3,
        "woodchuck": 5,
        "would": 5,
    }

    word_count = words_count(words_alphnum(words(input)))
    assert word_count == expected

    word_count_reduce = words_count_reduce(words_alphnum(words(input)))
    assert word_count_reduce == expected
