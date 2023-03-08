# from tkinter import *
# import tkinter.font
# from tkinter import messagebox
# import csv
# from time import *
# from threading import*

# root = Tk()
# root.geometry("350x500")
# changefont = tkinter.font.Font(size=15)

# judul = Label(root, text="Registrasi Data Karyawan", font=changefont).place(x=60, y=10)

# namalabel   = Label(root, text='Nama').place(x=20, y=50)
# niplabel    = Label(root, text='NIP').place(x=20, y=90)
# emaillabel  = Label(root, text='E-mail').place(x=20, y=130)
# asallabel   = Label(root, text='Asal').place(x=20, y=170)
# genderlabel = Label(root, text='Gender').place(x=20, y=210)
# divisilabel = Label(root, text='Divisi').place(x=20, y=250)
# shiftlabel  = Label(root, text='Shift').place(x=20, y=290)

# rgender = StringVar()
# rgender.set(" ")

# rdivisi = StringVar()
# rdivisi.set(" ")

# rshift = StringVar()
# rshift.set(" ")

# nama = Entry(root, width=40)
# nip = Entry(root, width=40)
# email = Entry(root, width=40)
# asal = Entry(root, width=40)

# nama.place(x=80, y=55)
# nip.place(x=80, y=95)
# email.place(x=80, y=135)
# asal.place(x=80, y=175)

# rb_pria   = Radiobutton(root, text="Pria", variable=rgender, value="Pria").place(x=80, y=210)
# rb_wanita = Radiobutton(root, text="Wanita", variable=rgender, value="Wanita").place(x=160, y=210)

# rb_emt  = Radiobutton(root, text="EMT", variable=rdivisi, value="EMT").place(x=80, y=250)
# rb_tmt  = Radiobutton(root, text="TMT", variable=rdivisi, value="TMT").place(x=160, y=250)
# rb_qc   = Radiobutton(root, text="QC", variable=rdivisi, value="QC").place(x=240, y=250)

# rb_pagi  = Radiobutton(root, text="Pagi", variable=rshift, value="Pagi").place(x=80, y=290)
# rb_siang = Radiobutton(root, text="Siang", variable=rshift, value="Siang").place(x=160, y=290)
# rb_malam = Radiobutton(root, text="Malam", variable=rshift, value="Malam").place(x=240, y=290)

# def regis():
#     isidata = [nama.get(), nip.get(),email.get(), asal.get(), rgender.get(), rdivisi.get(), rshift.get()]
#     with open('absen.csv', 'a', newline='') as csvfile:
#         writer = csv.writer(csvfile, delimiter=';')
#         writer.writerow(isidata)
#     messagebox.showinfo("Data Tersimpan", "Anda Telah Melakukan Registrasi")

# def delete():
#     isihapus =[nama.delete(0,END),
#             nip.delete(0,END),
#             email.delete(0,END),
#             asal.delete(0,END),
#             rgender.set(" "),
#             rdivisi.set(" "),
#             rshift.set(" ")] 
    
# data    = Button(root, text="Simpan Data", bg='lightgreen',command=regis).place(x=240, y=400)
# hapus   = Button(root,text="Hapus", bg='red',command=delete).place(x=180, y=400)

# start = time()
# t1 = Thread(target=regis, args=([]))
# t2 = Thread(target=delete, args=([]))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# end = time()

# print("Waktu mulai             :", start)
# print("Waktu selesai           :", end)
# print("Durasi eksekusi program :", end-start)

# root.mainloop()

from tkinter import *
import tkinter.font
from tkinter import messagebox
import csv
from time import *
from threading import*

root = Tk()
root.geometry("350x500")
changefont = tkinter.font.Font(size=15)

judul = Label(root, text="Registrasi Data Karyawan", font=changefont).place(x=60, y=10)

namalabel   = Label(root, text='Nama').place(x=20, y=50)
niplabel    = Label(root, text='NIP').place(x=20, y=90)
emaillabel  = Label(root, text='E-mail').place(x=20, y=130)
asallabel   = Label(root, text='Asal').place(x=20, y=170)
genderlabel = Label(root, text='Gender').place(x=20, y=210)
divisilabel = Label(root, text='Divisi').place(x=20, y=250)
shiftlabel  = Label(root, text='Shift').place(x=20, y=290)

rgender = StringVar()
rgender.set(" ")

rdivisi = StringVar()
rdivisi.set(" ")

rshift = StringVar()
rshift.set(" ")

nama = Entry(root, width=40)
nip = Entry(root, width=40)
email = Entry(root, width=40)
asal = Entry(root, width=40)

nama.place(x=80, y=55)
nip.place(x=80, y=95)
email.place(x=80, y=135)
asal.place(x=80, y=175)

rb_pria   = Radiobutton(root, text="Pria", variable=rgender, value="Pria").place(x=80, y=210)
rb_wanita = Radiobutton(root, text="Wanita", variable=rgender, value="Wanita").place(x=160, y=210)

rb_emt  = Radiobutton(root, text="EMT", variable=rdivisi, value="EMT").place(x=80, y=250)
rb_tmt  = Radiobutton(root, text="TMT", variable=rdivisi, value="TMT").place(x=160, y=250)
rb_qc   = Radiobutton(root, text="QC", variable=rdivisi, value="QC").place(x=240, y=250)

rb_pagi  = Radiobutton(root, text="Pagi", variable=rshift, value="Pagi").place(x=80, y=290)
rb_siang = Radiobutton(root, text="Siang", variable=rshift, value="Siang").place(x=160, y=290)
rb_malam = Radiobutton(root, text="Malam", variable=rshift, value="Malam").place(x=240, y=290)

def regis():
    isidata = [nama.get(), nip.get(),email.get(), asal.get(), rgender.get(), rdivisi.get(), rshift.get()]
    with open('absen.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(isidata)
    messagebox.showinfo("Data Tersimpan", "Anda Telah Melakukan Registrasi")

def delete():
    isihapus =[nama.delete(0,END),
            nip.delete(0,END),
            email.delete(0,END),
            asal.delete(0,END),
            rgender.set(" "),
            rdivisi.set(" "),
            rshift.set(" ")] 
    
data    = Button(root, text="Simpan Data", bg='lightgreen',command=regis).place(x=240, y=400)
hapus   = Button(root,text="Hapus", bg='red',command=delete).place(x=180, y=400)

startsingle = time()
regis()
delete()
endsingle = time()

print("Waktu mulai             :", startsingle)
print("Waktu selesai           :", endsingle)
print("Durasi eksekusi program :", endsingle-startsingle)

start = time()
t1 = Thread(target=regis, args=([]))
t2 = Thread(target=delete, args=([]))
t1.start()
t2.start()
t1.join()
t2.join()
end = time()

print("Waktu mulai             :", start)
print("Waktu selesai           :", end)
print("Durasi eksekusi program :", end-start)
root.mainloop()