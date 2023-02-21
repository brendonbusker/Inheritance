import a_PlantClass as pc

primrose = pc.Plant("Green")

sunflower = pc.Flower("Yellow", 12)

print(primrose.get_color())

#this works even though the get_color method was definied in the original class
print(sunflower.get_color())
print(sunflower.get_petals())


#print(primrose.get_petals())
