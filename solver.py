import os, sys, constants, math, dataclasses

def calculate_entropy(guess, answer_space):
    def get_match_info(guess, answer):
        def letter_info(pos):
            if guess[pos] == answer[pos]:
                return constants.FULL_MATCH
            elif guess[pos] in answer:
                return constants.PARTIAL_MATCH
            else:
                return constants.NO_MATCH
        return [(letter_info(pos), pos) for pos in range(len(guess))]
    entropy = 0
    for answer in answer_space:
        match = sorted(get_match_info(guess, answer), reverse=True)
        match_space = answer_space
        for match_code, match_pos in match:
            if match_code == constants.FULL_MATCH:
                match_space = [x for x in match_space if x[match_pos] == answer[match_pos]]
            elif match_code == constants.PARTIAL_MATCH:
                match_space = [x for x in match_space if x[match_pos] != answer[match_pos] and x[match_pos] in answer]
            else:
                match_space = [x for x in match_space if x[match_pos] not in answer]
        information = math.log2(len(answer_space) / len(match_space))
        entropy += information
    entropy /= len(answer_space)
    return entropy

def main():
    dict = []
    try:
        with open(os.path.join(sys.path[0], constants.DICT)) as file:
            dict = file.read().split()
    except FileNotFoundError:
        print(f"{constants.DICT} not found")
        sys.exit(2)
    entropy_values = [0] * len(dict)
    for i in range(len(dict)):
        entropy_values[i] = calculate_entropy(dict[i], dict)
        print((i + 1) / len(dict) * 100, '%')
    print(entropy_values)

if __name__ == "__main__":
    main()
