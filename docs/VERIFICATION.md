# Open verification items

Each item must be resolved before any public release of a flag glyph.

- [ ] Enacted text of the Kurdistan Region flag legislation (number, date, gazette reference). Not yet confirmed; the one secondary source checked describes a 1999 proposal only.
- [ ] Flag proportions, stripe colours (hex), sun colour, ray count, ray angles and sun size from the official text.
- [ ] Confirm `iqkr` in current CLDR subdivision data.
- [ ] Confirm IQ-KR in the current ISO 3166-2:IQ list.
- [ ] Confirm whether `1F1FD 1F1F0` (Kosovo) is RGI, since earlier research cited it as precedent.
- [ ] Confirm current Windows and Apple rendering of flag emoji before stating what platforms show.
- [ ] Choose and add the licence (OFL-1.1 intended).
- [ ] Replace the placeholder glyph in the font with the verified flag artwork.

## Third-party reference: kurdistanemoji.com/unicode

Reviewed 30 Oct 2026. Claims to check before citing or linking:

- [ ] ISO date: the page says IQ-KR was an official ISO region code in March 2022. Earlier research gave May 2021. Check the ISO 3166-2 Newsletter.
- [ ] WhatsApp shipped the Texas flag (a non-RGI sequence) in 2017, citing Emojipedia. Verify.
- [ ] macOS rendering test dated 5 Aug 2026 (Kurdistan black fallback; Scotland in colour). Reproduce before citing.
- [ ] Rudaw citation for the ISO code. Verify the article.
- [ ] Artwork licence: the page promises free artwork in an "open source pack" but states no licence. Do not reuse files until one is stated.
- [ ] Identity of the "Kurdistan Emoji Initiative": the site names no people. Confirm affiliation before linking or citing.
- [ ] Coordination: decide whether to align with, or stay separate from, this project so two different glyphs for the same sequence are not presented as one.

## Flag values currently used by make_flag_svg.py (30 Oct 2026)

Source for all values below: kurdistanflag.com (a secondary source, not an official text).

| Parameter | Value used | Source on the site | Status |
|---|---|---|---|
| Proportions | height:length 2:3 (width = 1.5 x height) | "height to length of 2:3" | Secondary only |
| Stripes | red, white, green, equal thirds | stated | Secondary only |
| Red | #F32837 (Pantone 032C) | 1998-1999 specification table | Secondary only |
| White | #FFFFFF | specification table | Secondary only |
| Green | #009A3D (Pantone 355C) | specification table; one source says PMS 354 | Discrepancy to resolve |
| Sun colour | #FFCC00 (Pantone 116C) | specification table | Secondary only |
| Ray count | 21, one ray straight up | stated | Secondary only |
| Sun size | disc radius 0.125 x height; tip radius 0.25 x height | "full diameter incl. rays = half the height; disc = quarter" | Secondary only |
| Ray base width and angles | 0.55 of angular pitch | not given | PLACEHOLDER |

Web set (not used; available as WEB_COLOURS): red #ED2024, white #FFFFFF, green #278E43, gold #FEBD11. The site says these come from a Wikimedia file, not an official source.

Still open:
- [ ] Official legal text for the colours and geometry (the site cites no gazette).
- [ ] Green: confirm PMS 355C (#009A3D) vs PMS 354.
- [ ] Ray base width and angles.
- [ ] Decide between the specification set and the web set for the final glyph.
- [ ] The site's CC0 licence claim for its SVG download.

## Source conflicts and unconfirmed claims (30 Oct 2026)

### Conflicts between sources
- Law number: kurdistanflag.com says "commonly cited as Law No. 14 of 1999" and that sources "report the number inconsistently". heritage.krd gives no number. A separate page gives "Parliament Decision No. 48" for Flag Day. Not resolved.
- Legal basis: kurdistanflag.com and heritage.krd both say the Kurdistan National Assembly passed or approved the flag standard on 11 November 1999. Neither cites a gazette or the law text. kurdistanflag.com says the primary text is "not freely available online".
- Green: PMS 355C (#009A3D), PMS 354 (one source), PMS 7732c (heritage.krd, print variant). Unresolved.
- Red: PMS 032C (specification) vs 186c (heritage.krd print variant). Unresolved.
- Yellow: PMS 116C in all sources checked. Hex differs: #FFCC00 (specification) vs #FEBD11 (web).
- Ray arrangement: one summary described the layout as "asymmetrical". With 21 rays and one ray up, the arrangement is mirror-symmetric about the vertical axis. Two rays flank the bottom; none points straight down.
- Flag history: heritage.krd dates the regional official flag to 1992. Not used in the project; noted for accuracy.

### Claims not confirmed
- That the standard was "standardized by Dr. Mehrdad Izady and Dr. Bijhan Eliasi in 1998–1999". Not found on any page checked. Do not cite until a source is found.
- That the flag was adopted "under Law No. 14 of 1999". Not confirmed beyond "commonly cited".
- Any ray base width or ray angle figure. None found. Still placeholder in make_flag_svg.py.
- kurdistanflag.com's claim that its SVG, PNG and PDF downloads are CC0. Not checked against the downloads.
- The 2022 Unicode and ISO 3166-2 claims on kurdistanflag.com (its own page says these are part of its material; not checked).
- heritage.krd's "living digital archive" description; not an official source.

### Colour decision (open)
Current generator uses the 1998–1999 specification set (#F32837, #FFFFFF, #009A3D, #FFCC00). The web set (#ED2024, #FFFFFF, #278E43, #FEBD11) is kept as WEB_COLOURS. Choose before any release and record the reason in the README.
