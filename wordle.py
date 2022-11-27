import random, sys, queue, argparse, dataclasses, threading

database = []

try:
    database = open('cuvinte_wordle.txt').read().split()
except:
    print("Fisierul 'cuvinte_wordle.txt' nu exista")
    sys.exit(1)

@dataclasses.dataclass(frozen=True)
class TermInput:
    input: str

@dataclasses.dataclass(frozen=True)
class TermOutput:
    output: str
    end: bool

input_queue = queue.Queue() # TermInput - input from console, must be responded to through console_out_queue.
                            # Exception - an input thread has exited
console_out_queue : queue.Queue[TermOutput] = queue.Queue()

def user_input_thread():
    try:
        while True:
            word = input("GUESS = ")
            input_queue.put(TermInput(word))
            out = console_out_queue.get()
            print(out.output)
            if out.end:
                input_queue.put(SystemExit())
                break
    except (KeyboardInterrupt, EOFError) as e:
        input_queue.put(e)


def validate_word(word : str):
    if len(word) == 5 and word.isupper():
        return word
    raise argparse.ArgumentTypeError("invalid word")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--secret-word', default=None, type=validate_word)
    args = parser.parse_args()
    if args.secret_word == None:
        secret_word = random.choice(database)
    else:
        secret_word = args.secret_word
    console_reader = threading.Thread(group=None, target=user_input_thread)
    console_reader.daemon = True
    console_reader.start()
    #TODO: IPC thread
    threads = [console_reader]
    while True:
        msg = input_queue.get()
        if isinstance(msg, BaseException):
            if True not in [t.is_alive() for t in threads]:
                break
            else:
                continue
        elif isinstance(msg, TermInput):
            guess = msg.input
        else:
            raise TypeError()
        out = str()
        for poz in range(5):
            if secret_word[poz] == guess[poz]:
                out += '✓'
            elif guess[poz] in secret_word:
                out += '✧'
            else:
                out += '✗'
        if isinstance(msg, TermInput):
            console_out_queue.put(TermOutput(guess + "\n" + out + "\n", out == "✓✓✓✓✓"))

if __name__ == "__main__":
    main()