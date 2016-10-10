#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.tag_dicc = {
            'root-layout': ['width', 'height',
                            'background-color'],
            'region': ['id', 'top', 'bottom', 'left', 
                       'right'],
            'img': ['src', 'region', 'begin', 'dur'],
            'audio': ['src', 'begin', 'dur'],
            'textstream': ['src', 'region']}
        self.tags = []

    def startElement(self, name, attrs):
        if name in self.tag_dicc:
            atributes = {}
            atributes['tag'] = name
            for atribute in self.tag_dicc[name]:
                atributes[atribute] = attrs.get(atribute, "")
            self.tags.append(atributes)

    def get_tags(self):
        return self.tags

if __name__ == "__main__":

    parser = make_parser()
    handler = SmallSMILHandler()
    parser.setContentHandler(handler)
    parser.parse(open('karaoke.smil'))
    print(handler.get_tags())
