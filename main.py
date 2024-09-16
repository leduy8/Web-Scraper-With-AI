import streamlit as st

st.title("AI Web Scraper")
url = st.text_input("Enter the website URL")

if st.button("Scrape Site"):
    if url:
        st.write("Scraping the website...")
        # Add your scraping logic here
        st.write("Scraping complete!")
    else:
        st.error("Please enter a valid URL")
