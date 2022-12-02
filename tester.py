import subprocess
import queue
import threading
import time
import constants
import signal
import os
import argparse

lines = queue.Queue()
total_written = 0

def writer_thread(file):
    global total_written
    cnt = 0
    with open(file, "a") as solutii:
        while True:
            l = lines.get()
            total_written += 1
            if l == [-1]:
                return
            print(*l, file=solutii, flush=True, sep=' ', end='\n')
            cnt += 1
            print(f"Write {cnt}.")

def compute(db, port):
    print("Thread active,", threading.get_ident())
    for i in range(len(db)):
        line = [db[i]]
        solver = subprocess.Popen(["PyPy", "solver.py", "--port", str(port)], stdout=subprocess.DEVNULL)
        wordle = subprocess.Popen(["PyPy", "wordle.py", "--secret-word", db[i], "--port", str(port), "--no-gui"], stdout=subprocess.PIPE)
        out = wordle.communicate()[0]
        out = out.decode(encoding='utf8')
        wr = wordle.wait()
        sr = solver.wait()
        for word in out.split():
            if word.isalpha():
                line.append(word)
        if sr != 0 or wr != 0:
            print(f"ERROR: Return codes s={sr}, w={wr} on word {db[i]}")
            return
        if len(line) > 7:
            print(f"Word {db[i]} took over 6 tries")
        lines.put(line)
    print("Thread exiting,", threading.get_ident())
        
def main():
    global total_written

    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("--amount", default=-1, type=int, help="amount of words to process")
    parser.add_argument("--processes", default=10, type=int, help="how many processes should be used")
    args = parser.parse_args()
    maxt = args.processes
    threading.Thread(group=None, target=writer_thread, daemon=True, args=[args.file]).start()
    prevr = 0
    db = open("cuvinte_wordle.txt").read().split()
    if args.amount != -1:
        db = db[:args.amount]
    full_len = len(db)
    already_done = [ln.split()[0] for ln in open(args.file).readlines()]
    total_written += len(already_done)
    db = [x for x in db if x not in already_done]
    work : list[threading.Thread] = []
    for i in range(maxt):
        l = prevr
        r = min(len(db) - 1, l + len(db)//maxt)
        tmp_db = db[l:r+1]
        work.append(threading.Thread(group=None, target=compute, args=(tmp_db, constants.PORT + i + 1)))
        work[-1].start()
        prevr = r + 1

    signal.signal(signal.SIGINT, lambda *args : os._exit(1))

    while work:
        time.sleep(1)
        print(total_written/full_len*100,'%')
        work = [t for t in work if t.is_alive()]
    file = None
    with open(args.file) as f:
        file = f.readlines()
    file = sorted(file)
    with open(args.file, "w") as f:
        for line in file:
            print(line.strip(), file=f)

if __name__ == "__main__":
    main()
