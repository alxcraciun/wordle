from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(str(OUTPUT_PATH) + r'\assets')

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("900x600")
window.resizable(False, False)
window.configure(bg = "#F1F1F1")
window.title('Wordle')

canvas = Canvas(
    window,
    bg = "#F1F1F1",
    height = 600,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=14.0,
    y=539.0,
    width=286.5714416503906,
    height=42.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=306.57147216796875,
    y=539.0,
    width=286.5714416503906,
    height=42.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=599.1429443359375,
    y=539.0,
    width=286.5714416503906,
    height=42.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    825.4693603515625,
    509.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    700.2244873046875,
    509.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    574.9796142578125,
    509.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    449.7347412109375,
    509.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    324.4898376464844,
    509.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    199.24493408203125,
    509.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    74.0,
    509.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    839.3016357421875,
    458.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    741.888916015625,
    458.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    644.4761962890625,
    458.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    547.0634765625,
    458.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    449.65081787109375,
    458.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    352.2381286621094,
    458.0,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    254.825439453125,
    458.0,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    157.4127197265625,
    458.0,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    60.0,
    458.0,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    844.04296875,
    407.0,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    756.37158203125,
    407.0,
    image=image_image_18
)

image_image_19 = PhotoImage(
    file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(
    668.7000732421875,
    407.0,
    image=image_image_19
)

image_image_20 = PhotoImage(
    file=relative_to_assets("image_20.png"))
image_20 = canvas.create_image(
    581.0286865234375,
    407.0,
    image=image_image_20
)

image_image_21 = PhotoImage(
    file=relative_to_assets("image_21.png"))
image_21 = canvas.create_image(
    493.3572082519531,
    407.0,
    image=image_image_21
)

image_image_22 = PhotoImage(
    file=relative_to_assets("image_22.png"))
image_22 = canvas.create_image(
    405.6857604980469,
    407.0,
    image=image_image_22
)

image_image_23 = PhotoImage(
    file=relative_to_assets("image_23.png"))
image_23 = canvas.create_image(
    318.0143127441406,
    407.0,
    image=image_image_23
)

image_image_24 = PhotoImage(
    file=relative_to_assets("image_24.png"))
image_24 = canvas.create_image(
    230.3428955078125,
    407.0,
    image=image_image_24
)

image_image_25 = PhotoImage(
    file=relative_to_assets("image_25.png"))
image_25 = canvas.create_image(
    142.67144775390625,
    407.0,
    image=image_image_25
)

image_image_26 = PhotoImage(
    file=relative_to_assets("image_26.png"))
image_26 = canvas.create_image(
    55.0,
    407.0,
    image=image_image_26
)

canvas.create_text(
    67.0,
    495.0,
    anchor="nw",
    text="Z",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    486.3572082519531,
    393.0,
    anchor="nw",
    text="Y",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    192.24493408203125,
    495.0,
    anchor="nw",
    text="X",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    132.67144775390625,
    393.0,
    anchor="nw",
    text="W",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    442.7347106933594,
    495.0,
    anchor="nw",
    text="V",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    573.0286865234375,
    393.0,
    anchor="nw",
    text="U",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    399.6857604980469,
    393.0,
    anchor="nw",
    text="T",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    150.4127197265625,
    444.0,
    anchor="nw",
    text="S",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    311.0143127441406,
    393.0,
    anchor="nw",
    text="R",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    47.0,
    393.0,
    anchor="nw",
    text="Q",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    838.04296875,
    393.0,
    anchor="nw",
    text="P",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    748.37158203125,
    393.0,
    anchor="nw",
    text="O",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    692.2244873046875,
    495.0,
    anchor="nw",
    text="N",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    816.4693603515625,
    495.0,
    anchor="nw",
    text="M",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    833.3016357421875,
    444.0,
    anchor="nw",
    text="L",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    734.888916015625,
    444.0,
    anchor="nw",
    text="K",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    639.4761962890625,
    444.0,
    anchor="nw",
    text="J",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    666.7000732421875,
    393.0,
    anchor="nw",
    text="I",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    539.0634765625,
    444.0,
    anchor="nw",
    text="H",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    441.65081787109375,
    444.0,
    anchor="nw",
    text="G",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    346.2381286621094,
    444.0,
    anchor="nw",
    text="F",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    224.3428955078125,
    393.0,
    anchor="nw",
    text="E",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    247.825439453125,
    444.0,
    anchor="nw",
    text="D",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    316.4898376464844,
    495.0,
    anchor="nw",
    text="C",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    567.9796142578125,
    495.0,
    anchor="nw",
    text="B",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

canvas.create_text(
    53.0,
    444.0,
    anchor="nw",
    text="A",
    fill="#000000",
    font=("SFProDisplay Regular", 22 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    90.5,
    273.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=61.0,
    y=223.0,
    width=59.0,
    height=98.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    269.5,
    273.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=240.0,
    y=223.0,
    width=59.0,
    height=98.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    448.5,
    273.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=419.0,
    y=223.0,
    width=59.0,
    height=98.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    627.5,
    273.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=598.0,
    y=223.0,
    width=59.0,
    height=98.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    806.5,
    273.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=777.0,
    y=223.0,
    width=59.0,
    height=98.0
)

entry_1.focus()

window.mainloop()
