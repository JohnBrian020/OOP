#Blueprint of the object
class DJ:
    
    #Instance properties
    def __init__(self, name, genre, gig):
        self.name = name
        self.genre = genre
        self.gig = gig
    #Instance methods
    # 1. Adding new gig
    def add_gig(self, amount):
        self.gig += amount
        
    # 2. Changing new genre
    def changing_genre(self, new_genre):
        self.genre = new_genre
        
    # 3. Return formatted details
    def mixcloud(self):
        return f"DJ :{self.name}, Genre : {self.genre}, gig {self.gig}"
    
#Class instances
music1 =  DJ("Friday Mashups","Afrobeats", 10)
music2 =  DJ("Throwback Thursday","Oldschool", 15)

#Calling instance methods
print(music1.mixcloud())

#Modify the instance
music1.add_gig(20)
print(music1.mixcloud())
