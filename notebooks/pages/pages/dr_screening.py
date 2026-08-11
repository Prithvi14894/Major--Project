import streamlit as st
from PIL import Image

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="DR Screening",
    page_icon="🩸",
    layout="wide"
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
    background-color:#F4F8FB;
}

.title{
    font-size:40px;
    font-weight:bold;
    color:#0B5394;
    text-align:center;
}

.subtitle{
    font-size:18px;
    color:#666666;
    text-align:center;
}

.result-card{
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 5px 12px rgba(0,0,0,0.12);
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Header
# --------------------------------------------------

col1, col2 = st.columns([1, 6])

with col1:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

with col2:
    st.markdown(
        "<div class='title'>🩸 Diabetic Retinopathy Screening</div>",
        unsafe_allow_html=True
    )

st.markdown(
    "<div class='subtitle'>Upload a retinal fundus image for screening.</div>",
    unsafe_allow_html=True
)

st.write("")
st.write("")

# --------------------------------------------------
# Upload Section
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Choose a retinal image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Uploaded Image")
        st.image(image, use_container_width=True)

    with col2:

        st.subheader("Prediction")

        if st.button("🔍 Predict", use_container_width=True):

            with st.spinner("Analyzing retinal image..."):

                # Placeholder
                st.success("Prediction completed!")

                st.markdown("---")

                st.markdown("### Disease")
                st.info("Waiting for model integration...")

                st.markdown("### Confidence")
                st.progress(0)

                st.markdown("### Description")
                st.write(
                    "The uploaded retinal image will be analyzed "
                    "using the Fine-Tuned ResNet50 model."
                )

                st.markdown("### Recommendation")
                st.write(
                    "Please wait until the AI model is connected."
                )

else:

    st.info("Please upload a retinal fundus image to continue.")