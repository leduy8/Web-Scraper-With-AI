import streamlit as st
from scrape import scrape_website

st.title("AI Web Scraper")
url = st.text_input("Enter the website URL")

if st.button("Scrape Site"):
    if url:
        st.write("Scraping the website...")
        # Add your scraping logic here
        result = scrape_website(url)
        print(result)
        st.write(result)
        st.write("Scraping complete!")
    else:
        st.error("Please enter a valid URL")
