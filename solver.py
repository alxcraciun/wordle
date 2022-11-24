import os, sys, constants, math, functools, dataclasses, argparse

database = []

try:
    with open(os.path.join(sys.path[0], constants.DICT)) as file:
        database = tuple(file.read().split())
except FileNotFoundError:
    print(f"ERROR: {constants.DICT} not found", file=sys.stderr)
    sys.exit(constants.ERROR_FILE_NOT_FOUND)

cache_table = [0] * (391)
cache_dict = {}

@dataclasses.dataclass(frozen=True)
class MatchSet:
    hashes: tuple[int]
    matches: set[str]

@dataclasses.dataclass(frozen=True)
class MatchInfo:
    code: int
    pos: int
    char: str

def get_match_hash(match : MatchInfo):
    return (ord(match.char) - ord('A')) + ((match.pos * 26) if match.code != 0 else 0) + 26 * 5 * match.code

def merge_hash_tuples(l1 : tuple[int], l2 : tuple[int]):
    return tuple(sorted(l1 + l2))

def filter_by_match(match : MatchInfo):
    hash = get_match_hash(match)
    if cache_table[hash] == 0:
        if match.code == constants.FULL_MATCH:
            cache_table[hash] = {x for x in database if x[match.pos] == match.char}
        elif match.code == constants.PARTIAL_MATCH:
            cache_table[hash] = {x for x in database if x[match.pos] != match.char and match.char in x}
        else:
            cache_table[hash] = {x for x in database if match.char not in x}
    return cache_table[hash]

def get_match_info(guess : str, answer : str):
    def letter_info(pos):
        if guess[pos] == answer[pos]:
            return constants.FULL_MATCH
        elif guess[pos] in answer:
            return constants.PARTIAL_MATCH
        else:
            return constants.NO_MATCH
    return [MatchInfo(letter_info(pos), pos, guess[pos]) for pos in range(len(guess))]

def reduce_sets(s1 : MatchSet, s2 : MatchSet):
    hash = merge_hash_tuples(s1.hashes, s2.hashes)
    if cache_dict.get(hash) == None:
        cache_dict[hash] = s1.matches & s2.matches
    return MatchSet(hash, cache_dict[hash])

def get_match_space(matches : list[MatchInfo]):
    sets : list[MatchSet] = [MatchSet((get_match_hash(m),), filter_by_match(m)) for m in matches]
    return functools.reduce(reduce_sets, sets).matches

def calculate_entropy(guess : str, prev_info: list[MatchInfo] = []):
    #TODO: WORDS AFTER OPENER NOT IMPLEMENTED YET
    entropy = 0
    for answer in database:
        match = sorted(get_match_info(guess, answer), reverse=True, key=lambda x : x.code)
        match_space = get_match_space(match)
        information = math.log2(len(database) / len(match_space))
        entropy += information
    entropy /= len(database)
    return entropy

def calculate_opener():
    print("Calculating Wordle opener entropies...")
    print("Using PyPy is recommended...")
    entropy_values = [0] * len(database)
    for i in range(len(database)):
        entropy_values[i] = calculate_entropy(database[i])
        if not(i%100):
            print(f"{(i+1)/len(database) * 100}%", flush=True)
    with open("entropii.txt", mode='w') as file:
        for val in zip(entropy_values, database):
            print(f"{val[1]} -> {val[0]}", file=file)
    with open("entropii_sortate.txt", mode='w') as file:
        for val in sorted(zip(entropy_values, database), reverse=True):
            print(f"{val[1]} -> {val[0]}", file=file)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--openers', action='store_true', help='calculate entropies for all possible openers')
    args = parser.parse_args()
    if args.openers:
        calculate_opener()
        return
    #TODO: IPC NOT IMPLEMENTED YET


if __name__ == "__main__":
    main()
