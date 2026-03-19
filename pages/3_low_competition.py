import streamlit as st
from data import LOW_COMPETITION

st.title("🏆 Low Competition Targets — 25 Companies")
st.markdown("Companies with less applicant crowd — higher response rates")

sectors = ["All"] + sorted(set(c["sector"] for c in LOW_COMPETITION))
with st.sidebar:
    st.header("🔍 Filter")
    sel_sector = st.selectbox("Sector", sectors, key="lc_sector")

if "low_comp_status" not in st.session_state:
    st.session_state.low_comp_status = {
        c["company"]: "Not Applied" for c in LOW_COMPETITION
    }

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
            f"<span class='{comp_class}'>{c['comp']}</span>", unsafe_allow_html=True
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
            index=["Not Applied", "Applied", "Interview", "Offer", "Rejected"].index(
                status
            )
            if status in ["Not Applied", "Applied", "Interview", "Offer", "Rejected"]
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
