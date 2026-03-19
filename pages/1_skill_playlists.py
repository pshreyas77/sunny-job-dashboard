import streamlit as st
from data import SKILLS, TOTAL_PLAYLISTS, ROADMAP

st.title("📚 Skill Playlists — Job Ready 2026")
st.markdown(
    "**All skills from resume · 100% Free · YouTube only · Data Analyst / AI-ML ready**"
)

with st.sidebar:
    st.header("🔍 Filter")
    selected = st.radio("Category", ["All"] + list(SKILLS.keys()), index=0)

if "watched" not in st.session_state:
    st.session_state.watched = set()

done_count = len(st.session_state.watched)
pct = int(done_count / TOTAL_PLAYLISTS * 100)

st.markdown(
    f"""
<div class="progress-bar-bg" style="max-width:600px">
    <div class="progress-bar-fill" style="width:{pct}%"></div>
</div>
<p style="color:#64748b;font-family:monospace;font-size:11px;margin-top:4px">{done_count} / {TOTAL_PLAYLISTS} playlists watched · {pct}% job-ready</p>
""",
    unsafe_allow_html=True,
)

categories = (
    list(SKILLS.items()) if selected == "All" else [(selected, SKILLS[selected])]
)

for cat_name, cat_data in categories:
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
            provider = ""
            if "Anthropic" in pl["channel"]:
                provider = " <span style='background:rgba(217,119,6,0.12);color:#d97706;padding:1px 6px;border-radius:3px;font-size:9px;font-family:monospace'>ANTHROPIC</span>"
            elif "NVIDIA" in pl["channel"]:
                provider = " <span style='background:rgba(118,185,71,0.12);color:#76b947;padding:1px 6px;border-radius:3px;font-size:9px;font-family:monospace'>NVIDIA</span>"
            st.markdown(
                f"""<div style="{strike}"><strong>{pl["title"]}</strong>{provider}<br>
            <span style="color:#64748b;font-size:11px">{pl["channel"]}</span><br>
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
                f"<span class='{lv_class}'>{pl['level']}</span>", unsafe_allow_html=True
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
        st.markdown(f"**{week['week']}**")
        st.markdown(f"### {week['title']}")
        for item in week["items"]:
            st.markdown(
                f"<span style='color:#00e5a0'>→</span> <span style='color:#64748b;font-size:11px'>{item}</span>",
                unsafe_allow_html=True,
            )
