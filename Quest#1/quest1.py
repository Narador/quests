import xml.etree.ElementTree as ET
import os
import sys
import string
import time

tree = ET.parse('MobileConfig.xml')
root = tree.getroot()

new = input('Choose a new value for max transcoding output fps: ')

def set_new():
    for fps in root.iter('max_transcoding_output_fps'):
        new_val = int(new)
        fps.text = str(new_val)
    
tree.write('MobileConfigTest.xml')
