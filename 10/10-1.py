dict = []
hame = []

from media import meedia
from clip import clipp
from film import filmm
from serial import seriall
from mostanad import mos
from pyfiglet import Figlet

welcam = Figlet(font='standard')
print (welcam.renderText('Paniz  store'))

class actor:
    pass

data = open("hamechi.txt","r")
data = data.read().split("\n")
for i in range (len(data)):
    hame = data[i].split(",")
    if hame[0]=="film":
        dict.append(filmm(hame[0],hame[1],hame[2],hame[3],hame[4],hame[5],hame[6],hame[7]))
    elif hame[0]=="series":
        dict.append(seriall(hame[0],hame[1],hame[2],hame[3],hame[4],hame[5],hame[6],hame[7]))
    elif hame[0]=="clip":
        dict.append(clipp(hame[0],hame[1],hame[2],hame[3],hame[4],hame[5],hame[6],hame[7]))
    elif hame[0]=="doc":
        dict.append(mos(hame[0],hame[1],hame[2],hame[3],hame[4],hame[5],hame[6],hame[7]))


def ad():
    typ = input("film? serial? mostanad? clip? ")
    i_D = int(input("code? "))
    name = input("name? ")
    directo = float(input("director? "))
    IMDBscor = float(input("IMDBscore? "))
    urll = input("url? ")
    duratio = int(input("duration? "))
    cast = input("casts? ")
    dict.append({"type": typ, "id": i_D, "name" : name, "director": directo, "IMDBsco" : IMDBscor,"url":urll, "duration": duratio, "casts": cast})
    print("shod")

def edit():
    idd = input("shomare chando mikhai edit koni? ")
    for i in range(len(hame)):
        if hame[i]["id"] == idd:
            while True:
                hame[i]['typ'] = input('name type: ')
                hame[i]['name'] = input('name jadid: ')
                hame[i]['IMDBscore'] = input('IMDBscore jadid: ')
                hame[i]['url'] = input('link jadid: ')
                hame[i]['duration'] = input('duration jadid: ')
                print("shod")
def lete():
    idd = int(input("kodumo mikhai vardari? "))
    for i in range(len(hame)):
        if hame[i]["id"] == idd:
            hame.pop(i)
            print("shod")

def serch():
    s = input("donbal chi hasti? " )
    for i in range (len(hame)):
        if s == hame[i]["name"]:
            print(hame[i])

def danlod():
    idd = int(input("kodum? "))
    for i in range(len(hame)):
        if idd == hame[i]["id"]:
            hame[i].download()

                
def sho_menu():
        print("1-add film")
        print("2- eddit film")
        print("3- del film")
        print("4- search")
        print("5- show list")
        print("6- download")

while True:
    sho_menu()
    choi = int(input('please entekhab komim:'))
    
    if choi == 1:
        ad()
    elif choi == 2:
        edit()
    elif choi ==3:
        lete()
    elif choi == 4:
        serch()
    elif choi == 5:
        print(hame)
    elif choi == 6:
        danlod()