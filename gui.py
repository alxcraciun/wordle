from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, Label
import constants
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH.joinpath("assets")
IMG_REF = []
IMAGE_COORDS = [(825.4693603515625, 509.0), (700.2244873046875, 509.0), (574.9796142578125, 509.0), (449.7347412109375, 509.0), (324.4898376464844, 509.0), (199.24493408203125, 509.0), (74.0, 509.0), (839.3016357421875, 458.0), (741.888916015625, 458.0), (644.4761962890625, 458.0), (547.0634765625, 458.0), (449.65081787109375, 458.0), (352.2381286621094, 458.0), (254.825439453125, 458.0), (157.4127197265625, 458.0), (60.0, 458.0), (844.04296875, 407.0), (756.37158203125, 407.0), (668.7000732421875, 407.0), (581.0286865234375, 407.0), (493.3572082519531, 407.0), (405.6857604980469, 407.0), (318.0143127441406, 407.0), (230.3428955078125, 407.0), (142.67144775390625, 407.0), (55.0, 407.0)]
LETTER_COORDS = [(67.0, 495.0), (486.3572082519531, 393.0), (192.24493408203125, 495.0), (132.67144775390625, 393.0), (442.7347106933594, 495.0), (573.0286865234375, 393.0), (399.6857604980469, 393.0), (150.4127197265625, 444.0), (311.0143127441406, 393.0), (47.0, 393.0), (838.04296875, 393.0), (748.37158203125, 393.0), (692.2244873046875, 495.0), (816.4693603515625, 495.0), (833.3016357421875, 444.0), (734.888916015625, 444.0), (639.4761962890625, 444.0), (666.7000732421875, 393.0), (539.0634765625, 444.0), (441.65081787109375, 444.0), (346.2381286621094, 444.0), (224.3428955078125, 393.0), (247.825439453125, 444.0), (316.4898376464844, 495.0), (567.9796142578125, 495.0), (53.0, 444.0)]
LETTERS = ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
BUTTON_COORDS = [(14.0, 539.0), (306.57147216796875, 539.0), (599.1429443359375, 539.0)]
KEY_IMAGE_COORDS = [(90.5, 273.0), (269.5, 273.0), (448.5, 273.0), (627.5, 273.0), (806.5, 273.0)]
KEY_ENTRY_COORDS = [(61.0, 223.0), (240.0, 223.0), (419.0, 223.0), (598.0, 223.0), (777.0, 223.0)]
HISTORY_ENTRY_IMAGE_COORD = [(816.800048828125, 140.38315963745117), (781.9500350952148, 140.38315963745117), (747.2500228881836, 140.38315963745117), (712.5500106811523, 140.38315963745117), (677.8500003814697, 140.38315963745117), (534.800048828125, 140.38315963745117), (499.95003509521484, 140.38315963745117), (465.2500228881836, 140.38315963745117), (430.55001068115234, 140.38315963745117), (395.8499984741211, 140.38315963745117), (252.800048828125, 140.38315963745117), (217.95004272460938, 140.38315963745117), (183.25003051757812, 140.38315963745117), (148.55001831054688, 140.38315963745117), (113.85000610351562, 140.38315963745117), (816.800048828125, 79.82242965698242), (781.9500350952148, 79.82242965698242), (747.2500228881836, 79.82242965698242), (712.5500106811523, 79.82242965698242), (677.8500003814697, 79.82242965698242), (534.800048828125, 79.82242965698242), (499.95003509521484, 79.82242965698242), (465.2500228881836, 79.82242965698242), (430.55001068115234, 79.82242965698242), (395.8499984741211, 79.82242965698242), (252.800048828125, 79.82242965698242), (217.95004272460938, 79.82242965698242), (183.25003051757812, 79.82242965698242), (148.55001831054688, 79.82242965698242), (113.85000610351562, 79.82242965698242)]
HISTORY_ENTRY_COORDS = [(808.0000491142273, 123.56072998046875), (773.300036907196, 123.56072998046875), (738.6000247001648, 123.56072998046875), (703.9000124931335, 123.56072998046875), (669.2000002861023, 123.56072998046875), (526.0000491142273, 123.56072998046875), (491.30003690719604, 123.56072998046875), (456.6000247001648, 123.56072998046875), (421.90001249313354, 123.56072998046875), (387.2000002861023, 123.56072998046875), (244.0000491142273, 123.56072998046875), (209.30003690719604, 123.56072998046875), (174.6000247001648, 123.56072998046875), (139.90001249313354, 123.56072998046875), (105.2000002861023, 123.56072998046875), (808.0000491142273, 63.0), (773.300036907196, 63.0), (738.6000247001648, 63.0), (703.9000124931335, 63.0), (669.2000002861023, 63.0), (526.0000491142273, 63.0), (491.30003690719604, 63.0), (456.6000247001648, 63.0), (421.90001249313354, 63.0), (387.2000002861023, 63.0), (244.0000491142273, 63.0), (209.30003690719604, 63.0), (174.6000247001648, 63.0), (139.90001249313354, 63.0), (105.2000002861023, 63.0)]
HISTORY_IMG_REG = []
HISTORY_NUMBER_COORDS = [(55, 68), (337, 68), (619, 68), (55, 129), (337, 129), (619, 129)]

window = None
canvas = None

entry_list : list[Entry] = []
history_entry_list : list[Entry] = []
history_label_list : list[Label] = []
history_number_list : list[Label] = []

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH.joinpath(path)

def init_image(x, y, path):
    image_image = PhotoImage(file=path)
    IMG_REF.append(image_image) # fix garbage collector bug
    canvas.create_image(x, y, image=image_image)

def init_key(x, y, char):
    canvas.create_text(x, y, anchor="nw", text=char, fill="#000000", font=("SFProDisplay Regular", 22 * -1))

def init_entry(x, y, i):
    def callback(*args):
        val = sv.get()
        if len(val) > 1:
            val = val[0]
        val = val.upper()
        sv.set(val)
        if i < len(entry_list):
            entry_list[i].focus()
    sv = StringVar()
    sv.trace_add("write", callback)
    entry = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, font = ('SFProDisplay Regular', 50), justify = 'center', textvariable=sv)
    entry.place(x=x, y=y, width=59.0, height=98.0)
    entry_list.append(entry)

def init_button(x, y, path, callback):
    button_image = PhotoImage(file=path)
    IMG_REF.append(button_image) # fix garbage collector bug
    button = Button(image=button_image, borderwidth=0, highlightthickness=0, command=callback, relief="flat")
    button.place(x=x, y=y, width=286.5714416503906, height=42.0)

def reset_history():
    for e in history_entry_list:
        e.destroy()
    for e in history_number_list:
        e.destroy()
    for e in history_label_list:
        e.destroy()
    HISTORY_IMG_REG = []

def init_history_letter(i, letter_code = 0, char = "A"):
    sv = StringVar()
    image_type = ("history_green.png" if letter_code == constants.FULL_MATCH else "history_yellow.png" if letter_code == constants.PARTIAL_MATCH else "history_red.png")
    entry_bg_hex = ("#DBFFB7" if letter_code == constants.FULL_MATCH else "#FFFA88" if letter_code == constants.PARTIAL_MATCH else "#FFB7B7")
    entry_image = PhotoImage(file=relative_to_assets(image_type))
    entry_label = Label(window, image=entry_image, background="#FFFFFF")
    entry_label.place(x = HISTORY_ENTRY_IMAGE_COORD[i][0], y = HISTORY_ENTRY_IMAGE_COORD[i][1], anchor="center")
    history_label_list.append(entry_label)
    HISTORY_IMG_REG.append(entry_image) # fix garbage collector bug
    entry = Entry(bd=0,disabledbackground=entry_bg_hex,fg="#000716",highlightthickness=0, font = ('SFProDisplay Regular', 16), justify = 'center', state="disabled", textvariable=sv)
    history_entry_list.append(entry)
    sv.set(char)
    entry.place(x=HISTORY_ENTRY_COORDS[i][0],y=HISTORY_ENTRY_COORDS[i][1],width=17.59999942779541,height=31.644859313964844)

def init_history_number(i, str = ""):
    if str == "":
        str = f"#0{i+1}"
    number = Label(window, text=str, background="#FFFFFF", foreground="#898A8D", font=("SFProDisplay Regular", 20 * -1))
    history_number_list.append(number)
    number.place(x=HISTORY_NUMBER_COORDS[i][0],y=HISTORY_NUMBER_COORDS[i][1],width=40,height=23,anchor="nw")

def debug_history():
    for i in range(30):
        init_history_letter(i)
    for i in range(6):
        init_history_number

def collect_guess():
    word = ""
    for e in entry_list:
        word += e.get()
    return word

def give_globals(callback):
    return lambda : callback(globals())

def update_history(match_info):
    default_history.destroy()
    i = iter(match_info)
    j = 29
    match_info = list(zip(i, i))
    to_the_left = len(match_info)
    match_info = match_info[-6:]
    to_the_left -= len(match_info)
    for word, info in match_info:
        for char, code in (zip(word, info)):
            init_history_letter(j, code, char)
            j -= 1
    for x in range(len(match_info)):
        init_history_number(x, f"#{x + to_the_left + 1}")

def start_window(callback_hint, callback_submit, callback_solve, callback_init):
    callback_init(update_history)
    global window
    global canvas
    window = Tk()

    window.title('Ntropy Wordle')
    window.iconbitmap(relative_to_assets('wordle.ico'))

    window.geometry("900x600")
    window.resizable(False, False)
    window.configure(bg = "#F1F1F1")

    canvas = Canvas(window, bg = "#F1F1F1", height = 600, width = 900, bd = 0, highlightthickness = 0, relief = "ridge")
    canvas.place(x = 0, y = 0)

    init_button(*BUTTON_COORDS[0], relative_to_assets("button_hint.png"), give_globals(callback_hint))
    init_button(*BUTTON_COORDS[1], relative_to_assets("button_submit.png"), give_globals(callback_submit))
    init_button(*BUTTON_COORDS[2], relative_to_assets("button_solve.png"), give_globals(callback_solve))

    for i, coords in enumerate(IMAGE_COORDS, start=1):
        init_image(*coords, relative_to_assets("key_large.png" if i < 8 else "key_medium.png" if i < 17 else "key_small.png"))

    for char, coords in zip(LETTERS, LETTER_COORDS):
        init_key(*coords, char)

    for i, [img_coords, entry_coords] in enumerate(zip(KEY_IMAGE_COORDS, KEY_ENTRY_COORDS), start=1):
        init_image(*img_coords, relative_to_assets(f"entry.png"))
        init_entry(*entry_coords, i)

    entry_list[0].focus()

    canvas.place(x = 0, y = 0)

    # History Widget Group

    history_background_image = PhotoImage(file=relative_to_assets("history.png"))
    history_background = canvas.create_image(449.0,110.0,image=history_background_image)

    global default_history
    default_history = Label(window, text="You haven’t submitted a word yet", background="#FFFFFF", foreground="#898A8D", font=("SFProDisplay Regular", 20 * -1))
    default_history.place(x=310.0,y=95.0,width=300,height=23,anchor="nw")

    window.mainloop()

    os._exit(0)
