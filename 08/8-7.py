#7
def jamm(x,y):
    result = {}
    result["surat"] = x["surat"] * y["makhraj"] + x["makhraj"] * y["surat"]
    result["makhraj"] = x["makhraj"] * y["makhraj"]
    return result
def tafriq(x,y):
    result = {}
    result["surat"] = x["surat"] * y["makhraj"] - x["makhraj"] * y["surat"]
    result["makhraj"] = x["makhraj"] * y["makhraj"]
    return result
def taqsim(x,y):
    result = {}
    result["surat"] = x["surat"] * y["makhraj"]
    result["makhraj"] = x["makhraj"] * y["surat"]
    return result

def zarb(x,y):
    result = {}
    result["surat"] = x["surat"] * y["surat"]
    result["makhraj"] = x["makhraj"] * y["makhraj"]
    return result

def sho(z):
    print( z["surat"], "/", z["makhraj"] )

kasr_a = {"surat": 2, "makhraj": 5}
kasr_b = {"surat": 1, "makhraj": 3}

kasr_c = zarb(kasr_a, kasr_b)
kasr_d = jamm(kasr_a , kasr_b)
kasr_e = tafriq(kasr_a , kasr_b)
kasr_f = taqsim(kasr_a , kasr_b)


choic = int(input("kudum? 1.jamm, 2.zarb, 3.tafriq, 4.taqsim: "))
if choic == 1:
    sho(kasr_d)
elif choic == 2:
    sho(kasr_c)
elif choic == 3:
    sho(kasr_e)
elif choic == 4:
    sho(kasr_f)
else:
    print("error")