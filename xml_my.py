import xml.etree.ElementTree as ET
import re
import csv

tree = ET.parse('../../files/gshop.xml')
root = tree.getroot()

with open('../../files/ListOfSKUForTestTask - Sheet1.csv', 'r') as f:
    reader = csv.reader(f)
    my_list = list(reader)

for item in root.findall('channel/item'):
    item = int()
    if item[1].text in my_list:
        print(item[1].text)
