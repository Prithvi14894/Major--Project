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

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp{
    background: linear-gradient(to bottom,#F4F8FB,#EAF4FF);
}

.title{
    font-size:48px;
    font-weight:700;
    color:#0B5394;
    text-align:center;
}

.subtitle{
    font-size:20px;
    text-align:center;
    color:#666666;
}

.card{
    background:white;
    border-radius:18px;
    padding:30px;
    box-shadow:0px 6px 18px rgba(0,0,0,0.12);
    text-align:center;
}

.card h2{
    color:#0B5394;
}

hr{
    margin-top:40px;
    margin-bottom:40px;
}

.stButton>button{
    width:100%;
    height:50px;
    border-radius:12px;
    font-size:18px;
    font-weight:bold;
    background:#0B5394;
    color:white;
    border:none;
}

.stButton>button:hover{
    background:#1565C0;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown("<div class='title'>👁️ Retinal Disease Screening System</div>", unsafe_allow_html=True)

st.markdown(
"""
<div class='subtitle'>
AI-Based Detection of <b>Diabetic Retinopathy</b> and <b>Glaucoma</b>
</div>
""",
unsafe_allow_html=True
)

st.write("")
st.write("")

# --------------------------------------------------
# Introduction
# --------------------------------------------------

st.info("""
### Welcome

This application uses a **Fine-Tuned ResNet50 Deep Learning Model**
to analyze retinal fundus images and detect:

✅ Normal Retina

🩸 Diabetic Retinopathy

👁️ Glaucoma

Please choose a screening option below.
""")

st.write("")
st.write("")

# --------------------------------------------------
# Two Columns
# --------------------------------------------------

col1,col2 = st.columns(2)

# --------------------------------------------------
# DR CARD
# --------------------------------------------------

with col1:

    st.markdown("""
<div class="card">

# 🩸

## Diabetic Retinopathy Screening

Detect diabetic retinal abnormalities
from retinal fundus images.

</div>
""", unsafe_allow_html=True)

    st.write("")

    if st.button("Open DR Screening"):

        st.switch_page("pages/dr_screening.py")


# --------------------------------------------------
# GLAUCOMA CARD
# --------------------------------------------------

with col2:

    st.markdown("""
<div class="card">

# 👁️

## Glaucoma Screening

Detect glaucoma from
retinal fundus images.

</div>
""", unsafe_allow_html=True)

    st.write("")

    if st.button("Open Glaucoma Screening"):

        st.switch_page("pages/glaucoma_screening.py")


st.write("")
st.write("")

st.markdown("---")

st.success("Select a screening module to begin retinal image analysis.")