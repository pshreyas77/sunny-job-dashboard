import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from ai_insights import generate_insights

st.set_page_config(
    page_title="IMDB Top 250 — TV Analytics",
    page_icon="▣",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_data
def load_data():
    return pd.read_csv('IMDB_cleaned.csv')

df = load_data()

BW_CHART = dict(
    paper_bgcolor="#080808",
    plot_bgcolor="#080808",
    font=dict(
        family="DM Mono, monospace",
        color="#2E2E2E",
        size=9
    ),
    xaxis=dict(
        gridcolor="#111111",
        linecolor="#141414",
        tickfont=dict(color="#333333", size=8),
        tickcolor="#141414",
        showgrid=True,
        zeroline=False,
        showline=True
    ),
    yaxis=dict(
        gridcolor="#111111",
        linecolor="#141414",
        tickfont=dict(color="#333333", size=8),
        tickcolor="#141414",
        showgrid=True,
        zeroline=False,
        showline=False
    ),
    legend=dict(
        bgcolor="rgba(0,0,0,0)",
        font=dict(color="#333333", size=8),
        orientation="h",
        yanchor="bottom", y=-0.35,
        xanchor="left", x=0,
        bordercolor="rgba(0,0,0,0)"
    ),
    margin=dict(l=10, r=10, t=10, b=40),
    hoverlabel=dict(
        bgcolor="#111111",
        bordercolor="#222222",
        font=dict(
            family="DM Mono, monospace",
            size=10,
            color="#AAAAAA"
        )
    ),
    colorway=["#FFFFFF","#999999","#666666","#444444","#CCCCCC","#777777"]
)

BW_TITLE = lambda t: dict(
    text=t.upper(),
    font=dict(
        family="DM Mono, monospace",
        size=8,
        color="#2A2A2A"
    ),
    x=0, xanchor="left", y=0.98
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Mono:ital,wght@0,300;0,400;0,500;1,300&family=DM+Sans:wght@300;400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; }

html, body, [class*="css"] {
  font-family: 'DM Sans', sans-serif !important;
  background: #000 !important;
  color: #E0E0E0 !important;
}

#MainMenu, footer, header,
.stDeployButton, [data-testid="stToolbar"],
[data-testid="stDecoration"] {
  display: none !important;
}

.main .block-container {
  padding: 0 !important;
  max-width: 100% !important;
}
section[data-testid="stMain"] > div {
  padding: 0 !important;
}

.topbar {
  background: #000;
  border-bottom: 1px solid #1C1C1C;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 2.5rem;
}
.tb-left {
  display: flex;
  align-items: baseline;
  gap: 0.8rem;
}
.tb-logo {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 1.2rem;
  letter-spacing: 0.2em;
  color: #FFF;
}
.tb-divider {
  width: 1px;
  height: 14px;
  background: #2A2A2A;
}
.tb-sub {
  font-family: 'DM Mono', monospace;
  font-size: 0.58rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #3A3A3A;
}
.tb-right {
  font-family: 'DM Mono', monospace;
  font-size: 0.58rem;
  letter-spacing: 0.1em;
  color: #2A2A2A;
  text-transform: uppercase;
}

.bc {
  background: #000;
  border-bottom: 1px solid #141414;
  padding: 0.4rem 2.5rem;
  font-family: 'DM Mono', monospace;
  font-size: 0.58rem;
  color: #2E2E2E;
  letter-spacing: 0.08em;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}
.bc-sep { color: #222; }
.bc-active { color: #666; }

.body-wrap {
  padding: 2rem 2.5rem;
}

.sec-header {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  padding-bottom: 1rem;
  border-bottom: 1px solid #1A1A1A;
  margin-bottom: 1.5rem;
}
.sec-eyebrow {
  font-family: 'DM Mono', monospace;
  font-size: 0.52rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: #333;
  margin-bottom: 0.2rem;
}
.sec-title {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 1.8rem;
  letter-spacing: 0.1em;
  color: #FFF;
  line-height: 1;
}
.sec-meta {
  text-align: right;
}
.sec-meta-val {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 1.4rem;
  color: #555;
  letter-spacing: 0.08em;
  line-height: 1;
}
.sec-meta-label {
  font-family: 'DM Mono', monospace;
  font-size: 0.52rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #2E2E2E;
}

[data-testid="metric-container"] {
  background: #0A0A0A !important;
  border: 1px solid #1A1A1A !important;
  border-top: 1px solid #2A2A2A !important;
  border-radius: 4px !important;
  padding: 1.2rem 1.4rem !important;
  transition: border-color 0.2s, transform 0.2s !important;
  position: relative !important;
}
[data-testid="metric-container"]:hover {
  border-color: #333 !important;
  border-top-color: #FFF !important;
  transform: translateY(-2px) !important;
}
[data-testid="stMetricLabel"] {
  font-family: 'DM Mono', monospace !important;
  font-size: 0.55rem !important;
  letter-spacing: 0.18em !important;
  text-transform: uppercase !important;
  color: #333 !important;
}
[data-testid="stMetricValue"] {
  font-family: 'Bebas Neue', sans-serif !important;
  font-size: 2.4rem !important;
  letter-spacing: 0.06em !important;
  color: #E8E8E8 !important;
  line-height: 1.1 !important;
}
[data-testid="stMetricDelta"] {
  font-family: 'DM Mono', monospace !important;
  font-size: 0.6rem !important;
  color: #333 !important;
  letter-spacing: 0.06em !important;
}

.cc {
  background: #080808;
  border: 1px solid #181818;
  border-radius: 4px;
  padding: 1.1rem 1.2rem 0.5rem;
  margin-bottom: 0.8rem;
}
.cc:hover { border-color: #222; }
.cc-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.6rem;
  padding-bottom: 0.6rem;
  border-bottom: 1px solid #141414;
}
.cc-title {
  font-family: 'DM Mono', monospace;
  font-size: 0.56rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #333;
}
.cc-badge {
  font-family: 'DM Mono', monospace;
  font-size: 0.5rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #222;
  border: 1px solid #1E1E1E;
  border-radius: 2px;
  padding: 0.15rem 0.5rem;
}

[data-baseweb="tab-list"] {
  background: transparent !important;
  border-bottom: 1px solid #1A1A1A !important;
  gap: 0 !important;
  margin-bottom: 1.5rem !important;
}
[data-baseweb="tab"] {
  font-family: 'DM Mono', monospace !important;
  font-size: 0.58rem !important;
  letter-spacing: 0.14em !important;
  text-transform: uppercase !important;
  color: #2E2E2E !important;
  background: transparent !important;
  border: none !important;
  border-bottom: 1px solid transparent !important;
  padding: 0.65rem 1.4rem !important;
  transition: color 0.15s !important;
}
[data-baseweb="tab"]:hover {
  color: #888 !important;
  background: transparent !important;
}
[aria-selected="true"] {
  color: #E0E0E0 !important;
  border-bottom: 1px solid #E0E0E0 !important;
  background: transparent !important;
}

[data-testid="stSidebar"] {
  background: #050505 !important;
  border-right: 1px solid #141414 !important;
}
[data-testid="stSidebar"] > div:first-child {
  padding: 0 !important;
}
.sb-head {
  padding: 1.2rem 1.3rem 1rem;
  border-bottom: 1px solid #141414;
  margin-bottom: 1rem;
}
.sb-title {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 0.9rem;
  letter-spacing: 0.2em;
  color: #2A2A2A;
}
.sb-section {
  padding: 0 1.3rem;
  margin-bottom: 1.2rem;
}
.sb-label {
  font-family: 'DM Mono', monospace;
  font-size: 0.5rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: #252525;
  margin-bottom: 0.9rem;
  padding-bottom: 0.4rem;
  border-bottom: 1px solid #141414;
}
[data-testid="stSidebar"] .stSelectbox label {
  font-family: 'DM Mono', monospace !important;
  font-size: 0.52rem !important;
  letter-spacing: 0.14em !important;
  text-transform: uppercase !important;
  color: #2E2E2E !important;
}
[data-testid="stSidebar"] .stSelectbox > div > div {
  background: #0A0A0A !important;
  border: 1px solid #1A1A1A !important;
  border-radius: 3px !important;
  color: #666 !important;
  font-family: 'DM Mono', monospace !important;
  font-size: 0.75rem !important;
}
[data-testid="stSidebar"] .stSlider label {
  font-family: 'DM Mono', monospace !important;
  font-size: 0.52rem !important;
  letter-spacing: 0.14em !important;
  text-transform: uppercase !important;
  color: #2E2E2E !important;
}
[data-testid="stSidebar"] .stSlider [data-baseweb="slider"] {
  margin-top: 0.3rem !important;
}

.div-line {
  border: none;
  border-top: 1px solid #141414;
  margin: 1.5rem 0;
}

.ai-wrap {
  background: #050505;
  border: 1px solid #1A1A1A;
  border-left: 1px solid #FFF;
  border-radius: 4px;
  padding: 1.2rem 1.5rem;
}
.ai-head {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  font-family: 'DM Mono', monospace;
  font-size: 0.54rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #333;
  margin-bottom: 1rem;
  padding-bottom: 0.8rem;
  border-bottom: 1px solid #141414;
}
.ai-dot {
  width: 5px; height: 5px;
  border-radius: 50%;
  background: #FFF;
  animation: blink 2s ease-in-out infinite;
}
@keyframes blink {
  0%,100%{opacity:1} 50%{opacity:0.1}
}
.ai-item {
  display: flex;
  gap: 0.8rem;
  padding: 0.6rem 0;
  border-bottom: 1px solid #0F0F0F;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.78rem;
  font-weight: 300;
  color: #555;
  line-height: 1.55;
}
.ai-item:first-of-type { color: #888; }
.ai-item:last-child { border-bottom: none; }
.ai-n {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 1.1rem;
  color: #222;
  line-height: 1;
  flex-shrink: 0;
  padding-top: 2px;
}

.show-card {
  background: #080808;
  border: 1px solid #1A1A1A;
  border-radius: 4px;
  padding: 1.5rem;
  margin-top: 1rem;
}
.show-rank {
  font-family: 'DM Mono', monospace;
  font-size: 0.52rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #2A2A2A;
  margin-bottom: 0.3rem;
}
.show-title {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 2rem;
  letter-spacing: 0.1em;
  color: #FFF;
  line-height: 1;
  margin-bottom: 1rem;
}
.show-stats {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
  border-top: 1px solid #141414;
  padding-top: 1rem;
}
.show-stat-val {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 1.6rem;
  color: #888;
  letter-spacing: 0.06em;
}
.show-stat-label {
  font-family: 'DM Mono', monospace;
  font-size: 0.5rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #2A2A2A;
}

.stButton > button {
  background: transparent !important;
  border: 1px solid #1E1E1E !important;
  color: #333 !important;
  font-family: 'DM Mono', monospace !important;
  font-size: 0.6rem !important;
  letter-spacing: 0.14em !important;
  text-transform: uppercase !important;
  border-radius: 3px !important;
  padding: 0.5rem 1.5rem !important;
  transition: all 0.15s !important;
}
.stButton > button:hover {
  border-color: #555 !important;
  color: #CCC !important;
}

.stTextInput > div > div > input {
  background: #0A0A0A !important;
  border: 1px solid #1A1A1A !important;
  border-radius: 3px !important;
  color: #CCC !important;
  font-family: 'DM Mono', monospace !important;
  font-size: 0.8rem !important;
  padding: 0.6rem 0.9rem !important;
}
.stTextInput > div > div > input:focus {
  border-color: #444 !important;
  box-shadow: none !important;
}
.stTextInput > div > div > input::placeholder {
  color: #2A2A2A !important;
  font-style: italic;
}

[data-testid="stDataFrame"] {
  border: 1px solid #141414 !important;
  border-radius: 4px !important;
}
[data-testid="stDataFrame"] th {
  background: #0A0A0A !important;
  font-family: 'DM Mono', monospace !important;
  font-size: 0.55rem !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  color: #333 !important;
  border-bottom: 1px solid #1A1A1A !important;
}
[data-testid="stDataFrame"] td {
  font-family: 'DM Mono', monospace !important;
  font-size: 0.72rem !important;
  color: #555 !important;
}

::-webkit-scrollbar { width: 3px; height: 3px; }
::-webkit-scrollbar-track { background: #000; }
::-webkit-scrollbar-thumb { background: #1A1A1A; border-radius: 2px; }
::-webkit-scrollbar-thumb:hover { background: #333; }

.modebar { display: none !important; }

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="topbar">
  <div class="tb-left">
    <div class="tb-logo">IMDB Analytics</div>
    <div class="tb-divider"></div>
    <div class="tb-sub">Top 250 TV Shows · Intelligence Report</div>
  </div>
  <div class="tb-right">Data Source: IMDB · 250 Records</div>
</div>
<div class="bc">
  <span>Analytics</span>
  <span class="bc-sep">›</span>
  <span>Television</span>
  <span class="bc-sep">›</span>
  <span class="bc-active">Top 250 Dashboard</span>
</div>
<div class="body-wrap">
<div class="sec-header">
  <div>
    <div class="sec-eyebrow">Interactive Report · IMDB Data</div>
    <div class="sec-title">TV Show Analytics</div>
  </div>
  <div class="sec-meta">
    <div class="sec-meta-val">250</div>
    <div class="sec-meta-label">Shows Analyzed</div>
  </div>
</div>
""", unsafe_allow_html=True)

def cc(title, badge="IMDB · 2024"):
    st.markdown(f"""
    <div class="cc">
      <div class="cc-head">
        <div class="cc-title">{title}</div>
        <div class="cc-badge">{badge}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

def render_insights(text):
    items = [i.strip().lstrip("•-▸0123456789. ") for i in text.split("\n") if i.strip()][:5]
    rows = "".join([f"""
    <div class="ai-item">
      <div class="ai-n">{str(i+1).zfill(2)}</div>
      <div>{item}</div>
    </div>""" for i, item in enumerate(items)])
    
    st.markdown(f"""
    <div class="ai-wrap">
      <div class="ai-head">
        <div class="ai-dot"></div>
        AI Analysis · Generated Insights
      </div>
      {rows}
    </div>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div class="sb-head">
      <div class="sb-title">Controls</div>
    </div>
    <div class="sb-section">
      <div class="sb-label">— Dataset Filters</div>
    </div>
    """, unsafe_allow_html=True)
    
    type_filter = st.selectbox("Show Type", ["All", "TV Series", "TV Mini Series"])
    decade_filter = st.selectbox("Decade", ["All", "1990s", "2000s", "2010s", "2020s"])
    age_filter = st.selectbox("Age Rating", ["All", "PG", "15", "18", "Unknown"])
    
    st.markdown("""
    <div class="sb-section" style="margin-top:1rem">
      <div class="sb-label">— Range Filters</div>
    </div>
    """, unsafe_allow_html=True)
    
    min_rating = st.slider("Min Rating", 8.5, 9.5, 8.5, 0.1, format="%.1f")
    min_votes = st.slider("Min Votes", 0, 2200000, 0, 50000, format="%d")

filtered = df.copy()
if type_filter != "All": filtered = filtered[filtered['Type'] == type_filter]
if decade_filter != "All": filtered = filtered[filtered['Decade'] == decade_filter]
if age_filter != "All": filtered = filtered[filtered['Age'] == age_filter]
filtered = filtered[filtered['Rating'] >= min_rating]
filtered = filtered[filtered['Votes'] >= min_votes]

k1, k2, k3, k4 = st.columns(4)
with k1:
    st.metric("Total Shows", f"{len(filtered):,}", "IMDB Top 250")
with k2:
    st.metric("Avg Rating", f"{filtered['Rating'].mean():.2f}", "of 10.0")
with k3:
    votes = filtered['Votes'].sum()
    st.metric("Total Votes", f"{votes/1e6:.1f}M", "Community votes")
with k4:
    st.metric("Avg Episodes", f"{int(filtered['Episodes'].mean())}", "Per show")

st.markdown("<div style='margin-bottom:1.5rem'></div>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overview", "Trends", "Deep Dive", "AI Insights", "Search"])

with tab1:
    c1, c2 = st.columns(2)
    with c1:
        cc("Top 10 Shows by Rating", "Rating · 9.5 max")
        top10 = filtered.nlargest(10, 'Rating').sort_values('Rating')
        fig1 = px.bar(top10, y='Title', x='Rating', orientation='h', color='Rating', color_continuous_scale=['#444444', '#FFFFFF'])
        fig1.update_layout(**BW_CHART, height=300, coloraxis_showscale=False)
        st.plotly_chart(fig1, use_container_width=True)
    with c2:
        cc("Rating Distribution", "Histogram · 20 bins")
        fig2 = px.histogram(filtered, x='Rating', nbins=20, color_discrete_sequence=['#FFFFFF'])
        fig2.update_layout(**BW_CHART, height=300, bargap=0.1)
        st.plotly_chart(fig2, use_container_width=True)
    c3, c4 = st.columns(2)
    with c3:
        cc("Type Distribution", "Series vs Mini Series")
        type_counts = filtered['Type'].value_counts()
        fig3 = go.Figure(data=[go.Pie(labels=type_counts.index, values=type_counts.values, hole=0.6, marker=dict(colors=['#FFFFFF', '#555555']))])
        fig3.update_layout(**BW_CHART, height=250, showlegend=True)
        st.plotly_chart(fig3, use_container_width=True)
    with c4:
        cc("Age Rating Distribution", "Content Ratings")
        age_counts = filtered['Age'].value_counts().head(8)
        fig4 = px.bar(x=age_counts.index, y=age_counts.values, color_discrete_sequence=['#FFFFFF'])
        fig4.update_layout(**BW_CHART, height=250)
        st.plotly_chart(fig4, use_container_width=True)

with tab2:
    c5, c6 = st.columns(2)
    with c5:
        cc("Shows per Decade", "Trend Analysis")
        decade_order = ['1990s', '2000s', '2010s', '2020s']
        dc = filtered['Decade'].value_counts().reindex([d for d in decade_order if d in filtered['Decade'].unique()])
        fig5 = px.bar(x=dc.index, y=dc.values, color_discrete_sequence=['#FFFFFF'])
        fig5.update_traces(texttemplate='%{y}', textposition='outside')
        fig5.update_layout(**BW_CHART, height=300)
        st.plotly_chart(fig5, use_container_width=True)
    with c6:
        cc("Avg Rating by Decade", "Quality Trend")
        rd = filtered.groupby('Decade')['Rating'].mean()
        rd = rd.reindex([d for d in decade_order if d in rd.index])
        fig6 = px.line(x=rd.index, y=rd.values, markers=True, color_discrete_sequence=['#FFFFFF'])
        fig6.update_traces(line_width=3, marker_size=8)
        fig6.update_layout(**BW_CHART, height=300)
        fig6.update_yaxes(range=[8.5, 9.1])
        st.plotly_chart(fig6, use_container_width=True)
    cc("Rating Tier Breakdown", "Elite · Excellent · Great · Good")
    tier_order = ['Elite', 'Excellent', 'Great', 'Good']
    tc = filtered['Rating_Tier'].value_counts().reindex([t for t in tier_order if t in filtered['Rating_Tier'].unique()])
    fig7 = px.bar(x=tc.index, y=tc.values, color_discrete_sequence=['#FFFFFF'])
    fig7.update_layout(**BW_CHART, height=250)
    st.plotly_chart(fig7, use_container_width=True)

with tab3:
    c7, c8 = st.columns(2)
    with c7:
        cc("Rating vs Votes", "Popularity Analysis")
        fig8 = px.scatter(filtered, x='Votes', y='Rating', size='Episodes', color='Type', hover_name='Title', color_discrete_map={'TV Series': '#FFFFFF', 'TV Mini Series': '#888888'})
        fig8.update_layout(**BW_CHART, height=350)
        st.plotly_chart(fig8, use_container_width=True)
    with c8:
        cc("Episodes vs Rating", "Length-Quality")
        fig9 = px.scatter(filtered, x='Episodes', y='Rating', hover_name='Title', hover_data={'Start_Year': True}, color_discrete_sequence=['#FFFFFF'])
        fig9.update_layout(**BW_CHART, height=350)
        st.plotly_chart(fig9, use_container_width=True)
    cc("Top 10 Shows", "Highest Rated")
    top10_table = filtered.nlargest(10, 'Rating')[['Title', 'Rating', 'Votes', 'Type', 'Start_Year', 'Episodes']]
    top10_table['Votes'] = top10_table['Votes'].apply(lambda x: f"{x/1e6:.1f}M" if x >= 1e6 else f"{x/1e3:.0f}K")
    st.dataframe(top10_table, use_container_width=True, hide_index=True)

with tab4:
    if st.button("Generate AI Insights"):
        with st.spinner("Analyzing data..."):
            insights = generate_insights(filtered)
        render_insights(insights)
    cc("Hidden Gems", "Rating ≥9.0 · Votes <200K")
    hidden = filtered[(filtered['Rating'] >= 9.0) & (filtered['Votes'] < 200000)].sort_values('Rating', ascending=False)
    if len(hidden) > 0:
        st.dataframe(hidden[['Title', 'Rating', 'Votes', 'Type', 'Start_Year']], use_container_width=True, hide_index=True)
    else:
        st.markdown("<p style='color: #555555;'>No hidden gems found with current filters.</p>", unsafe_allow_html=True)

with tab5:
    search = st.text_input("Search by show title", "")
    if search:
        results = filtered[filtered['Title'].str.contains(search, case=False, na=False)]
        for _, show in results.iterrows():
            st.markdown(f"""
            <div class="show-card">
                <div class="show-rank">#{filtered.index.get_loc(show.name) + 1}</div>
                <div class="show-title">{show['Title']}</div>
                <div class="show-stats">
                    <div>
                        <div class="show-stat-val">{show['Rating']}</div>
                        <div class="show-stat-label">Rating</div>
                    </div>
                    <div>
                        <div class="show-stat-val">{show['Start_Year']}</div>
                        <div class="show-stat-label">Year</div>
                    </div>
                    <div>
                        <div class="show-stat-val">{show['Episodes']}</div>
                        <div class="show-stat-label">Episodes</div>
                    </div>
                    <div>
                        <div class="show-stat-val">{show['Votes']:,}</div>
                        <div class="show-stat-label">Votes</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
