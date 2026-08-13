import streamlit as st
from document_process import DocumentProcess

st.set_page_config(
    page_title="Text Similarity App",
    layout="wide"
)

# =====================================================
# 1/3 LEFT + 2/3 RIGHT
# =====================================================

left, right = st.columns([1, 2])

# =====================================================
# LEFT SIDE - SETTINGS
# =====================================================

with left:

    st.header("⚙️ Settings")

    # -----------------------------
    # Embedding Method
    # -----------------------------

    st.subheader("🔤 Embedding Method")

    embedding_method = st.selectbox(
        "Select Embedding Method",
        [
            "CountVectorizer",
            "TF-IDF",
            "Word2Vec",
            "SentenceTransformer",
            "OpenAI"
        ]
    )

    st.write("Selected:", embedding_method)

    # ========================================================
    # OPENAI API KEY
    # ========================================================

    openai_api_key = None

    if embedding_method == "OpenAI":

        openai_api_key = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="sk-..."
        )

    # -----------------------------
    # Similarity Metric
    # -----------------------------

    st.subheader("📐 Similarity Metric")

    similarity_metric = st.selectbox(
        "Select Similarity Metric",
        [
            "Cosine Similarity",
            "Euclidean Distance"
        ]
    )

    st.write("Selected:", similarity_metric)
     # -----------------------------------------
    # TOP MATCHING RESULTS
    # -----------------------------------------

    st.subheader("🏆 Top Matching Results")

    top_k = st.slider(
        "Number of Results",
        min_value=1,
        max_value=10,
        value=5,
        step=1
    )

    st.write(f"Selected: **Top {top_k}**")



# =========================================================
# RIGHT SIDE
# =========================================================

with right:

    st.header("🔎 Ask a Question")

    # Question text box
    question = st.text_input(
        "Enter your question",
        placeholder="Example: What is machine learning?"
    )

    # Search button
    search = st.button(
        "🔍 Search",
        use_container_width=True
    )




# =====================================================
# SEARCH ENGINE
# =====================================================

    if search:
       



        # =================================================
        # OPENAI EMBEDDING
        # =================================================

        if embedding_method == "OpenAI":

            # ---------------------------------------------
            # CHECK API KEY
            # ---------------------------------------------

            if not openai_api_key:

                st.error(
                    "Please enter your OpenAI API key."
                )

                st.stop()


            # ---------------------------------------------
            # DOCUMENT PROCESS
            # ---------------------------------------------

            similarity_Score, model_generated_ans = (DocumentProcess(similarity_metric=similarity_metric, embedding_method=embedding_method, top_k=top_k, question=question, openai_api_key=openai_api_key).process())


        # =================================================
        # OTHER EMBEDDING METHODS
        # =================================================

        else:

            similarity_Score, model_generated_ans = (
                DocumentProcess(

                    similarity_metric=similarity_metric,

                    embedding_method=embedding_method,

                    top_k=top_k,

                    question=question, openai_api_key =None

                ).process()
            )


        # =================================================
        # ANSWER
        # =================================================

        st.subheader("Answer")


        # =================================================
        # SIMILARITY SCORE
        # =================================================

        st.write(
            "Similarity / Distance Score:"
        )

        st.write(
            similarity_Score
        )


        # =================================================
        # MODEL ANSWER
        # =================================================

        st.write(
            model_generated_ans
        )