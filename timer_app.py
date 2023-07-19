import time as t
import streamlit as st
from datetime import time


def convert(value):
    m,s,ms=value.split(":")
    minutes=int(m)
    milli=int(ms)
    seconds=int(s)
    return minutes,seconds,milli

def showatend():
    st.warning("TIME'S UP!")
    st.image("timesup.png", width=500)




st.markdown("<span style='font-size: 75px; font-family: Lucida Console, Courier New, monospace;'> Timer App</span>", unsafe_allow_html=True)
st.markdown("<span style='font-size: 30px; font-family: Lucida Console, Courier New, monospace;'> Please specify the time you want to put in the timer:</span>", unsafe_allow_html=True)
val=st.time_input("", value=time(0,0,0))
if str(val)=="00:00:00":
    st.markdown("<span style='font-size: 20px; font-family: Lucida Console, Courier New, monospace;'> Please enter time ^</span>", unsafe_allow_html=True)
else:
    minutes,seconds,milliseconds=convert(str(val))
    ans=minutes*60+seconds+(milliseconds/1000)
    bar=st.progress(0)
    fin_ans=ans/100;
    for i in range(100):
        bar.progress((i+1))
        t.sleep(fin_ans)
    
    showatend()
    

      
