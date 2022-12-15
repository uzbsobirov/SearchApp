from tkinter import *
import webbrowser
#1 - reja :
root = Tk()
root.title('Searcher panel')
root.geometry('500x300')
root.config(bg='#808080')

def systemWork():
    webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % searchQuery.get())

#2 = reja :
title = Label(root, text='@uzbsobirov',
              fg='white',
              font = ('Times', 10, 'bold'),
              bg='#000000',
              relief=SOLID,
              bd=1)
title.place(x=420, y=275)


#3 - reja :
searchTitle = Label(root, text='Nima qidiramiz?',
                     font = ('Times', 10, 'bold'),
                     fg='white',
                     bg='#000000')
searchTitle.place(x=200, y=75)

#4 - reja :
searchQuery = Entry(root, bg='white',
                    fg='#1E6AE1',
                    font = ('Comic Sans Ms', 10, 'bold'),
                    relief=SOLID,
                    width=30)
searchQuery.place(x=125, y=100)

#5 - reja :
searchButton = Button(root, text='Qidirish',
                      bg='#1ECBE1',
                      fg='black',
                      font = ('Comic Sans Ms', 10, 'bold'),
                      relief=SOLID,
                      cursor='hand2',
                      width=15,
                      command=systemWork)
searchButton.place(x=180, y=150)



root.mainloop()
