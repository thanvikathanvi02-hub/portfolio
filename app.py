import streamlit as st

st.set_page_config(page_title="Tetali Thanvika | Portfolio", page_icon="💡", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.main { background-color: #0e1117; }
.big-title { font-size: 42px; font-weight: 800; color: #4FD1C5; margin-bottom:0;}
.subtitle { font-size: 18px; color: #A0AEC0; margin-top:0;}
.section-header { font-size: 28px; font-weight: 700; color: #4FD1C5; margin-top: 30px; border-bottom: 2px solid #4FD1C5; padding-bottom:5px;}
.card { background-color: #1A202C; padding: 18px; border-radius: 12px; margin-bottom: 15px; border: 1px solid #2D3748;}
.skill-badge { display:inline-block; background-color:#2D3748; color:#4FD1C5; padding:6px 14px; border-radius:20px; margin:4px; font-size:14px;}
a { color: #4FD1C5 !important; }
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<p class="big-title">Tetali Thanvika</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Data Visualization & IoT Enthusiast | Python • SQL • Power BI • Tableau</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col1.markdown("📧 thanvikathanvika02@gmail.com")
col2.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/tetali-thanvika)")
col3.markdown("[💻 GitHub](https://github.com/thanvikathanvi02-hub)")

st.markdown("---")

# ---------- PROFILE SUMMARY ----------
st.markdown('<p class="section-header">Profile Summary</p>', unsafe_allow_html=True)
st.write("""
Engineering student with hands-on experience in IoT-based sensor data collection and real-time monitoring,
with strong skills in Python, SQL, and data visualization using Tableau and Power BI. Experienced in building
data pipelines, ML-based analytics, and BI dashboards.
""")

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
    st.markdown(f"**{cat}**")
    st.markdown("".join([f'<span class="skill-badge">{i}</span>' for i in items]), unsafe_allow_html=True)
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
- 🏆 Won 2nd Prize, IoTA Project — IoT Based Air Quality Monitoring System (Aug–Sep 2025)
- 🥇 Secured Rank 5201 (Top 0.2%), Naukri AINCAT 2026 (06/2026)
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
st.markdown("<center>Made with ❤️ using Streamlit</center>", unsafe_allow_html=True)
