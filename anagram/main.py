import romkan
import itertools

src_hiragana = "あさって"

# Container of the anagrams generated
anagrams = []

# Note that only the vowels "a", "u", "o" can connect to
# these double consonants in MOFA's Hepburn Romaji
double_consonants = ["ky", "sh", "ch", "ny",
                     "hy", "my", "ry", "gy", "by", "py"]


def grow_stem(pool, stem=[]):
    '''(Unused function) Get a single char from the pool, append it to the stem'''

    global anagrams

    if len(pool) == 0:
        anagrams.append(stem)
    else:
        for i, char in enumerate(pool):
            new_stem = stem.copy()
            new_pool = pool.copy()

            new_stem.append(char)
            new_pool.pop(i)

            grow_stem(new_pool, new_stem)


def get_anagrams(src_str):
    '''Get list of anagrams for the list of chars given'''

    return itertools.permutations(src_str, len(src_str))


def decompose_hiraganas(hiraganas):
    '''Decompose the hiragana str into consonants & vowels'''

    alphabets = []

    # Convert hiragans into Romaji,
    # then divide string (e.g. "abc") into list (e.g. ["a", "b", "c"])
    alphabets[:0] = romkan.to_roma(hiraganas)

    vowels = []

    for i, alphabet in enumerate(alphabets):
        if alphabet in ["a", "e", "i", "o", "u"]:
            vowels.append(alphabets.pop(i))

    return {"consonants": alphabets, "vowels": vowels}


def group_consonants(consonants):
    collections = []

    return collections


anagrams = get_anagrams(["ch", "b", "y", "k"])
for v in anagrams:
    print(v)
# alphabets = decompose_hiraganas(src_hiragana)
# print(alphabets)
