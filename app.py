import streamlit as st

st.set_page_config(page_title="Shreyas Job Tracker 2026", layout="wide")

CSS = """
<style>
.stApp { background-color: #080810 !important; }
h1, h2, h3 { color: #00e5a0 !important; }
.stMarkdown, .stText, .stTitle, .stHeader { color: #e2e8f0 !important; }
.stContainer { background-color: #0f0f1a !important; border: 1px solid #1c1c2e !important; border-radius: 10px !important; padding: 16px !important; margin-bottom: 16px !important; }
.stButton > button { background-color: #00e5a0 !important; color: #080810 !important; border: none !important; font-weight: bold !important; }
.stCheckbox label, .stCheckbox span { color: #e2e8f0 !important; }
.stSelectbox label, .stSelectbox > div > div { color: #e2e8f0 !important; }
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0f0f1a; }
::-webkit-scrollbar-thumb { background: #00e5a0; border-radius: 3px; }
.progress-bar-bg { background: #1c1c2e; border-radius: 4px; height: 8px; width: 100%; }
.progress-bar-fill { background: linear-gradient(90deg, #00e5a0, #7c6fcd); border-radius: 4px; height: 8px; transition: width 0.5s; }
.badge { display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; letter-spacing: 1px; }
.b-core { background: rgba(0,229,160,0.12); color: #00e5a0; border: 1px solid rgba(0,229,160,0.25); }
.b-ml { background: rgba(124,111,205,0.12); color: #a89ee8; border: 1px solid rgba(124,111,205,0.25); }
.b-ai { background: rgba(245,158,11,0.12); color: #fbbf24; border: 1px solid rgba(245,158,11,0.25); }
.b-db { background: rgba(59,130,246,0.12); color: #60a5fa; border: 1px solid rgba(59,130,246,0.25); }
.b-cloud { background: rgba(239,68,68,0.12); color: #f87171; border: 1px solid rgba(239,68,68,0.25); }
.b-tool { background: rgba(16,185,129,0.12); color: #34d399; border: 1px solid rgba(16,185,129,0.25); }
.b-stat { background: rgba(251,191,36,0.12); color: #fbbf24; border: 1px solid rgba(251,191,36,0.25); }
.b-dl { background: rgba(168,85,247,0.12); color: #c084fc; border: 1px solid rgba(168,85,247,0.25); }
.b-cert { background: rgba(251,191,36,0.12); color: #fbbf24; border: 1px solid rgba(251,191,36,0.25); }
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

pg = st.navigation(
    [
        st.Page("pages/1_skill_playlists.py", title="📚 Skill Playlists", icon="📚"),
        st.Page("pages/2_job_targets.py", title="🎯 Job Targets", icon="🎯"),
        st.Page("pages/3_low_competition.py", title="🏆 Low Competition", icon="🏆"),
    ]
)
pg.run()
