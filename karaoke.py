#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import sys
import json



if __name__ == "__main__":
    
    try:
        smil_file = sys.argv[1]
    except IndexError:
        sys.exit('Usage: python3 karaoke.py file.smil.')
        
    parser = make_parser()
    handler = SmallSMILHandler()
    parser.setContentHandler(handler)
    parser.parse(open(smil_file))
    atr_list = handler.get_tags()

    for element in atr_list:
        line = element [0]
        atributes = element[1]
        for atribute in element[1]:
            if element[1][atribute] != "":
                line = line + '\t' + atribute + '=' + "" + element[1][atribute]
            print(line)
            json_file = open(json_file, 'w')
            json.dump(atr_list, json_file)
