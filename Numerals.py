import streamlit as st
import akrophonobolos as obol


st.markdown("""
# Greek Akrophonic Numerals Demo

Demo of [akrophonobolos](https://github.com/seanredmond/Akrophonobolos) package for Python. akrophonobolos lets you parse, manipulate, and do math with [Attic acrophonic numerals](https://en.wikipedia.org/wiki/Attic_numerals)
""")

with st.expander("See explanation"):
    st.markdown(r"""

Athenian monetary denominations were the τάλαντον (_talanton_, or “talent”), δραχμή (_drakhmē_, or “drachma”) and ὀβολός (_obolos_, or “obol”). There were 6 obols in a drachma, which was a good day’s wage, and 6,000 drachmas in a talent, which was about 56 pounds of silver. Complete monetary values were usually a mix of these denominations. For instance, 1½ talents is 1 talent 3000 drachmas, written ΤΧΧΧ.

In Athens, special symbols were used based the first letters of the words for “five” (𐅃 from πέντε, _pente_), “ten” (Δ from δέκα, _deka_), “hundred” (Η from an old spelling for ἑκατόν, _hekaton_), and “thousand” (Χ from χιλιάς, _khilias_). “Fifty” is formed by inscribing a small Δ inside the 𐅃 indicating $ 10 \times 5 $; “five hundred” by inscribing a small Η meaning $ 100 \times 5 $. 

Single denominations are: Ι for one obol, 𐅂 for one drachma, and Τ for one talent. For numbers 5 and up, a small inscribed Τ means talents are indicated, otherwise it is drachmas. This Τ can be combined with the Δ for ten or Η for hundred, so that 𐅌 is the combination of 𐅃 + Η + Τ to mean “Five hundred talents.”

There is no special symbol for 5 obols so this is simply written ΙΙΙΙΙ. Obols come in ½- and ¼-obol denominations as well.
""")

st.markdown("""
## Conversion

### Abbreviations-to-Greek

Enter numbers followed “t” for talents, “d” from drachmas, and “b” for obols, for example “987t 654d 3.25b”. You can use upper-case or lower-case, and “o” for obols as well (though this might look too much like a zero). Press enter to have this converted to Greek.
""")



st.text_input("Abbreviation", key="akrostring")

if st.session_state.akrostring:
    st.write("“" + obol.Khremata(st.session_state.akrostring).as_phrase() + "” in Greek: " + obol.Khremata(st.session_state.akrostring).as_greek())
else:
    st.write("")

st.markdown("""
### Interpret Greek

Enter a Greek numeral to see it interpreted. You can try the examples below.
""")

st.text_input("Your name", key="akronumeral")

if st.session_state.akronumeral:
    st.write(st.session_state.akronumeral + " means: “" + obol.Khremata(st.session_state.akronumeral).as_phrase() +"”")
else:
    st.write("")


st.markdown("""
## Examples

Some numbers from [IG I³ 369](https://epigraphy.packhum.org/text/381) ([translation](https://www.atticinscriptions.com/inscription/IGI3/369)) you can copy and paste for interpreting.

- ΧΧΧΧ𐅅Η𐅄Δ𐅃ΙΙΙΙΙ (l. 29)
- 𐅊𐅈ΤΤΤΤΧΧΧΧ𐅅ΗΗΔΔ (39)
- ΧΗΗΗ𐅄ΔΔΔΔ𐅃𐅂ΙΙΙΙ (72)

""")


st.markdown("""

## Symbols

1 talent = 6000 drakhmas = about 56 lbs of silver

1 drakhma = 6 obols

|       | Talents | Drachmas | Obols |
| ----: | :-----: | :------: | ----- |
| 5,000 | 𐅎       | 𐅆        |       |
| 1,000 | 𐅍       | Χ        |       |
| 500   | 𐅌       | 𐅅        |  |
| 100   | 𐅋       | Η        |  |
| 50    | 𐅊       | 𐅄        |  |
| 10    | 𐅉       | Δ        |  |
| 5     | 𐅈       | 𐅃        | |
| 1     | Τ       | 𐅂        | Ι |
| ½     |         |          | 𐅁 |
| ¼     |         |          | 𐅀 |
""")

