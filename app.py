# author: Sepehr Mohammadi
from random import randint
from subprocess import call

characters = "abcdefghijklmnopqrstuvwxyz"


def makeDirectories(name):
    call(['cp', '-r', 'Base/Base.bundle', 'Generated/'])
    call(['mv', 'Generated/Base.bundle', 'Generated/' + name + '.bundle'])
    return


def replace_name(infile, new_word, utf16=False):
    if not utf16:
        m = open(infile, 'r').read().replace('&name', new_word)
    else:
        f1 = open(infile, 'rb')
        m = f1.read().decode(encoding='utf-8').replace('&name', new_word)
    f2 = open(infile, 'w')
    f2.write(m)
    f2.close()
    return

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
            # File Generated!
            makeDirectories(model[0])
            call(['mv', 'Generated/' + model[0] + '.keylayout',
                  'Generated/' + model[0] + '.bundle/Contents/Resources/' + model[0] + '.keylayout'])
            replace_name('Generated/' + model[0] + '.bundle' + '/Contents/Info.plist', model[0])
            replace_name('Generated/' + model[0] + '.bundle' + '/Contents/version.plist', model[0])
            replace_name('Generated/' + model[0] + '.bundle' + '/Contents/Resources/en.lproj/InfoPlist.strings',
                         model[0], True)
