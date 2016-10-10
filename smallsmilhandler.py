#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.atr_list = []
        self.atr_root_layout = ['width', 'height', 'background_color']
        self.atr_region = ['id', 'top', 'bottom', 'left', 'right']
        self.atr_img = ['src', 'region', 'begin', 'dur']
        self.atr_audio = ['src', 'begin', 'dur']
        self.atr_textstream = ['src', 'region']

        self.tags = {'root_layout': self.atr_root_layout,
                     'region': self.atr_region,
                     'img': self.atr_img,
                     'audio': self.atr_audio,
                     'textstream': self.atr_textstream}

    def startElement(self, tag, attrs):
        self.smil_data = {}
        if tag in self.tags:
            for atribute in self.tags[tag]:
                self.smil_data[atribute] = attrs.get(atribute, "")
            self.atr_list.append([tag, self.smil_data])
            
    def get_tags(self):
        return self.atr_list
        
if __name__ == "__main__":
    parser = make_parser()
    handler = SmallSMILHandler()
    parser.setContentHandler(handler)
    parser.parse(open('karaoke.smil'))
    print(handler.get_tags())
