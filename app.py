import streamlit as st

# Note the sidebar is requested to be hidden, so we populate the sidebar
# with page links instead.
with st.sidebar:
  st.page_link("app.py")
  st.page_link("pages/page1.py")
  st.page_link("pages/page2.py")
  st.page_link("pages/page3.py")
  st.page_link("pages/page4_no_sidebar.py")
  st.write("Some content")

st.write("## Repro Steps")
st.write("Switch between pages in the sidebar (ignoring page 4)")
st.write("## Expected Result")
st.write("The sidebar should not flicker between pages")
st.write("## Actual Result")
st.write("The sidebar flickers between pages")

st.caption("You can switch to page4 and notice it disappears the sidebar disappears intentionally")
