import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import os
from datetime import datetime, timezone, timedelta

title = os.getenv('ENVIRONMENT')
st.write(f"# この環境は {title}")

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

if st.button("Click here!"):
    jst = timezone(timedelta(hours=9))  # Japan Standard Time (UTC+9)
    today = datetime.now(jst)
    weekday = today.strftime('%A')  # Get the weekday name
    
    if weekday == "Monday":
        st.info("💪 Today is Monday: A fresh start! Let's tackle this week with energy!")
    elif weekday == "Tuesday":
        st.info("🚀 Today is Tuesday: Keep going! You're doing great!")
    elif weekday == "Wednesday":
        st.info("🐪 Today is Wednesday: You're halfway there! Stay strong!")
    elif weekday == "Thursday":
        st.info("🌟 Today is Thursday: Almost there! The weekend is in sight!")
    elif weekday == "Friday":
        st.info("🎉 Today is Friday: You made it! Finish strong and enjoy the weekend!")
    elif weekday == "Saturday":
        st.info("🌈 Today is Saturday: Take time to recharge and enjoy your day!")
    else:  # Sunday
        st.info("☀️ Today is Sunday: Rest well and prepare for a fantastic week ahead!")

num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
