import streamlit as st

st.set_page_config(page_title="Tetali Thanvika | Portfolio", page_icon="💡", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

/* Background */
.stApp{
    background:#2563EB;
}

/* Main Container */
.block-container{
    max-width:1200px;
    padding-top:2rem;
    padding-bottom:2rem;
}

/* Title */
.big-title{
    font-size:60px;
    font-weight:800;
    color:white;
    text-align:center;
    margin-bottom:5px;
}

/* Subtitle */
.subtitle{
    font-size:22px;
    color:white;
    text-align:center;
    margin-bottom:30px;
}

/* Section Heading */
.section-header{
    background:white;
    color:#2563EB;
    padding:12px 18px;
    border-radius:12px;
    font-size:28px;
    font-weight:bold;
    margin-top:30px;
    margin-bottom:15px;
}

/* Cards */
.card{
    background:white;
    color:#111827;
    border-radius:18px;
    padding:20px;
    margin-bottom:18px;
    box-shadow:0 10px 25px rgba(0,0,0,.18);
    transition:.3s;
}

.card:hover{
    transform:translateY(-6px);
}

/* Skills */
.skill-badge{
    display:inline-block;
    background:#2563EB;
    color:white;
    padding:8px 16px;
    margin:5px;
    border-radius:25px;
    font-weight:bold;
}

/* Links */
a{
    color:white !important;
    font-weight:bold;
    text-decoration:none;
}

/* Text */
p, li{
    color:#111827;
}

hr{
    border:1px solid rgba(255,255,255,.4);
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<div style="text-align:center;padding:25px;">
<h1 class="big-title">Tetali Thanvika</h1>
<p class="subtitle">
Data Analyst • Python Developer • IoT Enthusiast
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="display:flex;
justify-content:center;
align-items:center;
gap:35px;
font-size:18px;
font-weight:600;
margin-top:10px;
margin-bottom:25px;">

<span style="color:white;">📧 thanvikathanvika02@gmail.com</span>

<a href="https://www.linkedin.com/in/tetali-thanvika"
style="color:white;text-decoration:none;">
🔗 LinkedIn
</a>

<a href="https://github.com/thanvikathanvi02-hub"
style="color:white;text-decoration:none;">
💻 GitHub
</a>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------- PROFILE SUMMARY ----------
st.markdown('<p class="section-header">Profile Summary</p>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
Engineering student with hands-on experience in IoT-based sensor data collection and real-time monitoring,
with strong skills in Python, SQL, and data visualization using Tableau and Power BI.
Experienced in building data pipelines, ML-based analytics, and BI dashboards.
</div>
""", unsafe_allow_html=True)

# ---------- EDUCATION ----------
st.markdown('<p class="section-header">Education</p>', unsafe_allow_html=True)
education = [
    ("B.Tech in Internet of Things", "Gudlavalleru Engineering College, Gudlavalleru", "2024 – 2027"),
    ("Diploma in CSE", "ISTS for Women, Rajamahendravaram", "2021 – 2023"),
    ("Class X (SSC)", "Roots School of Essential Faculties, Bhimavaram", "2016 – 2021"),
]
for deg, school, yr in education:
    st.markdown(f"""<div class="card"><b>{deg}</b><br>{school}<br><i>{yr}</i></div>""", unsafe_allow_html=True)

# ---------- SKILLS ----------
st.markdown('<p class="section-header">Technical Skills</p>', unsafe_allow_html=True)
skills = {
    "Programming & Querying": ["Python", "SQL", "C", "C++"],
    "Data Analytics & BI": ["Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly", "Power BI", "Power Query", "Tableau"],
    "Web & Backend": ["HTML", "CSS", "JavaScript", "SQL Server", "MySQL"],
    "IoT & Embedded": ["ESP32", "Arduino IDE", "ThingSpeak Cloud", "DHT & Gas Sensors"],
    "Tools & Platforms": ["VS Code", "GitHub", "Excel", "Arduino IDE"],
}
for cat, items in skills.items():
    st.subheader(cat)
    st.pills(
        label="",
        options=items,
        selection_mode="multi",
        default=items
    )
    st.write("")

# ---------- WORK EXPERIENCE ----------
st.markdown('<p class="section-header">Work Experience</p>', unsafe_allow_html=True)

st.markdown("""<div class="card">
<b>Data Visualization Intern</b> — Infosys Springboard Virtual Internship 7.0 <i>(06/2026 – Present)</i>
<ul>
<li>Selected for a structured virtual internship focused on data visualization</li>
<li>Working with datasets to create dashboards and derive insights</li>
<li>Gained hands-on experience in visual storytelling and analytical thinking</li>
<li>Applied best practices in data cleaning and chart design for business reporting</li>
</ul></div>""", unsafe_allow_html=True)

st.markdown("""<div class="card">
<b>IoT Intern</b> — Skilldzire Technologies (Remote) <i>(05/2025 – 06/2025)</i>
<ul>
<li>Built end-to-end data pipeline from gas & DHT sensors via ESP32 to ThingSpeak cloud, improving data usability by ~35%</li>
<li>Analyzed real-time sensor data to generate safety and environmental insights, increasing monitoring effectiveness by ~20–25%</li>
<li>Documented sensor data workflows and prepared summary reports for project evaluation</li>
</ul></div>""", unsafe_allow_html=True)

st.markdown("""<div class="card">
<b>Industrial Training — Design & Development</b> <i>(Nov 2023 – Apr 2024)</i>
<ul>
<li>Trained in HTML, CSS, JavaScript, C#, ASP.NET MVC, and SQL Server for full-stack web development</li>
<li>Implemented CRUD operations integrating backend logic with UI to support real-time data-driven features</li>
</ul></div>""", unsafe_allow_html=True)

# ---------- PROJECTS ----------
st.markdown('<p class="section-header">Projects</p>', unsafe_allow_html=True)

projects = [
    ("IoT Based Air Quality Monitoring System", "Aug–Sep 2025",
     ["Built IoT system using ESP32 and DHT/MQ sensors with ThingSpeak cloud and Matplotlib visualizations",
      "Monitored real-time AQI levels and triggered alerts on threshold breaches",
      "Won 2nd Prize at IoTA Project competition"],
     "Python, ESP32, ThingSpeak, Matplotlib"),
    ("Neural Network SMS Classifier", "Feb 2026",
     ["Developed ML model to classify SMS as spam or ham using NLP techniques",
      "Applied TF-IDF vectorization and achieved high accuracy on test dataset",
      "Evaluated model using confusion matrix, precision, recall, and F1-score"],
     "Python, Pandas, Scikit-learn, TensorFlow/Keras"),
    ("IMDb Movies Data Analysis", "Mar 2026",
     ["Analyzed IMDb dataset (1920–2020) to identify trends in ratings, genres, and releases",
      "Built an interactive Tableau dashboard to visualize ratings, votes, and performance",
      "Derived insights on genre popularity, rating distribution, and long-term trends"],
     "Tableau, Excel"),
    ("HR Attrition Analysis", "May 2026",
     ["Built a predictive analytics model to identify employees at risk of attrition",
      "Performed feature engineering and correlation analysis on HR dataset",
      "Generated actionable insights through exploratory data analysis and visualizations"],
     "Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Jupyter Notebook"),
]

for title, date, bullets, tech in projects:
    bullet_html = "".join([f"<li>{b}</li>" for b in bullets])
    st.markdown(f"""<div class="card">
    <b>{title}</b> <i>({date})</i>
    <ul>{bullet_html}</ul>
    <b>Tech:</b> {tech}
    </div>""", unsafe_allow_html=True)

# ---------- ACHIEVEMENTS ----------
st.markdown('<p class="section-header">Achievements</p>', unsafe_allow_html=True)
st.markdown("""
-  Won 2nd Prize, IoTA Project — IoT Based Air Quality Monitoring System (Aug–Sep 2025)
-  Secured Rank 5201 (Top 0.2%), Naukri AINCAT 2026 (06/2026)
""")

# ---------- CERTIFICATIONS ----------
st.markdown('<p class="section-header">Certifications</p>', unsafe_allow_html=True)
st.markdown("""
- Data Analysis with Python — FreeCodeCamp
- Machine Learning with Python — FreeCodeCamp
- Joy of Computing with Python — NPTEL
- SQL (Basic) Certificate — HackerRank
""")

st.markdown("---")

