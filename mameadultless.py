'''
Created on 3 feb. 2017

@author: Bernardo Riveira (noni)
'''

import xml.etree.ElementTree
import os
import re

XMLdatabaseOfGoodRoms="d:\\mame_no_casino_mahjong_mature.xml"
path2MameRoms="D:\\mame"

if __name__ == '__main__':
    # good roms (with "zip" at the end) 
    goodRoms = map(lambda x: (x.get("name") + ".zip"), xml.etree.ElementTree.parse(XMLdatabaseOfGoodRoms).getroot().findall("game"))    
    goodRoms.sort()
    
    print("--------------------")
    print("good, known MAME roms: {0}\n".format(goodRoms.__len__()))
        
    # filenames in rom directory
    filenames = next(os.walk(path2MameRoms))[2]
    filenames = filter(re.compile(".+\\.zip").match, filenames)
    filenames.sort()

    print("--------------------")
    print("total MAME roms in {0}: {1}\n".format(path2MameRoms, filenames.__len__()))
    
    # filenames in rom dir not in good roms
    
    badRoms = filter(lambda x: x not in goodRoms, filenames)
    
    print("--------------------")
    print("total bad files {0}\n".format(badRoms.__len__()))
    # print out the files to remove (those in the directory not in "goodRoms" list)
    for filename in badRoms:
        print filename
    
    