import os, sys, constants, math, dataclasses

def calculate_entropy(guess, answer_space):
    def get_match_info(guess, answer):
        def letter_info(pos):
            if guess[pos] == answer[pos]:
                return constants.FULL_MATCH
            elif guess[pos] in answer[pos]:
                return constants.PARTIAL_MATCH
            else:
                return constants.NO_MATCH
        return [letter_info(pos) for pos in range(len(guess))]
    entropy = 0
    proc = 0
    for answer in answer_space:
        matching = 0
        match = get_match_info(guess, answer)
        for word in answer_space:
            if get_match_info(word, answer) == match:
                matching += 1
        information = math.log2(len(answer_space) / matching)
        entropy += information
        if not (proc % 100):
            print(proc / len(answer_space) * 100, '%')
        proc += 1
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
    entropy_values = [calculate_entropy(word, dict) for word in dict]
    print(entropy_values)

if __name__ == "__main__":
    main()
