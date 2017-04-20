"""
constants.py

DESCRIPTION:
  Defines constants required by multiple ui modules and subpackages,
  and constants that reach external files required by ui modules (whose
  definitions do not belong in resmaps.py).


Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.
"""
from os import path, listdir

from ..constants import ROOT_PATH
from ..util import get_first_textline, get_stripped_nonempty_file_lines
from ..config import DRIVE

file = open(path.join(ROOT_PATH, 'jeoparpy', 'dir.txt'), 'r')
directory = file.readline()

if DRIVE == False:
    _rulesPath = path.join(ROOT_PATH, 'games', directory, 'rules.txt')
    _subPath = path.join(ROOT_PATH, 'games', directory, 'subtitle.txt')
else:
    DEVICE = listdir('/media')[0]
    _rulesPath = path.join('/media', DEVICE, 'games', directory, 'rules.txt')
    _subPath = path.join('/media', DEVICE, 'games', directory, 'subtitle.txt')

# immo colors
IS24_GREY = (242, 242, 242)  #  grey background
IS24_BLUE = (0, 52, 104) # background-brandblue
IS24_ORANGE = (255, 117, 0) # background-brandorange

JEOP_BLUE = IS24_GREY
# color replacements
COLOR_BLUE = IS24_GREY
COLOR_WHITE = IS24_BLUE
COLOR_YELLOW = IS24_ORANGE

# special colors
COLOR_FOR_AMOUNT = IS24_ORANGE
COLOR_FOR_CATEGORIES = IS24_BLUE

SUBTITLE = 'Scout24 Hackdays - Pi Edition'
RULES = get_stripped_nonempty_file_lines(_rulesPath)
