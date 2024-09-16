import streamlit as st
from scrape import (
    scrape_website_locally,
    clean_body_content,
    split_dom_content,
    extract_body_content
)
from parse import parse_with_ollama

st.title("Web Scraper with AI")

st.session_state.dom_content = None

url = st.text_input("Enter the website URL")

if st.button("Scrape Site Locally"):
    if url:
        st.write("Scraping the website...")
        result = scrape_website_locally(url)
        body_content = extract_body_content(result)
        cleaned_content = clean_body_content(body_content)
        st.session_state.dom_content = cleaned_content
        with st.expander("View DOM Content"):
            st.text_area("DOM Content", cleaned_content, height=300)
        st.write("Scraping complete!")
    else:
        st.error("Please enter a valid URL")

if st.button("Scrape Site Remotely"):
    st.error("Not implemented yet")

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse from the DOM")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)
        else:
            st.error("Please enter a description of what you want to parse")
