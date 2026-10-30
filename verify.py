# Checks the six-scalar IQ-KR sequence shapes to exactly one glyph.
# Counts glyphs rather than names, because nanoemoji names glyphs itself.
import sys
import uharfbuzz as hb

font = hb.Font(hb.Face(hb.Blob.from_file_path(sys.argv[1])))
buf = hb.Buffer()
buf.add_str("\U0001F3F4\U000E0069\U000E0071\U000E006B\U000E0072\U000E007F")
buf.guess_segment_properties()
hb.shape(font, buf, {"ccmp": True, "liga": True})
glyphs = [info.codepoint for info in buf.glyph_infos]
print("glyph ids:", glyphs)
assert len(glyphs) == 1, f"expected 1 glyph, got {len(glyphs)}"
print("PASS")
