import streamlit as st
from utils.reviewer import review_code


st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="💻"
)


st.title("💻 AI Code Reviewer")

st.write(
    "Review your code using Gemini AI"
)


language = st.selectbox(
    "Choose Language",
    [
        "Java",
        "Python",
        "C++",
        "C",
        "JavaScript"
    ]
)


uploaded_file = st.file_uploader(
    "Upload Code File",
    type=[
        "java",
        "py",
        "cpp",
        "c",
        "js"
    ]
)


if uploaded_file:

    code = uploaded_file.read().decode("utf-8")

else:

    code = st.text_area(
        "Paste Your Code",
        height=300
    )


if st.button("Review Code"):

    if code == "":

        st.warning(
            "Please enter code"
        )

    else:

        with st.spinner(
            "AI is reviewing..."
        ):

            response = review_code(
                language,
                code
            )


        st.success(
            "Review Completed"
        )


        parts = response.split("###")


        for part in parts:

            if part.strip():

                title, text = part.split(
                    "\n",
                    1
                )


                with st.expander(title):

                    if "Optimized Code" in title:

                        st.code(
                            text,
                            language=language.lower()
                        )

                    else:

                        st.write(text)


        st.subheader(
            "Original Code"
        )

        st.code(
            code,
            language=language.lower()
        )