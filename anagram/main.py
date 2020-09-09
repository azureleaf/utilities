
# Container of the anagrams generated
anagrams = []


def grow_stem(pool, stem=[]):

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


def gen_anagrams(pool=[]):
    global anagrams

    # init the container
    anagrams = []

    grow_stem(pool)

    for anagram in anagrams:
        print(anagram)


gen_anagrams(["a", "b", "c"])
