# Kurdistan Region (IQ-KR) flag emoji: open-source font work

**Status: draft. Not a finished flag. Do not distribute as the official flag.**

## What this is

The Kurdistan Region of Iraq has the ISO 3166-2 subdivision code `IQ-KR` and the
CLDR subdivision subtag `iqkr`. The corresponding Unicode tag sequence is:

    U+1F3F4 U+E0069 U+E0071 U+E006B U+E0072 U+E007F

This sequence is valid Unicode, but it is not on the Unicode RGI recommended list,
so most platforms show a black flag with no Kurdistan flag. This repository holds
the open-source work to provide a glyph and ligature for the sequence in a font.

## Contents

| File | Purpose |
|---|---|
| `features.fea` | OpenType GSUB ligature mapping the six scalars to one colour glyph |
| `build_test_font.py` | Builds a placeholder test font containing the ligature |
| `verify.py` | Confirms the sequence shapes to exactly one glyph (HarfBuzz) |
| `make_flag_svg.py` | Parametric SVG generator. **All geometry and colours are placeholders.** |
| `docs/VERIFICATION.md` | Open items that must be resolved before any release |

## Quick start

```bash
pip install fonttools uharfbuzz
python build_test_font.py
python verify.py iqkr_test.ttf    # expect: PASS
```

## Known limits

- The glyph in the test font is a placeholder triangle, not the flag.
- The flag geometry and colours in `make_flag_svg.py` are unverified. The source
  for them must be the enacted text of the Kurdistan Region's flag legislation.
  The one secondary source checked so far describes a 1999 proposal and gives no
  geometry or colours.
- This is not affiliated with Google, Unicode, or any government.

## Colours and sources (draft)

The generator currently uses the 1998–1999 specification colours (#F32837 red, #FFFFFF white, #009A3D green, #FFCC00 gold). The web colours (#ED2024, #278E43, #FEBD11) are kept in the generator for comparison. The final choice is open; see `docs/VERIFICATION.md`.

Proportions (2:3) and sun geometry (21 rays, disc = H/4, total diameter = H/2) come from secondary sources:
- https://kurdistanflag.com/ (specifications and colour tables)
- https://heritage.krd/kurdistan-flag (heritage archive; not an official government source)
- https://www.fotw.info/FLAGS/iq-krg.html (Flags of the World)

None of these cites an official legal text. Ray base width and angles are not known and remain placeholders.

## Licence

To be decided. The intended licence for the font and artwork is SIL Open Font
License 1.1, matching Noto. Do not treat any file here as licensed until a
LICENSE file is added.
