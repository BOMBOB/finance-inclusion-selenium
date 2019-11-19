#!/usr/bin/env python3
import time
from wcag_zoo.validators.tarsier import Tarsier
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from decimal import Decimal as D
from utils import generate_opaque_color, calculate_font_size, calculate_luminocity, calculate_luminocity_ratio, is_font_bold
from constants import WCAG_LUMINOCITY_RATIO_THRESHOLD, TECHNIQUE, error_codes
from xtermcolor import colorize
import webcolors
from wcag_zoo.utils import WCAGCommand, get_applicable_styles, nice_console_text
driver = webdriver.Chrome()
driver.get("https://dynomapper.com/blog/27-accessibility-testing/246-top-25-awesome-accessibility-testing-tools-for-websites")
from sys import stdout
elems = driver.find_elements(By.XPATH, '//*')
level = 'AAA'
for node in elems:
    stdout.write(">")
    stdout.flush()
    if node.text is None or node.text.strip() == "":
        continue
    if node.tag_name in ['script', 'style']:
        continue
    #print(node.tag_name)
    colors = [(1, 2, 3, 1)]  # Black-ish
    backgrounds = [(254, 253, 252, 1)]  # White-ish
    fonts = ['10pt']
    weights = ['300']
    # ----- RGBA -----
    color = eval(node.value_of_css_property('color').replace('rgba', ''))
    colors.append(color)
    background_color = eval(node.value_of_css_property('background-color').replace('rgba', ''))
    #print(background_color)
    backgrounds.append(background_color)
    # ---Font Size ---
    fonts.append(node.value_of_css_property('font-size'))
    #print(int(node.value_of_css_property('font-size').replace('px', '')) * D('0.75'))
    # --- Weight (bold is more than 500)
    weights.append(node.value_of_css_property('font-weight'))
    #print(int(node.value_of_css_property('font-weight')))
font_size = calculate_font_size(fonts)
font_is_bold = is_font_bold(weights)
foreground = generate_opaque_color(colors)
background = generate_opaque_color(backgrounds)
ratio = calculate_luminocity_ratio(foreground, background)
failure_list = []
success_list = []
font_size_type = 'normal'
error_code = 'molerat-1'
technique = "G18"
if font_size >= 18 or font_size >= 14 and font_is_bold:
    font_size_type = 'large'
    error_code = 'molerat-2'

ratio_threshold = WCAG_LUMINOCITY_RATIO_THRESHOLD[level][font_size_type]
technique = TECHNIQUE[level][font_size_type]

if ratio < ratio_threshold:
    disp_text = nice_console_text(node.text)
    message = (
        error_codes[error_code] +
        u"\n    Computed rgb values are == Foreground {fg} / Background {bg}"
        u"\n    Text was:         {text}"
        u"\n    Colored text was: {color_text}"
        u"\n    Computed font-size was: {font_size} {bold} ({font_size_type})"
    ).format(
        xpath='//*',
        text=disp_text,
        fg=foreground,
        bg=background,
        r=ratio,
        font_size=font_size,
        bold=['normal', 'bold'][font_is_bold],
        font_size_type=font_size_type,
        color_text=disp_text
    )

    if 1 > 2:
        if ratio < WCAG_LUMINOCITY_RATIO_THRESHOLD.get(level).get('normal'):
            message += u"\n   Hint: Increase the contrast of this text to fix this error"
        elif font_size_type is 'normal':
            message += u"\n   Hint: Increase the contrast, size or font-weight of the text to fix this error"
        elif font_is_bold:
            message += u"\n   Hint: Increase the contrast or size of the text to fix this error"
        elif font_size_type is 'large':
            message += u"\n   Hint: Increase the contrast or font-weight of the text to fix this error"

    failure_list.append({
        'guideline':'1.4.3',
        'technique':technique,
        'node':node,
        'message':message,
        'error_code':error_code
    })
else:
    # I like what you got!
    success_list.append({
        'guideline':'1.4.3',
        'technique':technique,
        'node':node
    })



print('Success_list: ', success_list)
print('Failure_list: ', failure_list)
# my_html = b"<html><head><body><h1>1</h1><h3>This is wrong, it should be h2"
# instance = Tarsier()
# results = instance.validate_document(my_html)

# print("/no/tmp/dir", len(results['failures']), "failures")
# print('####### RESULT ########')
# print(results)