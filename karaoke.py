#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import sys
import json
from urllib.request import urlretrieve

try:
    file = sys.argv[1]
except IndexError:
    sys.exit('Usage: python3 karaoke.py file.smil.')

class KaraokeLocal():

    def __init__(self, smil_file):
        self.data = ""
        parser = make_parser()
        self.handler = SmallSMILHandler()
        parser.setContentHandler(self.handler)
        parser.parse(open(smil_file))
        self.atr_list = self.handler.get_tags()

    def __str__(self):
        for ele in self.atributes_list:
            line = ele[0]
            atributos = ele[1]
            for at in ele[1]:
                if ele[1][at] != "":
                    line = line + '\t' + at + '=' + '"' + ele[1][at] + '"'
            print(line)
            self.datos += line

    def to_json(self, name_json_file):
        json_file = name_json_file[:-4] + "json"
        json.dump(self.atr_list, open(json_file, 'w'))
        return json_file
        
    def do_local(self):
        for list in self.atr_list:
            atributes = list[1]
            for atribute in atributes:
                if atributes[atribute][:7] == "http://":
                    urlretrieve(atributes[atribute], 
                                atributes[atribute].split('/')[-1])
                    atributes[atribute] = atributes[atribute].split('/')[-1]

if __name__ == "__main__":

    smil_file = sys.argv[1]
    karaoke = KaraokeLocal(smil_file)
    karaoke.__str__()
    karaoke.to_json(smil_file)
    karaoke.do_local()
    karaoke.to_json(smil_file, "local.json")
    karaoke.__str__()          
