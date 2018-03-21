# -*- coding: utf-8 -*-


def lire():
    try:
        ReadFile=open("test.txt","r")
        for line in ReadFile:
            print(line)
        ReadFile.close()
    except IOError:
        print("File not found")
    print("app is done")


def ecrire():
    #Write to file
    out=open("test.txt","a")
    for i in range(5):
        inputToFile=input("enter string to write to file:")
        out.write("\n{}".format(inputToFile))
    out.close()

