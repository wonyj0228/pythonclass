print('welcome')

# import pack02.mysqldb
from pack02 import mysqldb
mysqldb.create()
mysqldb.read()
mysqldb.update()
mysqldb.delete()


from tkinter import *
window = Tk()
window.mainloop()