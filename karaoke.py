#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import sys
import json
from urllib.request import urlretrieve

try:
    smil_file = sys.argv[1]
except IndexError:
    sys.exit('Usage: python3 karaoke.py file.smil')


class KaraokeLocal():

    def __init__(self):
        parser = make_parser()
        handler = SmallSMILHandler()
        parser.setContentHandler(handler)
        parser.parse(open(smil_file))
        self.tags = handler.get_tags()

    def __srt__(self):
        data = ''
        for line in self.tags:
            data = data + line['tag'] + '\t'
            for atribute in line:
                if atribute != 'tag' and line[atribute] != "":
                    data = data + atribute + ' = "' + line[atribute] + '"\t'
            data = data + '\n'
        print(data)

    def to_json(self, smil_file, json_file):
        json = sys.argv[1][:-4] + 'json'
        json_file = open(json, 'w')
        json.dump(self.tags, json_file)

    def do_local(self):
        for line in self.tags:
            for tag in line:
                for atribute in line['tag']:
                    if line['tag'][atribute][:7] == "http://":
                        urlretrieve(line[tag][atribute])
                        url = line[tag][atribute].split('/')
                        line[tag][atribute] = url[-1]

if __name__ == "__main__":

    smil_file = sys.argv[1]
    karaoke = KaraokeLocal()
    karaoke.__init__()
    karaoke.__srt__()
    karaoke.to_json(smil_file)
    karaoke.do_local()
    karaoke.to_json(smil_file, "local.json")
    karaoke.__srt__()
