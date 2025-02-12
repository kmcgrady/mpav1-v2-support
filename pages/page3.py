import streamlit as st

# Note the sidebar is requested to be hidden, so we populate the sidebar
# with page links instead.
with st.sidebar:
  st.page_link("app.py")
  st.write("Some content for Page 3")

st.write("# Page 3")
