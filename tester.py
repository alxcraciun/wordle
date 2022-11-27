import subprocess
import queue
import threading
import time
import constants

lines = queue.Queue()
total_written = 0

def writer_thread():
    global total_written
    with open("solutii.txt", "a") as solutii:
        while True:
            print("WRITING", flush=True)
            l = lines.get()
            total_written += 1
            if l == [-1]:
                return
            print(*l, file=solutii, flush=True, sep=' ', end='\n')

def compute(db, port):
    print("Thread active, ", id(db))
    for i in range(len(db)):
        line = [db[i]]
        solver = subprocess.Popen(["PyPy", "solver.py", "--port", str(port)], stdout=subprocess.DEVNULL)
        wordle = subprocess.Popen(["PyPy", "wordle.py", "--secret-word", db[i], "--port", str(port)], stdout=subprocess.PIPE)
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
        
def main():
    maxt = 5
    threading.Thread(group=None, target=writer_thread).start()
    prevr = 0
    db = open("cuvinte_wordle.txt").read().split()
    already_done = [ln.split()[0] for ln in open("solutii.txt").readlines()]
    db = [x for x in db if x not in already_done][1:10]
    work = []
    for i in range(maxt):
        l = prevr
        r = min(len(db) - 1, l + len(db)//maxt)
        tmp_db = db[l:r+1]
        work.append(threading.Thread(group=None, target=compute, args=(tmp_db, constants.PORT + i + 1)))
        work[-1].start()
        prevr = r + 1
    while True:
        time.sleep(1)
        print(total_written/len(db)*100,'%')

if __name__ == "__main__":
    main()
