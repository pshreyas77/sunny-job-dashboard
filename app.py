import streamlit as st

st.set_page_config(page_title="Shreyas Job Tracker 2026", layout="wide")

CSS = """
<style>
.stApp { background-color: #080810 !important; }
.stMarkdown, .stText, .stTitle, .stHeader { color: #e2e8f0 !important; }
.stContainer { background-color: #0f0f1a !important; border: 1px solid #1c1c2e !important; border-radius: 10px !important; padding: 16px !important; margin-bottom: 16px !important; }
.stButton > button { background-color: #00e5a0 !important; color: #080810 !important; border: none !important; font-weight: bold !important; }
.stCheckbox label, .stCheckbox span { color: #e2e8f0 !important; }
.stSelectbox label, .stSelectbox > div > div { color: #e2e8f0 !important; }
h1, h2, h3 { color: #00e5a0 !important; }
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0f0f1a; }
::-webkit-scrollbar-thumb { background: #00e5a0; border-radius: 3px; }
.progress-bar-bg { background: #1c1c2e; border-radius: 4px; height: 8px; width: 100%; }
.progress-bar-fill { background: linear-gradient(90deg, #00e5a0, #7c6fcd); border-radius: 4px; height: 8px; transition: width 0.5s; }
.card { background: #0f0f1a; border: 1px solid #1c1c2e; border-radius: 10px; padding: 16px; margin-bottom: 12px; }
.card:hover { border-color: #00e5a0; }
.badge { display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; letter-spacing: 1px; }
.b-core { background: rgba(0,229,160,0.12); color: #00e5a0; border: 1px solid rgba(0,229,160,0.25); }
.b-ml { background: rgba(124,111,205,0.12); color: #a89ee8; border: 1px solid rgba(124,111,205,0.25); }
.b-ai { background: rgba(245,158,11,0.12); color: #fbbf24; border: 1px solid rgba(245,158,11,0.25); }
.b-db { background: rgba(59,130,246,0.12); color: #60a5fa; border: 1px solid rgba(59,130,246,0.25); }
.b-cloud { background: rgba(239,68,68,0.12); color: #f87171; border: 1px solid rgba(239,68,68,0.25); }
.b-tool { background: rgba(16,185,129,0.12); color: #34d399; border: 1px solid rgba(16,185,129,0.25); }
.b-stat { background: rgba(251,191,36,0.12); color: #fbbf24; border: 1px solid rgba(251,191,36,0.25); }
.b-dl { background: rgba(168,85,247,0.12); color: #c084fc; border: 1px solid rgba(168,85,247,0.25); }
.lv-beg { background: rgba(0,229,160,0.1); color: #00e5a0; padding: 2px 8px; border-radius: 4px; font-size: 10px; }
.lv-int { background: rgba(245,158,11,0.1); color: #fbbf24; padding: 2px 8px; border-radius: 4px; font-size: 10px; }
.lv-adv { background: rgba(239,68,68,0.1); color: #f87171; padding: 2px 8px; border-radius: 4px; font-size: 10px; }
.status-not { background: rgba(100,116,139,0.2); color: #94a3b8; padding: 2px 8px; border-radius: 4px; font-size: 10px; }
.status-app { background: rgba(59,130,246,0.2); color: #60a5fa; padding: 2px 8px; border-radius: 4px; font-size: 10px; }
.status-int { background: rgba(245,158,11,0.2); color: #fbbf24; padding: 2px 8px; border-radius: 4px; font-size: 10px; }
.status-off { background: rgba(0,229,160,0.2); color: #00e5a0; padding: 2px 8px; border-radius: 4px; font-size: 10px; }
.status-rej { background: rgba(239,68,68,0.2); color: #f87171; padding: 2px 8px; border-radius: 4px; font-size: 10px; }
.comp-low { background: rgba(0,229,160,0.15); color: #00e5a0; padding: 2px 8px; border-radius: 4px; font-size: 10px; }
.comp-med { background: rgba(245,158,11,0.15); color: #fbbf24; padding: 2px 8px; border-radius: 4px; font-size: 10px; }
</style>
"""

st.html(CSS)

# ---- DATA ----

SKILLS = {
    "🐍 Core Python": {
        "badge": "b-core",
        "id": "core",
        "playlists": [
            {
                "title": "Python Tutorials – Data Science & Web Dev",
                "channel": "Corey Schafer",
                "desc": "Gold standard Python tutorials — OOP, Pandas, Matplotlib, Generators. Clear, structured, real examples.",
                "dur": "~20 hrs",
                "level": "Beginner",
                "link": "https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU",
            },
            {
                "title": "Python for Beginners – Full Course",
                "channel": "freeCodeCamp",
                "desc": "4.5-hour comprehensive Python beginner course. Best single video to refresh fundamentals fast.",
                "dur": "4.5 hrs",
                "level": "Beginner",
                "link": "https://www.youtube.com/watch?v=rfscVS0vtbw",
            },
            {
                "title": "Data Analysis with Python & Pandas",
                "channel": "Data School (Kevin Markham)",
                "desc": "Best pandas playlist on YouTube. Practical real-world data manipulation, cleaning, merging.",
                "dur": "~8 hrs",
                "level": "Intermediate",
                "link": "https://www.youtube.com/playlist?list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y",
            },
            {
                "title": "Python Data Science Full Course",
                "channel": "Codebasics (Dhaval Patel)",
                "desc": "108-video Indian educator playlist. Covers Python + ML + Stats. Highly recommended for Indian fresher context.",
                "dur": "~30 hrs",
                "level": "Beginner",
                "link": "https://www.youtube.com/playlist?list=PLeo1K3hjS3us_ELKYSj_Fth2tIEkdKXvV",
            },
        ],
    },
    "🗄️ SQL / Database": {
        "badge": "b-db",
        "id": "db",
        "playlists": [
            {
                "title": "Data Analyst Bootcamp – SQL Complete",
                "channel": "Alex the Analyst",
                "desc": "The #1 DA bootcamp. Covers SQL basics → intermediate → advanced → portfolio projects in one 20-hr playlist.",
                "dur": "~20 hrs",
                "level": "Beginner",
                "link": "https://www.youtube.com/playlist?list=PLUaB-1hjhk8FE_XZ87vPPSfHqb6OcM0cF",
            },
            {
                "title": "SQL Tutorial – Full Database Course",
                "channel": "freeCodeCamp",
                "desc": "4-hour complete relational DB + SQL fundamentals. MySQL focused. Great for interview prep.",
                "dur": "4 hrs",
                "level": "Beginner",
                "link": "https://www.youtube.com/watch?v=HXV3zeQKqGY",
            },
            {
                "title": "Advanced SQL Tutorials (CTEs, Temp Tables, Stored Procs)",
                "channel": "Alex the Analyst",
                "desc": "Short focused videos on advanced SQL concepts tested in DA interviews.",
                "dur": "~2 hrs",
                "level": "Advanced",
                "link": "https://www.youtube.com/playlist?list=PLUaB-1hjhk8EBZNL4nx4Otoa5guqkep_n",
            },
            {
                "title": "MySQL Tutorial for Beginners",
                "channel": "Programming with Mosh",
                "desc": "Professional quality 3-hr MySQL complete tutorial. Covers all fundamentals + joins + stored procedures.",
                "dur": "3 hrs",
                "level": "Beginner",
                "link": "https://www.youtube.com/watch?v=7S_tz1z_5bA",
            },
        ],
    },
    "🤖 ML / Scikit-Learn": {
        "badge": "b-ml",
        "id": "ml",
        "playlists": [
            {
                "title": "Scikit-Learn Tutorial – ML in Python",
                "channel": "Data School (Kevin Markham)",
                "desc": "Best scikit-learn playlist. Covers entire ML workflow: preprocessing, modeling, evaluation, pipelines.",
                "dur": "~10 hrs",
                "level": "Intermediate",
                "link": "https://www.youtube.com/playlist?list=PL5-da3qGB5ICeMbQuqys6Us_2i-QbHOgA",
            },
            {
                "title": "Machine Learning with Python – Complete Course",
                "channel": "Codebasics",
                "desc": "End-to-end ML course with Indian-context examples. Linear/logistic regression, trees, SVM, clustering.",
                "dur": "~25 hrs",
                "level": "Beginner",
                "link": "https://www.youtube.com/playlist?list=PLeo1K3hjS3uvCeTYTeyfe0-rN5r8zn9rw",
            },
            {
                "title": "StatQuest: Machine Learning Fundamentals",
                "channel": "StatQuest (Josh Starmer)",
                "desc": "ESSENTIAL. Explains WHY algorithms work — decision trees, random forests, SVM, PCA, bias-variance. Highly visual.",
                "dur": "~15 hrs",
                "level": "Intermediate",
                "link": "https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF",
            },
            {
                "title": "ML Full Course – freeCodeCamp",
                "channel": "freeCodeCamp",
                "desc": "Multiple full-length ML courses covering linear regression to neural nets with Python.",
                "dur": "~12 hrs",
                "level": "Beginner",
                "link": "https://www.youtube.com/watch?v=NWONeJKn6kc",
            },
        ],
    },
    "🧠 TensorFlow / Deep Learning": {
        "badge": "b-dl",
        "id": "dl",
        "playlists": [
            {
                "title": "TensorFlow 2.0 Complete Course",
                "channel": "freeCodeCamp / Tim Ruscica",
                "desc": "7-hour complete TensorFlow 2.0 course. Neural nets, CNNs, RNNs, NLP. Project-based.",
                "dur": "7 hrs",
                "level": "Intermediate",
                "link": "https://www.youtube.com/watch?v=tPYj3fFJGjk",
            },
            {
                "title": "Deep Learning with Python (Keras + TF)",
                "channel": "Sentdex (Harrison Kinsley)",
                "desc": "Hands-on deep learning. Builds models step by step. Great for practical understanding of TF/Keras.",
                "dur": "~12 hrs",
                "level": "Intermediate",
                "link": "https://www.youtube.com/playlist?list=PLQVvvaa0QuDfhTox0AjmQ6tvTgMBZBEXN",
            },
            {
                "title": "Neural Networks – 3Blue1Brown",
                "channel": "3Blue1Brown (Grant Sanderson)",
                "desc": "WATCH THIS FIRST. Beautiful visual explanation of how neural networks and backprop actually work. 4 videos.",
                "dur": "1 hr",
                "level": "Beginner",
                "link": "https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi",
            },
            {
                "title": "Krish Naik – Complete Deep Learning Playlist",
                "channel": "Krish Naik",
                "desc": "Comprehensive DL series from Indian ML educator. ANN, CNN, RNN, LSTM, Transfer Learning.",
                "dur": "~20 hrs",
                "level": "Intermediate",
                "link": "https://www.youtube.com/playlist?list=PLZoTAELRMXVPGU70ZGsckrMdr0FteeRUi",
            },
        ],
    },
    "✨ LangChain / GenAI": {
        "badge": "b-ai",
        "id": "ai",
        "playlists": [
            {
                "title": "Complete LangChain Course for Generative AI",
                "channel": "Krish Naik",
                "desc": "3-hr complete LangChain course. Chatbots, RAG pipelines, API deployment, Groq + HuggingFace integration.",
                "dur": "3 hrs",
                "level": "Intermediate",
                "link": "https://www.youtube.com/watch?v=swCpkRLFWuQk",
            },
            {
                "title": "LangChain v1 Crash Course – Build Autonomous Agents",
                "channel": "Krish Naik",
                "desc": "Latest LangChain v1. Agents, tools, structured output, Pydantic, streaming, human-in-the-loop.",
                "dur": "2 hrs",
                "level": "Intermediate",
                "link": "https://www.youtube.com/watch?v=wCpkRLFWuQk",
            },
            {
                "title": "Complete RAG Crash Course with LangChain",
                "channel": "Krish Naik",
                "desc": "2-hour RAG systems from scratch. FAISS, vector DBs, retrieval augmented generation. Directly relevant to VerifAI.",
                "dur": "2 hrs",
                "level": "Intermediate",
                "link": "https://www.youtube.com/watch?v=sVcwVQRHIc8",
            },
            {
                "title": "Generative AI Full Course 2025",
                "channel": "freeCodeCamp",
                "desc": "Complete GenAI landscape: LLMs, prompt engineering, fine-tuning, agents, RAG, deployment.",
                "dur": "~10 hrs",
                "level": "Intermediate",
                "link": "https://www.youtube.com/watch?v=mEsleV16qdo",
            },
        ],
    },
    "⚡ FastAPI / Flask": {
        "badge": "b-tool",
        "id": "api",
        "playlists": [
            {
                "title": "FastAPI Tutorial – Complete Beginners Course",
                "channel": "Tech With Tim",
                "desc": "Beginner FastAPI course. CRUD, Pydantic, path params, request bodies. Clean and practical.",
                "dur": "~3 hrs",
                "level": "Beginner",
                "link": "https://www.youtube.com/watch?v=CBASjF0dYPU",
            },
            {
                "title": "FastAPI – Full Course (Endpoints to Deployment)",
                "channel": "Amigoscode",
                "desc": "REST APIs with FastAPI, SQLAlchemy, PostgreSQL, deployment. Production-ready patterns.",
                "dur": "~5 hrs",
                "level": "Intermediate",
                "link": "https://www.youtube.com/watch?v=0sOvCWFmrtA",
            },
            {
                "title": "Flask Tutorial Series",
                "channel": "Corey Schafer",
                "desc": "Best Flask series on YouTube. 15 videos covering routes, templates, DB, login, deployment.",
                "dur": "~8 hrs",
                "level": "Beginner",
                "link": "https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH",
            },
            {
                "title": "REST API with Python & Flask",
                "channel": "freeCodeCamp",
                "desc": "Build a complete REST API with Flask, authentication, and database from scratch.",
                "dur": "~2 hrs",
                "level": "Beginner",
                "link": "https://www.youtube.com/watch?v=GMppyAPbLYk",
            },
        ],
    },
    "☁️ AWS / Cloud": {
        "badge": "b-cloud",
        "id": "cloud",
        "playlists": [
            {
                "title": "AWS Tutorial for Beginners – Full 9hr Course",
                "channel": "freeCodeCamp",
                "desc": "Comprehensive AWS beginner course. EC2, S3, Lambda, networking, security, billing.",
                "dur": "9 hrs",
                "level": "Beginner",
                "link": "https://www.youtube.com/watch?v=ulprqHHWlng",
            },
            {
                "title": "AWS Fundamentals – Core Services",
                "channel": "TechWorld with Nana",
                "desc": "2.5-hr straight-to-the-point AWS course. IAM, EC2, S3, CloudFormation. Real-world practical focus.",
                "dur": "2.5 hrs",
                "level": "Beginner",
                "link": "https://www.youtube.com/watch?v=ZB5ONbD_SMY",
            },
            {
                "title": "AWS 107-Hour Cloud Project Bootcamp",
                "channel": "freeCodeCamp / Andrew Brown",
                "desc": "Full project bootcamp. Design, build, deploy real AWS cloud project end-to-end.",
                "dur": "107 hrs",
                "level": "Advanced",
                "link": "https://www.youtube.com/watch?v=zA8guDqfv40",
            },
            {
                "title": "Docker Tutorial for Beginners",
                "channel": "TechWorld with Nana",
                "desc": "Essential for cloud deployment. Docker concepts + hands-on. Pairs with FastAPI + AWS deployment.",
                "dur": "3 hrs",
                "level": "Beginner",
                "link": "https://www.youtube.com/watch?v=3c-iBn73dDE",
            },
        ],
    },
    "📊 Statistics / EDA": {
        "badge": "b-stat",
        "id": "stat",
        "playlists": [
            {
                "title": "Statistics Fundamentals",
                "channel": "StatQuest (Josh Starmer)",
                "desc": "THE best stats playlist. Probability, distributions, hypothesis testing, p-values, correlation. Visual + clear.",
                "dur": "~10 hrs",
                "level": "Beginner",
                "link": "https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9",
            },
            {
                "title": "Pandas Data Analysis – Visualization with Seaborn & Matplotlib",
                "channel": "Corey Schafer",
                "desc": "Matplotlib + Seaborn complete tutorials for data visualization. Directly for EDA projects.",
                "dur": "~5 hrs",
                "level": "Beginner",
                "link": "https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEviRg7LUgV14B7",
            },
            {
                "title": "Exploratory Data Analysis – Complete Python EDA",
                "channel": "Krish Naik",
                "desc": "Full EDA workflow in Python: missing values, outliers, feature engineering, visualization, correlation.",
                "dur": "~6 hrs",
                "level": "Beginner",
                "link": "https://www.youtube.com/playlist?list=PLZoTAELRMXVPzj1D0i_6ajJ6gyD22b3jh",
            },
            {
                "title": "Data Analyst Bootcamp – Tableau + Power BI",
                "channel": "Alex the Analyst",
                "desc": "Visualization tools: Tableau and Power BI from scratch. Essential for DA roles needing BI dashboards.",
                "dur": "~8 hrs",
                "level": "Beginner",
                "link": "https://www.youtube.com/playlist?list=PLUaB-1hjhk8FE_XZ87vPPSfHqb6OcM0cF",
            },
        ],
    },
}

TOTAL_PLAYLISTS = sum(len(v["playlists"]) for v in SKILLS.values())

JOB_TARGETS = [
    {
        "company": "Google",
        "role": "Data Analyst / ML Engineer",
        "sector": "Tech",
        "priority": "High",
        "platform": "careers.google.com",
        "link": "https://careers.google.com",
    },
    {
        "company": "Microsoft",
        "role": "Data Scientist / AI Engineer",
        "sector": "Tech",
        "priority": "High",
        "platform": "careers.microsoft.com",
        "link": "https://careers.microsoft.com",
    },
    {
        "company": "Amazon",
        "role": "Data Scientist / ML Engineer",
        "sector": "Tech",
        "priority": "High",
        "platform": "amazon.jobs",
        "link": "https://amazon.jobs",
    },
    {
        "company": "Meta",
        "role": "Data Analyst / ML Engineer",
        "sector": "Tech",
        "priority": "High",
        "platform": "meta.com/careers",
        "link": "https://www.metacareers.com",
    },
    {
        "company": "Apple",
        "role": "ML Engineer / Data Scientist",
        "sector": "Tech",
        "priority": "High",
        "platform": "apple.com/jobs",
        "link": "https://www.apple.com/jobs/us/",
    },
    {
        "company": "Netflix",
        "role": "Data Engineer / ML Engineer",
        "sector": "Media",
        "priority": "High",
        "platform": "jobs.netflix.com",
        "link": "https://jobs.netflix.com",
    },
    {
        "company": "Spotify",
        "role": "Data Scientist / ML Engineer",
        "sector": "Media",
        "priority": "Medium",
        "platform": "lifeatspotify.com",
        "link": "https://www.lifeatspotify.com",
    },
    {
        "company": "Uber",
        "role": "Data Scientist / ML Engineer",
        "sector": "Tech",
        "priority": "High",
        "platform": "uber.com/careers",
        "link": "https://www.uber.com/us/en/careers/",
    },
    {
        "company": "Airbnb",
        "role": "Data Scientist / ML Engineer",
        "sector": "Tech",
        "priority": "High",
        "platform": "airbnb.com/careers",
        "link": "https://www.airbnb.com/careers",
    },
    {
        "company": "LinkedIn",
        "role": "Data Scientist / ML Engineer",
        "sector": "Tech",
        "priority": "High",
        "platform": "linkedin.com/careers",
        "link": "https://www.linkedin.com/careers",
    },
    {
        "company": "Salesforce",
        "role": "Data Analyst / ML Engineer",
        "sector": "SaaS",
        "priority": "Medium",
        "platform": "salesforce.com/careers",
        "link": "https://www.salesforce.com/company/careers/",
    },
    {
        "company": "Adobe",
        "role": "Data Scientist / ML Engineer",
        "sector": "SaaS",
        "priority": "Medium",
        "platform": "adobe.com/careers",
        "link": "https://www.adobe.com/careers.html",
    },
    {
        "company": "Oracle",
        "role": "Data Analyst / ML Engineer",
        "sector": "SaaS",
        "priority": "Medium",
        "platform": "oracle.com/careers",
        "link": "https://www.oracle.com/careers/",
    },
    {
        "company": "IBM",
        "role": "Data Scientist / AI Engineer",
        "sector": "Tech",
        "priority": "Medium",
        "platform": "ibm.com/careers",
        "link": "https://www.ibm.com/careers/us-en/",
    },
    {
        "company": "Intel",
        "role": "ML Engineer / Data Scientist",
        "sector": "Hardware",
        "priority": "Medium",
        "platform": "intel.com/content/www/us/en/jobs",
        "link": "https://jobs.intel.com",
    },
    {
        "company": "NVIDIA",
        "role": "Deep Learning Engineer",
        "sector": "Hardware",
        "priority": "High",
        "platform": "nvidia.com/en-us/careers",
        "link": "https://www.nvidia.com/en-us/careers/",
    },
    {
        "company": "Palantir",
        "role": "Data Engineer / ML Engineer",
        "sector": "Tech",
        "priority": "High",
        "platform": "palantir.com/careers",
        "link": "https://www.palantir.com/careers/",
    },
    {
        "company": "Snowflake",
        "role": "Data Engineer / Data Scientist",
        "sector": "SaaS",
        "priority": "High",
        "platform": "snowflake.com/careers",
        "link": "https://www.snowflake.com/careers/",
    },
    {
        "company": "Databricks",
        "role": "Data Scientist / ML Engineer",
        "sector": "SaaS",
        "priority": "High",
        "platform": "databricks.com/careers",
        "link": "https://www.databricks.com/careers",
    },
    {
        "company": "Cloudera",
        "role": "Data Engineer / Data Scientist",
        "sector": "SaaS",
        "priority": "Low",
        "platform": "cloudera.com/about/careers",
        "link": "https://www.cloudera.com/about/careers.html",
    },
    {
        "company": "DataRobot",
        "role": "ML Engineer / Data Scientist",
        "sector": "SaaS",
        "priority": "Medium",
        "platform": "datarobot.com/careers",
        "link": "https://www.datarobot.com/careers/",
    },
    {
        "company": "Alteryx",
        "role": "Data Analyst / ML Engineer",
        "sector": "SaaS",
        "priority": "Low",
        "platform": "alteryx.com/company/careers",
        "link": "https://www.alteryx.com/company/careers",
    },
    {
        "company": "Qlik",
        "role": "Data Analyst",
        "sector": "SaaS",
        "priority": "Low",
        "platform": "qlik.com/us/company/careers",
        "link": "https://www.qlik.com/us/company/careers",
    },
    {
        "company": "Workday",
        "role": "Data Scientist",
        "sector": "SaaS",
        "priority": "Medium",
        "platform": "workday.com/careers",
        "link": "https://www.workday.com/en-us/company/careers.html",
    },
    {
        "company": "ServiceNow",
        "role": "ML Engineer / Data Scientist",
        "sector": "SaaS",
        "priority": "Medium",
        "platform": "servicenow.com/careers",
        "link": "https://www.servicenow.com/careers",
    },
    {
        "company": "Atlassian",
        "role": "Data Scientist / ML Engineer",
        "sector": "SaaS",
        "priority": "High",
        "platform": "atlassian.com/careers",
        "link": "https://www.atlassian.com/careers",
    },
]

LOW_COMPETITION = [
    {
        "company": "H2O.ai",
        "role": "ML Engineer / Data Scientist",
        "sector": "AI/ML SaaS",
        "priority": "High",
        "platform": "h2o.ai/careers",
        "link": "https://www.h2o.ai/company/careers/",
        "comp": "LOW",
    },
    {
        "company": "Dataiku",
        "role": "Data Scientist / ML Engineer",
        "sector": "AI/ML SaaS",
        "priority": "High",
        "platform": "dataiku.com/careers",
        "link": "https://www.dataiku.com/careers/",
        "comp": "LOW",
    },
    {
        "company": "Scale AI",
        "role": "ML Engineer / Data Analyst",
        "sector": "AI/ML SaaS",
        "priority": "High",
        "platform": "scale.com/careers",
        "link": "https://scale.com/careers",
        "comp": "LOW",
    },
    {
        "company": "C3.ai",
        "role": "Data Scientist / ML Engineer",
        "sector": "AI/ML SaaS",
        "priority": "High",
        "platform": "c3.ai/careers",
        "link": "https://www.c3.ai/careers/",
        "comp": "LOW",
    },
    {
        "company": "Databricks",
        "role": "Data Scientist / ML Engineer",
        "sector": "SaaS",
        "priority": "High",
        "platform": "databricks.com/careers",
        "link": "https://www.databricks.com/careers",
        "comp": "MED",
    },
    {
        "company": "Snowflake",
        "role": "Data Engineer / Data Scientist",
        "sector": "SaaS",
        "priority": "High",
        "platform": "snowflake.com/careers",
        "link": "https://www.snowflake.com/careers/",
        "comp": "MED",
    },
    {
        "company": "Alteryx",
        "role": "Data Analyst / ML Engineer",
        "sector": "SaaS",
        "priority": "Medium",
        "platform": "alteryx.com/careers",
        "link": "https://www.alteryx.com/company/careers",
        "comp": "LOW",
    },
    {
        "company": "Qlik",
        "role": "Data Analyst",
        "sector": "SaaS",
        "priority": "Medium",
        "platform": "qlik.com/careers",
        "link": "https://www.qlik.com/us/company/careers",
        "comp": "LOW",
    },
    {
        "company": "Trifacta (Google)",
        "role": "Data Engineer / Analyst",
        "sector": "SaaS",
        "priority": "Medium",
        "platform": "trifacta.com/careers",
        "link": "https://www.trifacta.com/careers/",
        "comp": "LOW",
    },
    {
        "company": "ThoughtSpot",
        "role": "Data Scientist / ML Engineer",
        "sector": "SaaS",
        "priority": "High",
        "platform": "thoughtspot.com/careers",
        "link": "https://www.thoughtspot.com/careers",
        "comp": "LOW",
    },
    {
        "company": "Fivetran",
        "role": "Data Engineer / Data Scientist",
        "sector": "SaaS",
        "priority": "High",
        "platform": "fivetran.com/careers",
        "link": "https://www.fivetran.com/careers",
        "comp": "LOW",
    },
    {
        "company": "Monte Carlo",
        "role": "Data Engineer / Analyst",
        "sector": "SaaS",
        "priority": "Medium",
        "platform": "montecarlodata.com/careers",
        "link": "https://www.montecarlodata.com/careers/",
        "comp": "LOW",
    },
    {
        "company": "dbt Labs",
        "role": "Data Engineer / Analyst",
        "sector": "SaaS",
        "priority": "High",
        "platform": "getdbt.com/careers",
        "link": "https://www.getdbt.com/careers/",
        "comp": "LOW",
    },
    {
        "company": "HashiCorp",
        "role": "Data Engineer / SRE",
        "sector": "DevOps/SaaS",
        "priority": "Medium",
        "platform": "hashicorp.com/careers",
        "link": "https://www.hashicorp.com/careers",
        "comp": "LOW",
    },
    {
        "company": "Confluent",
        "role": "Data Engineer / Platform Engineer",
        "sector": "SaaS",
        "priority": "High",
        "platform": "confluent.io/careers",
        "link": "https://www.confluent.io/careers/",
        "comp": "LOW",
    },
    {
        "company": "Elastic",
        "role": "ML Engineer / Data Scientist",
        "sector": "SaaS",
        "priority": "Medium",
        "platform": "elastic.co/careers",
        "link": "https://www.elastic.co/careers",
        "comp": "LOW",
    },
    {
        "company": "MongoDB",
        "role": "Data Engineer / Data Scientist",
        "sector": "SaaS",
        "priority": "Medium",
        "platform": "mongodb.com/company/careers",
        "link": "https://www.mongodb.com/company/careers",
        "comp": "MED",
    },
    {
        "company": "Neo4j",
        "role": "Data Scientist / ML Engineer",
        "sector": "SaaS",
        "priority": "Medium",
        "platform": "neo4j.com/careers",
        "link": "https://www.neo4j.com/careers/",
        "comp": "LOW",
    },
    {
        "company": "RapidMiner",
        "role": "Data Scientist / ML Engineer",
        "sector": "AI/ML SaaS",
        "priority": "Low",
        "platform": "rapidminer.com/careers",
        "link": "https://www.rapidminer.com/careers/",
        "comp": "LOW",
    },
    {
        "company": "HPE",
        "role": "Data Engineer / ML Engineer",
        "sector": "Enterprise",
        "priority": "Low",
        "platform": "hpe.com/careers",
        "link": "https://www.hpe.com/us/en/careers.html",
        "comp": "LOW",
    },
    {
        "company": "Teradata",
        "role": "Data Analyst / Data Engineer",
        "sector": "Enterprise",
        "priority": "Low",
        "platform": "teradata.com/careers",
        "link": "https://www.teradata.com/careers",
        "comp": "LOW",
    },
    {
        "company": "SAP",
        "role": "Data Scientist / ML Engineer",
        "sector": "Enterprise",
        "priority": "Medium",
        "platform": "sap.com/careers",
        "link": "https://www.sap.com/about/careers.html",
        "comp": "MED",
    },
    {
        "company": "Informatica",
        "role": "Data Engineer / Data Analyst",
        "sector": "Enterprise",
        "priority": "Low",
        "platform": "informatica.com/careers",
        "link": "https://www.informatica.com/about-us/careers.html",
        "comp": "LOW",
    },
]

ROADMAP = [
    {
        "week": "Week 1-2",
        "title": "Foundation Refresh",
        "items": [
            "Python for Data Science (Corey Schafer)",
            "Pandas & NumPy (Data School)",
            "SQL Basics → Advanced (Alex the Analyst)",
            "Build: EDA project on Kaggle dataset",
        ],
    },
    {
        "week": "Week 3-4",
        "title": "ML Core Skills",
        "items": [
            "Scikit-Learn full playlist (Data School)",
            "StatQuest Statistics Fundamentals",
            "ML with Python (Codebasics)",
            "Build: Customer Churn model",
        ],
    },
    {
        "week": "Week 5-6",
        "title": "Deep Learning + APIs",
        "items": [
            "TensorFlow/Keras (Sentdex / freeCodeCamp)",
            "FastAPI complete course (Tech With Tim)",
            "Flask tutorials (Corey Schafer)",
            "Build: ML model served as FastAPI endpoint",
        ],
    },
    {
        "week": "Week 7-8",
        "title": "GenAI + Cloud Deploy",
        "items": [
            "LangChain complete (Krish Naik)",
            "RAG pipeline + Agents (Krish Naik)",
            "AWS basics (freeCodeCamp / TechWorld Nana)",
            "Build: Deploy on AWS / Oracle Cloud",
        ],
    },
]

# ---- SESSION INIT ----
if "watched" not in st.session_state:
    st.session_state.watched = set()

if "job_status" not in st.session_state:
    st.session_state.job_status = {c["company"]: "Not Applied" for c in JOB_TARGETS}

if "low_comp_status" not in st.session_state:
    st.session_state.low_comp_status = {
        c["company"]: "Not Applied" for c in LOW_COMPETITION
    }


# ---- PAGE 1 ----
def page_playlists():
    st.title("📚 Skill Playlists — Job Ready 2026")
    st.markdown(
        "**All skills from resume · 100% Free · YouTube only · Data Analyst / AI-ML ready**"
    )

    with st.sidebar:
        st.header("🔍 Filter")
        selected = st.radio("Category", ["All"] + list(SKILLS.keys()), index=0)

    done_count = len(st.session_state.watched)
    pct = int(done_count / TOTAL_PLAYLISTS * 100)

    st.markdown(f"""
    <div class="progress-bar-bg" style="max-width:600px">
        <div class="progress-bar-fill" style="width:{pct}%"></div>
    </div>
    <p style="color:#64748b;font-family:monospace;font-size:11px;margin-top:4px">{done_count} / {TOTAL_PLAYLISTS} playlists watched · {pct}% job-ready</p>
    """)

    categories = (
        list(SKILLS.items()) if selected == "All" else [(selected, SKILLS[selected])]
    )

    for cat_name, cat_data in categories:
        with st.container():
            st.markdown(
                f"### {cat_name} <span class='badge {cat_data['badge']}'>{cat_data['id'].upper()}</span>",
                unsafe_allow_html=True,
            )

        for i, pl in enumerate(cat_data["playlists"]):
            key = f"{cat_data['id']}-{i}"
            checked = key in st.session_state.watched

            col1, col2, col3, col4, col5, col6 = st.columns([1, 5, 1, 1, 1, 1])

            lv_class = {
                "Beginner": "lv-beg",
                "Intermediate": "lv-int",
                "Advanced": "lv-adv",
            }.get(pl["level"], "lv-beg")
            strike = "text-decoration:line-through;opacity:0.5" if checked else ""

            with col1:
                new_val = st.checkbox("", value=checked, key=f"cb_{key}")
                if new_val and not checked:
                    st.session_state.watched.add(key)
                elif not new_val and checked:
                    st.session_state.watched.discard(key)

            with col2:
                st.markdown(
                    f"""<div style="{strike}"><strong>{pl["title"]}</strong><br>
                <span style="color:#64748b;font-size:11px">📺 {pl["channel"]}</span><br>
                <span style="color:#334155;font-size:11px">{pl["desc"]}</span></div>""",
                    unsafe_allow_html=True,
                )

            with col3:
                st.markdown(
                    f"<span style='color:#f59e0b;font-family:monospace;font-size:11px'>{pl['dur']}</span>",
                    unsafe_allow_html=True,
                )

            with col4:
                st.markdown(
                    f"<span class='{lv_class}'>{pl['level']}</span>",
                    unsafe_allow_html=True,
                )

            with col5:
                st.markdown(
                    f"<a href='{pl['link']}' target='_blank' style='color:#00e5a0;text-decoration:none;border:1px solid rgba(0,229,160,0.3);padding:4px 8px;border-radius:4px;font-family:monospace;font-size:10px'>▶ Watch</a>",
                    unsafe_allow_html=True,
                )

            with col6:
                st.markdown("✅" if checked else "⭕", unsafe_allow_html=True)

            st.divider()

    st.markdown("---")
    st.markdown("## 🗺️ 8-Week Job-Ready Study Roadmap")

    cols = st.columns(4)
    for i, week in enumerate(ROADMAP):
        with cols[i]:
            with st.container():
                st.markdown(f"**{week['week']}**")
                st.markdown(f"### {week['title']}")
                for item in week["items"]:
                    st.markdown(
                        f"<span style='color:#00e5a0'>→</span> <span style='color:#64748b;font-size:11px'>{item}</span>",
                        unsafe_allow_html=True,
                    )


# ---- PAGE 2 ----
def page_job_targets():
    st.title("🎯 Job Targets — 28 Companies")

    sectors = ["All"] + sorted(set(c["sector"] for c in JOB_TARGETS))
    with st.sidebar:
        st.header("🔍 Filter")
        sel_sector = st.selectbox("Sector", sectors)

    filtered = (
        JOB_TARGETS
        if sel_sector == "All"
        else [c for c in JOB_TARGETS if c["sector"] == sel_sector]
    )

    statuses = list(st.session_state.job_status.values())
    st.markdown(
        f"""
    <div style="display:flex;gap:16px;margin-bottom:20px">
        <div style="background:#0f0f1a;border:1px solid #1c1c2e;border-radius:8px;padding:12px 20px;text-align:center">
            <div style="color:#e2e8f0;font-size:24px;font-weight:bold">{len(JOB_TARGETS)}</div>
            <div style="color:#64748b;font-size:11px">Total</div>
        </div>
        <div style="background:#0f0f1a;border:1px solid #1c1c2e;border-radius:8px;padding:12px 20px;text-align:center">
            <div style="color:#60a5fa;font-size:24px;font-weight:bold">{statuses.count("Applied")}</div>
            <div style="color:#64748b;font-size:11px">Applied</div>
        </div>
        <div style="background:#0f0f1a;border:1px solid #1c1c2e;border-radius:8px;padding:12px 20px;text-align:center">
            <div style="color:#fbbf24;font-size:24px;font-weight:bold">{statuses.count("Interview")}</div>
            <div style="color:#64748b;font-size:11px">Interview</div>
        </div>
        <div style="background:#0f0f1a;border:1px solid #1c1c2e;border-radius:8px;padding:12px 20px;text-align:center">
            <div style="color:#00e5a0;font-size:24px;font-weight:bold">{statuses.count("Offer")}</div>
            <div style="color:#64748b;font-size:11px">Offer</div>
        </div>
        <div style="background:#0f0f1a;border:1px solid #1c1c2e;border-radius:8px;padding:12px 20px;text-align:center">
            <div style="color:#f87171;font-size:24px;font-weight:bold">{statuses.count("Rejected")}</div>
            <div style="color:#64748b;font-size:11px">Rejected</div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    for c in filtered:
        status = st.session_state.job_status[c["company"]]
        prio_color = {"High": "#00e5a0", "Medium": "#fbbf24", "Low": "#64748b"}.get(
            c["priority"], "#64748b"
        )

        with st.container():
            col1, col2, col3, col4, col5, col6 = st.columns([2, 2, 1, 1, 1, 1])
            with col1:
                st.markdown(f"**{c['company']}**")
            with col2:
                st.markdown(
                    f"<span style='color:#64748b;font-size:11px'>{c['role']}</span>",
                    unsafe_allow_html=True,
                )
            with col3:
                st.markdown(
                    f"<span style='color:{prio_color};font-size:11px'>{c['priority']}</span>",
                    unsafe_allow_html=True,
                )
            with col4:
                st.markdown(
                    f"<span style='color:#64748b;font-size:11px'>{c['sector']}</span>",
                    unsafe_allow_html=True,
                )
            with col5:
                new_status = st.selectbox(
                    "",
                    ["Not Applied", "Applied", "Interview", "Offer", "Rejected"],
                    index=[
                        "Not Applied",
                        "Applied",
                        "Interview",
                        "Offer",
                        "Rejected",
                    ].index(status)
                    if status
                    in ["Not Applied", "Applied", "Interview", "Offer", "Rejected"]
                    else 0,
                    key=f"job_{c['company']}",
                    label_visibility="collapsed",
                )
                st.session_state.job_status[c["company"]] = new_status
            with col6:
                st.markdown(
                    f"<a href='{c['link']}' target='_blank' style='color:#00e5a0;text-decoration:none;font-size:11px'>Apply ↗</a>",
                    unsafe_allow_html=True,
                )

            st.divider()


# ---- PAGE 3 ----
def page_low_comp():
    st.title("🏆 Low Competition Targets — 25 Companies")
    st.markdown("Companies with less applicant crowd — higher response rates")

    sectors = ["All"] + sorted(set(c["sector"] for c in LOW_COMPETITION))
    with st.sidebar:
        st.header("🔍 Filter")
        sel_sector = st.selectbox("Sector", sectors, key="lc_sector")

    filtered = (
        LOW_COMPETITION
        if sel_sector == "All"
        else [c for c in LOW_COMPETITION if c["sector"] == sel_sector]
    )

    statuses = list(st.session_state.low_comp_status.values())
    st.markdown(
        f"""
    <div style="display:flex;gap:16px;margin-bottom:20px">
        <div style="background:#0f0f1a;border:1px solid #1c1c2e;border-radius:8px;padding:12px 20px;text-align:center">
            <div style="color:#e2e8f0;font-size:24px;font-weight:bold">{len(LOW_COMPETITION)}</div>
            <div style="color:#64748b;font-size:11px">Total</div>
        </div>
        <div style="background:#0f0f1a;border:1px solid #1c1c2e;border-radius:8px;padding:12px 20px;text-align:center">
            <div style="color:#60a5fa;font-size:24px;font-weight:bold">{statuses.count("Applied")}</div>
            <div style="color:#64748b;font-size:11px">Applied</div>
        </div>
        <div style="background:#0f0f1a;border:1px solid #1c1c2e;border-radius:8px;padding:12px 20px;text-align:center">
            <div style="color:#fbbf24;font-size:24px;font-weight:bold">{statuses.count("Interview")}</div>
            <div style="color:#64748b;font-size:11px">Interview</div>
        </div>
        <div style="background:#0f0f1a;border:1px solid #1c1c2e;border-radius:8px;padding:12px 20px;text-align:center">
            <div style="color:#00e5a0;font-size:24px;font-weight:bold">{statuses.count("Offer")}</div>
            <div style="color:#64748b;font-size:11px">Offer</div>
        </div>
        <div style="background:#0f0f1a;border:1px solid #1c1c2e;border-radius:8px;padding:12px 20px;text-align:center">
            <div style="color:#f87171;font-size:24px;font-weight:bold">{statuses.count("Rejected")}</div>
            <div style="color:#64748b;font-size:11px">Rejected</div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    for c in filtered:
        status = st.session_state.low_comp_status[c["company"]]
        prio_color = {"High": "#00e5a0", "Medium": "#fbbf24", "Low": "#64748b"}.get(
            c["priority"], "#64748b"
        )
        comp_class = "comp-low" if c["comp"] == "LOW" else "comp-med"

        with st.container():
            col1, col2, col3, col4, col5, col6, col7 = st.columns([2, 2, 1, 1, 1, 1, 1])
            with col1:
                st.markdown(f"**{c['company']}**")
            with col2:
                st.markdown(
                    f"<span style='color:#64748b;font-size:11px'>{c['role']}</span>",
                    unsafe_allow_html=True,
                )
            with col3:
                st.markdown(
                    f"<span class='{comp_class}'>{c['comp']}</span>",
                    unsafe_allow_html=True,
                )
            with col4:
                st.markdown(
                    f"<span style='color:{prio_color};font-size:11px'>{c['priority']}</span>",
                    unsafe_allow_html=True,
                )
            with col5:
                st.markdown(
                    f"<span style='color:#64748b;font-size:11px'>{c['sector']}</span>",
                    unsafe_allow_html=True,
                )
            with col6:
                new_status = st.selectbox(
                    "",
                    ["Not Applied", "Applied", "Interview", "Offer", "Rejected"],
                    index=[
                        "Not Applied",
                        "Applied",
                        "Interview",
                        "Offer",
                        "Rejected",
                    ].index(status)
                    if status
                    in ["Not Applied", "Applied", "Interview", "Offer", "Rejected"]
                    else 0,
                    key=f"lc_{c['company']}",
                    label_visibility="collapsed",
                )
                st.session_state.low_comp_status[c["company"]] = new_status
            with col7:
                st.markdown(
                    f"<a href='{c['link']}' target='_blank' style='color:#00e5a0;text-decoration:none;font-size:11px'>Apply ↗</a>",
                    unsafe_allow_html=True,
                )

            st.divider()


# ---- NAVIGATION ----
pg = st.navigation(
    ["📚 Skill Playlists", "🎯 Job Targets", "🏆 Low Competition Targets"]
)
pg.run()
