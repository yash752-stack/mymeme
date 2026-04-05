import streamlit as st
import random
from datetime import datetime

st.set_page_config(
    page_title="Bakwaas Central 🔥",
    page_icon="💀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bangers&family=Comic+Neue:wght@700&family=Nunito:wght@400;700;900&display=swap');

:root {
  --yellow: #FFE600;
  --red:    #FF2D2D;
  --black:  #0D0D0D;
  --white:  #F5F5F5;
  --accent: #00FF87;
}

/* hide streamlit defaults */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

body, .stApp {
  background: var(--black);
  font-family: 'Nunito', sans-serif;
  color: var(--white);
}

/* ── HERO ── */
.hero {
  background: var(--yellow);
  padding: 40px 20px 30px;
  text-align: center;
  position: relative;
  overflow: hidden;
  border-bottom: 6px solid var(--black);
}
.hero::before {
  content: "💀😂🔥😭💀😂🔥😭💀😂🔥😭";
  position: absolute; top: 4px; left: 0; right: 0;
  font-size: 18px; opacity: .35; letter-spacing: 6px;
}
.hero-title {
  font-family: 'Bangers', cursive;
  font-size: clamp(56px, 12vw, 120px);
  color: var(--black);
  letter-spacing: 4px;
  line-height: 1;
  text-shadow: 6px 6px 0 var(--red);
  margin: 0;
}
.hero-sub {
  font-family: 'Comic Neue', cursive;
  font-size: clamp(14px, 2.5vw, 22px);
  color: var(--black);
  margin-top: 8px;
  font-weight: 700;
}
.hero-badge {
  display: inline-block;
  background: var(--red);
  color: var(--yellow);
  font-family: 'Bangers', cursive;
  font-size: 18px;
  letter-spacing: 2px;
  padding: 4px 18px;
  border-radius: 4px;
  margin-top: 12px;
  border: 3px solid var(--black);
  animation: wobble 2s infinite;
}
@keyframes wobble {
  0%,100%{transform:rotate(-2deg)} 50%{transform:rotate(2deg)}
}

/* ── NAV TABS ── */
.nav-bar {
  display: flex; gap: 0;
  background: var(--black);
  border-bottom: 4px solid var(--yellow);
  overflow-x: auto;
}
.nav-tab {
  padding: 14px 28px;
  font-family: 'Bangers', cursive;
  font-size: 22px;
  letter-spacing: 1px;
  color: var(--white);
  cursor: pointer;
  border: none;
  background: transparent;
  border-right: 2px solid #222;
  transition: background .15s, color .15s;
  white-space: nowrap;
}
.nav-tab:hover, .nav-tab.active {
  background: var(--yellow);
  color: var(--black);
}

/* ── MEME CARDS ── */
.meme-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
  padding: 30px 24px;
}
.meme-card {
  background: #1a1a1a;
  border: 3px solid #333;
  border-radius: 12px;
  overflow: hidden;
  transition: transform .2s, border-color .2s;
  cursor: pointer;
}
.meme-card:hover {
  transform: translateY(-6px) rotate(1deg);
  border-color: var(--yellow);
}
.meme-card img {
  width: 100%; display: block;
  aspect-ratio: 1;
  object-fit: cover;
}
.meme-card-body {
  padding: 14px;
}
.meme-card-title {
  font-family: 'Comic Neue', cursive;
  font-size: 15px;
  font-weight: 700;
  color: var(--white);
  margin-bottom: 8px;
}
.meme-card-footer {
  display: flex; justify-content: space-between; align-items: center;
}
.reaction-btn {
  background: #2a2a2a;
  border: 2px solid #444;
  border-radius: 20px;
  color: var(--white);
  font-size: 13px;
  padding: 4px 12px;
  cursor: pointer;
  transition: background .15s;
}
.reaction-btn:hover { background: var(--yellow); color: var(--black); border-color: var(--yellow); }
.tag {
  font-size: 11px;
  background: var(--red);
  color: var(--yellow);
  border-radius: 4px;
  padding: 2px 8px;
  font-weight: 700;
}

/* ── UPLOAD SECTION ── */
.upload-box {
  background: #111;
  border: 3px dashed var(--yellow);
  border-radius: 16px;
  padding: 40px;
  text-align: center;
  margin: 24px;
}
.upload-title {
  font-family: 'Bangers', cursive;
  font-size: 36px;
  color: var(--yellow);
  letter-spacing: 2px;
  margin-bottom: 8px;
}

/* ── TICKER ── */
.ticker-wrap {
  background: var(--red);
  border-top: 3px solid var(--black);
  border-bottom: 3px solid var(--black);
  padding: 10px 0;
  overflow: hidden;
  white-space: nowrap;
}
.ticker-inner {
  display: inline-block;
  animation: scroll-left 20s linear infinite;
  font-family: 'Bangers', cursive;
  font-size: 20px;
  letter-spacing: 3px;
  color: var(--yellow);
}
@keyframes scroll-left {
  0%   { transform: translateX(100vw); }
  100% { transform: translateX(-100%); }
}

/* ── SECTION HEADER ── */
.section-header {
  font-family: 'Bangers', cursive;
  font-size: 42px;
  letter-spacing: 2px;
  color: var(--yellow);
  padding: 30px 24px 0;
  border-left: 8px solid var(--red);
  margin-left: 24px;
}

/* ── CAPTION GENERATOR ── */
.caption-box {
  background: #1a1a1a;
  border: 3px solid var(--yellow);
  border-radius: 12px;
  padding: 24px;
  margin: 24px;
}
.caption-output {
  background: var(--yellow);
  color: var(--black);
  font-family: 'Bangers', cursive;
  font-size: 28px;
  letter-spacing: 1px;
  border-radius: 8px;
  padding: 20px;
  text-align: center;
  margin-top: 16px;
  min-height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* ── STATS BAR ── */
.stats-bar {
  display: flex; gap: 0;
  background: #111;
  border-top: 3px solid var(--yellow);
  border-bottom: 3px solid var(--yellow);
}
.stat-item {
  flex: 1;
  text-align: center;
  padding: 18px 10px;
  border-right: 2px solid #222;
}
.stat-num {
  font-family: 'Bangers', cursive;
  font-size: 36px;
  color: var(--yellow);
  display: block;
}
.stat-label {
  font-size: 12px;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 1px;
}
</style>
""", unsafe_allow_html=True)

# ── DATA ────────────────────────────────────────────────────────────────────
MEMES = [
    {"title": "Why you wanna goon to me 😭🐱", "img": "cat_meme.jpg", "tag": "ICONIC", "likes": 9999},
    {"title": "Exam kal hai aur main yahan hoon 💀", "img": "https://picsum.photos/seed/meme1/400/400", "tag": "RELATABLE", "likes": 4201},
    {"title": "Mom ne wifi password change kar diya 😭", "img": "https://picsum.photos/seed/meme2/400/400", "tag": "PAIN", "likes": 3892},
    {"title": "Free food dekh ke introvert bhi aajaata hai", "img": "https://picsum.photos/seed/meme3/400/400", "tag": "FACTS", "likes": 6610},
    {"title": "Alarm 6 baje set kiya, uthha 11 baje 🤝", "img": "https://picsum.photos/seed/meme4/400/400", "tag": "MOOD", "likes": 5123},
    {"title": "Ghar waale: beta doctor bano. Main:", "img": "https://picsum.photos/seed/meme5/400/400", "tag": "DESI", "likes": 7834},
    {"title": "3 AM ka hunger alag hi level ka hota hai", "img": "https://picsum.photos/seed/meme6/400/400", "tag": "NOCTURNAL", "likes": 2900},
    {"title": "Best friend ne read kiya reply nahi kiya 🔪", "img": "https://picsum.photos/seed/meme7/400/400", "tag": "BETRAYAL", "likes": 4455},
    {"title": "Monday morning aur phir Sunday yaad aana", "img": "https://picsum.photos/seed/meme8/400/400", "tag": "SUFFERING", "likes": 8001},
    {"title": "Presentation mein 'any questions?' 😶", "img": "https://picsum.photos/seed/meme9/400/400", "tag": "RELATABLE", "likes": 3311},
]

CAPTIONS = [
    "POV: Ghar walon ne tujhe IT mein daalna tha par tune meme career choose kiya 💀",
    "When the chai hits different at 2 AM and suddenly you're a philosopher 🫖",
    "Main khush hoon — actually nahi hoon — actually pata nahi 😐",
    "Ye post itna relatable hai ki mujhe legal action leni chahiye 🔥",
    "Salary credit aur phir UPI pe paise gayab — same day 😭",
    "Bhai tune meri life screenshot kar li kya? 👀",
    "Exam hall mein 'all the best' bolta hai aur khud nahi likhta 💀",
    "Ghar ka khana nahi tha toh Swiggy — wallet ka last rites 🪦",
    "Ek din main bhi famous ho jaaunga... maybe next year 🙏",
    "Skills: procrastinating, overthinking, memes banana. Weaknesses: sab kuch baaki 🫡",
]

TICKER_TEXT = "💀 BAKWAAS CENTRAL 🔥 INDIA KA NO.1 MEME HUB 😭 FOLLOW KARO WARNA SHAYAD KOI FARAK NA PADE 👀 DAILY FRESH MEMES 🔥 " * 3

# ── SESSION STATE ────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "home"
if "likes" not in st.session_state:
    st.session_state.likes = {i: m["likes"] for i, m in enumerate(MEMES)}
if "caption" not in st.session_state:
    st.session_state.caption = "Yahan apna meme topic likho aur magic dekho ✨"

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <h1 class="hero-title">BAKWAAS<br>CENTRAL</h1>
  <p class="hero-sub">India ka sabse bekar — par sabse funny — meme hub 🇮🇳</p>
  <span class="hero-badge">💀 EST. 2025 · NO CHILL ZONE 💀</span>
</div>
""", unsafe_allow_html=True)

# ── TICKER ───────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="ticker-wrap">
  <span class="ticker-inner">{TICKER_TEXT}</span>
</div>
""", unsafe_allow_html=True)

# ── NAV ──────────────────────────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("🏠  HOME", use_container_width=True):
        st.session_state.page = "home"
with col2:
    if st.button("🔥  TRENDING", use_container_width=True):
        st.session_state.page = "trending"
with col3:
    if st.button("✍️  CAPTION GEN", use_container_width=True):
        st.session_state.page = "caption"
with col4:
    if st.button("📤  UPLOAD", use_container_width=True):
        st.session_state.page = "upload"

st.markdown("<hr style='border-color:#222;margin:0'>", unsafe_allow_html=True)

# ── STATS BAR ────────────────────────────────────────────────────────────────
total_likes = sum(st.session_state.likes.values())
st.markdown(f"""
<div class="stats-bar">
  <div class="stat-item"><span class="stat-num">{len(MEMES)}</span><span class="stat-label">Memes Live</span></div>
  <div class="stat-item"><span class="stat-num">{total_likes:,}</span><span class="stat-label">Total Likes 💀</span></div>
  <div class="stat-item"><span class="stat-num">24/7</span><span class="stat-label">Bakwaas Mode</span></div>
  <div class="stat-item"><span class="stat-num">∞</span><span class="stat-label">Cringe Level</span></div>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# PAGE: HOME
# ════════════════════════════════════════════════════════════════════════════
if st.session_state.page == "home":
    st.markdown('<div class="section-header">🔥 FRESH MEMES</div>', unsafe_allow_html=True)

    cols = st.columns(3)
    for i, meme in enumerate(MEMES):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="meme-card">
              <img src="{meme['img']}" alt="meme"/>
              <div class="meme-card-body">
                <div class="meme-card-title">{meme['title']}</div>
                <div class="meme-card-footer">
                  <span class="tag">{meme['tag']}</span>
                </div>
              </div>
            </div>
            """, unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                if st.button(f"💀 {st.session_state.likes[i]}", key=f"like_{i}", use_container_width=True):
                    st.session_state.likes[i] += 1
                    st.rerun()
            with c2:
                if st.button("📤 Share", key=f"share_{i}", use_container_width=True):
                    st.toast("Link copy ho gaya bhai! 🔥", icon="📋")

# ════════════════════════════════════════════════════════════════════════════
# PAGE: TRENDING
# ════════════════════════════════════════════════════════════════════════════
elif st.session_state.page == "trending":
    st.markdown('<div class="section-header">📈 TRENDING ABHI</div>', unsafe_allow_html=True)

    sorted_memes = sorted(enumerate(MEMES), key=lambda x: st.session_state.likes[x[0]], reverse=True)

    for rank, (i, meme) in enumerate(sorted_memes):
        c1, c2, c3 = st.columns([1, 3, 1])
        with c1:
            medal = ["🥇","🥈","🥉"] [rank] if rank < 3 else f"#{rank+1}"
            st.markdown(f"<div style='font-family:Bangers;font-size:48px;text-align:center;color:var(--yellow,#FFE600);padding-top:20px'>{medal}</div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"""
            <div style='background:#1a1a1a;border:2px solid #333;border-radius:10px;padding:16px;margin:8px 0'>
              <div style='font-family:Comic Neue,cursive;font-weight:700;font-size:16px'>{meme['title']}</div>
              <div style='margin-top:8px'><span class='tag'>{meme['tag']}</span></div>
            </div>
            """, unsafe_allow_html=True)
        with c3:
            st.markdown(f"<div style='font-family:Bangers;font-size:28px;color:#FFE600;text-align:center;padding-top:20px'>💀 {st.session_state.likes[i]:,}</div>", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════════════
# PAGE: CAPTION GENERATOR
# ════════════════════════════════════════════════════════════════════════════
elif st.session_state.page == "caption":
    st.markdown('<div class="section-header">✍️ MEME CAPTION GENERATOR</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="caption-box">
      <p style='color:#888;margin-bottom:4px;font-size:13px;text-transform:uppercase;letter-spacing:1px'>Kya meme hai tera?</p>
    </div>
    """, unsafe_allow_html=True)

    topic = st.text_input("", placeholder="e.g. exam stress, ghar ka khana, Monday morning...", label_visibility="collapsed")

    col1, col2 = st.columns([1, 1])
    with col1:
        generate = st.button("🔥 CAPTION BANAO", use_container_width=True)
    with col2:
        lucky = st.button("🎲 RANDOM CAPTION", use_container_width=True)

    if generate and topic:
        templates = [
            f"POV: {topic} aur tujhe lagta tha sab theek hoga 💀",
            f"Bhai {topic} ne toh life barbad kar di but we move 😭🔥",
            f"When {topic} hits and you just stare at the ceiling at 3 AM 😶",
            f"{topic}? In this economy? In this family? In this body? 😐",
            f"Main {topic} se recover kar raha tha phir aur {topic} aa gaya 🪦",
        ]
        st.session_state.caption = random.choice(templates)
    elif lucky:
        st.session_state.caption = random.choice(CAPTIONS)
    elif generate and not topic:
        st.warning("Bhai kuch toh likho pehle! 😭")

    st.markdown(f"""
    <div style='background:var(--yellow,#FFE600);color:#0D0D0D;font-family:Bangers,cursive;
    font-size:clamp(20px,3vw,30px);letter-spacing:1px;border-radius:10px;
    padding:24px;text-align:center;margin-top:20px;border:4px solid #0D0D0D'>
      {st.session_state.caption}
    </div>
    """, unsafe_allow_html=True)

    if st.button("📋 COPY KARO", use_container_width=True):
        st.toast("Caption copy ho gaya! Insta pe daal de 🚀", icon="✅")

# ════════════════════════════════════════════════════════════════════════════
# PAGE: UPLOAD
# ════════════════════════════════════════════════════════════════════════════
elif st.session_state.page == "upload":
    st.markdown('<div class="section-header">📤 APNA MEME DAAL</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style='background:#111;border:3px dashed #FFE600;border-radius:16px;
    padding:40px;text-align:center;margin:24px'>
      <div style='font-family:Bangers,cursive;font-size:36px;color:#FFE600;letter-spacing:2px'>
        📸 MEME UPLOAD KRO
      </div>
      <p style='color:#888;margin-top:8px'>JPG, PNG, GIF — sab chalta hai bhai</p>
    </div>
    """, unsafe_allow_html=True)

    uploaded = st.file_uploader("Apna meme upload karo", type=["jpg","jpeg","png","gif","webp"], label_visibility="collapsed")

    if uploaded:
        st.image(uploaded, use_container_width=True)
        title_input = st.text_input("Meme ka title / caption:")
        tag_input = st.selectbox("Tag chuno:", ["RELATABLE","DESI","PAIN","MOOD","FACTS","NOCTURNAL","BETRAYAL","SUFFERING"])

        if st.button("🚀 PUBLISH KRO", use_container_width=True):
            if title_input:
                st.balloons()
                st.success(f"✅ '{title_input}' live ho gaya bhai! Ab tujhe bhi famous hone ki ummeed hai 😭🔥")
            else:
                st.error("Bhai title toh daal pehle 😤")

# ── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div style='background:#0D0D0D;border-top:4px solid #FFE600;padding:30px;
text-align:center;margin-top:40px'>
  <div style='font-family:Bangers,cursive;font-size:32px;color:#FFE600;letter-spacing:3px'>
    BAKWAAS CENTRAL 💀
  </div>
  <p style='color:#555;font-size:13px;margin-top:8px'>
    Made with 0% effort aur 100% cringe · India 🇮🇳 · No rights reserved, steal kar le bhai
  </p>
</div>
""", unsafe_allow_html=True)
