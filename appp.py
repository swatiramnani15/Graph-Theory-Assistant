# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 09:20:17 2026

@author: swati
"""
import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
page_title="Graph Theory Assistant",
page_icon="🕸️",
layout="wide",
initial_sidebar_state="collapsed",
)

# ── CSS ────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600;700&family=DM+Mono:wght@300;400;500&display=swap');

/* ── Reset & base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
background: #080c10 !important;
color: #e8e0d0 !important;
}

[data-testid="stAppViewContainer"] {
background: #080c10 !important;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] { display: none !important; }

[data-testid="stMain"] > div { padding: 0 !important; }
[data-testid="block-container"] { padding: 0 !important; max-width: 100% !important; }

/* ── Animated SVG background ── */
.bg-canvas {
position: fixed;
inset: 0;
z-index: 0;
overflow: hidden;
pointer-events: none;
}

.bg-canvas svg {
width: 100%; height: 100%;
}

/* ── Grain overlay ── */
.grain {
position: fixed;
inset: 0;
z-index: 1;
pointer-events: none;
opacity: 0.035;
background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
background-repeat: repeat;
background-size: 128px 128px;
}

/* ── Main wrapper ── */
.site-wrapper {
position: relative;
z-index: 2;
min-height: 100vh;
font-family: 'Cormorant Garamond', Georgia, serif;
overflow-x: hidden;
}

/* ── Hero ── */
.hero {
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
min-height: 100vh;
padding: 4rem 2rem 2rem;
text-align: center;
position: relative;
}

.eyebrow {
font-family: 'DM Mono', monospace;
font-size: 0.72rem;
letter-spacing: 0.25em;
text-transform: uppercase;
color: #6ee7b7;
margin-bottom: 1.8rem;
opacity: 0;
animation: fadeUp 0.8s ease forwards 0.2s;
}

.hero-title {
font-size: clamp(3.5rem, 9vw, 8rem);
font-weight: 300;
line-height: 0.95;
color: #f5f0e8;
letter-spacing: -0.02em;
opacity: 0;
animation: fadeUp 0.9s ease forwards 0.4s;
}

.hero-title em {
font-style: italic;
font-weight: 700;
color: #6ee7b7;
}

.hero-sub {
margin-top: 2rem;
max-width: 560px;
font-size: 1.18rem;
font-weight: 300;
line-height: 1.75;
color: #a09888;
opacity: 0;
animation: fadeUp 0.9s ease forwards 0.65s;
}

.hero-divider {
width: 1px;
height: 64px;
background: linear-gradient(to bottom, #6ee7b7, transparent);
margin: 3rem auto 0;
opacity: 0;
animation: fadeUp 0.9s ease forwards 0.9s;
}

/* ── CTA Button ── */
.cta-wrap {
margin-top: 3rem;
opacity: 0;
animation: fadeUp 0.9s ease forwards 1.1s;
}

.cta-btn {
display: inline-flex;
align-items: center;
gap: 0.75rem;
padding: 1rem 2.4rem;
background: transparent;
border: 1px solid #6ee7b7;
color: #6ee7b7;
font-family: 'DM Mono', monospace;
font-size: 0.82rem;
letter-spacing: 0.12em;
text-transform: uppercase;
text-decoration: none;
cursor: pointer;
position: relative;
transition: color 0.3s ease, background 0.3s ease;
overflow: hidden;
}

.cta-btn::before {
content: '';
position: absolute;
inset: 0;
background: #6ee7b7;
transform: scaleX(0);
transform-origin: left;
transition: transform 0.35s cubic-bezier(0.4,0,0.2,1);
z-index: -1;
}

.cta-btn:hover { color: #080c10; }
.cta-btn:hover::before { transform: scaleX(1); }

.cta-arrow {
display: inline-block;
transition: transform 0.3s ease;
}
.cta-btn:hover .cta-arrow { transform: translateX(4px); }

/* ── Section base ── */
.section {
padding: 7rem 2rem;
max-width: 1140px;
margin: 0 auto;
}

.section-label {
font-family: 'DM Mono', monospace;
font-size: 0.68rem;
letter-spacing: 0.3em;
text-transform: uppercase;
color: #6ee7b7;
margin-bottom: 3.5rem;
display: flex;
align-items: center;
gap: 1rem;
}

.section-label::after {
content: '';
flex: 1;
height: 1px;
background: linear-gradient(to right, #6ee7b740, transparent);
}

/* ── About section ── */
.about-grid {
display: grid;
grid-template-columns: 1fr 1fr;
gap: 5rem;
align-items: start;
}

@media (max-width: 768px) {
.about-grid { grid-template-columns: 1fr; gap: 3rem; }
}

.about-heading {
font-size: clamp(2rem, 4vw, 3.2rem);
font-weight: 300;
line-height: 1.15;
color: #f5f0e8;
margin-bottom: 2rem;
}

.about-heading strong {
font-weight: 700;
font-style: italic;
color: #6ee7b7;
}

.about-text {
font-size: 1.05rem;
line-height: 1.85;
color: #9a9080;
margin-bottom: 1.5rem;
}

/* ── Feature cards ── */
.features-grid {
display: grid;
grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
gap: 1.5px;
background: #1a1f26;
border: 1px solid #1a1f26;
overflow: hidden;
}

.feat-card {
background: #0d1117;
padding: 2.5rem 2rem;
transition: background 0.3s ease;
position: relative;
overflow: hidden;
}

.feat-card::before {
content: '';
position: absolute;
top: 0; left: 0; right: 0;
height: 2px;
background: #6ee7b7;
transform: scaleX(0);
transform-origin: left;
transition: transform 0.4s ease;
}

.feat-card:hover { background: #111820; }
.feat-card:hover::before { transform: scaleX(1); }

.feat-icon {
font-size: 1.8rem;
margin-bottom: 1.25rem;
display: block;
}

.feat-title {
font-size: 1.2rem;
font-weight: 600;
color: #f0e8dc;
margin-bottom: 0.75rem;
font-style: italic;
}

.feat-desc {
font-family: 'DM Mono', monospace;
font-size: 0.78rem;
line-height: 1.7;
color: #6a6258;
}

/* ── Topics ── */
.topics-section {
border-top: 1px solid #181e24;
padding: 7rem 2rem;
max-width: 1140px;
margin: 0 auto;
}

.topics-list {
display: flex;
flex-wrap: wrap;
gap: 0.75rem;
margin-top: 1rem;
}

.topic-tag {
font-family: 'DM Mono', monospace;
font-size: 0.75rem;
letter-spacing: 0.06em;
padding: 0.45rem 1rem;
border: 1px solid #232c36;
color: #6a7a8a;
background: transparent;
transition: border-color 0.25s, color 0.25s;
cursor: default;
}

.topic-tag:hover {
border-color: #6ee7b7;
color: #6ee7b7;
}

/* ── Chat CTA section ── */
.chat-section {
border-top: 1px solid #181e24;
padding: 8rem 2rem;
text-align: center;
}

.chat-heading {
font-size: clamp(2.2rem, 5vw, 4.5rem);
font-weight: 300;
color: #f5f0e8;
line-height: 1.1;
margin-bottom: 1.5rem;
}

.chat-heading em {
font-style: italic;
font-weight: 700;
color: #6ee7b7;
}

.chat-sub {
font-size: 1.05rem;
color: #7a7060;
max-width: 480px;
margin: 0 auto 3rem;
line-height: 1.75;
}

/* ── Footer ── */
.site-footer {
border-top: 1px solid #111820;
padding: 2.5rem 2rem;
display: flex;
justify-content: space-between;
align-items: center;
max-width: 1140px;
margin: 0 auto;
}

.footer-brand {
font-family: 'DM Mono', monospace;
font-size: 0.72rem;
letter-spacing: 0.15em;
color: #3a4450;
text-transform: uppercase;
}

.footer-note {
font-family: 'DM Mono', monospace;
font-size: 0.68rem;
color: #2a3038;
}

/* ── Keyframes ── */
@keyframes fadeUp {
from { opacity: 0; transform: translateY(28px); }
to { opacity: 1; transform: translateY(0); }
}

@keyframes float {
0%, 100% { transform: translateY(0px); }
50% { transform: translateY(-12px); }
}

@keyframes pulse-ring {
0% { transform: scale(0.9); opacity: 0.6; }
70% { transform: scale(1.4); opacity: 0; }
100% { transform: scale(0.9); opacity: 0; }
}

/* ── Graph node decoration ── */
.node-pulse {
position: absolute;
width: 10px; height: 10px;
border-radius: 50%;
background: #6ee7b7;
}

.node-pulse::after {
content: '';
position: absolute;
inset: -4px;
border-radius: 50%;
border: 1px solid #6ee7b7;
animation: pulse-ring 2.5s cubic-bezier(0.215, 0.61, 0.355, 1) infinite;
}

/* ── Author ── */
.author-section {
    border-top: 1px solid #181e24;
    padding: 7rem 2rem;
    max-width: 1140px;
    margin: 0 auto;
}

.author-card {
    display: flex;
    align-items: center;
    gap: 3rem;
    background: #0d1117;
    border: 1px solid #1a1f26;
    padding: 3rem;
    position: relative;
    overflow: hidden;
}

.author-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 3px;
    height: 100%;
    background: linear-gradient(to bottom, #6ee7b7, transparent);
}

.author-avatar {
    width: 90px;
    height: 90px;
    border-radius: 50%;
    background: transparent;
    border: 1px solid #6ee7b7;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'DM Mono', monospace;
    font-size: 1.1rem;
    color: #6ee7b7;
    letter-spacing: 0.1em;
    flex-shrink: 0;
}

.author-name {
    font-size: 1.9rem;
    font-weight: 600;
    font-style: italic;
    color: #f5f0e8;
    margin-bottom: 0.4rem;
}

.author-institution {
    font-family: 'DM Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #6ee7b7;
    margin-bottom: 1.2rem;
}

.author-bio {
    font-size: 1rem;
    line-height: 1.8;
    color: #7a7060;
    max-width: 580px;
}

@media (max-width: 600px) {
    .author-card { flex-direction: column; text-align: center; gap: 1.5rem; }
    .author-card::before { width: 100%; height: 3px; top: 0; left: 0; }
}

</style>
""", unsafe_allow_html=True)

# ── SVG Graph Background ──────────────────────────────────────────────────────
bg_svg = """
<div class="bg-canvas">
<svg viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
<defs>
<radialGradient id="glow1" cx="50%" cy="50%" r="50%">
<stop offset="0%" stop-color="#6ee7b7" stop-opacity="0.12"/>
<stop offset="100%" stop-color="#6ee7b7" stop-opacity="0"/>
</radialGradient>
<radialGradient id="glow2" cx="50%" cy="50%" r="50%">
<stop offset="0%" stop-color="#3b82f6" stop-opacity="0.08"/>
<stop offset="100%" stop-color="#3b82f6" stop-opacity="0"/>
</radialGradient>
<filter id="blur4"><feGaussianBlur stdDeviation="4"/></filter>
</defs>

<!-- Ambient glows -->
<ellipse cx="300" cy="400" rx="360" ry="360" fill="url(#glow2)"/>
<ellipse cx="1100" cy="500" rx="320" ry="320" fill="url(#glow1)"/>

<!-- Graph edges -->
<g stroke="#6ee7b730" stroke-width="1" fill="none">
<line x1="180" y1="220" x2="420" y2="310"/>
<line x1="420" y1="310" x2="660" y2="180"/>
<line x1="660" y1="180" x2="880" y2="340"/>
<line x1="880" y1="340" x2="1100" y2="220"/>
<line x1="1100" y1="220" x2="1280" y2="420"/>
<line x1="420" y1="310" x2="560" y2="520"/>
<line x1="560" y1="520" x2="780" y2="580"/>
<line x1="780" y1="580" x2="880" y2="340"/>
<line x1="780" y1="580" x2="960" y2="700"/>
<line x1="960" y1="700" x2="1200" y2="680"/>
<line x1="1200" y1="680" x2="1280" y2="420"/>
<line x1="180" y1="220" x2="320" y2="600"/>
<line x1="320" y1="600" x2="560" y2="520"/>
<line x1="660" y1="180" x2="780" y2="580"/>
<line x1="320" y1="600" x2="960" y2="700"/>
<line x1="1100" y1="220" x2="1200" y2="680"/>
</g>

<!-- Graph nodes -->
<g filter="url(#blur4)">
<circle cx="180" cy="220" r="18" fill="#6ee7b7" opacity="0.35"/>
<circle cx="660" cy="180" r="14" fill="#6ee7b7" opacity="0.3"/>
<circle cx="1100" cy="220" r="16" fill="#6ee7b7" opacity="0.28"/>
<circle cx="780" cy="580" r="20" fill="#3b82f6" opacity="0.25"/>
<circle cx="960" cy="700" r="12" fill="#6ee7b7" opacity="0.22"/>
</g>

<!-- Crisp nodes -->
<g fill="#6ee7b7">
<circle cx="180" cy="220" r="3.5" opacity="0.7"/>
<circle cx="420" cy="310" r="2.5" opacity="0.5"/>
<circle cx="660" cy="180" r="3" opacity="0.65"/>
<circle cx="880" cy="340" r="2.5" opacity="0.5"/>
<circle cx="1100" cy="220" r="3.5" opacity="0.7"/>
<circle cx="1280" cy="420" r="2.5" opacity="0.45"/>
<circle cx="560" cy="520" r="3" opacity="0.55"/>
<circle cx="780" cy="580" r="4" opacity="0.75"/>
<circle cx="320" cy="600" r="2.5" opacity="0.45"/>
<circle cx="960" cy="700" r="3" opacity="0.6"/>
<circle cx="1200" cy="680" r="2.5" opacity="0.5"/>
</g>
</svg>
</div>
<div class="grain"></div>
"""

CHATBOT_URL = "https://cdn.botpress.cloud/webchat/v3.6/shareable.html?configUrl=https://files.bpcontent.cloud/2026/03/07/10/20260307104758-SMSFRWPS.json"

topics = [
"Eulerian Paths", "Hamiltonian Cycles", "Dijkstra's Algorithm",
"Breadth-First Search", "Depth-First Search", "Minimum Spanning Trees",
"Kruskal's Algorithm", "Prim's Algorithm", "Planar Graphs",
"Graph Coloring", "Bipartite Graphs", "Adjacency Matrices",
"Trees & Forests", "Graph Isomorphism",
"Shortest Paths", "Cycle or Path Detection", "Hierholzer's Algorithm"
]

topics_html = "".join(f'<span class="topic-tag">{t}</span>' for t in topics)

html_content = f"""
{bg_svg}
<div class="site-wrapper">

<!-- ── HERO ── -->
<section class="hero">
<p class="eyebrow">⬡ AI-Powered · Graph Theory · Assistant ⬡</p>
<h1 class="hero-title" align="center">
Graph<br>Theory<br>Assistant
</h1>
<p class="hero-sub">
An intelligent chatbot helping students through the world of graphs and the algorithms that connect them.
</p>
<div class="hero-divider"></div>
<div class="cta-wrap">
<a class="cta-btn" href="{CHATBOT_URL}" target="_blank">
Open the Chatbot<span class="cta-arrow">→</span>
</a>
</div>
</section>

<!-- ── ABOUT ── -->
<div class="section">
<p class="section-label">About</p>
<div class="about-grid">
<div>
<h2 class="about-heading">
Your personal tutor for <strong>Graph Theory</strong>
</h2>
<p class="about-text">
Graph Theory Assistant is a purpose-built AI chatbot designed to make
one of  mathematics's most beautiful disciplines approachable and
engaging — whether you're a student, researcher, or curious mind.
</p>
<p class="about-text">
Whether you're exploring the basics of vertices and edges or diving deep into graph algorithms, the assistant is here to guide you. Complex problems become clear through step-by-step reasoning, proofs are explained in plain language, and understanding is built naturally along the way. 
</p>
<p class="about-text">
Upload a graph directly and let the assistant do the heavy lifting — identifying paths, walks, Eulerian trails, Hamiltonian Cycles, Connectedness, and much more!
</p>
</div>
<div class="features-grid">
<div class="feat-card">
<span class="feat-icon">🔍</span>
<p class="feat-title">Concept Explanations</p>
<p class="feat-desc">From basic definitions to advanced theorems — every concept explained clearly with examples.</p>
</div>
<div class="feat-card">
<span class="feat-icon">🔍</span>
<p class="feat-title">Graph Upload & Analysis</p>
<p class="feat-desc"> Bring your own graphs to the conversation — the assistant will analyse them for you! </p>
</div>
<div class="feat-card">
<span class="feat-icon">⚙️</span>
<p class="feat-title">Algorithm Walkthroughs</p>
<p class="feat-desc">Step-by-step traces of BFS, DFS, Dijkstra, Kruskal, and many more.</p>
</div>
<div class="feat-card">
<span class="feat-icon">🧩</span>
<p class="feat-title">Problem Solving</p>
<p class="feat-desc">Stuck on an assignment or a research challenge? The assistant works through every problem with you, step by step.</p>
</div>
</div>
</div>
</div>

<!-- ── TOPICS ── -->
<div class="topics-section">
<p class="section-label">Some of the Topics Covered</p>
<div class="topics-list">
{topics_html}
</div>
</div>

<!-- ── AUTHOR ── -->
  <div class="author-section">
    <p class="section-label">Creator</p>
    <div class="author-card">
      <div class="author-avatar">SGR</div>
      <div class="author-info">
        <p class="author-name">Swati G Ramnani</p>
        <p class="author-institution">St. Xavier's College, Ahmedabad</p>
        <p class="author-bio">
          With a deep passion for Mathematics, Swati built the Graph Theory Assistant to transform one of mathematics's most elegant disciplines into something every curious mind can explore and enjoy.
        </p>
      </div>
    </div>
  </div>

<!-- ── CHAT CTA ── -->
<div class="chat-section">
<h2 class="chat-heading">Ready to explore<br>the <em>graph universe</em>?</h2>
<p class="chat-sub">
Launch the assistant and start your conversation. No sign-up required.
</p>
<a class="cta-btn" href="{CHATBOT_URL}" target="_blank">
Start Chatting <span class="cta-arrow">→</span>
</a>
</div>


<!-- ── FOOTER ── -->
<footer class="site-footer">
<span class="footer-brand">Graph Theory Assistant</span>
<span class="footer-note">Powered by Botpress · Built with Streamlit</span>
</footer>

</div>
"""

st.markdown(html_content, unsafe_allow_html=True)