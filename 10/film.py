from media import meedia
class filmm(meedia):
    def __init__(self, typ, id,name,IMDBscore,url,duration,casts):
            meedia().__init__(typ,id,name,IMDBscore,url,duration,casts)
    def sho(self):
        return meedia().showInfo()