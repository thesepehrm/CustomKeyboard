characters = "abcdefghijklmnopqrstuvwxyz"

with open("fonts.ck", "r") as fontsFile:
    fonts = fontsFile.read().splitlines()
    with open("Base.keylayout", "r") as baseLayoutFile:
        base = baseLayoutFile.read()
        for font in fonts:
            if font[0] == "#":
                continue
            model = font.split(" ")
            temp = base
            for i in range(0, 26):
                temp.replace(characters[i], model[1][i])
            if model[2] != "NULL":
                for i in range(0, 26):
                    temp.replace('"' + characters[i].upper() + '"', '"' + model[2][i] + '"')
            output = open(model[0] + ".keylayout", "w")
            output.write(temp)
            output.close()
