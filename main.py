import time
import random


MATRIX_SIZE = 10


class  AnimaL: #
    def __init__(self, species, step_speed, strenght, age):
        self.species = species
        self.step_speed = step_speed
        self.strength = strenght
        self.age = age
        self.x = random.randint(0, MATRIX_SIZE - 1)
        self.y = random.randint(0, MATRIX_SIZE - 1)


    def step_up(self):
         eski_konum_x , eski_konum_y = self.x , self.y
         self.x = (self.x + random.choice([-1, 1])) % MATRIX_SIZE
         self.y = (self.y + random.choice([-1, 1])) % MATRIX_SIZE
         print(" {} adım attı  {} ,{} dan {} , {}".format(animal.species, eski_konum_x , eski_konum_y ,self.x , self.y))






    def show_general_features(self):
       print("""
       
        Species    : {}
        Step speed : {}
        Strength   : {}
        Age        : {}
         
     """.format(self.species, self.step_speed, self.strength, self.age))




class CAT(AnimaL):


   def __init__(self, nose_color , genus):
    super().__init__("Cat",5,1200,2)
    self.nose_color = nose_color
    self.genus = genus

   def show_cat_features(self):
       print( """ 
          
          Nose color : {} 
          Genus      : {} 
     
     """.format(self.nose_color  , self.genus))



class  DOG(AnimaL):


    def __init__(self, decibel_of_barking, genus ):
        super().__init__( "Dog",3, 600, 2)
        self.decibel_of_barking = decibel_of_barking
        self.genus = genus

    def show_dog_features(self):
        print("""
        
               Decibel of barking : {}
               Genus              : {}
               
               """.format(self.decibel_of_barking, self.genus))


class BIRD(AnimaL):


    def __init__(self, feather_color , genus ):
        super().__init__("kuş", 4,100,4)
        self.feather_color = feather_color
        self.genus = genus

    def show_bird_features(self):
       print(""" 
       
         Feather_color : {}
         Genus         : {}
         
         """.format(self.feather_color,self.genus))

class FISH(AnimaL):

    def __init__(self, scale_color ,genus):
        super().__init__("Fish",8,500,10)
        self.scale_color = scale_color
        self.genus = genus

    def show_fish_features(self):
        print(""" 
         Scale color : {}
         Genus       : {}
         """.format(self.scale_color,self.genus))

class DINOSAUR(AnimaL):

    def __init__(self, fire_ball_power, can_fly_ , genus):
        super().__init__("Dinosaur",10,750,2500)
        self.fire_ball_power = fire_ball_power
        self.can_fly_ = can_fly_
        self.genus = genus

    def show_dinosaur_features(self):
        print("""
             Fire ball power : {}
             Can fly ?       : {}
             Genus           : {}
         
        """.format(self.fire_ball_power,self.can_fly_,self.genus))



class HUMAN(AnimaL):
    def __init__(self, eye_color, hunting ):
        super().__init__("Human",2,1000,25)
        self.eye_color = eye_color
        self.hunting = hunting

    def hunting_power(self, using_arrow , runing , iq ,):
        self.hunting += (using_arrow + runing + iq)
        print("New hunting power = {} ".format(self.hunting))

_Lufi_ = CAT("blue","cat")
_Sivas_Kangalı_ = DOG(100,"dog")
_Maviş_ = BIRD("blue","bird")
_Palamut_ = FISH("gray","fısh")
_T_rex_ = DINOSAUR(5,"NO","dinosaur")
_Zeynep_ = HUMAN("black",0)#because she is a vegan person
animals = [_Lufi_, _Sivas_Kangalı_, _Maviş_, _Palamut_, _T_rex_, _Zeynep_]

def position_control(animals):
    positions = {}
    for animal in animals :
        position = (animal.x, animal.y)
        if position in positions :
            positions[position].append(animal)
        else:
            positions[position] = [animal]
    return positions

def war_of_animals(animals):
    survived_ones = [ ]
    positions = position_control(animals)


    for group_of_animals in positions.values():
        cat = next((animal for animal in group_of_animals if animal.species == "Cat"), None )
        human = next((animal for animal in group_of_animals if animal.species == "Human"), None)
        dinosaur = next((animal for animal in group_of_animals if animal.species == "dinosaur") , None)
        fish = next((animal for animal in group_of_animals if animal.species == "Fish"), None)

       # generator oluşturduk.Generator bellekte yer işgal etmeyen itarator oluşturmaktır.
       # iterable özelliği olan nesneden iterator oluşturduk. Bu elemanlar üzerinde tek tek dolaşabilmemizi sağlıyor.
       # hayvan grubunun içindeki her bir hayvan için eğer hayvan kedi ise al ve cat generatoruna koy.Kedi yok ise bişey yapma

        if len(group_of_animals) == 1:
            survived_ones.append(group_of_animals[0])
        elif cat and human:
            survived_ones.append(human)
        elif fish and dinosaur:
            survived_ones.append(fish)
       # elif len(group_of_animals) == 2:
        #    group_of_animals.remove(group_of_animals[0])
        else:
            survived_ones.append(max(group_of_animals, key=lambda AnimaL: AnimaL.strength))
        print("savaş")

    return survived_ones


if __name__ == "__main__":
    time = -1
    tur = 0
    while len(animals) > 3 :
        tur += 1
        time += 1
        for animal in animals:
            if time % animal.step_speed == 0:
                animal.step_up()
        animals = war_of_animals(animals)
    print("{}. turda hayatta kalan hayvan sayısı {}".format(tur, len(animals)))

print("Last animals = {} ,{} ,{}".format(animals[0].species , animals[1].species , animals[2].species))























