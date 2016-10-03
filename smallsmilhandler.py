#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):
        self.root_layout = ""
        self.region = ""
        self.img = ""
        self.audio = ""
        self.textstream = ""
        
        self.atr_root_layout = ['wi': 'width', 'he': 'height',
                                'ba': 'background_color']
        self.atr_region = ['id': 'id', 'to': 'top', 'bo': 'bottom',
                           'l': 'left', 'ri': 'right']
        self.atr_img = ['sr': 'src', 're': 'region',
                        'be': 'begin','du': 'dur']
        self.atr_audio = ['sr': 'src', 'be': 'begin', 'du':'dur']
        self.atr_textstream = ['sr': 'src', 're': 'region']

    def startElement(self, name, attrs):
        if name == 'root_layout':
            for atributo in self.atr_root_layout:
                self.atr_root_layout = attrs.get(atributo, '')
                
        elif name == 'region':
            for atributo in self.atr_region:
                self.atr_region = attrs.get(atributo, '')
                
        elif name == 'img':
            for atributo in self.atr_img:
                self.atr_img = attrs.get(atributo, '')
                
        elif name == 'audio':
            for atributo in self.atr_audio:
                self.atr_audio = attrs.get(atributo, '')

        elif name == 'textstream':
            for atributo in self.atr_textstream:
                self.atr_textstream = attrs.get(atributo, '')
                
        
if __name__ == "__main__":

    parser = make_parser()
    handler = SmallSMILHandler()
    parser.setContentHandler(handler)
    parser.parse(open('karaoke.smil')
