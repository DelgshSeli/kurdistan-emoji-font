# Checks the six-scalar IQ-KR sequence shapes to exactly one glyph.
import sys
import uharfbuzz as hb
face = hb.Face(hb.Blob.from_file_path(sys.argv[1]))
font = hb.Font(face)
buf = hb.Buffer()
buf.add_str("\U0001F3F4\U000E0069\U000E0071\U000E006B\U000E0072\U000E007F")
buf.guess_segment_properties()
hb.shape(font, buf, {"ccmp": True, "liga": True})
names = [font.glyph_to_string(i.codepoint) for i in buf.glyph_infos]
print("glyphs:", names)
assert names == ["emoji_u1f3f4_e0069_e0071_e006b_e0072_e007f"], names
print("PASS")
