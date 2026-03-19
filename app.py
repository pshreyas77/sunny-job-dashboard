import streamlit as st

st.set_page_config(page_title="Shreyas Job Tracker 2026", layout="wide")

CSS = """
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;700&family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
/* ═══ THE SKILLS GAZETTE — Black & White Editorial ═══ */
.stApp { background-color: #ffffff !important; font-family: 'DM Sans', sans-serif !important; }

/* Ruled lines */
.stApp::before {
  content: '';
  position: fixed; inset: 0;
  background-image: repeating-linear-gradient(180deg, transparent, transparent 39px, rgba(0,0,0,0.06) 39px, rgba(0,0,0,0.06) 40px);
  pointer-events: none; z-index: 0;
}

h1, h2, h3 { color: #000000 !important; font-family: 'Playfair Display', serif !important; letter-spacing: -0.5px !important; }
.stMarkdown, .stText, .stTitle, .stHeader { color: #000000 !important; font-family: 'DM Sans', sans-serif !important; }
.stContainer { background-color: #ffffff !important; border: 1px solid #000000 !important; border-radius: 0 !important; padding: 16px !important; margin-bottom: 0 !important; }
.stButton > button { background-color: #000000 !important; color: #ffffff !important; border: 1.5px solid #000000 !important; font-weight: bold !important; font-family: 'IBM Plex Mono', monospace !important; font-size: 10px !important; letter-spacing: 1.5px !important; text-transform: uppercase !important; border-radius: 0 !important; transition: all 0.15s !important; }
.stButton > button:hover { background-color: #ffffff !important; color: #000000 !important; }
.stCheckbox label, .stCheckbox span { color: #000000 !important; }
.stSelectbox label, .stSelectbox > div > div { color: #000000 !important; font-family: 'IBM Plex Mono', monospace !important; }
.stRadio label { color: #000000 !important; font-family: 'IBM Plex Mono', monospace !important; font-size: 11px !important; }

::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #ffffff; }
::-webkit-scrollbar-thumb { background: #000000; }

/* Progress bar — thin solid black */
.progress-bar-bg { background: #ffffff; border: 1px solid #000000; border-radius: 0; height: 2px; width: 100%; }
.progress-bar-fill { background: #000000; border-radius: 0; height: 100%; transition: width 0.5s; }

/* Badges — black border on white */
.badge { display: inline-block; padding: 2px 10px; border-radius: 0; font-size: 9px; font-weight: bold; letter-spacing: 2px; text-transform: uppercase; font-family: 'IBM Plex Mono', monospace; }
.b-core { background: #ffffff; color: #000000; border: 1.5px solid #000000; }
.b-ml { background: #ffffff; color: #000000; border: 1.5px solid #000000; }
.b-ai { background: #ffffff; color: #000000; border: 1.5px solid #000000; }
.b-db { background: #ffffff; color: #000000; border: 1.5px solid #000000; }
.b-cloud { background: #ffffff; color: #000000; border: 1.5px solid #000000; }
.b-tool { background: #ffffff; color: #000000; border: 1.5px solid #000000; }
.b-stat { background: #ffffff; color: #000000; border: 1.5px solid #000000; }
.b-dl { background: #ffffff; color: #000000; border: 1.5px solid #000000; }
.b-cert { background: #ffffff; color: #000000; border: 1.5px solid #000000; }

/* Level pills — B/W inversion */
.lv-beg { background: #ffffff; color: #000000; padding: 3px 8px; border: 1.5px solid #000000; font-size: 8px; font-family: 'IBM Plex Mono', monospace; letter-spacing: 1.5px; text-transform: uppercase; }
.lv-int { background: #000000; color: #ffffff; padding: 3px 8px; border: 1.5px solid #000000; font-size: 8px; font-family: 'IBM Plex Mono', monospace; letter-spacing: 1.5px; text-transform: uppercase; }
.lv-adv { background: #ffffff; color: #000000; padding: 3px 8px; border: 1.5px solid #000000; font-size: 8px; font-family: 'IBM Plex Mono', monospace; letter-spacing: 1.5px; text-transform: uppercase; text-decoration: underline; text-underline-offset: 2px; }

/* Job status pills — B/W only */
.status-not { background: #ffffff; color: #000000; padding: 3px 8px; border: 1px solid #000000; font-size: 9px; font-family: 'IBM Plex Mono', monospace; letter-spacing: 1px; text-transform: uppercase; }
.status-app { background: #000000; color: #ffffff; padding: 3px 8px; border: 1px solid #000000; font-size: 9px; font-family: 'IBM Plex Mono', monospace; letter-spacing: 1px; text-transform: uppercase; }
.status-int { background: #ffffff; color: #000000; padding: 3px 8px; border: 1.5px solid #000000; font-size: 9px; font-family: 'IBM Plex Mono', monospace; letter-spacing: 1px; text-transform: uppercase; font-weight: bold; }
.status-off { background: #000000; color: #ffffff; padding: 3px 8px; border: 1px solid #000000; font-size: 9px; font-family: 'IBM Plex Mono', monospace; letter-spacing: 1px; text-transform: uppercase; }
.status-rej { background: #ffffff; color: #000000; padding: 3px 8px; border: 1px dashed #000000; font-size: 9px; font-family: 'IBM Plex Mono', monospace; letter-spacing: 1px; text-transform: uppercase; }

/* Competition pills */
.comp-low { background: #ffffff; color: #000000; padding: 3px 8px; border: 1.5px solid #000000; font-size: 9px; font-family: 'IBM Plex Mono', monospace; letter-spacing: 1.5px; text-transform: uppercase; }
.comp-med { background: #000000; color: #ffffff; padding: 3px 8px; border: 1.5px solid #000000; font-size: 9px; font-family: 'IBM Plex Mono', monospace; letter-spacing: 1.5px; text-transform: uppercase; }
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
