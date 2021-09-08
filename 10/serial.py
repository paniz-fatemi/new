from media import meedia
class seriall(meedia):
    def __init__(self,typ,id,name,IMDBscore,url,duration,casts,teedad):
        meedia.__init__(typ,id,name,IMDBscore,url,duration,casts)
        self.teedad = teedad