from tkinter import *
root = Tk()
root.geometry('900x600')
root.resizable(False, False)
root.title('Wordle')

# Label1 = Label(root, text = 'Wordle Project')
# Label2 = Label(root, text = 'Please submit your word:').grid(row = 0, column = 10)

def myClick():
    if myButton['state'] == 'normal':
        myButton['state'] = 'disabled'
    user_name = e.get()
    myLabel = Label(root, text = f'{user_name} a introdus un cuvant')
    myLabel.grid(row = 2, column= 0)

myButton = Button(root, text = "Click me!", state = 'normal', padx = 15, pady = 5, command = myClick)

e = Entry(root, borderwidth=20)
e.grid(row = 0, column = 0)

myButton.grid(row = 1, column=0)

root.mainloop()