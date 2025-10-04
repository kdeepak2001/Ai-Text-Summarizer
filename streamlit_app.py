"""
Text Summarizer - Streamlit Web UI
Interactive interface for the CLI text summarizer
"""

import streamlit as st
from app import extractive_summarize, fetch_url_text

# Page configuration
st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📝",
    layout="centered"
)

# Title and description
st.title("📝 AI Text Summarizer")
st.markdown("Extract the most important sentences from any text using extractive summarization.")
st.markdown("---")

# Sidebar for options
st.sidebar.header("⚙️ Settings")
num_sentences = st.sidebar.slider("Number of sentences", 1, 10, 3, help="How many sentences to extract")
st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.info("This app uses word frequency scoring to identify key sentences. No API required!")

# Input method selection
input_method = st.radio("Choose input method:", ["📄 Text Input", "🌐 URL"], horizontal=True)

text_input = ""

if input_method == "📄 Text Input":
    text_input = st.text_area(
        "Enter or paste your text:",
        height=250,
        placeholder="Paste your article, essay, or any long text here...\n\nExample: Artificial intelligence is transforming industries worldwide. Machine learning enables computers to learn from data..."
    )
    
elif input_method == "🌐 URL":
    url_input = st.text_input(
        "Enter article URL:",
        placeholder="https://example.com/article"
    )
    
    if url_input:
        with st.spinner("🔍 Fetching content from URL..."):
            try:
                text_input = fetch_url_text(url_input)
                st.success(f"✅ Successfully fetched {len(text_input)} characters")
                with st.expander("👁️ Preview fetched text"):
                    st.text(text_input[:500] + "..." if len(text_input) > 500 else text_input)
            except Exception as e:
                st.error(f"❌ Error fetching URL: {str(e)}")
                st.info("💡 Tip: Some websites block automated requests. Try copy-pasting the text instead.")

# Summarize button
st.markdown("---")
if st.button("✨ Generate Summary", type="primary", use_container_width=True):
    if not text_input or len(text_input.strip()) < 50:
        st.warning("⚠️ Please enter at least 50 characters of text to summarize.")
    else:
        with st.spinner("🤖 Analyzing text and extracting key sentences..."):
            try:
                summary = extractive_summarize(text_input, num_sentences)
                
                st.success("✅ Summary generated successfully!")
                st.markdown("---")
                
                # Display summary
                st.subheader("📋 Summary")
                for i, sentence in enumerate(summary, 1):
                    st.markdown(f"**{i}.** {sentence}")
                
                st.markdown("---")
                
                # Statistics
                st.subheader("📊 Statistics")
                col1, col2, col3 = st.columns(3)
                
                original_words = len(text_input.split())
                summary_text = " ".join(summary)
                summary_words = len(summary_text.split())
                reduction = round((1 - summary_words / original_words) * 100, 1) if original_words > 0 else 0
                
                with col1:
                    st.metric("Original Length", f"{original_words} words")
                with col2:
                    st.metric("Summary Length", f"{summary_words} words")
                with col3:
                    st.metric("Reduction", f"{reduction}%", delta=f"-{reduction}%")
                
                # Copy to clipboard helper
                st.markdown("---")
                st.text_area("📋 Copy summary:", value=summary_text, height=100)
                
            except Exception as e:
                st.error(f"❌ Error generating summary: {str(e)}")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
        <p>Built with ❤️ using Python & Streamlit | 
        <a href='https://github.com/kdeepak2001/Ai-Text-Summarizer' target='_blank'>View on GitHub</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
