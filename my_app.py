try:
    import streamlit as st
except ImportError:
    import sys
    print("Streamlit is not installed. Install it with 'pip install streamlit'.")
    sys.exit(1)

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")