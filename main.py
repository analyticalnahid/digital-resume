from pathlib import Path
import streamlit as st
from PIL import Image


#... PATH SETTINGS ...#

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "My Resume.pdf"
profile_pic = current_dir / "assets" / "profile.jpeg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Nahidul Islam"
PAGE_ICON = ":wave:"
NAME = "Nahidul Islam"
DESCRIPTION = """
Machine Learning Engineer
"""
EMAIL = "analyticalnahid@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/analyticalnahid/",
    "YouTube": "https://www.youtube.com/channel/UCLeFKnFwC11FQWvtFk32vJQ",
    "GitHub": "https://github.com/analyticalnahid",
    "Medium": "https://medium.com/@analyticalnahid"
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2)
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    
    
# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Strong hands on experience and knowledge in Python and SQL
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
""")

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Numpy, Pandas, Scikit-learn, Tensorflow), SQL
- 🗄️ Databases: MySQL
- 📊 Data Visulization: Matplotlib, Seaborn, Plotly
- 📚 Tools: Jupyter Notebook, Google Colab, PyCharm, VS Code
-    Web: Flask, FastAPI, Streamlit
-    Operating Systems: Linux
- 📈 Machine Learning: Regression, Classification, Clustering, Anomaly Detection
- 📊 Deep Learning: ANN, CNN, RNN, LSTM
- Computer Vision: OpenCV, YOLO, ResNet, VGG, UNet, StrongSort
- Cloud: AWS SageMaker, Heroku

 
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Computer Vision & IoT Intern**")
st.write("09/2022 - 09/2022")
st.write(
    """
- ► Data Accumulation: Collecting data from different sources (eg; Kaggle, Web Scraping).
- ► Data Annotation: Labeling data with predefined tools(eg: RoboFlow) or pretrained models.
- ► Model Building/Testing: Making model with Tensorflow/PyTorch or Transfer Learning.
- ► Model Deployment: Model from development to production environment using Tensorflow Extended/MLFlow
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")