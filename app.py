import streamlit as st
from search import semantic_search
from llm import summarize

# Page Config
st.set_page_config(page_title="Customer Intelligence RAG", layout="centered")

st.title("Customer Intelligence RAG 🤖")
st.write("Ask questions about customer feedback, complaints, and sentiments.")

# Input
query = st.text_input("Enter your question:", placeholder="e.g., What are the common complaints?")

if st.button("Search"):
    if not query or len(query.split()) < 3:
        st.warning("Please enter a more descriptive question (at least 3 words).")
    else:
        with st.spinner("Searching and analyzing..."):
            try:
                # 1. Retrieve context
                context = semantic_search(query)
                
                # 2. Generate answer
                answer = summarize(context, query)
                
                # 3. Display Result
                st.success("Analysis Complete")
                st.markdown("### Answer")
                st.write(answer)
                
                # 4. Show Source Documents (Optional but helpful)
                with st.expander("View Source Documents"):
                    for i, doc in enumerate(context):
                        st.markdown(f"**Source {i+1}:**")
                        st.info(doc)
                        
            except Exception as e:
                st.error(f"An error occurred: {e}")
