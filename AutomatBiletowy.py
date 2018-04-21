import sys
import locale
from tkinter import Tk,Button
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Automat:
        def wyjscie(self):
                wyjsc=messagebox.askyesno(title="Wyjście", message="Czy na pewno chcesz zamknąć program?")
                if wyjsc > 0:
                        okno.destroy()
                        return
        def pomoc(self):
                helpp=messagebox.showinfo(title="Pomoc", message="1) Wybierz bilet który chciałbyś kupić w okienku po lewej stronie\n2) Wprowadz ilość biletów w okienku wyboru poniżej\n3) Naciśnij przycisk odpowiedniego biletu\n4) W okienku po prawej stronie z klawiatury wprowadź ilość wrzucanych monet\n5) Po wprowadzeniu odpowiedniej kwoty naciśnij 'ZAPŁAĆ'\n6) Odbierz bilety oraz resztę\n7) Aby USUNĄĆ bilet wybierz go ponownie ustawiając jego ilość na 0")
                return

        def informacje(self):
                information = messagebox.showinfo(title="Informacje", message="Jakies coś tu bydzie ale pozniej")
                return

        def ileBiletow(self):
                self.biu2=0
                self.biu4=0
                self.biu6=0
                self.bin2=0
                self.bin4=0
                self.bin6=0
                self.naleznosc=0
                self.naleznoscmain=0
                self.wrzucono=0
                self.wrzuconomain=0
                
        def incbiu2(self):
                self.biu2+=1
                biletu20['text']=self.biu2
                incnalezn(self)
        def incbiu4(self):
                self.biu4+=1
                biletu40['text']=self.biu4
                incnalezn(self)
        def incbiu6(self):
                self.biu6+=1
                biletu60['text']=self.biu6
                incnalezn(self)
        def incbin2(self):
                self.bin2+=1
                biletn20['text']=self.bin2
                incnalezn(self)
        def incbin4(self):
                self.bin4+=1
                biletn40['text']=self.bin4
                incnalezn(self)
        def incbin6(self):
                self.bin6+=1
                biletn60['text']=self.bin6
                incnalezn(self)
                
        def incnalezn(self):
                self.naleznoscmain=self.biu2*140+self.biu4*190+self.biu6*250+self.bin2*280+self.bin4*380+self.bin6*500
                self.naleznosc=self.naleznoscmain/100
                podsumowanie['text'] = self.naleznosc

        def add1(self):
                self.wrzuconomain+=1
                self.wrzucono=self.wrzuconomain/100
                podsumowanie2['text']=self.wrzucono
        def add2(self):
                self.wrzuconomain+=2
                self.wrzucono=self.wrzuconomain/100
                podsumowanie2['text']=self.wrzucono
        def add5(self):
                self.wrzuconomain+=5
                self.wrzucono=self.wrzuconomain/100
                podsumowanie2['text']=self.wrzucono
        def add10(self):
                self.wrzuconomain+=10
                self.wrzucono=self.wrzuconomain/100
                podsumowanie2['text']=self.wrzucono
        def add20(self):
                self.wrzuconomain+=20
                self.wrzucono=self.wrzuconomain/100
                podsumowanie2['text']=self.wrzucono
        def add50(self):
                self.wrzuconomain+=50
                self.wrzucono=self.wrzuconomain/100
                podsumowanie2['text']=self.wrzucono
        def add100(self):
                self.wrzuconomain+=100
                self.wrzucono=self.wrzuconomain/100
                podsumowanie2['text']=self.wrzucono
        def add200(self):
                self.wrzuconomain+=200
                self.wrzucono=self.wrzuconomain/100
                podsumowanie2['text']=self.wrzucono
        def add500(self):
                self.wrzuconomain+=500
                self.wrzucono=self.wrzuconomain/100
                podsumowanie2['text']=self.wrzucono
        def add1000(self):
                self.wrzuconomain+=1000
                self.wrzucono=self.wrzuconomain/100
                podsumowanie2['text']=self.wrzucono
        def add2000(self):
                self.wrzuconomain+=2000
                self.wrzucono=self.wrzuconomain/100
                podsumowanie2['text']=self.wrzucono
        def add5000(self):
                self.wrzuconomain+=5000
                self.wrzucono=self.wrzuconomain/100
                podsumowanie2['text']=self.wrzucono
        def add10000(self):
                self.wrzuconomain+=10000
                self.wrzucono=self.wrzuconomain/100
                podsumowanie2['text']=self.wrzucono
        def add20000(self):
                self.wrzuconomain+=20000
                self.wrzucono=self.wrzuconomain/100
                podsumowanie2['text']=self.wrzucono
        def add50000(self):
                self.wrzuconomain+=50000
                self.wrzucono=self.wrzuconomain/100
                podsumowanie2['text']=self.wrzucono

        def __init__(self):
                self.ileBiletow()
                guzik1 = ttk.Button(text="20 minutowy\nUlgowy\n1,40zł", style="Blue.TButton",command=lambda: incbiu2(self))
                guzik1.place(x=10,y=120)

                guzik2 = ttk.Button(text="40 minutowy\nUlgowy\n1,90zł", style="Blue.TButton", command=lambda: incbiu4(self))
                guzik2.place(x=10,y=220)
                
                
                guzik3 = ttk.Button(text="60 minutowy\nUlgowy\n2,50zł", style="Blue.TButton", command=lambda: incbiu6(self))
                guzik3.place(x=10,y=320)
                
                guzik4 = ttk.Button(text="\nPOMOC\n", style="Orange.TButton",command=self.pomoc)
                guzik4.place(x=10,y=420)

                guzik1p = ttk.Button(text="20 minutowy\nNormalny\n2,80zł",style="Green.TButton", command=lambda: incbin2(self))
                guzik1p.place(x=265,y=120)
        
                guzik2p = ttk.Button(text="40 minutowy\nNormalny\n3,80zł",style="Green.TButton", command=lambda: incbin4(self))
                guzik2p.place(x=265,y=220)
                
                guzik3p = ttk.Button(text="60 minutowy\nNormalny\n5,00zł", style="Green.TButton",command=lambda: incbin6(self))
                guzik3p.place(x=265,y=320)
                
                guzik4p = ttk.Button(okno,text="\nINFORMACJE\n",style="Black.TButton",command=self.informacje)
                guzik4p.place(x=265,y=420)

                guzik_exit = ttk.Button(text="\nWYJŚCIE\n", style="Red.TButton",command=self.wyjscie).place(x=130,y=520)

                line=Canvas(width=5, height=100000, bg="black").place(x=500,y=0)

                button1 = Button(width=5,text="+1gr", command=lambda: add1(self))
                button1.place(x=520,y=450)

                button2 = Button(width=5, text="+2gr", command=lambda: add2(self))
                button2.place(x=570,y=450)

                button5 = Button(width=5, text="+5gr", command=lambda: add5(self))
                button5.place(x=620,y=450)

                button10 = Button(width=5,text="+10gr", command=lambda: add10(self))
                button10.place(x=520,y=480)

                button20 = Button(width=5, text="+20gr", command=lambda: add20(self))
                button20.place(x=570,y=480)

                button50 = Button(width=5, text="+50gr", command=lambda: add50(self))
                button50.place(x=620,y=480)

                button100 = Button(width=5,text="+1zł",command=lambda: add100(self))
                button100.place(x=520,y=510)

                button200 = Button(width=5, text="+2zł",command=lambda: add200(self))
                button200.place(x=570,y=510)

                button500 = Button(width=5, text="+5zł",command=lambda: add500(self))
                button500.place(x=620,y=510)

                button1000 = Button(width=5,text="+10zł",command=lambda: add1000(self))
                button1000.place(x=520,y=540)

                button2000 = Button(width=5, text="+20zł",command=lambda: add2000(self))
                button2000.place(x=570,y=540)

                button5000 = Button(width=5, text="+50zł",command=lambda: add5000(self))
                button5000.place(x=620,y=540)

                button10000 = Button(width=5,text="+100zł",command=lambda: add10000(self))
                button10000.place(x=520,y=570)

                button20000 = Button(width=5, text="+200zł",command=lambda: add20000(self))
                button20000.place(x=570,y=570)
                
                button50000 = Button(width=5, text="+500zł",command=lambda: add50000(self))
                button50000.place(x=620,y=570)

                buttonpay = Button(width=19, text="ZAPŁAĆ")
                buttonpay.place(x=522,y=600)

                tytul2 = Label(text='Kasa',fg="black",bg="white", font=("Helvetica",32,"bold")).place(x=540,y=20)

           
                koszyk1 = Label(text='Ulgowy 20').place(x=550,y=120)
                biletu20=Label(fg="red",bg="white",text=self.biu2)
                biletu20.place(x=630, y=120)
                
                koszyk2 = Label(text='Ulgowy 40').place(x=550,y=140)
                biletu40=Label(fg="red",bg="white",text=self.biu4)
                biletu40.place(x=630, y=140)
                
                koszyk3 = Label(text='Ulgowy 60').place(x=550,y=160)
                biletu60=Label(fg="red",bg="white",text=self.biu6)
                biletu60.place(x=630, y=160)

                koszyk4 = Label(text='Normalny 20').place(x=550,y=200)
                biletn20=Label(fg="red",bg="white",text=self.bin2)
                biletn20.place(x=630, y=200)
                
                koszyk5 = Label(text='Normalny 40').place(x=550,y=220)
                biletn40=Label(fg="red",bg="white",text=self.bin4)
                biletn40.place(x=630, y=220)
                
                koszyk6 = Label(text='Normalny 60').place(x=550,y=240)
                biletn60=Label(fg="red",bg="white",text=self.bin6)
                biletn60.place(x=630, y=240)

                dozaplaty = Label(text='Do zapłaty: ').place(x=550,y=300)
                podsumowanie=Label(fg="red",bg="white",text=self.naleznosc)
                podsumowanie.place(x=550,y=320)
                podsumowanie['text'] = incnalezn(self)
                zloty=Label(text='zł').place(x=600,y=320)

                japlace = Label(text='Wrzucono: ').place(x=550,y=360)
                podsumowanie2=Label(fg="red",bg="white",text=self.wrzucono)
                podsumowanie2.place(x=550,y=380)
                zloty=Label(text='zł').place(x=600,y=380)
                
                
                        
okno = Tk()     
styl = ttk.Style()
styl.configure('TButton', foreground='black', width=30, font=("TimesNewRoman", 10, "bold"),justify=CENTER)
style = ttk.Style()
style.configure("Blue.TButton", foreground="blue", background="blue")

style = ttk.Style()
style.configure("Green.TButton", foreground="green", background="green")

style = ttk.Style()
style.configure("Orange.TButton", foreground="#e68a00", background="#e68a00")
style = ttk.Style()
style.configure("Black.TButton", foreground="black", background="black")

style = ttk.Style()
style.configure("Red.TButton", foreground="red", background="red")

okno.geometry('680x640+300+20')
okno.title("Automat biletowy MPK")
tytul = Label(text='Automat biletowy MPK',fg="black",bg="white", font=("Helvetica",32,"bold")).place(x=12,y=20)
kreditsy = Label(text=' Copyright: © 2017 Mateusz Ciałowicz, all rights reserved ',fg="red",font=("TimesNewRoman", 8),justify=CENTER).place(x=110,y=620)
Automat()
okno.mainloop()


        


