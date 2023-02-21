
class Plant:
    def __init__(self,color):
        self.__color = color


    def get_color(self):
        return self.__color

#Subclass
class Flower(Plant):
    #Cant create subclass without first creating superclass 
    def __init__(self,color, petals):
        Plant.__init__(self,color)

        self.__petals = petals

    def get_petals(self):
        return self.__petals
