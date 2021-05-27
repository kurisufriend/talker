#programs importing this file as a library should load() the phenomes then use talk() to speak
import os
import sys
import requests
from pydub import AudioSegment
def talk(word, dict):
    all = ["AA", "AE", "AH", "AO", "AW", "AY", "B", "CH", "D", "DH", "EH", "ER", "EY", "F", "G", "HH", "IH", "IY", "JH", "K", "L", "M", "N", "NG", "OW", "OY", "P", "R", "S", "SH", "T", "TH", "UH", "UW", "V", "W", "Y", "Z", "ZH"]
    if not os.path.exists("phenome-samples"): os.mkdir("phenome-samples")
    for phenome in all:
        if not os.path.isfile("phenome-samples/"+phenome):
            print("missing phenome audio:", phenome)
    new = []
    for phenome in dict[word.upper()]:
        if phenome[-1].isdigit(): new.append(phenome[0:-1])
        else: new.append(phenome)
    print("<", new)
def load():
    ps = {}
    if not os.path.isfile("cmudict.txt"):
        print("downloading phenomes...")
        f = open("cmudict.txt", "w", encoding="utf-8")
        f.write(requests.get("http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict-0.7b").text)
        f.close()
    print("loading phenomes...")
    f = open("cmudict.txt", "r", encoding="utf-8")
    for line in f.read().split("\n"):
        if line.startswith(";") or line == "": continue
        sp1 = line.split("  ")
        ps[sp1[0]] = sp1[1].split(" ")
    print("succesfully loaded phenomes")
    return ps
def main():
    ps = load()
    while True:
        inp = input("> ")
        try:
            for word in inp.split(" "): talk(word, ps)
        except:
            print("word(s) not in phenome dictionary")
if __name__ == "__main__":
    main()