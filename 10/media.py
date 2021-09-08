import pytube

class meedia:
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

        print(f"name: {self.name} director: {self.director} IMDBscore:{self.IMDBscore} duration:{self.duration} casts:{self.casts}")

    def download(self):
        ur = self.url
        adres = pytube.YouTube(ur).streams.first()
        adres.download(save_at='Downloads', save_as='newmedia.mp4')