products_f = []
products_s = []
products_c = []
products_m = []
class actor:
    pass
class media:
    def __init__(self,id,name,director,IMDBscore,url,duration,casts):
        self.id = id
        self.name = name
        self.director = director
        self.IMDBscore= IMDBscore
        self.url = url
        self.duration = duration
        self.casts = casts
    

    def showInfo(self):
        print("loading...")

        print("1-add film")
        print("2- eddit film")
        print("3- del film")
        print("4- search")
        print("5- show list")
        print("6- download")
        print("7- exit")
        
        dict = []
        
        myfile = open("film.txt" , "r" )
        mysile = open("serial.txt" , "r" )
        mycile = open("clip.txt" , "r" )
        mymile = open("mostanad.txt" , "r" )
        fata = myfile.read().split("\n")
        sata = mysile.read().split("\n")
        cata = mycile.read().split("\n")
        mata = mymile.read().split("\n")
        for i in range(len(fata)):
            product_info = fata[i].split(",")
            dict["id"] = int(product_info[0])
            dict["name"] = str(product_info[0])
            dict["director"] = product_info[1]
            dict["IMDBscore"] = float(product_info[2])
            dict["url"] = product_info[3]
            dict["duration"] = int(product_info[4])
            dict["casts"] = product_info[5]
            products_f.append(dict)
        myfile.close()
        print(self.products)

        for i in range(len(sata)):
            product_info = sata[i].split(",")
            dict["id"] = int(product_info[0])
            dict["name"] = str(product_info[0])
            dict["director"] = product_info[1]
            dict["IMDBscore"] = float(product_info[2])
            dict["url"] = product_info[3]
            dict["duration"] = int(product_info[4])
            dict["casts"] = product_info[5]
            products_s.append(dict)
        mysile.close()
        print(self.products)
        print("welcome")

        for i in range(len(cata)):
            product_info = cata[i].split(",")
            dict["id"] = int(product_info[0])
            dict["name"] = str(product_info[0])
            dict["director"] = product_info[1]
            dict["IMDBscore"] = float(product_info[2])
            dict["url"] = product_info[3]
            dict["duration"] = int(product_info[4])
            dict["casts"] = product_info[5]
            products_c.append(dict)
        mycile.close()
        print(self.products)

        for i in range(len(mata)):
            product_info = mata[i].split(",")
            dict["id"] = int(product_info[0])
            dict["name"] = str(product_info[0])
            dict["director"] = product_info[1]
            dict["IMDBscore"] = float(product_info[2])
            dict["url"] = product_info[3]
            dict["duration"] = int(product_info[4])
            dict["casts"] = product_info[5]
            products_m.append(dict)
        mymile.close()
        print(self.products)
    def show_list():
        for i in range(len(products)):
            print(products_f[i]["id"], "\t",products_f[i]["name"],"\t",products[i]["price"],"\t",products[i]["count"] )
    def download():
        pass
    def ad():
        u = input("1.serial, 2.film, 3.clip, 4.mostanad")
        if  u == 1:
            i_D = int(input("code? "))
            name = input("name? ")
            directo = float(input("director? "))
            IMDBscor = float(input("IMDBscore? "))
            urll = input("url? ")
            duratio = int(input("duration? "))
            cast = input("casts? ")
            products_s.append({"id": i_D, "name" : name, "director": directo, "IMDBsco" : IMDBscor,"url":urll, "duration": duratio, "casts": cast})
            print("shod")
        elif u == 2:
            i_D = int(input("code? "))
            name = input("name? ")
            directo = float(input("director? "))
            IMDBscor = float(input("IMDBscore? "))
            urll = input("url? ")
            duratio = int(input("duration? "))
            cast = input("casts? ")
            products_f.append({"id": i_D, "name" : name, "director": directo, "IMDBsco" : IMDBscor,"url":urll, "duration": duratio, "casts": cast})
            print("shod")
        elif u == 2:
            i_D = int(input("code? "))
            name = input("name? ")
            directo = float(input("director? "))
            IMDBscor = float(input("IMDBscore? "))
            urll = input("url? ")
            duratio = int(input("duration? "))
            cast = input("casts? ")
            products_c.append({"id": i_D, "name" : name, "director": directo, "IMDBsco" : IMDBscor,"url":urll, "duration": duratio, "casts": cast})
            print("shod")

        elif u == 2:
            i_D = int(input("code? "))
            name = input("name? ")
            directo = float(input("director? "))
            IMDBscor = float(input("IMDBscore? "))
            urll = input("url? ")
            duratio = int(input("duration? "))
            cast = input("casts? ")
            products_m.append({"id": i_D, "name" : name, "director": directo, "IMDBsco" : IMDBscor,"url":urll, "duration": duratio, "casts": cast})
            print("shod")
    choic = input("wich one? ")
    if choic == 1 :
            ad()
    if choic == 2:
        pass
    if choic == 3:
        pass
    if choic == 4:
        pass
    if choic == 5:
        pass
    if choic == 6:
        download()
    if choic == 7:
        pass



class Clip(media):
    def __init__(self):
        pass
class Documentary(media):
    def __init__(self):
        pass
class Series(media):
    def __init__(self):
        pass
    def teedad_qesmat():
        print("teedad qesmat ha: ")
class film(media):
    def janr():
        print("janr film is: ")
    def __init__(self):
        pass