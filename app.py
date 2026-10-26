
import streamlit as st
from document_reader import extract_pdf_text, validate_pdf
from comparison import compare_documents
from report_generator import create_docx_report

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="MADHU | AI Document Comparison Assistant",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# PROFESSIONAL DESIGN / CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background: linear-gradient(135deg, #f5f7ff 0%, #f8f6ff 55%, #f0f7ff 100%);
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 1250px;
    padding-top: 1.8rem;
    padding-bottom: 1rem;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #172554 0%, #312e81 100%);
}

[data-testid="stSidebar"] * {
    color: #ffffff;
}

[data-testid="stSidebar"] button {
    border-radius: 10px;
}

.hero {
    background: linear-gradient(120deg, #172554 0%, #4338ca 55%, #7c3aed 100%);
    padding: 38px 34px;
    border-radius: 24px;
    color: white;
    margin-bottom: 24px;
    box-shadow: 0 14px 35px rgba(67, 56, 202, 0.18);
}

.hero-label {
    display: inline-block;
    padding: 7px 12px;
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.22);
    border-radius: 30px;
    color: #e0e7ff;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 14px;
}

.hero h1 {
    color: #ffffff !important;
    font-size: clamp(26px, 4vw, 40px);
    font-weight: 800;
    line-height: 1.2;
    margin: 0;
}

.hero p {
    color: #e0e7ff !important;
    font-size: 15px;
    line-height: 1.8;
    margin-top: 13px;
    margin-bottom: 0;
}

.section-heading {
    font-size: 23px;
    font-weight: 800;
    color: #172554;
    margin-top: 24px;
    margin-bottom: 5px;
}

.section-description {
    color: #64748b;
    font-size: 14px;
    margin-bottom: 18px;
}

.upload-heading {
    color: #312e81;
    font-weight: 700;
    font-size: 17px;
    margin-bottom: 5px;
}

.upload-description {
    color: #64748b;
    font-size: 13px;
    margin-bottom: 12px;
}

div[data-testid="stFileUploader"] {
    background: #ffffff;
    border: 1px dashed #a5b4fc;
    border-radius: 15px;
    padding: 12px;
}

div[data-testid="stMetric"] {
    background: #ffffff;
    border: 1px solid #e0e7ff;
    border-radius: 16px;
    padding: 18px 20px;
    box-shadow: 0 5px 18px rgba(30, 41, 59, 0.04);
}

div[data-testid="stMetricLabel"] {
    color: #64748b;
    font-weight: 600;
}

div[data-testid="stMetricValue"] {
    color: #312e81;
    font-weight: 800;
}

.stButton > button,
.stDownloadButton > button {
    border-radius: 12px;
    font-weight: 700;
    min-height: 46px;
    transition: all 0.2s ease;
}

.stButton > button[kind="primary"],
.stDownloadButton > button[kind="primary"] {
    background: linear-gradient(90deg, #4338ca, #7c3aed);
    color: #ffffff;
    border: none;
}

.stButton > button[kind="primary"]:hover,
.stDownloadButton > button[kind="primary"]:hover {
    box-shadow: 0 7px 18px rgba(79, 70, 229, 0.22);
    border: none;
    transform: translateY(-1px);
}

div[data-testid="stTabs"] button {
    font-weight: 600;
}

div[data-testid="stExpander"] {
    background: rgba(255,255,255,0.85);
    border: 1px solid #e0e7ff;
    border-radius: 13px;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}

.result-banner {
    background: #ffffff;
    border: 1px solid #e0e7ff;
    border-left: 5px solid #6366f1;
    border-radius: 14px;
    padding: 18px 22px;
    margin-bottom: 20px;
}

.result-banner h3 {
    color: #312e81;
    margin: 0 0 6px 0;
    font-size: 20px;
}

.result-banner p {
    color: #64748b;
    margin: 0;
    font-size: 14px;
}

.footer {
    margin-top: 48px;
    padding: 24px 12px 10px 12px;
    border-top: 1px solid #dbe2f0;
    text-align: center;
    color: #64748b;
    font-size: 13px;
    line-height: 2;
}

.footer strong {
    color: #4338ca;
    font-size: 15px;
}

.footer .footer-brand {
    color: #172554;
    font-weight: 700;
}

.small-note {
    color: #64748b;
    font-size: 12px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown("""
<div class="hero">
    <div class="hero-label">✦ AI-POWERED DOCUMENT ANALYSIS</div>
    <h1>📄MADHU AI Document Comparison Assistant</h1>
    <p>
        Compare two PDF documents intelligently.
        Discover similarities, identify differences, extract key details,
        and generate a professional comparison report.
    </p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
with st.sidebar:
    st.markdown("## 📘 About This Tool")
    st.write(
        "An AI-powered application that compares two PDF documents "
        "and presents summaries, similarities, differences, and key details."
    )

    st.divider()

    st.markdown("### ✨ Features")
    st.markdown("""
    - 📄 Compare two PDF documents
    - 📝 Generate document summaries
    - 🔍 Identify similarities
    - ⚖️ Find important differences
    - 📊 Display key details
    - 📥 Download a Word report
    """)

    st.divider()

    st.caption(
        "Only text-based PDFs, or PDFs containing an extractable text layer, "
        "are supported. Scanned documents may require OCR."
    )

    if st.button(
        "🔄 Reset / New Comparison",
        use_container_width=True
    ):
        for key in [
            "results",
            "doc_a_text",
            "doc_b_text",
            "doc_a_name",
            "doc_b_name",
        ]:
            st.session_state.pop(key, None)

        st.rerun()

# --------------------------------------------------
# DOCUMENT UPLOAD SECTION
# --------------------------------------------------
st.markdown(
    '<div class="section-heading">📂 Upload Your Documents</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Select two PDF files to begin your intelligent document comparison.'
    '</div>',
    unsafe_allow_html=True
)

col_a, col_b = st.columns(2, gap="large")

with col_a:
    st.markdown(
        '<div class="upload-heading">📘 Document A</div>'
        '<div class="upload-description">Upload the first PDF document.</div>',
        unsafe_allow_html=True
    )
    file_a = st.file_uploader(
        "Choose Document A",
        type=["pdf"],
        key="file_a",
        help="Select the first PDF file.",
        label_visibility="collapsed"
    )

with col_b:
    st.markdown(
        '<div class="upload-heading">📗 Document B</div>'
        '<div class="upload-description">Upload the second PDF document.</div>',
        unsafe_allow_html=True
    )
    file_b = st.file_uploader(
        "Choose Document B",
        type=["pdf"],
        key="file_b",
        help="Select the second PDF file.",
        label_visibility="collapsed"
    )

# --------------------------------------------------
# PDF READER
# --------------------------------------------------
def read_uploaded(uploaded):
    if uploaded is None:
        return None

    raw = uploaded.getvalue()
    validate_pdf(raw, uploaded.name)
    return extract_pdf_text(raw)


# --------------------------------------------------
# DOCUMENT VALIDATION AND ANALYSIS
# --------------------------------------------------
if file_a and file_b:
    try:
        with st.spinner("Reading and validating your PDF documents..."):
            text_a = read_uploaded(file_a)
            text_b = read_uploaded(file_b)

        if not text_a["text"].strip():
            st.error(
                f"No readable text was extracted from {file_a.name}. "
                "The PDF may be scanned or empty."
            )
            st.stop()

        if not text_b["text"].strip():
            st.error(
                f"No readable text was extracted from {file_b.name}. "
                "The PDF may be scanned or empty."
            )
            st.stop()

        st.markdown(
            '<div class="section-heading">📊 Document Overview</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-description">'
            'Review the extracted content before comparing the documents.'
            '</div>',
            unsafe_allow_html=True
        )

        # Document A metrics
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("📘 Document A Pages", text_a["pages"])
        col2.metric(
            "Characters in A",
            f'{len(text_a["text"]):,}'
        )
        col3.metric("📗 Document B Pages", text_b["pages"])
        col4.metric(
            "Characters in B",
            f'{len(text_b["text"]):,}'
        )

        # File names
        info_a, info_b = st.columns(2)

        with info_a:
            st.success(f"Document A: {file_a.name}")

        with info_b:
            st.success(f"Document B: {file_b.name}")

        # Preview extracted text
        with st.expander("👁️ Preview Extracted PDF Text"):
            p1, p2 = st.columns(2)

            with p1:
                st.markdown(f"**📘 {file_a.name}**")
                preview_a = text_a["text"][:2500]
                if len(text_a["text"]) > 2500:
                    preview_a += "…"
                st.text_area(
                    "Extracted content from Document A",
                    value=preview_a,
                    height=250,
                    disabled=True,
                    label_visibility="collapsed"
                )

            with p2:
                st.markdown(f"**📗 {file_b.name}**")
                preview_b = text_b["text"][:2500]
                if len(text_b["text"]) > 2500:
                    preview_b += "…"
                st.text_area(
                    "Extracted content from Document B",
                    value=preview_b,
                    height=250,
                    disabled=True,
                    label_visibility="collapsed"
                )

        # AI settings
        st.markdown(
            '<div class="section-heading">⚙️ Comparison Settings</div>',
            unsafe_allow_html=True
        )

        max_chars = st.number_input(
            "Maximum characters per document sent to AI",
            min_value=5000,
            max_value=100000,
            value=30000,
            step=5000,
            help=(
                "Long documents are truncated to this limit. "
                "The generated report will disclose this limitation."
            )
        )

        if st.button(
            "✨ Compare Documents with AI",
            type="primary",
            use_container_width=True
        ):
            try:
                with st.spinner(
                    "🤖 AI is analyzing both documents. Please wait..."
                ):
                    results = compare_documents(
                        text_a["text"][:int(max_chars)],
                        text_b["text"][:int(max_chars)],
                        file_a.name,
                        file_b.name,
                        truncated_a=len(text_a["text"]) > max_chars,
                        truncated_b=len(text_b["text"]) > max_chars
                    )

                st.session_state["results"] = results
                st.session_state["doc_a_name"] = file_a.name
                st.session_state["doc_b_name"] = file_b.name

                st.success("Document comparison completed successfully!")

            except Exception as exc:
                st.error(f"Comparison could not be completed: {exc}")
                st.info(
                    "Check your API key, internet connection, and "
                    "Gemini model availability, then try again."
                )

    except Exception as exc:
        st.error(f"Could not read the uploaded PDF: {exc}")

elif file_a or file_b:
    st.info("📌 Please upload both Document A and Document B to continue.")

else:
    st.markdown("""
    <div class="result-banner">
        <h3>🚀 Ready to Compare?</h3>
        <p>
            Upload two PDF documents above. The AI will analyze their content
            and prepare an organized comparison with downloadable results.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# COMPARISON RESULTS
# --------------------------------------------------
results = st.session_state.get("results")

if results:
    st.divider()

    st.markdown("""
    <div class="result-banner">
        <h3>📈 Document Comparison Results</h3>
        <p>
            Review the summaries, similarities, differences, key details,
            and final conclusion below.
        </p>
    </div>
    """, unsafe_allow_html=True)

    tabs = st.tabs([
        "📘 Summary A",
        "📗 Summary B",
        "🔗 Similarities",
        "⚖️ Differences",
        "📊 Key Details",
        "✅ Conclusion"
    ])

    with tabs[0]:
        st.subheader(
            st.session_state.get("doc_a_name", "Document A")
        )
        st.write(
            results.get(
                "summary_a",
                "Not found in the provided text."
            )
        )

    with tabs[1]:
        st.subheader(
            st.session_state.get("doc_b_name", "Document B")
        )
        st.write(
            results.get(
                "summary_b",
                "Not found in the provided text."
            )
        )

    with tabs[2]:
        similarities = results.get("similarities", [])

        if similarities:
            for i, item in enumerate(similarities, start=1):
                st.markdown(f"**{i}.** {item}")
        else:
            st.info("No supported similarities were identified.")

    with tabs[3]:
        differences = results.get("differences", [])

        if differences:
            for i, item in enumerate(differences, start=1):
                st.markdown(f"**{i}.** {item}")
        else:
            st.info("No supported differences were identified.")

    with tabs[4]:
        details = results.get("key_details", [])

        if details:
            st.dataframe(
                details,
                use_container_width=True,
                hide_index=True
            )
        else:
            st.info("No key details were returned.")

    with tabs[5]:
        st.markdown("### 🎯 Overall Conclusion")
        st.write(
            results.get(
                "overall_conclusion",
                "Not found in the provided text."
            )
        )

        st.divider()

        st.markdown("### ⚠️ Limitations")
        limitations = results.get("limitations", [])

        if limitations:
            for item in limitations:
                st.markdown(f"- {item}")
        else:
            st.write(
                "No additional limitations reported. "
                "Verify important findings against the original PDFs."
            )

    # --------------------------------------------------
    # DOWNLOAD REPORT
    # --------------------------------------------------
    st.divider()

    st.markdown(
        '<div class="section-heading">📥 Download Your Report</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'Save the comparison results as a Microsoft Word document.'
        '</div>',
        unsafe_allow_html=True
    )

    report_bytes = create_docx_report(
        st.session_state.get("doc_a_name", "Document A"),
        st.session_state.get("doc_b_name", "Document B"),
        results
    )

    st.download_button(
        "⬇️ Download Comparison Report (DOCX)",
        data=report_bytes,
        file_name="document_comparison_report.docx",
        mime=(
            "application/vnd.openxmlformats-officedocument."
            "wordprocessingml.document"
        ),
        type="primary",
        use_container_width=True
    )

    st.caption(
        "AI-generated results are informational. Review important findings "
        "against the original documents before making decisions."
    )

# --------------------------------------------------
# FOOTER - DEVELOPER CREDIT
# --------------------------------------------------
st.markdown("""
<div class="footer">
    <div class="footer-brand">
        📄 MADHU AI Document Comparison Assistant
    </div>
    Designed &amp; Developed by <strong>Madhukumar</strong>
    <br>
    <span class="small-note">
        Intelligent Document Analysis · Powered by AI · © 2026
    </span>
</div>
""", unsafe_allow_html=True)
