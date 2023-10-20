## Fontbakery report

Fontbakery version: 0.8.13

<details><summary><b>[13] BriemHand-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.13, while a newer 0.10.1 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>⚠ <b>WARN:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* ⚠ **WARN** GF_Phonetics_APA is almost fulfilled. Missing codepoints:

	- 0x1D7E (LATIN SMALL CAPITAL LETTER U WITH STROKE)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- Aogonek.latnNAV

	- Eogonek.latnNAV

	- IJ_acutecomb

	- aogonek.latnNAV

	- dotlessi_ogonek

	- eogonek.latnNAV

	- ff.loclEWE

	- ij_acutecomb

	- j.latnNLD

	- j_acutecomb

	- uni013B.latnMAH

	- uni013C.latnMAH

	- uni0145.latnMAH

	- uni0146.latnMAH

	- uni01B2.loclTOD0

	- uni01B7.localGAD

	- uni025F.dotless

	- uni028B.loclTOD0

	- uni03020300.case.loclKYU

	- uni03020300.loclKYU

	- uni03020301.case.loclKYU

	- uni03020301.loclKYU

	- uni03020303.case.loclKYU

	- uni03020303.loclKYU

	- uni03080300.case

	- uni03080301.case

	- uni03080304.case

	- uni0308030C.case

	- uni0328.alt

	- x.p 

	- x.x
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: onehalf	Contours detected: 2	Expected: 3

	- Glyph name: Imacron	Contours detected: 1	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni024E	Contours detected: 1	Expected: 2

	- Glyph name: beta	Contours detected: 1	Expected: 2

	- Glyph name: uni1D4D	Contours detected: 2	Expected: 3

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E39	Contours detected: 2	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni20AD	Contours detected: 2	Expected: 1

	- Glyph name: uni2153	Contours detected: 2	Expected: 3

	- Glyph name: uni2154	Contours detected: 2	Expected: 1 or 3

	- Glyph name: uni2155	Contours detected: 2	Expected: 3

	- Glyph name: uni2156	Contours detected: 2	Expected: 3

	- Glyph name: uni2159	Contours detected: 3	Expected: 4

	- Glyph name: uni215A	Contours detected: 3	Expected: 4

	- Glyph name: oneeighth	Contours detected: 4	Expected: 5

	- Glyph name: threeeighths	Contours detected: 4	Expected: 5

	- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

	- Glyph name: seveneighths	Contours detected: 4	Expected: 5

	- Glyph name: arrowleft	Contours detected: 2	Expected: 1

	- Glyph name: arrowup	Contours detected: 2	Expected: 1

	- Glyph name: arrowright	Contours detected: 2	Expected: 1

	- Glyph name: arrowdown	Contours detected: 2	Expected: 1

	- Glyph name: Imacron	Contours detected: 1	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: arrowdown	Contours detected: 2	Expected: 1

	- Glyph name: arrowup	Contours detected: 2	Expected: 1

	- Glyph name: beta	Contours detected: 1	Expected: 2

	- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: oneeighth	Contours detected: 4	Expected: 5

	- Glyph name: onehalf	Contours detected: 2	Expected: 3

	- Glyph name: seveneighths	Contours detected: 4	Expected: 5

	- Glyph name: threeeighths	Contours detected: 4	Expected: 5

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni024E	Contours detected: 1	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E39	Contours detected: 2	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni20AD	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* ⚠ **WARN** The dot of soft dotted characters should disappear in other cases, for example: ј̀ ј́ ј̂ ј̃ ј̄ ј̆ ј̇ ј̈ ј̉ ј̊ ј̋ ј̌ ј̍ ј̏ ј̐ ј̑ ј̒ ј̓ ј᷄ ј᷅ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 540 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 559:
plus

Width = 553:
equal

Width = 542:
greater, greaterequal

Width = 507:
logicalnot

Width = 474:
plusminus

Width = 552:
multiply

Width = 496:
divide

Width = 528:
minus

Width = 564:
approxequal

Width = 582:
notequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni0183 (U+0183): L<<148.0,756.0>--<151.0,756.0>> -> L<<151.0,756.0>--<415.0,756.0>>

	* uni023C (U+023C): L<<163.0,154.0>--<241.0,294.0>> -> L<<241.0,294.0>--<328.0,459.0>>

	* uni023C (U+023C): L<<361.0,436.0>--<272.0,273.0>> -> L<<272.0,273.0>--<181.0,101.0>>

	* uni0283 (U+0283): L<<205.0,561.0>--<202.0,499.0>> -> L<<202.0,499.0>--<200.0,-1.0>>

	* uni0283 (U+0283): L<<97.0,71.0>--<92.0,499.0>> -> L<<92.0,499.0>--<92.0,513.0>>

	* uni2C65 (U+2C65): L<<180.0,138.0>--<269.0,294.0>> -> L<<269.0,294.0>--<365.0,469.0>>

	* uni2C65 (U+2C65): L<<409.0,462.0>--<300.0,273.0>> -> L<<300.0,273.0>--<193.0,78.0>>

	* uni2C66 (U+2C66): L<<193.0,276.0>--<204.0,294.0>> -> L<<204.0,294.0>--<281.0,442.0>>

	* uni2C66 (U+2C66): L<<328.0,442.0>--<235.0,273.0>> -> L<<235.0,273.0>--<190.0,188.0>>

	* uniA7B9 (U+A7B9): L<<179.0,152.0>--<260.0,294.0>> -> L<<260.0,294.0>--<422.0,588.0>> 

	* uniA7B9 (U+A7B9): L<<455.0,557.0>--<291.0,273.0>> -> L<<291.0,273.0>--<186.0,80.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Eng (U+014A): B<<201.0,259.0>-<199.0,232.0>-<198.0,224.0>>/B<<198.0,224.0>-<212.0,261.0>-<244.0,306.5>> = 13.600542516658704

	* m (U+006D): B<<194.0,217.0>-<192.0,188.0>-<191.0,180.0>>/B<<191.0,180.0>-<205.0,217.0>-<231.5,262.5>> = 13.600542516658704

	* r (U+0072): B<<196.5,302.0>-<194.0,273.0>-<193.0,263.0>>/B<<193.0,263.0>-<225.0,356.0>-<258.0,414.0>> = 13.277030950370508

	* racute (U+0155): B<<196.5,302.0>-<194.0,273.0>-<193.0,263.0>>/B<<193.0,263.0>-<225.0,356.0>-<258.0,414.0>> = 13.277030950370508

	* rcaron (U+0159): B<<196.5,302.0>-<194.0,273.0>-<193.0,263.0>>/B<<193.0,263.0>-<225.0,356.0>-<258.0,414.0>> = 13.277030950370508

	* rmacronbelow (U+1E5F): B<<196.5,302.0>-<194.0,273.0>-<193.0,263.0>>/B<<193.0,263.0>-<225.0,356.0>-<258.0,414.0>> = 13.277030950370508

	* uni0157 (U+0157): B<<196.5,302.0>-<194.0,273.0>-<193.0,263.0>>/B<<193.0,263.0>-<225.0,356.0>-<258.0,414.0>> = 13.277030950370508

	* uni019C (U+019C): B<<437.5,391.5>-<439.0,416.0>-<439.0,421.0>>/B<<439.0,421.0>-<425.0,364.0>-<398.5,303.5>> = 13.799485396019362

	* uni019C (U+019C): B<<772.5,387.5>-<774.0,415.0>-<774.0,422.0>>/B<<774.0,422.0>-<761.0,364.0>-<734.5,304.0>> = 12.633361935275003

	* uni0211 (U+0211): B<<196.5,302.0>-<194.0,273.0>-<193.0,263.0>>/B<<193.0,263.0>-<225.0,356.0>-<258.0,414.0>> = 13.277030950370508

	* uni0213 (U+0213): B<<196.5,302.0>-<194.0,273.0>-<193.0,263.0>>/B<<193.0,263.0>-<225.0,356.0>-<258.0,414.0>> = 13.277030950370508

	* uni0220 (U+0220): B<<201.0,259.0>-<199.0,232.0>-<198.0,224.0>>/B<<198.0,224.0>-<212.0,261.0>-<244.0,306.5>> = 13.600542516658704

	* uni0271 (U+0271): B<<194.0,217.0>-<192.0,188.0>-<191.0,180.0>>/B<<191.0,180.0>-<205.0,217.0>-<231.5,262.5>> = 13.600542516658704

	* uni0272 (U+0272): B<<198.0,217.0>-<196.0,188.0>-<195.0,180.0>>/B<<195.0,180.0>-<209.0,217.0>-<235.5,262.5>> = 13.600542516658704

	* uni1D7D (U+1D7D): B<<198.0,208.0>-<198.0,203.0>-<197.0,198.0>>/B<<197.0,198.0>-<199.0,203.0>-<201.0,208.0>> = 10.491477012331565

	* uni1E3F (U+1E3F): B<<194.0,217.0>-<192.0,188.0>-<191.0,180.0>>/B<<191.0,180.0>-<205.0,217.0>-<231.5,262.5>> = 13.600542516658704

	* uni1E41 (U+1E41): B<<194.0,217.0>-<192.0,188.0>-<191.0,180.0>>/B<<191.0,180.0>-<205.0,217.0>-<231.5,262.5>> = 13.600542516658704

	* uni1E43 (U+1E43): B<<194.0,217.0>-<192.0,188.0>-<191.0,180.0>>/B<<191.0,180.0>-<205.0,217.0>-<231.5,262.5>> = 13.600542516658704

	* uni1E59 (U+1E59): B<<196.5,302.0>-<194.0,273.0>-<193.0,263.0>>/B<<193.0,263.0>-<225.0,356.0>-<258.0,414.0>> = 13.277030950370508

	* uni1E5B (U+1E5B): B<<196.5,302.0>-<194.0,273.0>-<193.0,263.0>>/B<<193.0,263.0>-<225.0,356.0>-<258.0,414.0>> = 13.277030950370508 

	* uni1E5D (U+1E5D): B<<196.5,302.0>-<194.0,273.0>-<193.0,263.0>>/B<<193.0,263.0>-<225.0,356.0>-<258.0,414.0>> = 13.277030950370508 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* beta (U+03B2): L<<197.0,549.0>--<194.0,0.0>>

	* f (U+0066): L<<222.0,442.0>--<219.0,-1.0>>

	* florin (U+0192): L<<197.0,442.0>--<194.0,-1.0>>

	* germandbls (U+00DF): L<<197.0,549.0>--<194.0,0.0>>

	* germandbls (U+00DF): L<<89.0,72.0>--<91.0,523.0>>

	* integral (U+222B): L<<124.0,72.0>--<122.0,513.0>>

	* integral (U+222B): L<<229.0,514.0>--<226.0,13.0>>

	* uni0283 (U+0283): L<<202.0,499.0>--<200.0,-1.0>>

	* uni1E1F (U+1E1F): L<<222.0,442.0>--<219.0,-1.0>> 

	* uniA7B5 (U+A7B5): L<<197.0,549.0>--<194.0,0.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[13] BriemHand-Thin.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.13, while a newer 0.10.1 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>⚠ <b>WARN:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* ⚠ **WARN** GF_Phonetics_APA is almost fulfilled. Missing codepoints:

	- 0x1D7E (LATIN SMALL CAPITAL LETTER U WITH STROKE)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- Aogonek.latnNAV

	- Eogonek.latnNAV

	- IJ_acutecomb

	- aogonek.latnNAV

	- dotlessi_ogonek

	- eogonek.latnNAV

	- ff.loclEWE

	- ij_acutecomb

	- j.latnNLD

	- j_acutecomb

	- uni013B.latnMAH

	- uni013C.latnMAH

	- uni0145.latnMAH

	- uni0146.latnMAH

	- uni01B2.loclTOD0

	- uni01B7.localGAD

	- uni025F.dotless

	- uni028B.loclTOD0

	- uni03020300.case.loclKYU

	- uni03020300.loclKYU

	- uni03020301.case.loclKYU

	- uni03020301.loclKYU

	- uni03020303.case.loclKYU

	- uni03020303.loclKYU

	- uni03080300.case

	- uni03080301.case

	- uni03080304.case

	- uni0308030C.case

	- uni0328.alt

	- x.p 

	- x.x
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: onehalf	Contours detected: 2	Expected: 3

	- Glyph name: Imacron	Contours detected: 1	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni024D	Contours detected: 2	Expected: 1

	- Glyph name: uni024E	Contours detected: 1	Expected: 2

	- Glyph name: beta	Contours detected: 1	Expected: 2

	- Glyph name: uni1D4D	Contours detected: 2	Expected: 3

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E39	Contours detected: 2	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni20AD	Contours detected: 2	Expected: 1

	- Glyph name: uni2153	Contours detected: 2	Expected: 3

	- Glyph name: uni2154	Contours detected: 2	Expected: 1 or 3

	- Glyph name: uni2155	Contours detected: 2	Expected: 3

	- Glyph name: uni2156	Contours detected: 2	Expected: 3

	- Glyph name: uni2159	Contours detected: 3	Expected: 4

	- Glyph name: uni215A	Contours detected: 3	Expected: 4

	- Glyph name: oneeighth	Contours detected: 4	Expected: 5

	- Glyph name: threeeighths	Contours detected: 4	Expected: 5

	- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

	- Glyph name: seveneighths	Contours detected: 4	Expected: 5

	- Glyph name: arrowleft	Contours detected: 2	Expected: 1

	- Glyph name: arrowup	Contours detected: 2	Expected: 1

	- Glyph name: arrowright	Contours detected: 2	Expected: 1

	- Glyph name: arrowdown	Contours detected: 2	Expected: 1

	- Glyph name: Imacron	Contours detected: 1	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: arrowdown	Contours detected: 2	Expected: 1

	- Glyph name: arrowup	Contours detected: 2	Expected: 1

	- Glyph name: beta	Contours detected: 1	Expected: 2

	- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: oneeighth	Contours detected: 4	Expected: 5

	- Glyph name: onehalf	Contours detected: 2	Expected: 3

	- Glyph name: seveneighths	Contours detected: 4	Expected: 5

	- Glyph name: threeeighths	Contours detected: 4	Expected: 5

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni024D	Contours detected: 2	Expected: 1

	- Glyph name: uni024E	Contours detected: 1	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E39	Contours detected: 2	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni20AD	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* ⚠ **WARN** The dot of soft dotted characters should disappear in other cases, for example: ј̀ ј́ ј̂ ј̃ ј̄ ј̆ ј̇ ј̈ ј̉ ј̊ ј̋ ј̌ ј̍ ј̏ ј̐ ј̑ ј̒ ј̓ ј᷄ ј᷅ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 550 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 540:
lessequal, less

Width = 530:
greater, greaterequal

Width = 489:
logicalnot

Width = 459:
plusminus

Width = 553:
multiply

Width = 487:
divide

Width = 537:
minus

Width = 554:
approxequal

Width = 570:
notequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* etTironian (U+204A): L<<340.0,510.0>--<337.0,510.0>> -> L<<337.0,510.0>--<46.0,510.0>>

	* uni01C2 (U+01C2): L<<68.0,497.0>--<190.0,497.0>> -> L<<190.0,497.0>--<192.0,497.0>>

	* uni023C (U+023C): L<<140.0,122.0>--<233.0,294.0>> -> L<<233.0,294.0>--<325.0,474.0>>

	* uni023C (U+023C): L<<354.0,451.0>--<260.0,275.0>> -> L<<260.0,275.0>--<160.0,81.0>>

	* uni0283 (U+0283): L<<110.0,40.0>--<105.0,499.0>> -> L<<105.0,499.0>--<105.0,504.0>>

	* uni0283 (U+0283): L<<172.0,571.0>--<169.0,499.0>> -> L<<169.0,499.0>--<169.0,-28.0>>

	* uni02FB (U+02FB): L<<134.0,-116.0>--<136.0,-116.0>> -> L<<136.0,-116.0>--<306.0,-116.0>>

	* uni1DC6 (U+1DC6): L<<62.0,668.0>--<61.0,668.0>> -> L<<61.0,668.0>--<-182.0,668.0>>

	* uni2C65 (U+2C65): L<<146.0,69.0>--<273.0,294.0>> -> L<<273.0,294.0>--<371.0,474.0>>

	* uni2C65 (U+2C65): L<<411.0,469.0>--<300.0,275.0>> -> L<<300.0,275.0>--<178.0,50.0>>

	* uni2C66 (U+2C66): L<<166.0,245.0>--<193.0,294.0>> -> L<<193.0,294.0>--<274.0,453.0>>

	* uni2C66 (U+2C66): L<<315.0,453.0>--<220.0,275.0>> -> L<<220.0,275.0>--<164.0,166.0>>

	* uniA7B9 (U+A7B9): L<<148.0,74.0>--<273.0,294.0>> -> L<<273.0,294.0>--<434.0,590.0>> 

	* uniA7B9 (U+A7B9): L<<465.0,564.0>--<300.0,275.0>> -> L<<300.0,275.0>--<176.0,47.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* uni019C (U+019C): B<<450.5,463.5>-<452.0,493.0>-<452.0,496.0>>/B<<452.0,496.0>-<434.0,423.0>-<403.5,350.5>> = 13.851419013804975

	* uni019C (U+019C): B<<785.5,461.0>-<787.0,493.0>-<787.0,496.0>>/B<<787.0,496.0>-<769.0,423.0>-<738.5,350.5>> = 13.851419013804975 

	* uni1D43 (U+1D43): B<<394.0,635.5>-<432.0,630.0>-<466.0,623.0>>/B<<466.0,623.0>-<465.0,623.0>-<468.0,622.0>> = 11.633633998940427 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* uni01A9 (U+01A9): L<<263.0,259.0>--<262.0,399.0>>

	* uni01E4 (U+01E4): L<<578.0,134.0>--<408.0,133.0>> 

	* uni0248 (U+0248): L<<242.0,510.0>--<120.0,509.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[13] BriemHand-Black.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.13, while a newer 0.10.1 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>⚠ <b>WARN:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* ⚠ **WARN** GF_Phonetics_APA is almost fulfilled. Missing codepoints:

	- 0x1D7E (LATIN SMALL CAPITAL LETTER U WITH STROKE)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- Aogonek.latnNAV

	- Eogonek.latnNAV

	- IJ_acutecomb

	- aogonek.latnNAV

	- dotlessi_ogonek

	- eogonek.latnNAV

	- ff.loclEWE

	- ij_acutecomb

	- j.latnNLD

	- j_acutecomb

	- uni013B.latnMAH

	- uni013C.latnMAH

	- uni0145.latnMAH

	- uni0146.latnMAH

	- uni01B2.loclTOD0

	- uni01B7.localGAD

	- uni025F.dotless

	- uni028B.loclTOD0

	- uni03020300.case.loclKYU

	- uni03020300.loclKYU

	- uni03020301.case.loclKYU

	- uni03020301.loclKYU

	- uni03020303.case.loclKYU

	- uni03020303.loclKYU

	- uni03080300.case

	- uni03080301.case

	- uni03080304.case

	- uni0308030C.case

	- uni0328.alt

	- x.p 

	- x.x
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: onehalf	Contours detected: 2	Expected: 3

	- Glyph name: Imacron	Contours detected: 1	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni023A	Contours detected: 2	Expected: 3

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni023E	Contours detected: 1	Expected: 2

	- Glyph name: uni0247	Contours detected: 2	Expected: 4

	- Glyph name: uni024E	Contours detected: 1	Expected: 2

	- Glyph name: beta	Contours detected: 1	Expected: 2

	- Glyph name: uni1D4D	Contours detected: 2	Expected: 3

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E39	Contours detected: 2	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni2153	Contours detected: 2	Expected: 3

	- Glyph name: uni2154	Contours detected: 2	Expected: 1 or 3

	- Glyph name: uni2155	Contours detected: 2	Expected: 3

	- Glyph name: uni2156	Contours detected: 2	Expected: 3

	- Glyph name: uni2159	Contours detected: 3	Expected: 4

	- Glyph name: uni215A	Contours detected: 3	Expected: 4

	- Glyph name: oneeighth	Contours detected: 4	Expected: 5

	- Glyph name: threeeighths	Contours detected: 4	Expected: 5

	- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

	- Glyph name: seveneighths	Contours detected: 4	Expected: 5

	- Glyph name: arrowleft	Contours detected: 2	Expected: 1

	- Glyph name: arrowup	Contours detected: 2	Expected: 1

	- Glyph name: arrowright	Contours detected: 2	Expected: 1

	- Glyph name: arrowdown	Contours detected: 2	Expected: 1

	- Glyph name: Imacron	Contours detected: 1	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: arrowdown	Contours detected: 2	Expected: 1

	- Glyph name: arrowup	Contours detected: 2	Expected: 1

	- Glyph name: beta	Contours detected: 1	Expected: 2

	- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: oneeighth	Contours detected: 4	Expected: 5

	- Glyph name: onehalf	Contours detected: 2	Expected: 3

	- Glyph name: seveneighths	Contours detected: 4	Expected: 5

	- Glyph name: threeeighths	Contours detected: 4	Expected: 5

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni023A	Contours detected: 2	Expected: 3

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni023E	Contours detected: 1	Expected: 2

	- Glyph name: uni0247	Contours detected: 2	Expected: 4

	- Glyph name: uni024E	Contours detected: 1	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E39	Contours detected: 2	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* ⚠ **WARN** The dot of soft dotted characters should disappear in other cases, for example: ј̀ ј́ ј̂ ј̃ ј̄ ј̆ ј̇ ј̈ ј̉ ј̊ ј̋ ј̌ ј̍ ј̏ ј̐ ј̑ ј̒ ј̓ ј᷄ ј᷅ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 540 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 580:
plus

Width = 560:
equal

Width = 570:
greater, greaterequal

Width = 550:
logicalnot, multiply

Width = 512:
plusminus

Width = 519:
divide

Width = 507:
minus

Width = 588:
approxequal

Width = 610:
notequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni023C (U+023C): L<<238.0,258.0>--<260.0,295.0>> -> L<<260.0,295.0>--<333.0,424.0>>

	* uni023C (U+023C): L<<378.0,400.0>--<300.0,269.0>> -> L<<300.0,269.0>--<240.0,160.0>>

	* uni0247 (U+0247): L<<257.0,290.0>--<260.0,295.0>> -> L<<260.0,295.0>--<332.0,423.0>>

	* uni0283 (U+0283): L<<284.0,536.0>--<284.0,499.0>> -> L<<284.0,499.0>--<274.0,65.0>>

	* uni0283 (U+0283): L<<66.0,146.0>--<61.0,499.0>> -> L<<61.0,499.0>--<61.0,534.0>>

	* uni2C65 (U+2C65): L<<394.0,428.0>--<300.0,269.0>> -> L<<300.0,269.0>--<264.0,205.0>>

	* uni2C66 (U+2C66): L<<358.0,417.0>--<270.0,269.0>> -> L<<270.0,269.0>--<253.0,238.0>>

	* uniA71A (U+A71A): L<<427.0,380.0>--<426.0,380.0>> -> L<<426.0,380.0>--<27.0,380.0>> 

	* uniA7B9 (U+A7B9): L<<384.0,461.0>--<270.0,269.0>> -> L<<270.0,269.0>--<253.0,239.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Eng (U+014A): B<<299.5,407.5>-<297.0,371.0>-<294.0,342.0>>/B<<294.0,342.0>-<296.0,362.0>-<315.5,392.5>> = 0.1955479762700748

	* a (U+0061): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* aacute (U+00E1): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* abreve (U+0103): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* acircumflex (U+00E2): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* adieresis (U+00E4): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* agrave (U+00E0): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* amacron (U+0101): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* aogonek (U+0105): B<<384.0,191.5>-<385.0,212.0>-<386.0,224.0>>/B<<386.0,224.0>-<381.0,205.0>-<363.0,175.5>> = 9.979921145744504

	* aring (U+00E5): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* aringacute (U+01FB): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* at (U+0040): B<<530.5,146.0>-<532.0,176.0>-<533.0,191.0>>/B<<533.0,191.0>-<529.0,175.0>-<513.5,149.5>> = 10.222168633636109

	* atilde (U+00E3): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* b (U+0062): B<<256.0,315.0>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* bmacronbelow (U+1E07): B<<256.0,315.0>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* d (U+0064): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* dcaron (U+010F): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* dcroat (U+0111): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* dmacronbelow (U+1E0F): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* dong (U+20AB): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* eng (U+014B): B<<260.0,312.0>-<258.0,288.0>-<256.0,275.0>>/B<<256.0,275.0>-<258.0,295.0>-<275.5,325.5>> = 3.03556912505556

	* g (U+0067): B<<367.0,183.5>-<366.0,215.0>-<364.0,237.0>>/B<<364.0,237.0>-<362.0,217.0>-<344.5,186.0>> = 10.905022045234459

	* gbreve (U+011F): B<<367.0,183.5>-<366.0,215.0>-<364.0,237.0>>/B<<364.0,237.0>-<362.0,217.0>-<344.5,186.0>> = 10.905022045234459

	* gcaron (U+01E7): B<<367.0,183.5>-<366.0,215.0>-<364.0,237.0>>/B<<364.0,237.0>-<362.0,217.0>-<344.5,186.0>> = 10.905022045234459

	* gcircumflex (U+011D): B<<367.0,183.5>-<366.0,215.0>-<364.0,237.0>>/B<<364.0,237.0>-<362.0,217.0>-<344.5,186.0>> = 10.905022045234459

	* gdotaccent (U+0121): B<<367.0,183.5>-<366.0,215.0>-<364.0,237.0>>/B<<364.0,237.0>-<362.0,217.0>-<344.5,186.0>> = 10.905022045234459

	* h (U+0068): B<<256.0,315.0>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* hbar (U+0127): B<<256.5,315.5>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* hcircumflex (U+0125): B<<256.0,315.0>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* hmacronbelow (U+1E96): B<<256.0,315.0>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* k (U+006B): B<<256.0,315.0>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* kgreenlandic (U+0138): B<<259.0,313.0>-<256.0,289.0>-<256.0,275.0>>/B<<256.0,275.0>-<258.0,295.0>-<275.5,325.5>> = 5.710593137499633

	* kmacronbelow (U+1E35): B<<256.0,315.0>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* m (U+006D): B<<262.5,340.0>-<259.0,306.0>-<256.0,275.0>>/B<<256.0,275.0>-<258.0,295.0>-<275.5,325.5>> = 0.18305298584087132

	* m (U+006D): B<<598.0,326.5>-<595.0,301.0>-<592.0,276.0>>/B<<592.0,276.0>-<595.0,296.0>-<612.5,327.0>> = 1.6879921973171763

	* n (U+006E): B<<262.5,340.0>-<259.0,306.0>-<256.0,275.0>>/B<<256.0,275.0>-<258.0,295.0>-<275.5,325.5>> = 0.18305298584087132

	* nacute (U+0144): B<<262.5,340.0>-<259.0,306.0>-<256.0,275.0>>/B<<256.0,275.0>-<258.0,295.0>-<275.5,325.5>> = 0.18305298584087132

	* ncaron (U+0148): B<<262.5,340.0>-<259.0,306.0>-<256.0,275.0>>/B<<256.0,275.0>-<258.0,295.0>-<275.5,325.5>> = 0.18305298584087132

	* nlongrightleg (U+019E): B<<262.5,340.0>-<259.0,306.0>-<256.0,275.0>>/B<<256.0,275.0>-<258.0,295.0>-<275.5,325.5>> = 0.18305298584087132

	* nmacronbelow (U+1E49): B<<262.5,340.0>-<259.0,306.0>-<256.0,275.0>>/B<<256.0,275.0>-<258.0,295.0>-<275.5,325.5>> = 0.18305298584087132

	* ntilde (U+00F1): B<<262.5,340.0>-<259.0,306.0>-<256.0,275.0>>/B<<256.0,275.0>-<258.0,295.0>-<275.5,325.5>> = 0.18305298584087132

	* ordfeminine (U+00AA): B<<265.0,429.0>-<266.0,451.0>-<267.0,463.0>>/B<<267.0,463.0>-<263.0,448.0>-<245.5,423.0>> = 10.167775487411356

	* p (U+0070): B<<251.5,340.0>-<248.0,306.0>-<245.0,275.0>>/B<<245.0,275.0>-<247.0,295.0>-<264.5,325.5>> = 0.18305298584087132

	* q (U+0071): B<<362.0,197.0>-<364.0,228.0>-<364.0,237.0>>/B<<364.0,237.0>-<362.0,217.0>-<344.5,186.0>> = 5.710593137499633

	* r (U+0072): B<<264.0,356.0>-<261.0,327.0>-<258.0,296.0>>/B<<258.0,296.0>-<290.0,400.0>-<333.5,462.0>> = 11.57518881739615

	* racute (U+0155): B<<264.0,356.0>-<261.0,327.0>-<258.0,296.0>>/B<<258.0,296.0>-<290.0,400.0>-<333.5,462.0>> = 11.57518881739615

	* rcaron (U+0159): B<<264.0,356.0>-<261.0,327.0>-<258.0,296.0>>/B<<258.0,296.0>-<290.0,400.0>-<333.5,462.0>> = 11.57518881739615

	* rmacronbelow (U+1E5F): B<<264.0,356.0>-<261.0,327.0>-<258.0,296.0>>/B<<258.0,296.0>-<290.0,400.0>-<333.5,462.0>> = 11.57518881739615

	* rtail (U+027D): B<<268.0,356.0>-<265.0,327.0>-<262.0,296.0>>/B<<262.0,296.0>-<294.0,400.0>-<337.5,462.0>> = 11.57518881739615

	* thorn (U+00FE): B<<259.5,323.5>-<257.0,290.0>-<255.0,275.0>>/B<<255.0,275.0>-<257.0,295.0>-<274.5,325.5>> = 1.8840502310916725

	* threeeighths (U+215C): B<<320.5,483.5>-<301.0,476.0>-<290.0,475.0>>/B<<290.0,475.0>-<348.0,468.0>-<378.5,438.0>> = 12.076152538371728

	* threequarters (U+00BE): B<<320.5,483.5>-<301.0,476.0>-<290.0,475.0>>/B<<290.0,475.0>-<348.0,468.0>-<378.5,438.0>> = 12.076152538371728

	* u (U+0075): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uacute (U+00FA): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* ubreve (U+016D): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* ucircumflex (U+00FB): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* udieresis (U+00FC): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* ugrave (U+00F9): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uhorn (U+01B0): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uhungarumlaut (U+0171): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* umacron (U+016B): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uni00B3 (U+00B3): B<<320.5,530.5>-<301.0,523.0>-<290.0,522.0>>/B<<290.0,522.0>-<348.0,515.0>-<378.5,485.0>> = 12.076152538371728

	* uni00B5 (U+00B5): B<<400.0,191.5>-<401.0,212.0>-<402.0,224.0>>/B<<402.0,224.0>-<397.0,203.0>-<375.5,168.5>> = 8.628856063024877

	* uni0123 (U+0123): B<<367.0,183.5>-<366.0,215.0>-<364.0,237.0>>/B<<364.0,237.0>-<362.0,217.0>-<344.5,186.0>> = 10.905022045234459

	* uni0137 (U+0137): B<<256.0,315.0>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* uni0146 (U+0146): B<<262.5,340.0>-<259.0,306.0>-<256.0,275.0>>/B<<256.0,275.0>-<258.0,295.0>-<275.5,325.5>> = 0.18305298584087132

	* uni0157 (U+0157): B<<264.0,356.0>-<261.0,327.0>-<258.0,296.0>>/B<<258.0,296.0>-<290.0,400.0>-<333.5,462.0>> = 11.57518881739615

	* uni0180 (U+0180): B<<256.0,313.5>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* uni0183 (U+0183): B<<256.0,311.5>-<254.0,283.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* uni018C (U+018C): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni0199 (U+0199): B<<278.0,317.0>-<276.0,286.0>-<276.0,275.0>>/B<<276.0,275.0>-<278.0,295.0>-<295.5,325.5>> = 5.710593137499633

	* uni019C (U+019C): B<<402.5,190.0>-<405.0,216.0>-<408.0,240.0>>/B<<408.0,240.0>-<405.0,220.0>-<387.5,189.0>> = 1.4057492610462028

	* uni019C (U+019C): B<<737.5,176.5>-<741.0,211.0>-<744.0,241.0>>/B<<744.0,241.0>-<742.0,222.0>-<724.5,191.0>> = 0.2984128199930731

	* uni01A5 (U+01A5): B<<270.5,326.5>-<268.0,293.0>-<266.0,275.0>>/B<<266.0,275.0>-<268.0,295.0>-<285.5,325.5>> = 0.6295986084106898

	* uni01B4 (U+01B4): B<<381.0,195.5>-<380.0,221.0>-<378.0,237.0>>/B<<378.0,237.0>-<376.0,217.0>-<358.5,186.0>> = 12.835609486401424

	* uni01C6 (U+01C6): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni01CC (U+01CC): B<<262.5,340.0>-<259.0,306.0>-<256.0,275.0>>/B<<256.0,275.0>-<258.0,295.0>-<275.5,325.5>> = 0.18305298584087132

	* uni01CE (U+01CE): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni01D4 (U+01D4): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uni01D6 (U+01D6): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uni01D8 (U+01D8): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uni01DA (U+01DA): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uni01DC (U+01DC): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uni01DF (U+01DF): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni01E5 (U+01E5): B<<367.0,183.5>-<366.0,215.0>-<364.0,237.0>>/B<<364.0,237.0>-<362.0,217.0>-<344.5,186.0>> = 10.905022045234459

	* uni01E9 (U+01E9): B<<256.0,315.0>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* uni01F3 (U+01F3): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni01F5 (U+01F5): B<<367.0,183.5>-<366.0,215.0>-<364.0,237.0>>/B<<364.0,237.0>-<362.0,217.0>-<344.5,186.0>> = 10.905022045234459

	* uni01F9 (U+01F9): B<<262.5,340.0>-<259.0,306.0>-<256.0,275.0>>/B<<256.0,275.0>-<258.0,295.0>-<275.5,325.5>> = 0.18305298584087132

	* uni0201 (U+0201): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni0203 (U+0203): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni0211 (U+0211): B<<264.0,356.0>-<261.0,327.0>-<258.0,296.0>>/B<<258.0,296.0>-<290.0,400.0>-<333.5,462.0>> = 11.57518881739615

	* uni0213 (U+0213): B<<264.0,356.0>-<261.0,327.0>-<258.0,296.0>>/B<<258.0,296.0>-<290.0,400.0>-<333.5,462.0>> = 11.57518881739615

	* uni0215 (U+0215): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uni0217 (U+0217): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uni021F (U+021F): B<<256.0,315.0>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* uni0220 (U+0220): B<<299.5,407.5>-<297.0,371.0>-<294.0,342.0>>/B<<294.0,342.0>-<296.0,362.0>-<315.5,392.5>> = 0.1955479762700748

	* uni0227 (U+0227): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni0233 (U+0233): B<<381.0,195.5>-<380.0,221.0>-<378.0,237.0>>/B<<378.0,237.0>-<376.0,217.0>-<358.5,186.0>> = 12.835609486401424

	* uni024A (U+024A): L<<466.0,169.0>--<482.0,483.0>>/B<<482.0,483.0>-<450.0,368.0>-<406.5,282.0>> = 12.632796883073842

	* uni024D (U+024D): B<<264.0,356.0>-<261.0,327.0>-<258.0,296.0>>/B<<258.0,296.0>-<290.0,400.0>-<333.5,462.0>> = 11.57518881739615

	* uni024F (U+024F): B<<408.0,195.5>-<407.0,221.0>-<405.0,237.0>>/B<<405.0,237.0>-<403.0,217.0>-<385.5,186.0>> = 12.835609486401424

	* uni0253 (U+0253): B<<256.0,314.5>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* uni0257 (U+0257): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni0260 (U+0260): B<<392.0,183.5>-<391.0,215.0>-<389.0,237.0>>/B<<389.0,237.0>-<387.0,217.0>-<369.5,186.0>> = 10.905022045234459

	* uni0261 (U+0261): B<<367.0,183.5>-<366.0,215.0>-<364.0,237.0>>/B<<364.0,237.0>-<362.0,217.0>-<344.5,186.0>> = 10.905022045234459

	* uni0266 (U+0266): B<<256.5,316.0>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* uni026F (U+026F): B<<412.5,198.0>-<415.0,224.0>-<418.0,248.0>>/B<<418.0,248.0>-<415.0,228.0>-<397.5,197.0>> = 1.4057492610462028

	* uni026F (U+026F): B<<747.5,184.5>-<751.0,219.0>-<754.0,249.0>>/B<<754.0,249.0>-<752.0,230.0>-<734.5,199.0>> = 0.2984128199930731

	* uni0271 (U+0271): B<<262.5,340.0>-<259.0,306.0>-<256.0,275.0>>/B<<256.0,275.0>-<258.0,295.0>-<275.5,325.5>> = 0.18305298584087132

	* uni0271 (U+0271): B<<598.0,326.5>-<595.0,301.0>-<592.0,276.0>>/B<<592.0,276.0>-<595.0,296.0>-<612.5,327.0>> = 1.6879921973171763

	* uni0272 (U+0272): B<<275.5,340.0>-<272.0,306.0>-<269.0,275.0>>/B<<269.0,275.0>-<271.0,295.0>-<288.5,325.5>> = 0.18305298584087132

	* uni0289 (U+0289): B<<400.0,191.5>-<401.0,212.0>-<402.0,224.0>>/B<<402.0,224.0>-<397.0,205.0>-<379.0,175.5>> = 9.979921145744504

	* uni02B0 (U+02B0): B<<218.0,449.0>-<216.0,422.0>-<216.0,415.0>>/B<<216.0,415.0>-<220.0,435.0>-<236.5,463.5>> = 11.309932474020195

	* uni03BC (U+03BC): B<<400.0,191.5>-<401.0,212.0>-<402.0,224.0>>/B<<402.0,224.0>-<397.0,203.0>-<375.5,168.5>> = 8.628856063024877

	* uni0430 (U+0430): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni0440 (U+0440): B<<251.5,340.0>-<248.0,306.0>-<245.0,275.0>>/B<<245.0,275.0>-<247.0,295.0>-<264.5,325.5>> = 0.18305298584087132

	* uni0443 (U+0443): B<<381.0,195.5>-<380.0,221.0>-<378.0,237.0>>/B<<378.0,237.0>-<376.0,217.0>-<358.5,186.0>> = 12.835609486401424

	* uni1D43 (U+1D43): B<<355.5,376.0>-<358.0,395.0>-<364.0,404.0>>/B<<364.0,404.0>-<345.0,374.0>-<316.0,337.0>> = 1.3426240265375242

	* uni1D58 (U+1D58): B<<315.0,352.0>-<317.0,390.0>-<318.0,412.0>>/B<<318.0,412.0>-<313.0,392.0>-<297.0,363.0>> = 11.433681265426625

	* uni1D7D (U+1D7D): B<<272.5,340.0>-<269.0,306.0>-<266.0,275.0>>/B<<266.0,275.0>-<268.0,295.0>-<285.5,325.5>> = 0.18305298584087132

	* uni1D91 (U+1D91): B<<358.0,186.0>-<360.0,217.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 6.613460482314664

	* uni1DB6 (U+1DB6): B<<324.0,348.5>-<326.0,387.0>-<327.0,412.0>>/B<<327.0,412.0>-<322.0,391.0>-<306.0,362.0>> = 11.101887711112571

	* uni1E01 (U+1E01): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni1E03 (U+1E03): B<<256.0,315.0>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* uni1E05 (U+1E05): B<<256.0,315.0>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* uni1E0B (U+1E0B): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni1E0D (U+1E0D): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni1E11 (U+1E11): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni1E13 (U+1E13): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni1E21 (U+1E21): B<<367.0,183.5>-<366.0,215.0>-<364.0,237.0>>/B<<364.0,237.0>-<362.0,217.0>-<344.5,186.0>> = 10.905022045234459

	* uni1E23 (U+1E23): B<<256.0,315.0>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* uni1E25 (U+1E25): B<<256.0,315.0>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* uni1E27 (U+1E27): B<<256.0,315.0>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* uni1E29 (U+1E29): B<<256.0,315.0>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* uni1E2B (U+1E2B): B<<256.0,315.0>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* uni1E31 (U+1E31): B<<256.0,315.0>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* uni1E33 (U+1E33): B<<256.0,315.0>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* uni1E3F (U+1E3F): B<<262.5,340.0>-<259.0,306.0>-<256.0,275.0>>/B<<256.0,275.0>-<258.0,295.0>-<275.5,325.5>> = 0.18305298584087132

	* uni1E3F (U+1E3F): B<<598.0,326.5>-<595.0,301.0>-<592.0,276.0>>/B<<592.0,276.0>-<595.0,296.0>-<612.5,327.0>> = 1.6879921973171763

	* uni1E41 (U+1E41): B<<262.5,340.0>-<259.0,306.0>-<256.0,275.0>>/B<<256.0,275.0>-<258.0,295.0>-<275.5,325.5>> = 0.18305298584087132

	* uni1E41 (U+1E41): B<<598.0,326.5>-<595.0,301.0>-<592.0,276.0>>/B<<592.0,276.0>-<595.0,296.0>-<612.5,327.0>> = 1.6879921973171763

	* uni1E43 (U+1E43): B<<262.5,340.0>-<259.0,306.0>-<256.0,275.0>>/B<<256.0,275.0>-<258.0,295.0>-<275.5,325.5>> = 0.18305298584087132

	* uni1E43 (U+1E43): B<<598.0,326.5>-<595.0,301.0>-<592.0,276.0>>/B<<592.0,276.0>-<595.0,296.0>-<612.5,327.0>> = 1.6879921973171763

	* uni1E45 (U+1E45): B<<262.5,340.0>-<259.0,306.0>-<256.0,275.0>>/B<<256.0,275.0>-<258.0,295.0>-<275.5,325.5>> = 0.18305298584087132

	* uni1E47 (U+1E47): B<<262.5,340.0>-<259.0,306.0>-<256.0,275.0>>/B<<256.0,275.0>-<258.0,295.0>-<275.5,325.5>> = 0.18305298584087132

	* uni1E4B (U+1E4B): B<<262.5,340.0>-<259.0,306.0>-<256.0,275.0>>/B<<256.0,275.0>-<258.0,295.0>-<275.5,325.5>> = 0.18305298584087132

	* uni1E55 (U+1E55): B<<251.5,340.0>-<248.0,306.0>-<245.0,275.0>>/B<<245.0,275.0>-<247.0,295.0>-<264.5,325.5>> = 0.18305298584087132

	* uni1E57 (U+1E57): B<<251.5,340.0>-<248.0,306.0>-<245.0,275.0>>/B<<245.0,275.0>-<247.0,295.0>-<264.5,325.5>> = 0.18305298584087132

	* uni1E59 (U+1E59): B<<264.0,356.0>-<261.0,327.0>-<258.0,296.0>>/B<<258.0,296.0>-<290.0,400.0>-<333.5,462.0>> = 11.57518881739615

	* uni1E5B (U+1E5B): B<<264.0,356.0>-<261.0,327.0>-<258.0,296.0>>/B<<258.0,296.0>-<290.0,400.0>-<333.5,462.0>> = 11.57518881739615

	* uni1E5D (U+1E5D): B<<264.0,356.0>-<261.0,327.0>-<258.0,296.0>>/B<<258.0,296.0>-<290.0,400.0>-<333.5,462.0>> = 11.57518881739615

	* uni1E73 (U+1E73): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uni1E75 (U+1E75): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uni1E77 (U+1E77): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uni1E79 (U+1E79): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uni1E7B (U+1E7B): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uni1E8F (U+1E8F): B<<381.0,195.5>-<380.0,221.0>-<378.0,237.0>>/B<<378.0,237.0>-<376.0,217.0>-<358.5,186.0>> = 12.835609486401424

	* uni1E99 (U+1E99): B<<381.0,195.5>-<380.0,221.0>-<378.0,237.0>>/B<<378.0,237.0>-<376.0,217.0>-<358.5,186.0>> = 12.835609486401424

	* uni1E9A (U+1E9A): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni1EA1 (U+1EA1): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni1EA3 (U+1EA3): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni1EA5 (U+1EA5): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni1EA7 (U+1EA7): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni1EA9 (U+1EA9): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni1EAB (U+1EAB): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni1EAD (U+1EAD): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni1EAF (U+1EAF): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni1EB1 (U+1EB1): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni1EB3 (U+1EB3): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni1EB5 (U+1EB5): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni1EB7 (U+1EB7): B<<359.0,191.5>-<360.0,212.0>-<361.0,224.0>>/B<<361.0,224.0>-<356.0,205.0>-<338.0,175.5>> = 9.979921145744504

	* uni1EE5 (U+1EE5): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uni1EE7 (U+1EE7): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uni1EE9 (U+1EE9): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uni1EEB (U+1EEB): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uni1EED (U+1EED): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uni1EEF (U+1EEF): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uni1EF1 (U+1EF1): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uni1EF5 (U+1EF5): B<<381.0,195.5>-<380.0,221.0>-<378.0,237.0>>/B<<378.0,237.0>-<376.0,217.0>-<358.5,186.0>> = 12.835609486401424

	* uni1EF7 (U+1EF7): B<<381.0,195.5>-<380.0,221.0>-<378.0,237.0>>/B<<378.0,237.0>-<376.0,217.0>-<358.5,186.0>> = 12.835609486401424

	* uni1EF9 (U+1EF9): B<<381.0,195.5>-<380.0,221.0>-<378.0,237.0>>/B<<378.0,237.0>-<376.0,217.0>-<358.5,186.0>> = 12.835609486401424

	* uni207F (U+207F): B<<253.5,476.0>-<250.0,448.0>-<247.0,424.0>>/B<<247.0,424.0>-<251.0,440.0>-<268.5,464.5>> = 6.911227119024662

	* uni2083 (U+2083): B<<320.5,120.5>-<301.0,113.0>-<290.0,112.0>>/B<<290.0,112.0>-<348.0,105.0>-<378.5,75.0>> = 12.076152538371728

	* uni2153 (U+2153): B<<636.5,270.5>-<617.0,263.0>-<606.0,262.0>>/B<<606.0,262.0>-<664.0,255.0>-<694.5,225.0>> = 12.076152538371728

	* uni2154 (U+2154): B<<726.5,270.5>-<707.0,263.0>-<696.0,262.0>>/B<<696.0,262.0>-<754.0,255.0>-<784.5,225.0>> = 12.076152538371728

	* uni2C65 (U+2C65): B<<384.0,191.5>-<385.0,212.0>-<386.0,224.0>>/B<<386.0,224.0>-<381.0,205.0>-<363.0,175.5>> = 9.979921145744504

	* uniA727 (U+A727): B<<256.0,315.0>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* uniA741 (U+A741): B<<256.0,313.5>-<254.0,284.0>-<254.0,275.0>>/B<<254.0,275.0>-<256.0,295.0>-<273.5,325.5>> = 5.710593137499633

	* uniA7B9 (U+A7B9): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uogonek (U+0173): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* uring (U+016F): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* utilde (U+0169): B<<373.0,191.5>-<374.0,212.0>-<375.0,224.0>>/B<<375.0,224.0>-<370.0,205.0>-<352.0,175.5>> = 9.979921145744504

	* y (U+0079): B<<381.0,195.5>-<380.0,221.0>-<378.0,237.0>>/B<<378.0,237.0>-<376.0,217.0>-<358.5,186.0>> = 12.835609486401424

	* yacute (U+00FD): B<<381.0,195.5>-<380.0,221.0>-<378.0,237.0>>/B<<378.0,237.0>-<376.0,217.0>-<358.5,186.0>> = 12.835609486401424

	* ycircumflex (U+0177): B<<381.0,195.5>-<380.0,221.0>-<378.0,237.0>>/B<<378.0,237.0>-<376.0,217.0>-<358.5,186.0>> = 12.835609486401424

	* ydieresis (U+00FF): B<<381.0,195.5>-<380.0,221.0>-<378.0,237.0>>/B<<378.0,237.0>-<376.0,217.0>-<358.5,186.0>> = 12.835609486401424 

	* ygrave (U+1EF3): B<<381.0,195.5>-<380.0,221.0>-<378.0,237.0>>/B<<378.0,237.0>-<376.0,217.0>-<358.5,186.0>> = 12.835609486401424 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* x_x (U+E03F): L<<-75.0,-3.0>--<-74.0,181.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[14] BriemHand-ExtraLight.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.13, while a newer 0.10.1 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>⚠ <b>WARN:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* ⚠ **WARN** GF_Phonetics_APA is almost fulfilled. Missing codepoints:

	- 0x1D7E (LATIN SMALL CAPITAL LETTER U WITH STROKE)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Briem Hand ExtraLight' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- Aogonek.latnNAV

	- Eogonek.latnNAV

	- IJ_acutecomb

	- aogonek.latnNAV

	- dotlessi_ogonek

	- eogonek.latnNAV

	- ff.loclEWE

	- ij_acutecomb

	- j.latnNLD

	- j_acutecomb

	- uni013B.latnMAH

	- uni013C.latnMAH

	- uni0145.latnMAH

	- uni0146.latnMAH

	- uni01B2.loclTOD0

	- uni01B7.localGAD

	- uni025F.dotless

	- uni028B.loclTOD0

	- uni03020300.case.loclKYU

	- uni03020300.loclKYU

	- uni03020301.case.loclKYU

	- uni03020301.loclKYU

	- uni03020303.case.loclKYU

	- uni03020303.loclKYU

	- uni03080300.case

	- uni03080301.case

	- uni03080304.case

	- uni0308030C.case

	- uni0328.alt

	- x.p 

	- x.x
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: onehalf	Contours detected: 2	Expected: 3

	- Glyph name: Imacron	Contours detected: 1	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni024E	Contours detected: 1	Expected: 2

	- Glyph name: beta	Contours detected: 1	Expected: 2

	- Glyph name: uni1D4D	Contours detected: 2	Expected: 3

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E39	Contours detected: 2	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni20AD	Contours detected: 2	Expected: 1

	- Glyph name: uni2153	Contours detected: 2	Expected: 3

	- Glyph name: uni2154	Contours detected: 2	Expected: 1 or 3

	- Glyph name: uni2155	Contours detected: 2	Expected: 3

	- Glyph name: uni2156	Contours detected: 2	Expected: 3

	- Glyph name: uni2159	Contours detected: 3	Expected: 4

	- Glyph name: uni215A	Contours detected: 3	Expected: 4

	- Glyph name: oneeighth	Contours detected: 4	Expected: 5

	- Glyph name: threeeighths	Contours detected: 4	Expected: 5

	- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

	- Glyph name: seveneighths	Contours detected: 4	Expected: 5

	- Glyph name: arrowleft	Contours detected: 2	Expected: 1

	- Glyph name: arrowup	Contours detected: 2	Expected: 1

	- Glyph name: arrowright	Contours detected: 2	Expected: 1

	- Glyph name: arrowdown	Contours detected: 2	Expected: 1

	- Glyph name: Imacron	Contours detected: 1	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: arrowdown	Contours detected: 2	Expected: 1

	- Glyph name: arrowup	Contours detected: 2	Expected: 1

	- Glyph name: beta	Contours detected: 1	Expected: 2

	- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: oneeighth	Contours detected: 4	Expected: 5

	- Glyph name: onehalf	Contours detected: 2	Expected: 3

	- Glyph name: seveneighths	Contours detected: 4	Expected: 5

	- Glyph name: threeeighths	Contours detected: 4	Expected: 5

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni024E	Contours detected: 1	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E39	Contours detected: 2	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni20AD	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* ⚠ **WARN** The dot of soft dotted characters should disappear in other cases, for example: ј̀ ј́ ј̂ ј̃ ј̄ ј̆ ј̇ ј̈ ј̉ ј̊ ј̋ ј̌ ј̍ ј̏ ј̐ ј̑ ј̒ ј̓ ј᷄ ј᷅ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 540 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 552:
plus

Width = 551:
equal

Width = 533:
greater, greaterequal

Width = 494:
logicalnot

Width = 463:
plusminus

Width = 553:
multiply

Width = 489:
divide

Width = 535:
minus

Width = 557:
approxequal

Width = 573:
notequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni01C2 (U+01C2): L<<67.0,497.0>--<187.0,497.0>> -> L<<187.0,497.0>--<188.0,497.0>>

	* uni023C (U+023C): L<<146.0,130.0>--<235.0,294.0>> -> L<<235.0,294.0>--<325.0,470.0>>

	* uni023C (U+023C): L<<356.0,447.0>--<263.0,275.0>> -> L<<263.0,275.0>--<166.0,87.0>>

	* uni0283 (U+0283): L<<107.0,48.0>--<102.0,499.0>> -> L<<102.0,499.0>--<102.0,506.0>>

	* uni0283 (U+0283): L<<181.0,568.0>--<178.0,499.0>> -> L<<178.0,499.0>--<177.0,-21.0>>

	* uni1DC6 (U+1DC6): L<<58.0,665.0>--<57.0,665.0>> -> L<<57.0,665.0>--<-184.0,665.0>>

	* uni1DC7 (U+1DC7): L<<62.0,665.0>--<-146.0,665.0>> -> L<<-146.0,665.0>--<-147.0,665.0>>

	* uni2C65 (U+2C65): L<<154.0,87.0>--<272.0,294.0>> -> L<<272.0,294.0>--<370.0,473.0>>

	* uni2C65 (U+2C65): L<<410.0,467.0>--<300.0,275.0>> -> L<<300.0,275.0>--<181.0,56.0>>

	* uni2C66 (U+2C66): L<<174.0,253.0>--<196.0,294.0>> -> L<<196.0,294.0>--<276.0,450.0>>

	* uni2C66 (U+2C66): L<<319.0,450.0>--<224.0,275.0>> -> L<<224.0,275.0>--<171.0,172.0>>

	* uniA7B9 (U+A7B9): L<<156.0,94.0>--<270.0,294.0>> -> L<<270.0,294.0>--<431.0,589.0>> 

	* uniA7B9 (U+A7B9): L<<462.0,562.0>--<298.0,275.0>> -> L<<298.0,275.0>--<177.0,52.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Eng (U+014A): B<<172.0,221.5>-<170.0,193.0>-<169.0,188.0>>/B<<169.0,188.0>-<187.0,230.0>-<222.5,280.0>> = 11.888658039627968

	* uni019C (U+019C): B<<447.0,445.0>-<449.0,473.0>-<449.0,476.0>>/B<<449.0,476.0>-<432.0,407.0>-<402.0,338.0>> = 13.840695491655588

	* uni019C (U+019C): B<<782.0,442.0>-<784.0,473.0>-<784.0,476.0>>/B<<784.0,476.0>-<767.0,407.0>-<737.5,338.0>> = 13.840695491655588

	* uni01C2 (U+01C2): L<<186.0,451.0>--<186.0,451.0>>/B<<186.0,451.0>-<155.0,450.0>-<122.5,448.5>> = 1.8476102659945155 

	* uni0220 (U+0220): B<<172.0,221.5>-<170.0,193.0>-<169.0,188.0>>/B<<169.0,188.0>-<187.0,230.0>-<222.5,280.0>> = 11.888658039627968 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* beta (U+03B2): L<<174.0,553.0>--<173.0,-20.0>>

	* f (U+0066): L<<205.0,450.0>--<204.0,-21.0>>

	* fi (U+FB01): L<<205.0,450.0>--<204.0,-21.0>>

	* fl (U+FB02): L<<205.0,450.0>--<204.0,-21.0>>

	* florin (U+0192): L<<172.0,450.0>--<171.0,-21.0>>

	* germandbls (U+00DF): L<<174.0,553.0>--<173.0,-20.0>>

	* integral (U+222B): L<<206.0,507.0>--<205.0,-2.0>>

	* uni01A9 (U+01A9): L<<255.0,255.0>--<254.0,402.0>>

	* uni0248 (U+0248): L<<232.0,504.0>--<115.0,503.0>>

	* uni0283 (U+0283): L<<178.0,499.0>--<177.0,-21.0>>

	* uni1E1F (U+1E1F): L<<205.0,450.0>--<204.0,-21.0>> 

	* uniA7B5 (U+A7B5): L<<174.0,553.0>--<173.0,-20.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[13] BriemHand-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.13, while a newer 0.10.1 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>⚠ <b>WARN:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* ⚠ **WARN** GF_Phonetics_APA is almost fulfilled. Missing codepoints:

	- 0x1D7E (LATIN SMALL CAPITAL LETTER U WITH STROKE)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- Aogonek.latnNAV

	- Eogonek.latnNAV

	- IJ_acutecomb

	- aogonek.latnNAV

	- dotlessi_ogonek

	- eogonek.latnNAV

	- ff.loclEWE

	- ij_acutecomb

	- j.latnNLD

	- j_acutecomb

	- uni013B.latnMAH

	- uni013C.latnMAH

	- uni0145.latnMAH

	- uni0146.latnMAH

	- uni01B2.loclTOD0

	- uni01B7.localGAD

	- uni025F.dotless

	- uni028B.loclTOD0

	- uni03020300.case.loclKYU

	- uni03020300.loclKYU

	- uni03020301.case.loclKYU

	- uni03020301.loclKYU

	- uni03020303.case.loclKYU

	- uni03020303.loclKYU

	- uni03080300.case

	- uni03080301.case

	- uni03080304.case

	- uni0308030C.case

	- uni0328.alt

	- x.p 

	- x.x
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: onehalf	Contours detected: 2	Expected: 3

	- Glyph name: Imacron	Contours detected: 1	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni024E	Contours detected: 1	Expected: 2

	- Glyph name: beta	Contours detected: 1	Expected: 2

	- Glyph name: uni1D4D	Contours detected: 2	Expected: 3

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E39	Contours detected: 2	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni20AD	Contours detected: 2	Expected: 1

	- Glyph name: uni2153	Contours detected: 2	Expected: 3

	- Glyph name: uni2154	Contours detected: 2	Expected: 1 or 3

	- Glyph name: uni2155	Contours detected: 2	Expected: 3

	- Glyph name: uni2156	Contours detected: 2	Expected: 3

	- Glyph name: uni2159	Contours detected: 3	Expected: 4

	- Glyph name: uni215A	Contours detected: 3	Expected: 4

	- Glyph name: oneeighth	Contours detected: 4	Expected: 5

	- Glyph name: threeeighths	Contours detected: 4	Expected: 5

	- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

	- Glyph name: seveneighths	Contours detected: 4	Expected: 5

	- Glyph name: arrowleft	Contours detected: 2	Expected: 1

	- Glyph name: arrowup	Contours detected: 2	Expected: 1

	- Glyph name: arrowright	Contours detected: 2	Expected: 1

	- Glyph name: arrowdown	Contours detected: 2	Expected: 1

	- Glyph name: Imacron	Contours detected: 1	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: arrowdown	Contours detected: 2	Expected: 1

	- Glyph name: arrowup	Contours detected: 2	Expected: 1

	- Glyph name: beta	Contours detected: 1	Expected: 2

	- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: oneeighth	Contours detected: 4	Expected: 5

	- Glyph name: onehalf	Contours detected: 2	Expected: 3

	- Glyph name: seveneighths	Contours detected: 4	Expected: 5

	- Glyph name: threeeighths	Contours detected: 4	Expected: 5

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni024E	Contours detected: 1	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E39	Contours detected: 2	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni20AD	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* ⚠ **WARN** The dot of soft dotted characters should disappear in other cases, for example: ј̀ ј́ ј̂ ј̃ ј̄ ј̆ ј̇ ј̈ ј̉ ј̊ ј̋ ј̌ ј̍ ј̏ ј̐ ј̑ ј̒ ј̓ ј᷄ ј᷅ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 540 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 562:
plus

Width = 554:
equal

Width = 547:
greater, greaterequal

Width = 514:
logicalnot

Width = 481:
plusminus

Width = 552:
multiply

Width = 500:
divide

Width = 525:
minus

Width = 568:
approxequal

Width = 587:
notequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni0183 (U+0183): L<<140.0,756.0>--<142.0,756.0>> -> L<<142.0,756.0>--<419.0,756.0>>

	* uni023C (U+023C): L<<175.0,169.0>--<244.0,294.0>> -> L<<244.0,294.0>--<329.0,453.0>>

	* uni023C (U+023C): L<<364.0,429.0>--<277.0,273.0>> -> L<<277.0,273.0>--<191.0,110.0>>

	* uni0283 (U+0283): L<<219.0,556.0>--<217.0,499.0>> -> L<<217.0,499.0>--<213.0,11.0>>

	* uni0283 (U+0283): L<<92.0,84.0>--<87.0,499.0>> -> L<<87.0,499.0>--<87.0,516.0>>

	* uni2C65 (U+2C65): L<<195.0,167.0>--<268.0,294.0>> -> L<<268.0,294.0>--<362.0,466.0>>

	* uni2C65 (U+2C65): L<<408.0,459.0>--<300.0,273.0>> -> L<<300.0,273.0>--<203.0,95.0>>

	* uni2C66 (U+2C66): L<<205.0,289.0>--<208.0,294.0>> -> L<<208.0,294.0>--<284.0,437.0>>

	* uni2C66 (U+2C66): L<<333.0,437.0>--<241.0,273.0>> -> L<<241.0,273.0>--<201.0,197.0>>

	* uniA71A (U+A71A): L<<359.0,456.0>--<357.0,456.0>> -> L<<357.0,456.0>--<21.0,456.0>>

	* uniA7B9 (U+A7B9): L<<194.0,187.0>--<255.0,294.0>> -> L<<255.0,294.0>--<417.0,587.0>> 

	* uniA7B9 (U+A7B9): L<<451.0,554.0>--<288.0,273.0>> -> L<<288.0,273.0>--<194.0,103.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Eng (U+014A): B<<218.5,291.5>-<216.0,256.0>-<215.0,244.0>>/B<<215.0,244.0>-<227.0,279.0>-<256.5,321.5>> = 14.16100272532503

	* m (U+006D): B<<206.0,233.5>-<204.0,206.0>-<203.0,197.0>>/B<<203.0,197.0>-<214.0,230.0>-<239.5,273.0>> = 12.094757077012058

	* m (U+006D): B<<541.0,228.5>-<539.0,205.0>-<538.0,197.0>>/B<<538.0,197.0>-<550.0,231.0>-<575.0,274.0>> = 12.315018479274388

	* r (U+0072): B<<208.5,309.0>-<206.0,281.0>-<205.0,269.0>>/B<<205.0,269.0>-<249.0,403.0>-<297.5,463.5>> = 13.41437710769231

	* racute (U+0155): B<<208.5,309.0>-<206.0,281.0>-<205.0,269.0>>/B<<205.0,269.0>-<249.0,403.0>-<297.5,463.5>> = 13.41437710769231

	* rcaron (U+0159): B<<208.5,309.0>-<206.0,281.0>-<205.0,269.0>>/B<<205.0,269.0>-<249.0,403.0>-<297.5,463.5>> = 13.41437710769231

	* rmacronbelow (U+1E5F): B<<208.5,309.0>-<206.0,281.0>-<205.0,269.0>>/B<<205.0,269.0>-<249.0,403.0>-<297.5,463.5>> = 13.41437710769231

	* uni0157 (U+0157): B<<208.5,309.0>-<206.0,281.0>-<205.0,269.0>>/B<<205.0,269.0>-<249.0,403.0>-<297.5,463.5>> = 13.41437710769231

	* uni019C (U+019C): B<<431.0,351.0>-<433.0,381.0>-<434.0,389.0>>/B<<434.0,389.0>-<422.0,338.0>-<397.0,283.0>> = 6.115503566285384

	* uni019C (U+019C): B<<766.0,345.5>-<768.0,380.0>-<769.0,390.0>>/B<<769.0,390.0>-<758.0,339.0>-<732.5,284.0>> = 6.460865071087786

	* uni0211 (U+0211): B<<208.5,309.0>-<206.0,281.0>-<205.0,269.0>>/B<<205.0,269.0>-<249.0,403.0>-<297.5,463.5>> = 13.41437710769231

	* uni0213 (U+0213): B<<208.5,309.0>-<206.0,281.0>-<205.0,269.0>>/B<<205.0,269.0>-<249.0,403.0>-<297.5,463.5>> = 13.41437710769231

	* uni0220 (U+0220): B<<218.5,291.5>-<216.0,256.0>-<215.0,244.0>>/B<<215.0,244.0>-<227.0,279.0>-<256.5,321.5>> = 14.16100272532503

	* uni023E (U+023E): B<<346.5,505.0>-<344.0,471.0>-<341.0,430.0>>/L<<341.0,430.0>--<382.0,562.0>> = 13.070194876973531

	* uni024A (U+024A): L<<465.0,134.0>--<488.0,513.0>>/B<<488.0,513.0>-<453.0,403.0>-<406.5,314.5>> = 14.177330651334636

	* uni026F (U+026F): B<<453.0,295.5>-<455.0,319.0>-<456.0,327.0>>/B<<456.0,327.0>-<444.0,293.0>-<419.0,250.0>> = 12.315018479274388

	* uni0271 (U+0271): B<<206.0,233.5>-<204.0,206.0>-<203.0,197.0>>/B<<203.0,197.0>-<214.0,230.0>-<239.5,273.0>> = 12.094757077012058

	* uni0271 (U+0271): B<<541.0,228.5>-<539.0,205.0>-<538.0,197.0>>/B<<538.0,197.0>-<550.0,231.0>-<575.0,274.0>> = 12.315018479274388

	* uni0272 (U+0272): B<<211.5,233.5>-<209.0,206.0>-<208.0,197.0>>/B<<208.0,197.0>-<220.0,230.0>-<245.0,273.0>> = 13.642914775990052

	* uni1E3F (U+1E3F): B<<206.0,233.5>-<204.0,206.0>-<203.0,197.0>>/B<<203.0,197.0>-<214.0,230.0>-<239.5,273.0>> = 12.094757077012058

	* uni1E3F (U+1E3F): B<<541.0,228.5>-<539.0,205.0>-<538.0,197.0>>/B<<538.0,197.0>-<550.0,231.0>-<575.0,274.0>> = 12.315018479274388

	* uni1E41 (U+1E41): B<<206.0,233.5>-<204.0,206.0>-<203.0,197.0>>/B<<203.0,197.0>-<214.0,230.0>-<239.5,273.0>> = 12.094757077012058

	* uni1E41 (U+1E41): B<<541.0,228.5>-<539.0,205.0>-<538.0,197.0>>/B<<538.0,197.0>-<550.0,231.0>-<575.0,274.0>> = 12.315018479274388

	* uni1E43 (U+1E43): B<<206.0,233.5>-<204.0,206.0>-<203.0,197.0>>/B<<203.0,197.0>-<214.0,230.0>-<239.5,273.0>> = 12.094757077012058

	* uni1E43 (U+1E43): B<<541.0,228.5>-<539.0,205.0>-<538.0,197.0>>/B<<538.0,197.0>-<550.0,231.0>-<575.0,274.0>> = 12.315018479274388

	* uni1E59 (U+1E59): B<<208.5,309.0>-<206.0,281.0>-<205.0,269.0>>/B<<205.0,269.0>-<249.0,403.0>-<297.5,463.5>> = 13.41437710769231

	* uni1E5B (U+1E5B): B<<208.5,309.0>-<206.0,281.0>-<205.0,269.0>>/B<<205.0,269.0>-<249.0,403.0>-<297.5,463.5>> = 13.41437710769231 

	* uni1E5D (U+1E5D): B<<208.5,309.0>-<206.0,281.0>-<205.0,269.0>>/B<<205.0,269.0>-<249.0,403.0>-<297.5,463.5>> = 13.41437710769231 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* germandbls (U+00DF): L<<82.0,85.0>--<84.0,525.0>>

	* integral (U+222B): L<<117.0,85.0>--<115.0,516.0>>

	* integral (U+222B): L<<242.0,518.0>--<238.0,22.0>>

	* product (U+220F): L<<443.0,561.0>--<266.0,562.0>>

	* uni0283 (U+0283): L<<217.0,499.0>--<213.0,11.0>> 

	* x_x (U+E03F): L<<-130.0,-5.0>--<-129.0,117.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[13] BriemHand-Light.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.13, while a newer 0.10.1 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>⚠ <b>WARN:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* ⚠ **WARN** GF_Phonetics_APA is almost fulfilled. Missing codepoints:

	- 0x1D7E (LATIN SMALL CAPITAL LETTER U WITH STROKE)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- Aogonek.latnNAV

	- Eogonek.latnNAV

	- IJ_acutecomb

	- aogonek.latnNAV

	- dotlessi_ogonek

	- eogonek.latnNAV

	- ff.loclEWE

	- ij_acutecomb

	- j.latnNLD

	- j_acutecomb

	- uni013B.latnMAH

	- uni013C.latnMAH

	- uni0145.latnMAH

	- uni0146.latnMAH

	- uni01B2.loclTOD0

	- uni01B7.localGAD

	- uni025F.dotless

	- uni028B.loclTOD0

	- uni03020300.case.loclKYU

	- uni03020300.loclKYU

	- uni03020301.case.loclKYU

	- uni03020301.loclKYU

	- uni03020303.case.loclKYU

	- uni03020303.loclKYU

	- uni03080300.case

	- uni03080301.case

	- uni03080304.case

	- uni0308030C.case

	- uni0328.alt

	- x.p 

	- x.x
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: onehalf	Contours detected: 2	Expected: 3

	- Glyph name: Imacron	Contours detected: 1	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni024E	Contours detected: 1	Expected: 2

	- Glyph name: beta	Contours detected: 1	Expected: 2

	- Glyph name: uni1D4D	Contours detected: 2	Expected: 3

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E39	Contours detected: 2	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni20AD	Contours detected: 2	Expected: 1

	- Glyph name: uni2153	Contours detected: 2	Expected: 3

	- Glyph name: uni2154	Contours detected: 2	Expected: 1 or 3

	- Glyph name: uni2155	Contours detected: 2	Expected: 3

	- Glyph name: uni2156	Contours detected: 2	Expected: 3

	- Glyph name: uni2159	Contours detected: 3	Expected: 4

	- Glyph name: uni215A	Contours detected: 3	Expected: 4

	- Glyph name: oneeighth	Contours detected: 4	Expected: 5

	- Glyph name: threeeighths	Contours detected: 4	Expected: 5

	- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

	- Glyph name: seveneighths	Contours detected: 4	Expected: 5

	- Glyph name: arrowleft	Contours detected: 2	Expected: 1

	- Glyph name: arrowup	Contours detected: 2	Expected: 1

	- Glyph name: arrowright	Contours detected: 2	Expected: 1

	- Glyph name: arrowdown	Contours detected: 2	Expected: 1

	- Glyph name: Imacron	Contours detected: 1	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: arrowdown	Contours detected: 2	Expected: 1

	- Glyph name: arrowup	Contours detected: 2	Expected: 1

	- Glyph name: beta	Contours detected: 1	Expected: 2

	- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: oneeighth	Contours detected: 4	Expected: 5

	- Glyph name: onehalf	Contours detected: 2	Expected: 3

	- Glyph name: seveneighths	Contours detected: 4	Expected: 5

	- Glyph name: threeeighths	Contours detected: 4	Expected: 5

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni024E	Contours detected: 1	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E39	Contours detected: 2	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni20AD	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* ⚠ **WARN** The dot of soft dotted characters should disappear in other cases, for example: ј̀ ј́ ј̂ ј̃ ј̄ ј̆ ј̇ ј̈ ј̉ ј̊ ј̋ ј̌ ј̍ ј̏ ј̐ ј̑ ј̒ ј̓ ј᷄ ј᷅ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 540 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 555:
plus

Width = 552:
equal

Width = 537:
greater, greaterequal

Width = 499:
logicalnot

Width = 468:
plusminus

Width = 553:
multiply

Width = 492:
divide

Width = 532:
minus

Width = 560:
approxequal

Width = 577:
notequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* etTironian (U+204A): L<<60.0,544.0>--<363.0,544.0>> -> L<<363.0,544.0>--<363.0,544.0>>

	* uni018C (U+018C): L<<281.0,756.0>--<470.0,756.0>> -> L<<470.0,756.0>--<471.0,756.0>>

	* uni01C2 (U+01C2): L<<65.0,497.0>--<183.0,497.0>> -> L<<183.0,497.0>--<183.0,497.0>>

	* uni023C (U+023C): L<<153.0,139.0>--<237.0,294.0>> -> L<<237.0,294.0>--<326.0,465.0>>

	* uni023C (U+023C): L<<358.0,442.0>--<267.0,274.0>> -> L<<267.0,274.0>--<172.0,93.0>>

	* uni0283 (U+0283): L<<103.0,58.0>--<98.0,499.0>> -> L<<98.0,499.0>--<98.0,509.0>>

	* uni0283 (U+0283): L<<191.0,565.0>--<188.0,499.0>> -> L<<188.0,499.0>--<186.0,-13.0>>

	* uni2C65 (U+2C65): L<<165.0,108.0>--<271.0,294.0>> -> L<<271.0,294.0>--<368.0,471.0>>

	* uni2C65 (U+2C65): L<<410.0,465.0>--<300.0,274.0>> -> L<<300.0,274.0>--<185.0,64.0>>

	* uni2C66 (U+2C66): L<<182.0,262.0>--<199.0,294.0>> -> L<<199.0,294.0>--<278.0,447.0>>

	* uni2C66 (U+2C66): L<<322.0,447.0>--<228.0,274.0>> -> L<<228.0,274.0>--<179.0,179.0>>

	* uniA7B9 (U+A7B9): L<<166.0,118.0>--<266.0,294.0>> -> L<<266.0,294.0>--<427.0,589.0>> 

	* uniA7B9 (U+A7B9): L<<459.0,560.0>--<295.0,274.0>> -> L<<295.0,274.0>--<180.0,62.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Eng (U+014A): B<<184.0,237.0>-<182.0,209.0>-<181.0,203.0>>/B<<181.0,203.0>-<197.0,243.0>-<231.0,291.0>> = 12.33908727832618

	* m (U+006D): B<<518.0,195.5>-<516.0,169.0>-<515.0,163.0>>/B<<515.0,163.0>-<531.0,203.0>-<559.5,251.0>> = 12.33908727832618

	* uni019C (U+019C): B<<778.0,419.5>-<780.0,449.0>-<780.0,454.0>>/B<<780.0,454.0>-<764.0,389.0>-<736.0,323.5>> = 13.828650972280153

	* uni0220 (U+0220): B<<184.0,237.0>-<182.0,209.0>-<181.0,203.0>>/B<<181.0,203.0>-<197.0,243.0>-<231.0,291.0>> = 12.33908727832618

	* uni0271 (U+0271): B<<518.0,195.5>-<516.0,169.0>-<515.0,163.0>>/B<<515.0,163.0>-<531.0,203.0>-<559.5,251.0>> = 12.33908727832618

	* uni0272 (U+0272): B<<185.0,199.5>-<183.0,169.0>-<182.0,163.0>>/B<<182.0,163.0>-<198.0,203.0>-<226.5,251.0>> = 12.33908727832618

	* uni1E3F (U+1E3F): B<<518.0,195.5>-<516.0,169.0>-<515.0,163.0>>/B<<515.0,163.0>-<531.0,203.0>-<559.5,251.0>> = 12.33908727832618

	* uni1E41 (U+1E41): B<<518.0,195.5>-<516.0,169.0>-<515.0,163.0>>/B<<515.0,163.0>-<531.0,203.0>-<559.5,251.0>> = 12.33908727832618 

	* uni1E43 (U+1E43): B<<518.0,195.5>-<516.0,169.0>-<515.0,163.0>>/B<<515.0,163.0>-<531.0,203.0>-<559.5,251.0>> = 12.33908727832618 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* beta (U+03B2): L<<184.0,551.0>--<182.0,-12.0>>

	* f (U+0066): L<<212.0,447.0>--<210.0,-13.0>>

	* fi (U+FB01): L<<212.0,447.0>--<211.0,-13.0>>

	* fl (U+FB02): L<<212.0,447.0>--<211.0,-13.0>>

	* florin (U+0192): L<<182.0,447.0>--<181.0,-13.0>>

	* germandbls (U+00DF): L<<184.0,551.0>--<182.0,-12.0>>

	* germandbls (U+00DF): L<<96.0,58.0>--<97.0,521.0>>

	* integral (U+222B): L<<130.0,58.0>--<129.0,509.0>>

	* integral (U+222B): L<<216.0,510.0>--<214.0,4.0>>

	* uni01A9 (U+01A9): L<<246.0,251.0>--<245.0,404.0>>

	* uni01E4 (U+01E4): L<<563.0,135.0>--<407.0,134.0>>

	* uni0283 (U+0283): L<<188.0,499.0>--<186.0,-13.0>>

	* uni1E1F (U+1E1F): L<<212.0,447.0>--<210.0,-13.0>> 

	* uniA7B5 (U+A7B5): L<<184.0,551.0>--<182.0,-12.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[13] BriemHand-SemiBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.13, while a newer 0.10.1 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>⚠ <b>WARN:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* ⚠ **WARN** GF_Phonetics_APA is almost fulfilled. Missing codepoints:

	- 0x1D7E (LATIN SMALL CAPITAL LETTER U WITH STROKE)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- Aogonek.latnNAV

	- Eogonek.latnNAV

	- IJ_acutecomb

	- aogonek.latnNAV

	- dotlessi_ogonek

	- eogonek.latnNAV

	- ff.loclEWE

	- ij_acutecomb

	- j.latnNLD

	- j_acutecomb

	- uni013B.latnMAH

	- uni013C.latnMAH

	- uni0145.latnMAH

	- uni0146.latnMAH

	- uni01B2.loclTOD0

	- uni01B7.localGAD

	- uni025F.dotless

	- uni028B.loclTOD0

	- uni03020300.case.loclKYU

	- uni03020300.loclKYU

	- uni03020301.case.loclKYU

	- uni03020301.loclKYU

	- uni03020303.case.loclKYU

	- uni03020303.loclKYU

	- uni03080300.case

	- uni03080301.case

	- uni03080304.case

	- uni0308030C.case

	- uni0328.alt

	- x.p 

	- x.x
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: onehalf	Contours detected: 2	Expected: 3

	- Glyph name: Imacron	Contours detected: 1	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni024E	Contours detected: 1	Expected: 2

	- Glyph name: beta	Contours detected: 1	Expected: 2

	- Glyph name: uni1D4D	Contours detected: 2	Expected: 3

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E39	Contours detected: 2	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni2153	Contours detected: 2	Expected: 3

	- Glyph name: uni2154	Contours detected: 2	Expected: 1 or 3

	- Glyph name: uni2155	Contours detected: 2	Expected: 3

	- Glyph name: uni2156	Contours detected: 2	Expected: 3

	- Glyph name: uni2159	Contours detected: 3	Expected: 4

	- Glyph name: uni215A	Contours detected: 3	Expected: 4

	- Glyph name: oneeighth	Contours detected: 4	Expected: 5

	- Glyph name: threeeighths	Contours detected: 4	Expected: 5

	- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

	- Glyph name: seveneighths	Contours detected: 4	Expected: 5

	- Glyph name: arrowleft	Contours detected: 2	Expected: 1

	- Glyph name: arrowup	Contours detected: 2	Expected: 1

	- Glyph name: arrowright	Contours detected: 2	Expected: 1

	- Glyph name: arrowdown	Contours detected: 2	Expected: 1

	- Glyph name: Imacron	Contours detected: 1	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: arrowdown	Contours detected: 2	Expected: 1

	- Glyph name: arrowup	Contours detected: 2	Expected: 1

	- Glyph name: beta	Contours detected: 1	Expected: 2

	- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: oneeighth	Contours detected: 4	Expected: 5

	- Glyph name: onehalf	Contours detected: 2	Expected: 3

	- Glyph name: seveneighths	Contours detected: 4	Expected: 5

	- Glyph name: threeeighths	Contours detected: 4	Expected: 5

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni024E	Contours detected: 1	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E39	Contours detected: 2	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* ⚠ **WARN** The dot of soft dotted characters should disappear in other cases, for example: ј̀ ј́ ј̂ ј̃ ј̄ ј̆ ј̇ ј̈ ј̉ ј̊ ј̋ ј̌ ј̍ ј̏ ј̐ ј̑ ј̒ ј̓ ј᷄ ј᷅ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 540 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 568:
plus

Width = 556:
equal

Width = 555:
greater, greaterequal

Width = 526:
logicalnot

Width = 491:
plusminus

Width = 551:
multiply

Width = 507:
divide

Width = 519:
minus

Width = 575:
approxequal

Width = 595:
notequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni023C (U+023C): L<<194.0,196.0>--<250.0,295.0>> -> L<<250.0,295.0>--<330.0,443.0>>

	* uni023C (U+023C): L<<369.0,419.0>--<285.0,271.0>> -> L<<285.0,271.0>--<206.0,125.0>>

	* uni0283 (U+0283): L<<241.0,550.0>--<239.0,499.0>> -> L<<239.0,499.0>--<233.0,29.0>>

	* uni0283 (U+0283): L<<83.0,105.0>--<78.0,499.0>> -> L<<78.0,499.0>--<78.0,522.0>>

	* uni2C65 (U+2C65): L<<219.0,214.0>--<265.0,295.0>> -> L<<265.0,295.0>--<358.0,462.0>>

	* uni2C65 (U+2C65): L<<407.0,454.0>--<300.0,271.0>> -> L<<300.0,271.0>--<221.0,127.0>>

	* uni2C66 (U+2C66): L<<341.0,430.0>--<251.0,271.0>> -> L<<251.0,271.0>--<218.0,211.0>>

	* uniA7B9 (U+A7B9): L<<217.0,244.0>--<247.0,295.0>> -> L<<247.0,295.0>--<408.0,585.0>> 

	* uniA7B9 (U+A7B9): L<<415.0,500.0>--<282.0,271.0>> -> L<<282.0,271.0>--<213.0,146.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Eng (U+014A): B<<245.5,326.0>-<243.0,293.0>-<242.0,277.0>>/B<<242.0,277.0>-<250.0,307.0>-<276.5,345.5>> = 11.355082803140162

	* b (U+0062): B<<225.0,288.0>-<222.0,250.0>-<221.0,233.0>>/B<<221.0,233.0>-<230.0,262.0>-<252.0,299.5>> = 13.874998735510172

	* bmacronbelow (U+1E07): B<<225.0,288.0>-<222.0,250.0>-<221.0,233.0>>/B<<221.0,233.0>-<230.0,262.0>-<252.0,299.5>> = 13.874998735510172

	* eng (U+014B): B<<222.0,254.5>-<220.0,231.0>-<219.0,223.0>>/B<<219.0,223.0>-<228.0,252.0>-<250.5,291.0>> = 10.116443050038137

	* m (U+006D): B<<225.0,273.0>-<222.0,239.0>-<221.0,223.0>>/B<<221.0,223.0>-<229.0,252.0>-<251.5,291.0>> = 11.845826943741303

	* m (U+006D): B<<560.5,265.0>-<558.0,237.0>-<556.0,224.0>>/B<<556.0,224.0>-<565.0,253.0>-<587.5,291.5>> = 8.49529713638477

	* n (U+006E): B<<224.0,273.0>-<221.0,239.0>-<219.0,223.0>>/B<<219.0,223.0>-<228.0,252.0>-<250.5,291.0>> = 10.116443050038137

	* nacute (U+0144): B<<224.0,273.0>-<221.0,239.0>-<219.0,223.0>>/B<<219.0,223.0>-<228.0,252.0>-<250.5,291.0>> = 10.116443050038137

	* ncaron (U+0148): B<<224.0,273.0>-<221.0,239.0>-<219.0,223.0>>/B<<219.0,223.0>-<228.0,252.0>-<250.5,291.0>> = 10.116443050038137

	* nlongrightleg (U+019E): B<<224.0,273.0>-<221.0,239.0>-<219.0,223.0>>/B<<219.0,223.0>-<228.0,252.0>-<250.5,291.0>> = 10.116443050038137

	* nmacronbelow (U+1E49): B<<224.0,273.0>-<221.0,239.0>-<219.0,223.0>>/B<<219.0,223.0>-<228.0,252.0>-<250.5,291.0>> = 10.116443050038137

	* ntilde (U+00F1): B<<224.0,273.0>-<221.0,239.0>-<219.0,223.0>>/B<<219.0,223.0>-<228.0,252.0>-<250.5,291.0>> = 10.116443050038137

	* p (U+0070): B<<221.0,292.5>-<218.0,258.0>-<216.0,233.0>>/B<<216.0,233.0>-<224.0,262.0>-<246.0,299.5>> = 10.848240058837815

	* r (U+0072): B<<226.5,320.0>-<224.0,294.0>-<223.0,278.0>>/B<<223.0,278.0>-<263.0,402.0>-<309.5,463.0>> = 14.302362220843962

	* racute (U+0155): B<<226.5,320.0>-<224.0,294.0>-<223.0,278.0>>/B<<223.0,278.0>-<263.0,402.0>-<309.5,463.0>> = 14.302362220843962

	* rcaron (U+0159): B<<226.5,320.0>-<224.0,294.0>-<223.0,278.0>>/B<<223.0,278.0>-<263.0,402.0>-<309.5,463.0>> = 14.302362220843962

	* rmacronbelow (U+1E5F): B<<226.5,320.0>-<224.0,294.0>-<223.0,278.0>>/B<<223.0,278.0>-<263.0,402.0>-<309.5,463.0>> = 14.302362220843962

	* thorn (U+00FE): B<<226.0,287.5>-<223.0,249.0>-<222.0,233.0>>/B<<222.0,233.0>-<231.0,262.0>-<252.5,299.5>> = 13.665125023942625

	* uni0146 (U+0146): B<<224.0,273.0>-<221.0,239.0>-<219.0,223.0>>/B<<219.0,223.0>-<228.0,252.0>-<250.5,291.0>> = 10.116443050038137

	* uni0157 (U+0157): B<<226.5,320.0>-<224.0,294.0>-<223.0,278.0>>/B<<223.0,278.0>-<263.0,402.0>-<309.5,463.0>> = 14.302362220843962

	* uni0180 (U+0180): B<<225.0,288.0>-<222.0,250.0>-<221.0,233.0>>/B<<221.0,233.0>-<230.0,262.0>-<252.0,299.5>> = 13.874998735510172

	* uni0183 (U+0183): B<<224.5,282.5>-<222.0,248.0>-<221.0,233.0>>/B<<221.0,233.0>-<230.0,262.0>-<252.0,299.5>> = 13.427384564649621

	* uni019C (U+019C): B<<422.0,304.0>-<424.0,329.0>-<425.0,339.0>>/B<<425.0,339.0>-<416.0,299.0>-<393.5,252.0>> = 6.969790354320093

	* uni019C (U+019C): B<<757.5,297.5>-<760.0,327.0>-<761.0,340.0>>/B<<761.0,340.0>-<752.0,299.0>-<729.5,252.5>> = 7.982051573811601

	* uni01A5 (U+01A5): B<<232.5,287.5>-<230.0,253.0>-<228.0,233.0>>/B<<228.0,233.0>-<237.0,262.0>-<259.0,299.5>> = 11.530866261440329

	* uni01CC (U+01CC): B<<224.0,273.0>-<221.0,239.0>-<219.0,223.0>>/B<<219.0,223.0>-<228.0,252.0>-<250.5,291.0>> = 10.116443050038137

	* uni01F9 (U+01F9): B<<224.0,273.0>-<221.0,239.0>-<219.0,223.0>>/B<<219.0,223.0>-<228.0,252.0>-<250.5,291.0>> = 10.116443050038137

	* uni0211 (U+0211): B<<226.5,320.0>-<224.0,294.0>-<223.0,278.0>>/B<<223.0,278.0>-<263.0,402.0>-<309.5,463.0>> = 14.302362220843962

	* uni0213 (U+0213): B<<226.5,320.0>-<224.0,294.0>-<223.0,278.0>>/B<<223.0,278.0>-<263.0,402.0>-<309.5,463.0>> = 14.302362220843962

	* uni0220 (U+0220): B<<245.5,326.0>-<243.0,293.0>-<242.0,277.0>>/B<<242.0,277.0>-<250.0,307.0>-<276.5,345.5>> = 11.355082803140162

	* uni023E (U+023E): B<<365.5,514.5>-<364.0,497.0>-<363.0,477.0>>/L<<363.0,477.0>--<384.0,546.0>> = 14.065107838035287

	* uni024A (U+024A): L<<466.0,146.0>--<486.0,503.0>>/B<<486.0,503.0>-<452.0,392.0>-<406.5,304.0>> = 13.823660918283608

	* uni0253 (U+0253): B<<224.5,289.5>-<222.0,251.0>-<221.0,233.0>>/B<<221.0,233.0>-<230.0,262.0>-<252.0,299.5>> = 14.061629279075722

	* uni026F (U+026F): B<<439.5,259.0>-<442.0,287.0>-<443.0,300.0>>/B<<443.0,300.0>-<434.0,271.0>-<411.5,232.5>> = 12.842754043944451

	* uni026F (U+026F): B<<774.5,251.0>-<777.0,285.0>-<779.0,301.0>>/B<<779.0,301.0>-<770.0,272.0>-<747.5,233.0>> = 10.116443050038137

	* uni0271 (U+0271): B<<225.0,273.0>-<222.0,239.0>-<221.0,223.0>>/B<<221.0,223.0>-<229.0,252.0>-<251.5,291.0>> = 11.845826943741303

	* uni0271 (U+0271): B<<560.5,265.0>-<558.0,237.0>-<556.0,224.0>>/B<<556.0,224.0>-<565.0,253.0>-<587.5,291.5>> = 8.49529713638477

	* uni0272 (U+0272): B<<233.0,273.0>-<230.0,239.0>-<229.0,223.0>>/B<<229.0,223.0>-<237.0,252.0>-<259.5,291.0>> = 11.845826943741303

	* uni0440 (U+0440): B<<221.0,292.5>-<218.0,258.0>-<216.0,233.0>>/B<<216.0,233.0>-<224.0,262.0>-<246.0,299.5>> = 10.848240058837815

	* uni1E03 (U+1E03): B<<225.0,288.0>-<222.0,250.0>-<221.0,233.0>>/B<<221.0,233.0>-<230.0,262.0>-<252.0,299.5>> = 13.874998735510172

	* uni1E05 (U+1E05): B<<225.0,288.0>-<222.0,250.0>-<221.0,233.0>>/B<<221.0,233.0>-<230.0,262.0>-<252.0,299.5>> = 13.874998735510172

	* uni1E3F (U+1E3F): B<<225.0,273.0>-<222.0,239.0>-<221.0,223.0>>/B<<221.0,223.0>-<229.0,252.0>-<251.5,291.0>> = 11.845826943741303

	* uni1E3F (U+1E3F): B<<560.5,265.0>-<558.0,237.0>-<556.0,224.0>>/B<<556.0,224.0>-<565.0,253.0>-<587.5,291.5>> = 8.49529713638477

	* uni1E41 (U+1E41): B<<225.0,273.0>-<222.0,239.0>-<221.0,223.0>>/B<<221.0,223.0>-<229.0,252.0>-<251.5,291.0>> = 11.845826943741303

	* uni1E41 (U+1E41): B<<560.5,265.0>-<558.0,237.0>-<556.0,224.0>>/B<<556.0,224.0>-<565.0,253.0>-<587.5,291.5>> = 8.49529713638477

	* uni1E43 (U+1E43): B<<225.0,273.0>-<222.0,239.0>-<221.0,223.0>>/B<<221.0,223.0>-<229.0,252.0>-<251.5,291.0>> = 11.845826943741303

	* uni1E43 (U+1E43): B<<560.5,265.0>-<558.0,237.0>-<556.0,224.0>>/B<<556.0,224.0>-<565.0,253.0>-<587.5,291.5>> = 8.49529713638477

	* uni1E45 (U+1E45): B<<224.0,273.0>-<221.0,239.0>-<219.0,223.0>>/B<<219.0,223.0>-<228.0,252.0>-<250.5,291.0>> = 10.116443050038137

	* uni1E47 (U+1E47): B<<224.0,273.0>-<221.0,239.0>-<219.0,223.0>>/B<<219.0,223.0>-<228.0,252.0>-<250.5,291.0>> = 10.116443050038137

	* uni1E4B (U+1E4B): B<<224.0,273.0>-<221.0,239.0>-<219.0,223.0>>/B<<219.0,223.0>-<228.0,252.0>-<250.5,291.0>> = 10.116443050038137

	* uni1E55 (U+1E55): B<<221.0,292.5>-<218.0,258.0>-<216.0,233.0>>/B<<216.0,233.0>-<224.0,262.0>-<246.0,299.5>> = 10.848240058837815

	* uni1E57 (U+1E57): B<<221.0,292.5>-<218.0,258.0>-<216.0,233.0>>/B<<216.0,233.0>-<224.0,262.0>-<246.0,299.5>> = 10.848240058837815

	* uni1E59 (U+1E59): B<<226.5,320.0>-<224.0,294.0>-<223.0,278.0>>/B<<223.0,278.0>-<263.0,402.0>-<309.5,463.0>> = 14.302362220843962

	* uni1E5B (U+1E5B): B<<226.5,320.0>-<224.0,294.0>-<223.0,278.0>>/B<<223.0,278.0>-<263.0,402.0>-<309.5,463.0>> = 14.302362220843962

	* uni1E5D (U+1E5D): B<<226.5,320.0>-<224.0,294.0>-<223.0,278.0>>/B<<223.0,278.0>-<263.0,402.0>-<309.5,463.0>> = 14.302362220843962 

	* uni207F (U+207F): B<<223.5,428.5>-<221.0,402.0>-<219.0,389.0>>/B<<219.0,389.0>-<228.0,411.0>-<249.0,441.0>> = 13.502861394657142 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* product (U+220F): L<<450.0,543.0>--<300.0,544.0>> 

	* uni01A9 (U+01A9): L<<199.0,230.0>--<198.0,419.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[13] BriemHand-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.13, while a newer 0.10.1 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>⚠ <b>WARN:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* ⚠ **WARN** GF_Phonetics_APA is almost fulfilled. Missing codepoints:

	- 0x1D7E (LATIN SMALL CAPITAL LETTER U WITH STROKE)
 [code: missing-codepoints]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure Stylistic Sets have description. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/stylisticset_description">com.google.fonts/check/stylisticset_description</a>)</summary><div>


* ⚠ **WARN** The stylistic set ss01 lacks a description string on the 'name' table. [code: missing-description]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- Aogonek.latnNAV

	- Eogonek.latnNAV

	- IJ_acutecomb

	- aogonek.latnNAV

	- dotlessi_ogonek

	- eogonek.latnNAV

	- ff.loclEWE

	- ij_acutecomb

	- j.latnNLD

	- j_acutecomb

	- uni013B.latnMAH

	- uni013C.latnMAH

	- uni0145.latnMAH

	- uni0146.latnMAH

	- uni01B2.loclTOD0

	- uni01B7.localGAD

	- uni025F.dotless

	- uni028B.loclTOD0

	- uni03020300.case.loclKYU

	- uni03020300.loclKYU

	- uni03020301.case.loclKYU

	- uni03020301.loclKYU

	- uni03020303.case.loclKYU

	- uni03020303.loclKYU

	- uni03080300.case

	- uni03080301.case

	- uni03080304.case

	- uni0308030C.case

	- uni0328.alt

	- x.p 

	- x.x
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: onehalf	Contours detected: 2	Expected: 3

	- Glyph name: Imacron	Contours detected: 1	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni0247	Contours detected: 3	Expected: 4

	- Glyph name: uni024E	Contours detected: 1	Expected: 2

	- Glyph name: beta	Contours detected: 1	Expected: 2

	- Glyph name: uni1D4D	Contours detected: 2	Expected: 3

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E39	Contours detected: 2	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: uni2153	Contours detected: 2	Expected: 3

	- Glyph name: uni2154	Contours detected: 2	Expected: 1 or 3

	- Glyph name: uni2155	Contours detected: 2	Expected: 3

	- Glyph name: uni2156	Contours detected: 2	Expected: 3

	- Glyph name: uni2159	Contours detected: 3	Expected: 4

	- Glyph name: uni215A	Contours detected: 3	Expected: 4

	- Glyph name: oneeighth	Contours detected: 4	Expected: 5

	- Glyph name: threeeighths	Contours detected: 4	Expected: 5

	- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

	- Glyph name: seveneighths	Contours detected: 4	Expected: 5

	- Glyph name: arrowleft	Contours detected: 2	Expected: 1

	- Glyph name: arrowup	Contours detected: 2	Expected: 1

	- Glyph name: arrowright	Contours detected: 2	Expected: 1

	- Glyph name: arrowdown	Contours detected: 2	Expected: 1

	- Glyph name: Imacron	Contours detected: 1	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: arrowdown	Contours detected: 2	Expected: 1

	- Glyph name: arrowup	Contours detected: 2	Expected: 1

	- Glyph name: beta	Contours detected: 1	Expected: 2

	- Glyph name: fiveeighths	Contours detected: 4	Expected: 5

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: oneeighth	Contours detected: 4	Expected: 5

	- Glyph name: onehalf	Contours detected: 2	Expected: 3

	- Glyph name: seveneighths	Contours detected: 4	Expected: 5

	- Glyph name: threeeighths	Contours detected: 4	Expected: 5

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni01EC	Contours detected: 4	Expected: 3

	- Glyph name: uni01ED	Contours detected: 4	Expected: 3

	- Glyph name: uni0228	Contours detected: 2	Expected: 1

	- Glyph name: uni0229	Contours detected: 3	Expected: 2

	- Glyph name: uni023D	Contours detected: 2	Expected: 1

	- Glyph name: uni0247	Contours detected: 3	Expected: 4

	- Glyph name: uni024E	Contours detected: 1	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E39	Contours detected: 2	Expected: 3

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* ⚠ **WARN** The dot of soft dotted characters should disappear in other cases, for example: ј̀ ј́ ј̂ ј̃ ј̄ ј̆ ј̇ ј̈ ј̉ ј̊ ј̋ ј̌ ј̍ ј̏ ј̐ ј̑ ј̒ ј̓ ј᷄ ј᷅ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 540 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 574:
plus

Width = 558:
equal

Width = 562:
greater, greaterequal

Width = 538:
logicalnot

Width = 502:
plusminus

Width = 551:
multiply

Width = 513:
divide, minus

Width = 582:
approxequal

Width = 602:
notequal
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* uni023C (U+023C): L<<216.0,227.0>--<255.0,295.0>> -> L<<255.0,295.0>--<331.0,433.0>>

	* uni023C (U+023C): L<<374.0,410.0>--<292.0,270.0>> -> L<<292.0,270.0>--<222.0,142.0>>

	* uni0283 (U+0283): L<<263.0,543.0>--<262.0,499.0>> -> L<<262.0,499.0>--<254.0,47.0>>

	* uni0283 (U+0283): L<<74.0,126.0>--<69.0,499.0>> -> L<<69.0,499.0>--<69.0,528.0>>

	* uni2C65 (U+2C65): L<<243.0,261.0>--<262.0,295.0>> -> L<<262.0,295.0>--<354.0,458.0>>

	* uni2C65 (U+2C65): L<<406.0,449.0>--<300.0,270.0>> -> L<<300.0,270.0>--<242.0,165.0>>

	* uni2C66 (U+2C66): L<<349.0,422.0>--<260.0,270.0>> -> L<<260.0,270.0>--<236.0,225.0>>

	* uniA71A (U+A71A): L<<404.0,405.0>--<403.0,405.0>> -> L<<403.0,405.0>--<25.0,405.0>> 

	* uniA7B9 (U+A7B9): L<<399.0,480.0>--<276.0,270.0>> -> L<<276.0,270.0>--<233.0,193.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* Eng (U+014A): B<<273.0,375.0>-<270.0,334.0>-<268.0,310.0>>/B<<268.0,310.0>-<274.0,335.0>-<296.5,369.5>> = 8.732091590069578

	* b (U+0062): B<<240.5,301.5>-<238.0,267.0>-<238.0,254.0>>/B<<238.0,254.0>-<243.0,278.0>-<262.5,312.5>> = 11.768288932020628

	* bmacronbelow (U+1E07): B<<240.5,301.5>-<238.0,267.0>-<238.0,254.0>>/B<<238.0,254.0>-<243.0,278.0>-<262.5,312.5>> = 11.768288932020628

	* eng (U+014B): B<<241.5,289.0>-<239.0,260.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 6.5738600242857865

	* g (U+0067): B<<378.5,197.0>-<378.0,233.0>-<378.0,260.0>>/B<<378.0,260.0>-<372.0,235.0>-<352.0,200.5>> = 13.495733280795811

	* gbreve (U+011F): B<<378.5,197.0>-<378.0,233.0>-<378.0,260.0>>/B<<378.0,260.0>-<372.0,235.0>-<352.0,200.5>> = 13.495733280795811

	* gcaron (U+01E7): B<<378.5,197.0>-<378.0,233.0>-<378.0,260.0>>/B<<378.0,260.0>-<372.0,235.0>-<352.0,200.5>> = 13.495733280795811

	* gcircumflex (U+011D): B<<378.5,197.0>-<378.0,233.0>-<378.0,260.0>>/B<<378.0,260.0>-<372.0,235.0>-<352.0,200.5>> = 13.495733280795811

	* gdotaccent (U+0121): B<<378.5,197.0>-<378.0,233.0>-<378.0,260.0>>/B<<378.0,260.0>-<372.0,235.0>-<352.0,200.5>> = 13.495733280795811

	* h (U+0068): B<<240.0,290.0>-<238.0,257.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 11.768288932020628

	* hbar (U+0127): B<<240.5,293.0>-<238.0,258.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 11.768288932020628

	* hcircumflex (U+0125): B<<240.0,290.0>-<238.0,257.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 11.768288932020628

	* hmacronbelow (U+1E96): B<<240.0,290.0>-<238.0,257.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 11.768288932020628

	* k (U+006B): B<<240.5,302.5>-<238.0,270.0>-<238.0,261.0>>/B<<238.0,261.0>-<245.0,290.0>-<265.5,325.0>> = 13.570434385161475

	* kgreenlandic (U+0138): B<<242.0,302.0>-<239.0,275.0>-<239.0,261.0>>/B<<239.0,261.0>-<246.0,290.0>-<266.5,325.0>> = 13.570434385161475

	* kmacronbelow (U+1E35): B<<240.5,302.5>-<238.0,270.0>-<238.0,261.0>>/B<<238.0,261.0>-<245.0,290.0>-<265.5,325.0>> = 13.570434385161475

	* m (U+006D): B<<243.0,299.0>-<240.0,269.0>-<239.0,249.0>>/B<<239.0,249.0>-<244.0,273.0>-<264.0,308.0>> = 8.905883705908852

	* m (U+006D): B<<578.5,289.5>-<576.0,266.0>-<574.0,250.0>>/B<<574.0,250.0>-<580.0,275.0>-<600.0,309.5>> = 6.370716931893944

	* n (U+006E): B<<242.5,299.0>-<240.0,269.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 6.057695794520992

	* nacute (U+0144): B<<242.5,299.0>-<240.0,269.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 6.057695794520992

	* ncaron (U+0148): B<<242.5,299.0>-<240.0,269.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 6.057695794520992

	* nlongrightleg (U+019E): B<<242.5,299.0>-<240.0,269.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 6.057695794520992

	* nmacronbelow (U+1E49): B<<242.5,299.0>-<240.0,269.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 6.057695794520992

	* ntilde (U+00F1): B<<242.5,299.0>-<240.0,269.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 6.057695794520992

	* p (U+0070): B<<235.5,308.0>-<233.0,278.0>-<230.0,254.0>>/B<<230.0,254.0>-<236.0,278.0>-<255.5,312.5>> = 6.911227119024609

	* q (U+0071): B<<378.0,212.5>-<380.0,247.0>-<381.0,260.0>>/B<<381.0,260.0>-<375.0,235.0>-<355.0,200.5>> = 9.097027925800269

	* r (U+0072): B<<246.5,346.5>-<243.0,313.0>-<241.0,287.0>>/B<<241.0,287.0>-<277.0,401.0>-<322.0,462.5>> = 13.126863018727317

	* racute (U+0155): B<<246.5,346.5>-<243.0,313.0>-<241.0,287.0>>/B<<241.0,287.0>-<277.0,401.0>-<322.0,462.5>> = 13.126863018727317

	* rcaron (U+0159): B<<246.5,346.5>-<243.0,313.0>-<241.0,287.0>>/B<<241.0,287.0>-<277.0,401.0>-<322.0,462.5>> = 13.126863018727317

	* rmacronbelow (U+1E5F): B<<246.5,346.5>-<243.0,313.0>-<241.0,287.0>>/B<<241.0,287.0>-<277.0,401.0>-<322.0,462.5>> = 13.126863018727317

	* rtail (U+027D): B<<252.5,408.5>-<252.0,374.0>-<248.0,334.0>>/B<<248.0,334.0>-<275.0,412.0>-<308.0,442.5>> = 13.38289886298597

	* thorn (U+00FE): B<<243.0,306.0>-<240.0,270.0>-<239.0,254.0>>/B<<239.0,254.0>-<244.0,278.0>-<263.5,312.5>> = 8.191954557023243

	* threeeighths (U+215C): B<<314.0,483.0>-<295.0,475.0>-<284.0,474.0>>/B<<284.0,474.0>-<340.0,467.0>-<370.5,436.5>> = 12.319445256636563

	* threequarters (U+00BE): B<<314.0,483.0>-<295.0,475.0>-<284.0,474.0>>/B<<284.0,474.0>-<340.0,467.0>-<370.5,436.5>> = 12.319445256636563

	* uni00B3 (U+00B3): B<<314.0,530.0>-<295.0,522.0>-<284.0,521.0>>/B<<284.0,521.0>-<340.0,514.0>-<370.5,483.5>> = 12.319445256636563

	* uni0123 (U+0123): B<<378.5,197.0>-<378.0,233.0>-<378.0,260.0>>/B<<378.0,260.0>-<372.0,235.0>-<352.0,200.5>> = 13.495733280795811

	* uni0137 (U+0137): B<<240.5,302.5>-<238.0,270.0>-<238.0,261.0>>/B<<238.0,261.0>-<245.0,290.0>-<265.5,325.0>> = 13.570434385161475

	* uni0146 (U+0146): B<<242.5,299.0>-<240.0,269.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 6.057695794520992

	* uni0157 (U+0157): B<<246.5,346.5>-<243.0,313.0>-<241.0,287.0>>/B<<241.0,287.0>-<277.0,401.0>-<322.0,462.5>> = 13.126863018727317

	* uni0180 (U+0180): B<<240.5,301.0>-<238.0,267.0>-<238.0,254.0>>/B<<238.0,254.0>-<243.0,278.0>-<262.5,312.5>> = 11.768288932020628

	* uni0183 (U+0183): B<<240.5,297.5>-<238.0,266.0>-<238.0,254.0>>/B<<238.0,254.0>-<243.0,278.0>-<262.5,312.5>> = 11.768288932020628

	* uni0199 (U+0199): B<<258.0,304.0>-<256.0,272.0>-<256.0,261.0>>/B<<256.0,261.0>-<263.0,290.0>-<283.5,325.0>> = 13.570434385161475

	* uni019C (U+019C): B<<412.5,246.0>-<415.0,273.0>-<416.0,289.0>>/B<<416.0,289.0>-<411.0,259.0>-<391.0,220.0>> = 5.885987833028254

	* uni019C (U+019C): B<<747.5,237.0>-<750.0,270.0>-<752.0,290.0>>/B<<752.0,290.0>-<747.0,260.0>-<727.0,221.0>> = 3.7517290705259434

	* uni01A5 (U+01A5): B<<251.5,307.0>-<249.0,273.0>-<247.0,254.0>>/B<<247.0,254.0>-<253.0,278.0>-<272.5,312.5>> = 8.027237510431856

	* uni01CC (U+01CC): B<<242.5,299.0>-<240.0,269.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 6.057695794520992

	* uni01E5 (U+01E5): B<<378.5,197.0>-<378.0,233.0>-<378.0,260.0>>/B<<378.0,260.0>-<372.0,235.0>-<352.0,200.5>> = 13.495733280795811

	* uni01E9 (U+01E9): B<<240.5,302.5>-<238.0,270.0>-<238.0,261.0>>/B<<238.0,261.0>-<245.0,290.0>-<265.5,325.0>> = 13.570434385161475

	* uni01F5 (U+01F5): B<<378.5,197.0>-<378.0,233.0>-<378.0,260.0>>/B<<378.0,260.0>-<372.0,235.0>-<352.0,200.5>> = 13.495733280795811

	* uni01F9 (U+01F9): B<<242.5,299.0>-<240.0,269.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 6.057695794520992

	* uni0211 (U+0211): B<<246.5,346.5>-<243.0,313.0>-<241.0,287.0>>/B<<241.0,287.0>-<277.0,401.0>-<322.0,462.5>> = 13.126863018727317

	* uni0213 (U+0213): B<<246.5,346.5>-<243.0,313.0>-<241.0,287.0>>/B<<241.0,287.0>-<277.0,401.0>-<322.0,462.5>> = 13.126863018727317

	* uni021F (U+021F): B<<240.0,290.0>-<238.0,257.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 11.768288932020628

	* uni0220 (U+0220): B<<273.0,375.0>-<270.0,334.0>-<268.0,310.0>>/B<<268.0,310.0>-<274.0,335.0>-<296.5,369.5>> = 8.732091590069578

	* uni024A (U+024A): L<<466.0,158.0>--<484.0,493.0>>/B<<484.0,493.0>-<451.0,380.0>-<406.5,293.0>> = 13.204051561051253

	* uni024D (U+024D): B<<246.5,346.5>-<243.0,313.0>-<241.0,287.0>>/B<<241.0,287.0>-<277.0,401.0>-<322.0,462.5>> = 13.126863018727317

	* uni024F (U+024F): B<<415.5,204.0>-<415.0,237.0>-<414.0,260.0>>/B<<414.0,260.0>-<409.0,235.0>-<388.5,200.5>> = 13.799485396019362

	* uni0253 (U+0253): B<<240.5,302.5>-<238.0,268.0>-<238.0,254.0>>/B<<238.0,254.0>-<243.0,278.0>-<262.5,312.5>> = 11.768288932020628

	* uni0260 (U+0260): B<<402.5,197.0>-<402.0,233.0>-<402.0,260.0>>/B<<402.0,260.0>-<396.0,235.0>-<376.0,200.5>> = 13.495733280795811

	* uni0261 (U+0261): B<<378.5,197.0>-<378.0,233.0>-<378.0,260.0>>/B<<378.0,260.0>-<372.0,235.0>-<352.0,200.5>> = 13.495733280795811

	* uni0266 (U+0266): B<<239.5,282.0>-<238.0,256.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 11.768288932020628

	* uni026F (U+026F): B<<426.5,234.5>-<429.0,258.0>-<430.0,274.0>>/B<<430.0,274.0>-<425.0,249.0>-<405.0,214.5>> = 7.733598099022774

	* uni026F (U+026F): B<<761.5,225.0>-<764.0,255.0>-<766.0,275.0>>/B<<766.0,275.0>-<761.0,251.0>-<741.0,216.0>> = 6.057695794520992

	* uni0271 (U+0271): B<<243.0,299.0>-<240.0,269.0>-<239.0,249.0>>/B<<239.0,249.0>-<244.0,273.0>-<264.0,308.0>> = 8.905883705908852

	* uni0271 (U+0271): B<<578.5,289.5>-<576.0,266.0>-<574.0,250.0>>/B<<574.0,250.0>-<580.0,275.0>-<600.0,309.5>> = 6.370716931893944

	* uni0272 (U+0272): B<<254.0,299.0>-<251.0,269.0>-<249.0,249.0>>/B<<249.0,249.0>-<254.0,273.0>-<274.0,308.0>> = 6.057695794520992

	* uni0289 (U+0289): B<<408.5,203.0>-<410.0,230.0>-<412.0,249.0>>/B<<412.0,249.0>-<404.0,225.0>-<383.5,191.5>> = 12.425942865427455

	* uni0440 (U+0440): B<<235.5,308.0>-<233.0,278.0>-<230.0,254.0>>/B<<230.0,254.0>-<236.0,278.0>-<255.5,312.5>> = 6.911227119024609

	* uni1D43 (U+1D43): B<<364.5,387.0>-<367.0,409.0>-<372.0,422.0>>/B<<372.0,422.0>-<352.0,389.0>-<321.5,348.5>> = 10.18089173892452

	* uni1D58 (U+1D58): B<<323.5,381.0>-<325.0,409.0>-<326.0,429.0>>/B<<326.0,429.0>-<319.0,406.0>-<301.5,374.5>> = 14.06510783803526

	* uni1D7D (U+1D7D): B<<252.5,308.0>-<250.0,278.0>-<247.0,254.0>>/B<<247.0,254.0>-<253.0,278.0>-<272.5,312.5>> = 6.911227119024609

	* uni1D91 (U+1D91): B<<374.5,203.5>-<377.0,238.0>-<378.0,249.0>>/B<<378.0,249.0>-<370.0,225.0>-<349.5,191.5>> = 13.240519915187184

	* uni1DB6 (U+1DB6): B<<330.5,379.5>-<332.0,408.0>-<333.0,429.0>>/B<<333.0,429.0>-<326.0,405.0>-<308.5,373.0>> = 13.53389371440569

	* uni1E03 (U+1E03): B<<240.5,301.5>-<238.0,267.0>-<238.0,254.0>>/B<<238.0,254.0>-<243.0,278.0>-<262.5,312.5>> = 11.768288932020628

	* uni1E05 (U+1E05): B<<240.5,301.5>-<238.0,267.0>-<238.0,254.0>>/B<<238.0,254.0>-<243.0,278.0>-<262.5,312.5>> = 11.768288932020628

	* uni1E21 (U+1E21): B<<378.5,197.0>-<378.0,233.0>-<378.0,260.0>>/B<<378.0,260.0>-<372.0,235.0>-<352.0,200.5>> = 13.495733280795811

	* uni1E23 (U+1E23): B<<240.0,290.0>-<238.0,257.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 11.768288932020628

	* uni1E25 (U+1E25): B<<240.0,290.0>-<238.0,257.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 11.768288932020628

	* uni1E27 (U+1E27): B<<240.0,290.0>-<238.0,257.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 11.768288932020628

	* uni1E29 (U+1E29): B<<240.0,290.0>-<238.0,257.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 11.768288932020628

	* uni1E2B (U+1E2B): B<<240.0,290.0>-<238.0,257.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 11.768288932020628

	* uni1E31 (U+1E31): B<<240.5,302.5>-<238.0,270.0>-<238.0,261.0>>/B<<238.0,261.0>-<245.0,290.0>-<265.5,325.0>> = 13.570434385161475

	* uni1E33 (U+1E33): B<<240.5,302.5>-<238.0,270.0>-<238.0,261.0>>/B<<238.0,261.0>-<245.0,290.0>-<265.5,325.0>> = 13.570434385161475

	* uni1E3F (U+1E3F): B<<243.0,299.0>-<240.0,269.0>-<239.0,249.0>>/B<<239.0,249.0>-<244.0,273.0>-<264.0,308.0>> = 8.905883705908852

	* uni1E3F (U+1E3F): B<<578.5,289.5>-<576.0,266.0>-<574.0,250.0>>/B<<574.0,250.0>-<580.0,275.0>-<600.0,309.5>> = 6.370716931893944

	* uni1E41 (U+1E41): B<<243.0,299.0>-<240.0,269.0>-<239.0,249.0>>/B<<239.0,249.0>-<244.0,273.0>-<264.0,308.0>> = 8.905883705908852

	* uni1E41 (U+1E41): B<<578.5,289.5>-<576.0,266.0>-<574.0,250.0>>/B<<574.0,250.0>-<580.0,275.0>-<600.0,309.5>> = 6.370716931893944

	* uni1E43 (U+1E43): B<<243.0,299.0>-<240.0,269.0>-<239.0,249.0>>/B<<239.0,249.0>-<244.0,273.0>-<264.0,308.0>> = 8.905883705908852

	* uni1E43 (U+1E43): B<<578.5,289.5>-<576.0,266.0>-<574.0,250.0>>/B<<574.0,250.0>-<580.0,275.0>-<600.0,309.5>> = 6.370716931893944

	* uni1E45 (U+1E45): B<<242.5,299.0>-<240.0,269.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 6.057695794520992

	* uni1E47 (U+1E47): B<<242.5,299.0>-<240.0,269.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 6.057695794520992

	* uni1E4B (U+1E4B): B<<242.5,299.0>-<240.0,269.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 6.057695794520992

	* uni1E55 (U+1E55): B<<235.5,308.0>-<233.0,278.0>-<230.0,254.0>>/B<<230.0,254.0>-<236.0,278.0>-<255.5,312.5>> = 6.911227119024609

	* uni1E57 (U+1E57): B<<235.5,308.0>-<233.0,278.0>-<230.0,254.0>>/B<<230.0,254.0>-<236.0,278.0>-<255.5,312.5>> = 6.911227119024609

	* uni1E59 (U+1E59): B<<246.5,346.5>-<243.0,313.0>-<241.0,287.0>>/B<<241.0,287.0>-<277.0,401.0>-<322.0,462.5>> = 13.126863018727317

	* uni1E5B (U+1E5B): B<<246.5,346.5>-<243.0,313.0>-<241.0,287.0>>/B<<241.0,287.0>-<277.0,401.0>-<322.0,462.5>> = 13.126863018727317

	* uni1E5D (U+1E5D): B<<246.5,346.5>-<243.0,313.0>-<241.0,287.0>>/B<<241.0,287.0>-<277.0,401.0>-<322.0,462.5>> = 13.126863018727317

	* uni207F (U+207F): B<<237.5,445.5>-<235.0,422.0>-<233.0,407.0>>/B<<233.0,407.0>-<240.0,425.0>-<259.0,452.5>> = 13.655862138541766

	* uni2083 (U+2083): B<<314.0,120.0>-<295.0,112.0>-<284.0,111.0>>/B<<284.0,111.0>-<340.0,104.0>-<370.5,73.5>> = 12.319445256636563

	* uni2153 (U+2153): B<<633.0,270.0>-<614.0,262.0>-<603.0,261.0>>/B<<603.0,261.0>-<659.0,254.0>-<689.5,223.5>> = 12.319445256636563

	* uni2154 (U+2154): B<<719.0,270.0>-<700.0,262.0>-<689.0,261.0>>/B<<689.0,261.0>-<745.0,254.0>-<775.5,223.5>> = 12.319445256636563

	* uniA727 (U+A727): B<<240.0,290.0>-<238.0,257.0>-<238.0,249.0>>/B<<238.0,249.0>-<243.0,273.0>-<263.0,308.0>> = 11.768288932020628 

	* uniA741 (U+A741): B<<240.5,302.0>-<238.0,270.0>-<238.0,261.0>>/B<<238.0,261.0>-<245.0,290.0>-<265.5,325.0>> = 13.570434385161475 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* product (U+220F): L<<457.0,525.0>--<335.0,526.0>> 

	* x_x (U+E03F): L<<-93.0,-4.0>--<-92.0,160.0>> [code: found-semi-vertical]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 8 | 97 | 938 | 49 | 757 | 0 |
| 0% | 0% | 5% | 51% | 3% | 41% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**