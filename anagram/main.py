

def show_anagrams(pool, stem=[]):

    if len(pool) == 0:
        print("result", stem)
    else:
        for i, char in enumerate(pool):
            new_stem = stem
            new_pool = pool

            new_stem.append(char)
            new_pool.pop(i)

            print(i, "stem", new_stem, "pool", new_pool)

            show_anagrams(new_pool, new_stem)


show_anagrams(["a", "b", "c"])
