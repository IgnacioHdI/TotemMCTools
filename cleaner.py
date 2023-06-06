#This file will be run before making any changes to the GitHub repository

from PIL import Image
import os

icon = Image.open("Pack/pack_icon.png")
totem = Image.open("Pack/textures/items/totem.png")
icon2 = Image.open("Pack_2/pack.png")
totem2 = Image.open("Pack_2/assets/minecraft/textures/item/totem_of_undying.png")
en = open("Pack/texts/en_US.lang", "w")
es = open("Pack/texts/es_ES.lang", "w")
dirList = os.listdir()
packList = []

print("Deleting language file contents")
en.write("")
es.write("")

print("Erasing pixels from textures")
for y in range(16):
    for x in range(16):
        icon.putpixel((x,y), (0,0,0,0))
        totem.putpixel((x,y), (0,0,0,0))        
        icon2.putpixel((x,y), (0,0,0,0))
        totem2.putpixel((x,y), (0,0,0,0))

icon.save("Pack/pack_icon.png")
totem.save("Pack/textures/items/totem.png")
icon2.save("Pack_2/pack.png")
totem2.save("Pack_2/assets/minecraft/textures/item/totem_of_undying.png")

print("Detecting resource pack files")
for i in range(len(dirList)):
    if 'Totem_Pack_' in dirList[i]:
        packList.append(dirList[i])

print("Deleting resource pack files")
for i in range(len(packList)):
    os.remove(packList[i])