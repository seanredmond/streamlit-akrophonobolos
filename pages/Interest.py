import streamlit as st
import akrophonobolos as obol

def calc_days(p, i, r):
    p_o = obol.Khremata(p)
    i_o = obol.Khremata(i)
    days = (i_o / rate) / p_o

    return f"{i_o.as_abbr()} interest on {p_o.as_abbr()} principal at the rate {r} indicates a term of {days} days"



def calc_interest(p, d, r):
    p_o = obol.Khremata(p)
    interest = p_o * d * r

    return(f"A principal of {p_o.as_abbr()} for {d} days at the rate {r} yields {interest.as_abbr()} ({interest.as_greek()}) interest")


def calc_principal(i, d, r):
    p_i = obol.Khremata(i)
    principal = (p_i / rate) / d
    
    return(f"{p_i.as_abbr()} interest for {d} days at the rate {r} indicates a principal of {principal.as_abbr()} ({principal.as_greek()})")


def only(a, b, c):
    return a and not (b or c)


def both(a, b, c):
    return bool((a and b) and not c)



def do_calc(p, i, d, r):
    if not any((p, i, d)):
        return ""
    
    if only(p, i, d):
        p_o = obol.Khremata(p)
        return f"Principal: {p_o.as_abbr()} ({p_o.as_greek()})"

    if only(i, p, d):
        p_i = obol.Khremata(i)
        return f"Interest: {p_i.as_abbr()} ({p_i.as_greek()})"

    if only (d, i, p):
        return f"Term: {d} day{'' if d == 1 else 's'}"

    if both(p, i, d):
        return calc_days(p, i, r)

    if both(p, d, i):
        return calc_interest(p, d, r)

    if both(d, i, p):
        return calc_principal(i, d, r)

    return ""





st.markdown("# Calculating Interest")

st.markdown("## Interest Rate")

with st.expander("About the interest rate"):
    st.markdown(r"""
Athenians used simple interest, so the interest amount was simply calculated as the principal times the interest rate times the number or days of the loan. We usually talk about this as am amount of interest per amount of principal per number of days.

The most famous financial inscription, [IG I³ 369](https://epigraphy.packhum.org/text/381) ([translation](https://www.atticinscriptions.com/inscription/IGI3/369)) , or the “Logistai Inscription” uses a rate of 1 drachma per 5 talents per day which you could also state as 1 drachma per 5 talents per 5 days. Either way, if you put those values into the form below you will get a rate of $ \frac{1}{30000} $  per day.
""")


st.text_input("Principal", key="rate_p", value="5t")
st.text_input("Interest", key="rate_i", value="1d")
st.number_input("Days", key="rate_d", value=1, min_value=1)

rate = (obol.Khremata(st.session_state.rate_i)/obol.Khremata(st.session_state.rate_p))/st.session_state.rate_d

st.write(rate)


st.markdown("""
## Calculate Interest, Principal, or Term

Enter any two values below to calculate the third at the above rate
""")

with st.expander("Athenian financial calculations"):
    st.markdown(r"""
Line seven of [IG I³ 369](https://epigraphy.packhum.org/text/381) ([translation](https://www.atticinscriptions.com/inscription/IGI3/369)) records a loan and interest in this way: 𐅊· τόκος τούτον ΤΤΧ𐅅ΗΗΗΗ𐅄ΔΔ, which means “50 talents, interest on this 2 talents, 1970 drachmas.” Knowing the interest rate was 1 drachma per 5 talents per 1 day you can determine, using the form below, that the money was loaned for 1,397 days (put “50t” or 𐅊 in for the principal, “2t 1970d” or ΤΤΧ𐅅ΗΗΗΗ𐅄ΔΔ for the interest, and leave the term blank or 0). A few lines later (l. 12) another loan of 100t generated 3t 5940d interest and from these amounts we can verify that loan lasted 1,197 days. 

The very first loan in the inscription was for 20T, but the first few letters of the interest are lost, so we only have [......]ΔΔ𐅃𐅂 (the brackets and dots indicate 6 missing letters). But since we have the date we know that it was 27 days before the 50t loan, above, or 1,424 days. If you put 30t principal in the form below with 1424 days for the term (and nothing for the interest), you can check that the interest should be 5696d or 𐅆𐅅Η𐅄ΔΔΔΔ𐅃𐅂 which exactly fills out the missing space.

The math doesn't always work out so well, so the challenges of IG I³ 369 are filling in the missing amounts, figuring out where the mistakes are, and seeing if there is any explanation that allows us to correct the mistakes.
""")



st.text_input("Principal", key="p")
st.text_input("Interest", key="i")
st.number_input("Term (days)", key="d", value=0)

st.write(do_calc(st.session_state.p, st.session_state.i, st.session_state.d, rate))



