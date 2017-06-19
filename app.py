# author: Sepehr Mohammadi
from random import randint

characters = "abcdefghijklmnopqrstuvwxyz"

with open("fonts.ck", "r") as fontsFile:
    fonts = fontsFile.read().splitlines()
    with open("Base/Base.keylayout", "r") as baseLayoutFile:
        base = baseLayoutFile.read()
        for font in fonts:
            if font[0] == "#":
                continue
            model = font.split(" ")
            temp = base
            temp = temp.replace("<NAME>", model[0])
            temp = temp.replace("<ID>", str(randint(1000, 10000)))
            for i in range(0, 26):
                temp = temp.replace('"' + characters[i] + '"', '"' + model[1][i] + '"')
            if model[2] != "NULL":
                for i in range(0, 26):
                    temp = temp.replace('"' + characters[i].upper() + '"', '"' + model[2][i] + '"')
            output = open("Generated/" + model[0] + ".keylayout", "w")
            output.write(temp)
            output.close()
