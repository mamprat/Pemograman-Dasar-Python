# from tkinter import *
# import tkinter.font
# import csv

# root = Tk()
# root.geometry("350x400")

# changefont = tkinter.font.Font(size=15)
# judul = Label(root,text = "Sistem Absensi Karyawan",font =changefont)
# judul.place(x =80,y = 10)

# ket = LabelFrame(root,text = "Data Karyawan",padx=20,pady=20)
# ket.place(x = 60,y = 380)

# namalabel   = Label(root, text='Nama')
# niplabel    = Label(root, text='NIP')
# shiftlabel  = Label(root, text='Shift ')

# r = StringVar()
# r.set(" ")

# nama    = Entry(root,width=40)
# nip     = Entry(root,width=40)
# rb      = Radiobutton(root,text = "Pagi",variable=r,value="Pagi")
# rb2     = Radiobutton(root,text = "Siang",variable=r,value="Siang")
# rb3     = Radiobutton(root,text = "Malam",variable=r,value="Malam")

# namalabel.place (x = 20, y =50)
# niplabel.place  (x = 20, y =90)
# shiftlabel.place(x = 20, y =130)
# nama.place      (x = 80, y = 55)
# nip.place       (x = 80, y = 95)

# rb.place (x = 80,y  =135)
# rb2.place(x = 160,y =135)
# rb3.place(x = 240,y =135)

# def regis():
#     class karyawan:
#         def __init__(self,namalabel,niplabel,shiftlabel):
#             self.namalabel  = namalabel
#             self.niplabel   = niplabel
#             self.shiftlabel = shiftlabel
#         def hasil(self):
#             kethasil = Label(ket,text="first Nama ="+self.namalabel+"\nlast NIP ="+self.niplabel+"\nShift ="+self.shiftlabel).grid()
#     ditampilkan = karyawan(nama.get(),nip.get(),r.get())
#     ditampilkan.hasil()

# btn = Button(root,text = "Masukan Data",command=regis).place(x = 240,y = 180)


# root.mainloop()
# # import csv

# # def regis():
# #     print("***************************************")
# #     print("Selamat Melakukan Registrasi")  
# #     nama        = input("Masukkan Nama Anda : ")
# #     nip         = input("Masukkan NIP Anda  : ")
# #     shift       = input("Shift ke           : ")
# #     print("***************************************")

# #     simpan(nama, nip, shift)
# #     # regisguest(nama,nip)

# # def regisguest(nama, nip):
# #     print ("")
# #     print ("***Selamat Datang " + nama + " "+ nip +" ***")
            
# # def simpan(nama, nip, shift):
# #     data=[nama, nip, shift]
# #     with open('absen.csv', 'a',newline='') as csvfile: 
# #         writer=csv.writer(csvfile,delimiter = ';')
# #         writer.writerow(data)    
# # regis()

