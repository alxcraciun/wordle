import os, sys, constants, math, functools, itertools

dict = []

cache_table = [0] * (391)

def filter_by_match(match_code, match_pos, match_char):
    hash = (ord(match_char) - ord('A')) + match_pos * 26 + 26 * 5 * match_code
    if cache_table[hash] == 0:
        if match_code == constants.FULL_MATCH:
            cache_table[hash] = {x for x in dict if x[match_pos] == match_char}
        elif match_code == constants.PARTIAL_MATCH:
            cache_table[hash] = {x for x in dict if x[match_pos] != match_char and match_char in x}
        else:
            cache_table[hash] = {x for x in dict if match_char not in x}
    return [hash], cache_table[hash]

def get_match_info(guess, answer):
    def letter_info(pos):
        if guess[pos] == answer[pos]:
            return constants.FULL_MATCH
        elif guess[pos] in answer:
            return constants.PARTIAL_MATCH
        else:
            return constants.NO_MATCH
    return [(letter_info(pos), pos) for pos in range(len(guess))]

cache_dict = {}

def set_int(sa : tuple[tuple[int], set], sb: tuple[tuple[int], set]):
    hash = tuple(sorted(set(sa[0] + sb[0])))
    if cache_dict.get(hash, None) == None:
        cache_dict[hash] = (list(hash), sa[1] & sb[1])
    return cache_dict[hash]    

def calculate_entropy(guess):
    entropy = 0
    for answer in dict:
        match = sorted(get_match_info(guess, answer), reverse=True)
        match_lists = [filter_by_match(match_code, match_pos if match_code != 0 else 0, guess[match_pos]) for match_code, match_pos in match]
        match_space = functools.reduce(set_int, match_lists)[1]
        information = math.log2(len(dict) / len(match_space))
        entropy += information
    entropy /= len(dict)
    return entropy

def main():
    global dict
    try:
        with open(os.path.join(sys.path[0], constants.DICT)) as file:
            dict = file.read().split()
    except FileNotFoundError:
        print(f"{constants.DICT} not found")
        sys.exit(2)
    filter_by_match.dict = dict
    entropy_values = [0] * len(dict)
    cache = 0
    for i in range(len(dict)):
        entropy_values[i] = calculate_entropy(dict[i])
        if not(i%100):
            print(f"{i/len(dict) * 100}%", file=sys.stderr, flush=True)
    print(entropy_values, sep='\n')


if __name__ == "__main__":
    main()
