class Student :
    def __init__(self, name , score ):
        self.name = name
        self.score = score
    def status (self) :
        if self.score >= 10 :
            print("passed")
        else :
            print("failed")
    def change_score (self , new_score) :
        if 0<=new_score<=20 :
           self.score = new_score
        else :
            print("invalid score")