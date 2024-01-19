import tkinter
main_window=tkinter.Tk()
def event_tekan():
    label2=tkinter.Label(main_window,text="ini Halaman GUI RFID dan ESP")
    label2.pack()

label=tkinter.Label(main_window,text="RFID")
tombol=tkinter.Button(main_window,text="Daftarkan TAG RFID",command=event_tekan)
input01=tkinter.Entry(main_window, text="")
input02=tkinter.Entry(main_window, text="")

label.pack()
input01.pack()
input02.pack()
tombol.pack()
main_window.mainloop()

