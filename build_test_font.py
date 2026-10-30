# Builds a minimal test font (placeholder outlines) containing the IQ-KR ligature.
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.feaLib.builder import addOpenTypeFeaturesFromString

names = [".notdef", "uni1F3F4", "uniE0069", "uniE0071", "uniE006B", "uniE0072", "uniE007F",
         "emoji_u1f3f4_e0069_e0071_e006b_e0072_e007f"]
cmap = {0x1F3F4: "uni1F3F4", 0xE0069: "uniE0069", 0xE0071: "uniE0071",
        0xE006B: "uniE006B", 0xE0072: "uniE0072", 0xE007F: "uniE007F"}
fb = FontBuilder(1000, isTTF=True)
fb.setupGlyphOrder(names)
fb.setupCharacterMap(cmap)
empty = TTGlyphPen(None).glyph()
pen = TTGlyphPen(None)
pen.moveTo((0, 0)); pen.lineTo((0, 500)); pen.lineTo((500, 250)); pen.closePath()
glyphs = {n: empty for n in names}
glyphs["uni1F3F4"] = pen.glyph()
glyphs["emoji_u1f3f4_e0069_e0071_e006b_e0072_e007f"] = pen.glyph()
fb.setupGlyf(glyphs)
fb.setupHorizontalMetrics({n: (0 if n.startswith("uniE") else 1000, 0) for n in names})
fb.setupHorizontalHeader(ascent=800, descent=-200)
fb.setupNameTable({"familyName": "IQKR Test", "styleName": "Regular"})
fb.setupOS2()
fb.setupPost()
addOpenTypeFeaturesFromString(fb.font, open("features.fea", encoding="utf-8").read())
fb.save("iqkr_test.ttf")
print("built iqkr_test.ttf")
