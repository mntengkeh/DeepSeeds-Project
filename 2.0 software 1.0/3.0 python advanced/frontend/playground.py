import streamlit as st

# pressed = st.button("Click me")
# if pressed:
#     st.write("I have been clicked")

import time

progress = st.progress(0)

for i in range (100):
    time.sleep(0.02) # simulate computation
    progress.progress(i + 1)

st.success("Generation complete!")