
import streamlit as st
from utils.reviewer import review_code

st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="💻",
    layout="wide"
)


# Load custom CSS
def load_css():
    with open("style.css", "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


load_css()


# Hero section
st.markdown("""
<div class="hero">
    <div class="hero-tag">✦ INTELLIGENT CODE ANALYSIS</div>
    <h1>Code <span>Refined.</span></h1>
    <p>
        Your AI-powered programming companion.
        Detect issues, improve quality, and write cleaner code.
    </p>
</div>
""", unsafe_allow_html=True)


# Configuration
st.markdown("""
<div class="section-heading">
    <span>01 / CONFIGURATION</span>
    <h3>Start your code review</h3>
</div>
""", unsafe_allow_html=True)


col1, col2 = st.columns([1, 2])

with col1:

    st.markdown(
        '<div class="field-label">PROGRAMMING LANGUAGE</div>',
        unsafe_allow_html=True
    )

    language = st.selectbox(
        "Choose Language",
        ["Java", "Python", "C++", "C", "JavaScript"],
        label_visibility="collapsed"
    )


with col2:

    st.markdown("""
    <div class="field-label">REVIEW ENGINE</div>
    <div class="engine-card">
        <span class="engine-dot"></span>
        Gemini AI
        <span class="engine-status">READY</span>
    </div>
    """, unsafe_allow_html=True)


# Source code section
st.markdown("""
<div class="section-heading">
    <span>02 / SOURCE CODE</span>
    <h3>Provide your code</h3>
</div>
""", unsafe_allow_html=True)


upload_col, info_col = st.columns([1.5, 1])

with upload_col:

    uploaded_file = st.file_uploader(
        "Upload source file",
        type=["java", "py", "cpp", "c", "js"],
        help="Supported formats: JAVA, PY, CPP, C, JS"
    )


with info_col:

    st.markdown("""
    <div class="upload-info">
        <div class="info-symbol">⌘</div>
        <b>Quick tip</b>
        <p>
            Upload your source file or paste your code
            directly into the editor.
        </p>
        <div class="supported-formats">
            JAVA &nbsp; PY &nbsp; CPP &nbsp; C &nbsp; JS
        </div>
    </div>
    """, unsafe_allow_html=True)


# Read uploaded code or accept pasted code
if uploaded_file:

    code = uploaded_file.read().decode("utf-8")

    st.success(f"Loaded: {uploaded_file.name}")

else:

    code = st.text_area(
        "Paste Your Code",
        height=320,
        placeholder="// Paste your code here...",
        label_visibility="collapsed"
    )


# Editor information
line_count = len(code.splitlines()) if code else 0

st.markdown(f"""
<div class="editor-footer">
    <span>● EDITOR READY</span>
    <span>{line_count} LINES</span>
    <span>{language.upper()}</span>
</div>
""", unsafe_allow_html=True)


# Review button
st.markdown("<br>", unsafe_allow_html=True)

review_clicked = st.button(
    "✦  ANALYZE MY CODE",
    use_container_width=True
)


if review_clicked:

    if not code.strip():

        st.warning("Please enter or upload your code first.")

    else:

        with st.spinner("Analyzing your code with Gemini AI..."):

            response = review_code(
                language,
                code
            )


        st.success("Review completed successfully!")


        # Analysis report
        st.markdown("""
        <div class="section-heading">
            <span>03 / ANALYSIS REPORT</span>
            <h3>Your code review results</h3>
        </div>
        """, unsafe_allow_html=True)


        parts = response.split("###")

        for part in parts:

            if part.strip():

                section = part.strip()

                if "\n" in section:
                    title, text = section.split("\n", 1)
                else:
                    title = section
                    text = ""

                with st.expander(title.strip(), expanded=True):

                    if "Optimized Code" in title:

                        st.code(
                            text,
                            language=language.lower()
                        )

                    else:

                        st.write(text)


        # Original source
        st.markdown("""
        <div class="section-heading">
            <span>04 / SOURCE REFERENCE</span>
            <h3>Original submission</h3>
        </div>
        """, unsafe_allow_html=True)


        st.code(
            code,
            language=language.lower()
        )


# Footer
st.markdown("""
<div class="footer">
    BUILT FOR DEVELOPERS &nbsp;·&nbsp; POWERED BY GEMINI AI
</div>
""", unsafe_allow_html=True)
