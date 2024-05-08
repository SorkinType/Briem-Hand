from fontTools.ttLib import TTFont
import string
import unicodedata
from vharfbuzz import Vharfbuzz
import argparse

parser = argparse.ArgumentParser(description='Find unjoined pairs')
parser.add_argument('font', metavar='FONT',
                    help='font file to check')

args = parser.parse_args()

font = TTFont(args.font)
vharfbuzz = Vharfbuzz(args.font)

def is_decomposed(l):
    buf = vharfbuzz.shape(l)
    return len(buf.glyph_infos) > 1


for codepoint in font["cmap"].getBestCmap().keys():
    char = chr(codepoint)
    if unicodedata.decomposition(char) and unicodedata.category(char) == "Ll":
        if not is_decomposed(char):
            print(char, end=" ")
