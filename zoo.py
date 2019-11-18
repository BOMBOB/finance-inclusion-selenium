#!/usr/bin/env python3
from wcag_zoo.validators.tarsier import Tarsier
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from decimal import Decimal as D
from utils import generate_opaque_color
driver = webdriver.Chrome()
driver.get("http://www.python.org")

elems = driver.find_elements(By.XPATH, '//*')

for node in elems:
    if node.text is None or node.text.strip() == "":
        continue
    if node.tag_name in ['script', 'style']:
        continue
    #print(node.tag_name)
    colors = [[1, 2, 3, 1]]  # Black-ish
    backgrounds = [[254, 253, 252, 1]]  # White-ish
    fonts = [{'font-size': '10pt', 'font-weight': 'normal'}]
    # ----- RGBA -----
    #print(eval(node.value_of_css_property('color').replace('rgba', '')))
    #print(eval(node.value_of_css_property('background-color').replace('rbga', '')))
    # ---Font Size ---
    #print(int(node.value_of_css_property('font-size').replace('px', '')) * D('0.75'))
    # --- Weight (bold is more than 500)
    #print(int(node.value_of_css_property('font-weight')))
    # for styles in get_applicable_styles(node):
    #     if "color" in styles.keys():
    #         colors.append(normalise_color(styles['color']))
    #     if "background-color" in styles.keys():
    #         backgrounds.append(normalise_color(styles['background-color']))
    #     font_rules = {}
    #     for rule in styles.keys():
    #         if 'font' in rule:
    #             font_rules[rule] = styles[rule]
    #     fonts.append(font_rules)

# my_html = b"<html><head><body><h1>1</h1><h3>This is wrong, it should be h2"
# instance = Tarsier()
# results = instance.validate_document(my_html)

# print("/no/tmp/dir", len(results['failures']), "failures")
# print('####### RESULT ########')
# print(results)