#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):
        #self.inRoot_Layout = 0
        self.root_layout = ""
        self.width = ""
        self.height = ""
        self.background_color = ""
        
        #self.inRegion = 0
        self.region = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right =""
        
        #self.inImg = 0
        self.img = ""
        self.src = ""
        self.begin = ""
        self.dur = ""
        
        #self.inAudio = 0
        self.audio = ""
        
        #self.inTextstream = 0
        self.textstream = ""
        
        self.tags = []

    def startElement(self, name, attrs):
        if name == 'root_layout':
            self.width = attrs.get('width', "")
            self.height = attrs.get('height', "")
            self.background_color = attrs.get('background_color', "")
        elif name == 'region':
            self.id = attrs.get('id', "")
            self.top = attrs.get('top', "")
            self.bottom = attrs.get('bottom', "")
            self.left = attrs.get('left', "")
            self.right = attrs.get('right', "")
        elif name == 'img':
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
        elif name == 'audio':
            self.src = attrs.get('src', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
        elif name == 'textstream':
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")

    def get_tags(self):
        
        return self.tags
        
if __name__ == "__main__":

    parser = make_parser()
    handler = SmallSMILHandler()
    parser.setContentHandler(handler)
    parser.parse(open('karaoke.smil')
    self.tags = handler.get_tags()
    print(self.tags)
