import streamlit as st
st.title("Weather Forcast for the Next Days")
place = st.text_input(label="Place")
days = st.slider("Forcast days", min_value=1, max_value=5,
                 help="select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "sky"))
st.subheader(f"{option} for the next {days} days in {place}")
