import xml.etree.ElementTree as ET
import re
import csv
import json

from transliterate import translit

finish = []
data = {}
model_fields = {}


def add_data(key, value):
    need_fields = {'gtin', 'title', 'price', 'retail-price', 'product_type', 'gross_weight', 'color', 'sale'}
    if key == 'id':
        data['pk'] = value
        data['model'] = 'emma.item'
    elif key in need_fields:
        model_fields[key] = value


tree = ET.parse('src/fixtures/fixture.xml')
root = tree.getroot()

with open('src/fixtures/ListOfSKUForTestTask - Sheet1.csv', 'r') as f:
    reader = csv.reader(f)
    r_list = list(reader)
    my_list = [val for sublist in r_list for val in sublist]

with open('src/fixtures/ListOfSKU2ForTestTask - Sheet1.csv', 'r') as f:
    reader = csv.reader(f)
    reader_list = list(reader)

with open('db.json', 'w') as outfile:
    for item in root.findall('channel/item'):
        if item[1].text in my_list:
            for elem in item:
                tag = re.sub(r'\{.*\}', '', elem.tag)
                add_data(tag, elem.text)
            for var in reader_list[1:]:
                if item[1].text == var[0]:
                    add_data('weight', var[1])
                    add_data('color', translit(var[2], reversed=True))
                    add_data('sale', var[3])
            data['fields'] = model_fields.copy()
            finish.append(data.copy())
            json.dump(finish, outfile)