#1
class kasr:
    #property:
    surat = None
    makhraj = None


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
    def zarb(x,y):
        result = {}
        result["surat"] = x["surat"] * y["surat"]
        result["makhraj"] = x["makhraj"] * y["makhraj"]
        return result
            
    def taqsim(x,y):
        result = {}
        result["surat"] = x["surat"] * y["makhraj"]
        result["makhraj"] = x["makhraj"] * y["surat"]
        return result

        
    def sho(a):
            print(a.surat, "/", a.makhraj)

kasr1 = kasr()
kasr1.surat= 5
kasr1.makhraj = 7

kasr2 = kasr()
kasr2.surat = 3
kasr2.makhraj = 8
