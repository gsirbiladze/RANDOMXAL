#!/usr/bin/python

import os
import sys
import time
import argparse

from random import randint

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


parser = argparse.ArgumentParser(description='Stamp time or text on the image ...')
parser.add_argument('image_file', help='Image file location')
parser.add_argument('--font', '-f',  default='DejaVuSansMono', help='Font name or font file location. Default=%(default)s')
parser.add_argument('--size', '-s', type=int, default=16, help='Font size, Default=%(default)s')
parser.add_argument('--bg-color', '-b',  help='Background color')
parser.add_argument('--stamp-color', '-c', default='#000000', help='Stamp color')
parser.add_argument('--stamp-position', '-p', default='bottom', choices=['top', 'top_left', 'top_right',
                                                                        'center', 'center_left', 'center_right',
                                                                        'bottom', 'bottom_left', 'bottom_right'], help='Text position on the image. Default=%(default)s')
parser.add_argument('--text', '-t', help='Text')
parser.add_argument('--time-format', default='%m-%d-%Y %I:%M:%S %p', help="DateTime display format. Default='%(default)s'")
parser.add_argument('--duplicate', '-d', action='store_true', help='Duplicate and then make a change')
parser.add_argument('--show',  action='store_true', help='Show Picture')
args = parser.parse_args()


image_source  = args.image_file
font_file     = args.font
font_size     = args.size
bg_color      = args.bg_color
text_position = args.stamp_position
text_color    = args.stamp_color
make_a_copy   = args.duplicate
show          = args.show

if not os.path.isfile(image_source):
    print("Can't find file '%s'. Make sure file exists ..."%image_source)
    sys.exit(1)

try:
    img = Image.open(image_source)
except:
    print("Can't open image file '%s'. Make sure file is an image ..."%image_source)
    sys.exit(1)

imgW, imgH = img.size

if args.text:
    text_to_draw  = args.text
else:
    text_to_draw  = time.strftime(args.time_format)


try:
    font = ImageFont.truetype(font=font_file, size=font_size)
except:
    print("Coudn't find font '%s' ..."%font_file)
    font = ImageFont.load_default()

textW, textH = font.getsize(text_to_draw)

text_offset = 5
text_positions = {
    'top'          : (int(imgW/2 - textW/2),int( text_offset)),
    'top_left'     : (int(text_offset), int(text_offset)),
    'top_right'    : (int(imgW-text_offset-textW), int(text_offset)),
    'center'       : (int(imgW/2 - textW/2), int(imgH/2 - textH/2)),
    'center_left'  : (int(text_offset), int(imgH/2 - textH/2)),
    'center_right' : (int(imgW-text_offset-textW), int(imgH/2 - textH/2)),
    'bottom'       : (int(imgW/2 - textW/2), int(imgH-text_offset-textH)),
    'bottom_left'  : (int(text_offset), int(imgH-text_offset-textH)),
    'bottom_right' : (int(imgW-text_offset-textW), int(imgH-text_offset-textH)),
}

if bg_color:
    text_bg = Image.new('RGBA', (textW, textH), color=bg_color)
    draw_bg = ImageDraw.Draw(text_bg)
    draw_bg.text((0, 0), text_to_draw, font=font, fill=text_color)
    img.paste(text_bg, text_positions[text_position])
else:
    draw = ImageDraw.Draw(img)
    draw.text(text_positions[text_position], text_to_draw, font=font, fill=text_color)

if make_a_copy:
    file_part, ext = os.path.splitext(image_source)
    file_part = file_part + '_dupl' + str(randint(10000, 99999)) + ext
    img.save(file_part)
else:
    img.save(image_source)

if show: img.show()

img.close()

