#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import sys
import json


if __name__ == "__main__":
    try:
        file = sys.argv[1]
    except IndexError:
        sys.exit('Usage: python3 karaoke.py file.smil.')
        
    parser = make_parser()
    handler = SmallSMILHandler()
    parser.setContentHandler(handler)
    parser.parse(open(file))
    atr_list = handler.get_tags()
    print(atr_list)
