#8
a,b,c =None,None,None
t1 = {"saat":8, "daqiqeh":2, "sanieh": 31}
t2 = {"saat":1, "daqiqeh":29, "sanieh": 40}

def sho(x):
    print(x["saat"],":",x["daqiqeh"],":",x["sanieh"])

def zaman_be_saineh(a,b,c):
    a = int(input("saat :" ))
    b = int(input("daghigheh :" ))
    c = int(input("sanieh :" ))
    sanieh = (a*3600) + (b*60) + c
    return sanieh

def sanieh_be_zaman(a):
    a=int(input("adad :"))
    saat = a//3600
    b = a - (3600*saat)
    daghigheh = b//60
    sanieh = b-60*daghigheh
    return (saat ,":" ,daghigheh , ":" , sanieh)

def jamm(x,y):
    result = {}
    result["sanieh"] = x["sanieh"] + y["sanieh"]
    result["daqiqeh"] = x["daqiqeh"] + y["daqiqeh"]
    result["saat"] = x["saat"] + y["saat"]
    if result["sanieh"] >= 60:
        result["sanieh"] -= 60
        result["daqiqeh"] += 1
    if result["daqiqeh"] >= 60:
        result["daqiqeh"] -= 60
        result["saat"] += 1
    return result

def tafriq(x,y): 
    if x["sanieh"] < y["sanieh"]:
        x["daqiqeh"] = x["daqiqeh"] - 1
        x["sanieh"] = x["sanieh"] + 60
    if x["daqiqeh"] < y["daqiqeh"]:
        x["saat"] = x["saat"] - 1
        x["daqiqeh"] = x["daqiqeh"] + 60
    result = {}
    result["sanieh"] = x["sanieh"] - y["sanieh"]
    result["daqiqeh"] = x["daqiqeh"] - y["daqiqeh"]
    result["saat"] = x["saat"] - y["saat"]
    return result

choic = int(input("wich one? 1.tabdil zaman be sanieh, 2.tabdil sanieh be zaman, 3.jamm do zaman, 4.tafriq do zaman: "))
def cho(choic):
    if choic == 1:
        print(zaman_be_saineh(a,b,c))
    elif choic == 2:
        print(sanieh_be_zaman(a))
    elif choic == 3:
        sho(jamm(t1,t2))
    elif choic == 4:
        # tafriq(t1,t2)
        sho(tafriq(t1,t2))
    else:
        print("error")
cho(choic)