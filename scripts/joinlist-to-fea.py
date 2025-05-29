from glyphsLib import GSFont
import sys

combos = {}

fh = open("sources/JoinList.txt", "r", encoding="UTF-16")
joinlist = fh.readlines()[1].split(" ")
font = GSFont("sources/BriemHand.glyphs")
cmap = {}
for glyph in font.glyphs:
    if glyph.unicode is not None:
        cmap[int(glyph.unicode, 16)] = glyph.name

for join in joinlist:
    left, joiner, right = join
    left = cmap.get(ord(left), None)
    if left is None:
        print(f"Left glyph '{left}' not found in font.")
        sys.exit(1)
    joiner = cmap.get(ord(joiner), None)
    if joiner is None:
        print(f"Joiner glyph '{joiner}' not found in font.")
        sys.exit(1)
    right = cmap.get(ord(right), None)
    if right is None:
        print(f"Right glyph '{right}' not found in font.")
        sys.exit(1)
    combos.setdefault((left, joiner), []).append(right)

for (left, joiner), rights in sorted(combos.items()):
    if len(rights) == 1:
        right = rights[0]
        print(f"sub {left}' {right} by {left} {joiner};")
    else:
        right = " ".join(rights)
        print(f"sub {left}' [{right}] by {left} {joiner};")
