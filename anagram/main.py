import romkan

src_hiragana = "あした"

# Container of the anagrams generated
anagrams = []

# Note that only the vowels "a", "u", "o" can connect to
# these sequential consonants in MOFA's Hepburn Romaji
seq_consonants = ["ky", "sh", "ch", "ny", "hy", "my", "ry", "gy", "by", "py"]


def grow_stem(pool, stem=[]):
    '''Get a single char from the pool, append it to the stem'''

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


def get_anagrams(pool=[]):
    '''Get list of anagrams for the list of chars given'''

    global anagrams

    # init the container
    anagrams = []

    grow_stem(pool)

    return anagrams


def decompose_hiragana(hiraganas):
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


# gen_anagrams(["a", "b", "c"])
alphabets = decompose_hiragana(src_hiragana)
print(alphabets)
