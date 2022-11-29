import os, sys, constants, math, functools, dataclasses, argparse, ipc

database = []

try:
    with open(os.path.join(sys.path[0], constants.DICT)) as file:
        database = tuple(file.read().split())
except FileNotFoundError:
    print(f"ERROR: {constants.DICT} not found", file=sys.stderr)
    sys.exit(constants.ERROR_FILE_NOT_FOUND)

cache_table = [0] * (391)   # stocheaza cele 26 litere * 5 pozitii posibile * 3 variante culori
cache_dict = {}
cached_set = None

@dataclasses.dataclass(frozen=True)
class MatchSet:            
    hashes: tuple[int]      # hashurile seturilor care au fost intersectate
    matches: set[str]       # setul de cuvinte care au fost intersectate

@dataclasses.dataclass(frozen=True)     # frozen o face imutabila
class MatchInfo:
    code: int       # 0, 1, 2 pt o culoare
    pos: int        # pozitia pe care e culoarea
    char: str       # litera cu care avem acea culoare

def invalidate_cache():
    cache_table = [0] * (391)
    cache_dist = {}

def get_match_hash(match : MatchInfo):      # converteste structura MatchInfo intr-un hash 
    return (ord(match.char) - ord('A')) + ((match.pos * 26) if match.code != 0 else 0) + 26 * 5 * match.code

def merge_hash_tuples(l1 : tuple[int], l2 : tuple[int]):
    return tuple(sorted(l1 + l2))

def filter_by_match(match : MatchInfo, db=database):
    hash = get_match_hash(match)
    if cache_table[hash] == 0:
        if match.code == constants.FULL_MATCH:
            cache_table[hash] = {x for x in db if x[match.pos] == match.char}
        elif match.code == constants.PARTIAL_MATCH:
            cache_table[hash] = {x for x in db if x[match.pos] != match.char and match.char in x}
        else:
            cache_table[hash] = {x for x in db if match.char not in x}
    return cache_table[hash]

def get_match_info(guess : str, answer : str):
    def letter_info(pos):
        if guess[pos] == answer[pos]:
            return constants.FULL_MATCH     # 2 - litera e verde
        elif guess[pos] in answer:
            return constants.PARTIAL_MATCH  # 1 - litera e galbena
        else:
            return constants.NO_MATCH       # 0 - litera e rosie
    return [MatchInfo(letter_info(pos), pos, guess[pos]) for pos in range(len(guess))]

def reduce_sets(s1 : MatchSet, s2 : MatchSet):
    hash = merge_hash_tuples(s1.hashes, s2.hashes)
    if cache_dict.get(hash) == None:
        cache_dict[hash] = s1.matches & s2.matches   # intersectia de set-uri
    return MatchSet(hash, cache_dict[hash])

def get_match_space(matches : list[MatchInfo], base_set = database):
    if matches == []:
        return database
    sets : list[MatchSet] = [MatchSet((get_match_hash(m),), filter_by_match(m, base_set)) for m in matches]
    return functools.reduce(reduce_sets, sets).matches

def calculate_entropy(guess : str, prev_info: list[MatchInfo] = []):
    global cached_set
    entropy = 0
    possible_words = get_match_space(prev_info) if prev_info != [] else database
    if possible_words != cached_set:
        cached_set = possible_words
        invalidate_cache()
    for answer in possible_words:
        match = sorted(get_match_info(guess, answer), reverse=True, key=lambda x : x.code)      # incep cu literele verzi
        match_space = get_match_space(match, possible_words)
        information = math.log2(len(possible_words) / len(match_space))       # informatie primita datorita cuvantului
        entropy += information      # formula entropiei
    entropy /= len(possible_words)        # deoarece probabilitatile cuvintelor sunt egale
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

def calculate_best_guess(prev_info : list[MatchInfo], hard_mode = False):
    if prev_info == []:
        return constants.OPENER
    db = database
    possible = list(get_match_space(prev_info))
    if len(possible) == 1:
        return possible[0]
    if hard_mode:
        db = possible
    entropy_values = [0] * len(db)
    for i in range(len(db)):
        entropy_values[i] = calculate_entropy(db[i], prev_info)
        if not(i%1000):
            print(f"{round((i+1)/len(db) * 100, 2)}%", flush=True)
    return sorted(zip(entropy_values, db), reverse=True)[0][1]

def parse_prev_data(msg):
    try:
        prev_data = []
        for pair in msg.split():
            for i, [char, code] in enumerate(zip(*pair.split("="))):
                prev_data.append(MatchInfo(int(code), i, char))
        return prev_data
    except:
        ipc.err()

def wait_for_command():
    #TODO: wait for GUI request on PORT + 1
    pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--openers', action='store_true', help='calculate entropies for all possible openers')
    parser.add_argument('--port', default=constants.PORT, help='port to use for IPC')
    args = parser.parse_args()
    if args.openers:
        calculate_opener()
        return
    ipc.set_port(args.port)
    while True:
        wait_for_command()
        ipc.write("LIST")
        prev_data = parse_prev_data(ipc.read())
        guess = calculate_best_guess(prev_data)
        ipc.write(guess)
        result = ipc.read()
        if result == "CASTIGAT":
            print("DONE")
            return
        elif result != "OK":
            ipc.err()

if __name__ == "__main__":
    main()
