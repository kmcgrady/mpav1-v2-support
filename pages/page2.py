import streamlit as st

# Note the sidebar is requested to be hidden, so we populate the sidebar
# with page links instead.
with st.sidebar:
  st.page_link("app.py")
  st.page_link("pages/page1.py")
  st.page_link("pages/page2.py")
  st.page_link("pages/page3.py")
  st.page_link("pages/page4_no_sidebar.py")
  st.write("Some content for Page 2")

st.write("# Page 2")
