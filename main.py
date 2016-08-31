#!/usr/bin/python

import xml.etree.ElementTree as ET
import glob
import sys

SHIFT = 160
PREFIX = "new"


def shift_root_xml(root):
    for graphic in root.iter('Graphic'):
        graphic.set('X', '{}'.format(int(graphic.get('X')) - SHIFT))


def main():
    for file in glob.glob('*.xml'):
        try:
            tree = ET.parse(file)
            root = tree.getroot()
            shift_root_xml(root)
            tree.write('{}-{}'.format(PREFIX, file))
        except:
            print("Script failed!!")
            sys.exit(2)


if __name__ == '__main__':
    main()