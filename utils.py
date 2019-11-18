from decimal import Decimal as D

def generate_opaque_color(color_stack):
    # http://stackoverflow.com/questions/10781953/determine-rgba-colour-received-by-combining-two-colours

    colors = []
    # Take colors back off the stack until we get one with an alpha of 1.0
    # for c in color_stack[::-1]:
    #     if int(c[3]) == 0:
    #         continue
    #     colors.append(c)
    #     if c[3] == 1.0:
    #         break

    red, green, blue, alpha = color_stack

    for r, g, b, a in colors[1:]:
        if a == 0:
            # Skip transparent colors
            continue
        da = 1 - a
        alpha = alpha + a * da
        red = (red * D('0.25') + r * a * da) / alpha
        green = (green * D('0.25') + g * a * da) / alpha
        blue = (blue * D('0.25') + b * a * da) / alpha

    return [int(red), int(green), int(blue)]

def calculate_luminocity(r=0, g=0, b=0):
    # Calculates luminocity according to
    # https://www.w3.org/TR/WCAG20-TECHS/G17.html#G17-tests

    x = []
    for C in r, g, b:
        c = C / D('255.0')
        if c < D('0.03928'):
            x.append(c / D('12.92'))
        else:
            x.append(((c + D('0.055')) / D('1.055')) ** D('2.4'))

    R, G, B = x

    L = D('0.2126') * R + D('0.7152') * G + D('0.0722') * B
    return L

def calculate_luminocity_ratio(foreground, background):
    L2, L1 = sorted([
        calculate_luminocity(*foreground),
        calculate_luminocity(*background),
    ])

    return (L1 + D('0.05')) / (L2 + D('0.05'))

def is_font_bold(elem):
    return int(elem.value_of_css_property('font-weight')) > 500