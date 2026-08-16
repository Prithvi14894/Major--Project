import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Retinal Disease Screening",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------
st.markdown("""
<style>

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp{
    background-color:#F4F8FB;
}

.title{
    font-size:48px;
    font-weight:bold;
    text-align:center;
    color:#0B5394;
}

.subtitle{
    font-size:22px;
    text-align:center;
    color:#555555;
}

.card{
    background:white;
    padding:30px;
    border-radius:15px;
    box-shadow:0 4px 15px rgba(0,0,0,0.15);
    text-align:center;
    height:240px;
}

.card h2{
    color:#0B5394;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.markdown("""
<div class='title'>
👁️ Retinal Disease Screening System
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='subtitle'>
Deep Learning Based Detection of
<b>Diabetic Retinopathy</b> and
<b>Glaucoma</b>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# --------------------------------------------------
# Description
# --------------------------------------------------

st.info("""
### Welcome

This application analyzes retinal fundus images using a Fine-Tuned ResNet50 model.

The system can identify:

- ✅ Normal Retina
- 🩸 Diabetic Retinopathy
- 👁️ Glaucoma

Select a screening option below to continue.
""")

st.write("")
st.write("")

# --------------------------------------------------
# Cards
# --------------------------------------------------

col1, col2 = st.columns(2)

# ---------------- DR ----------------

with col1:

    st.markdown("""
    <div class='card'>
        <h1>🩸</h1>
        <h2>Diabetic Retinopathy</h2>

        <p>
        Upload a retinal fundus image to detect
        diabetic retinopathy using deep learning.
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("Open DR Screening", use_container_width=True):
        st.switch_page("notebooks/pages/dr screening.py")

# ---------------- Glaucoma ----------------

with col2:

    st.markdown("""
    <div class='card'>
        <h1>👁️</h1>
        <h2>Glaucoma</h2>

        <p>
        Upload a retinal fundus image to detect
        glaucoma using deep learning.
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("Open Glaucoma Screening", use_container_width=True):
        st.switch_page("notebooks/pages/glaucoma screening.py")