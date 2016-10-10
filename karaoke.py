#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import sys
import json
from urllib.request import urlretrieve

try:
    first_json = sys.argv[1]
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
        data = ""
        for tag in self.atr_list:
            name = tag[0]
            data += name
            atributes = tag[1]
            for atribute in atributes:
                if atributes[atribute] != "":
                    data += "\t" + atribute + '="' + atributes[atribute] + '"'
            data += "\n"
        return data
           

    def to_json(self, smil_file, json_file = first_json):
        first_json = sys.argv[1][:-4]+"json"
        json_file = open(json_file, 'w')
        json.dump(self.atr_list, json_file)

    def do_local(self):
        for tag in self.tags:
            atts = tag[1]
            for att in atts:
                if atts[att][0:7] == "http://":
                    os.system("wget -q " + atts[att])
                    campos = atts[att].split('/')
                    atts[att] = campos[-1]    
        
    

if __name__ == "__main__":

    smil_file = sys.argv[1]
    karaoke = KaraokeLocal(smil_file)
    karaoke.__str__()
    karaoke.to_json(smil_file)
    karaoke.do_local()
    karaoke.to_json(smil_file, "local.json")
    karaoke.__str__()          
