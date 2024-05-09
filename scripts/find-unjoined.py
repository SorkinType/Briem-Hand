from fontTools.ttLib import TTFont
import string
from youseedee import ucd_data
from vharfbuzz import Vharfbuzz
import argparse

parser = argparse.ArgumentParser(description='Find unjoined pairs')
parser.add_argument('font', metavar='FONT',
                    help='font file to check')
parser.add_argument('--ascii-only', action='store_true',
                    help='Check only ascii pairs')

args = parser.parse_args()

font = TTFont(args.font)
vharfbuzz = Vharfbuzz(args.font)

marks = { k for k,v in font["GDEF"].table.GlyphClassDef.classDefs.items() if v == 3 }

def is_connected(l,r):
    buf = vharfbuzz.shape(l+r)
    gi = []
    # Excluding mark glyphs, there should be three
    count_of_bases = len([
        info for info in buf.glyph_infos
        if font.glyphOrder[info.codepoint] not in marks
    ])
    return count_of_bases > 2


letters = []
for codepoint in font["cmap"].getBestCmap().keys():
    d = ucd_data(codepoint)
    if d.get("Script") != "Latin":
        continue
    if args.ascii_only and chr(codepoint) not in string.ascii_lowercase:
        continue
    if d.get("General_Category") == "Ll":
        letters.append(chr(codepoint))


for l in letters:
    if l in "qjg":
        continue
    unconnected = [l+r for r in letters if not is_connected(l, r)]
    if unconnected:
        print(" ".join(unconnected))
