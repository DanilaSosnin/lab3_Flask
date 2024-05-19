import urllib.request
import xml.dom.minidom as md

def get_data():
    web_file = urllib.request.urlopen('https://cbr.ru/scripts/XML_daily.asp?')
    return web_file.read()


def get_currencies_dictionary(content):

    global char_code, value
    dom = md.parseString(content)
    dom.normalize()

    elements = dom.getElementsByTagName("Valute")
    currency_dict = {}

    currency_dict['RUB'] = 1
    for node in elements:
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == "VunitRate":
                    if child.firstChild.nodeType == 3:
                        value = float(child.firstChild.data.replace(',', '.'))
                if child.tagName == "CharCode":
                    if child.firstChild.nodeType == 3:
                        char_code = child.firstChild.data
        currency_dict[char_code] = value
    return currency_dict


currency_dict = get_currencies_dictionary(get_data())