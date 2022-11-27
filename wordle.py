import random, sys, queue, argparse, dataclasses, threading, constants, ipc

database = []

try:
    database = open('cuvinte_wordle.txt').read().split()
except:
    print("Fisierul 'cuvinte_wordle.txt' nu exista")
    sys.exit(constants.ERROR_FILE_NOT_FOUND)

@dataclasses.dataclass(frozen=True)
class TermInput:
    input: str

@dataclasses.dataclass(frozen=True)
class TermOutput:
    output: str
    end: bool

@dataclasses.dataclass(frozen=True)
class IPCInput:
    input: str

@dataclasses.dataclass(frozen=True)
class IPCOutput:
    output: str
    end: bool

input_queue = queue.Queue()
ipc_out_queue : queue.Queue[IPCOutput] = queue.Queue()

def ipc_input_thread():
    try:
        while True:
            word = ipc.read()
            input_queue.put(IPCInput(word))
            out = ipc_out_queue.get()
            ipc.write(out.output)
            if out.end:
                break
    except Exception as e:
        ipc.err()

def user_input_thread():
    if constants.DEBUG_IPC:
        while True:
            pass
    try:
        while True:
            word = input()
            input_queue.put(TermInput(word))
    except (KeyboardInterrupt, EOFError) as e:
        return

def get_match_info(guess, answer):
    assert(len(guess) == len(answer))
    def get_letter_info(pos):
        if guess[pos] == answer[pos]:
            return constants.FULL_MATCH
        elif guess[pos] in answer:
            return constants.PARTIAL_MATCH
        else:
            return constants.NO_MATCH
    return [get_letter_info(i) for i in range(len(answer))]

def validate_word(word : str):
    if len(word) == 5 and word.isupper():
        return word
    raise argparse.ArgumentTypeError("invalid word")

def match_to_unicode(match : list[int]):
    conv = {2:'\u2713',1:'\u2727',0:'\u2717'}
    return "".join([conv[code] for code in match])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--secret-word', default=None, type=validate_word)
    parser.add_argument('--port', default=constants.PORT, help='port to use for IPC')
    args = parser.parse_args()
    ipc.set_port(args.port)
    if args.secret_word == None:
        secret_word = random.choice(database)
    else:
        secret_word = args.secret_word
    
    console_reader = threading.Thread(group=None, target=user_input_thread)
    console_reader.daemon = True
    console_reader.start()

    ipc_reader = threading.Thread(group=None, target=ipc_input_thread)
    ipc_reader.daemon = True
    ipc_reader.start()

    guess_history = []

    while [constants.FULL_MATCH] * 5 not in guess_history:
        msg = input_queue.get()

        if isinstance(msg, BaseException):
            raise msg

        elif isinstance(msg, TermInput):
            guess = msg.input

        elif isinstance(msg, IPCInput):
            if msg.input == "LIST":
                it = iter(guess_history)
                ipc_out_queue.put(IPCOutput(" ".join(f"{word}={''.join([str(x) for x in match])}" for word, match in zip(it, it)), False))
                continue
            elif len(msg.input) != 5 or not msg.input.isupper():
                ipc.err()
            guess = msg.input

        else:
            raise TypeError()

        if guess not in database:
            print("Invalid guess.")
            continue

        match = get_match_info(guess, secret_word)
        won = match == [constants.FULL_MATCH] * 5
        print(guess + "\n" + match_to_unicode(match) + "\n")

        if isinstance(msg, IPCInput):
            ipc_out_queue.put(IPCOutput("OK", False) if not won else IPCOutput("CASTIGAT", True))
            if won:
                while ipc_reader.is_alive():
                    pass # let IPC finish before exiting
                
        guess_history.append(guess)
        guess_history.append(match)

if __name__ == "__main__":
    main()
