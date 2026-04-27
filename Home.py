import streamlit as st
import os
import base64

# --- 1. 初始化 Session State ---
if 'animation_played' not in st.session_state:
    st.session_state.animation_played = False

# --- 2. 基础数据统计 ---
STATS = {
    "total_academic": 23,
    "projects": 4
}


def get_image_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return None


# --- 3. 页面配置 ---
st.set_page_config(page_title="所向 (Xiang Suo)", page_icon="🎓", layout="wide")

# --- 4. 核心 CSS 样式 (极致大字号与高级感) ---
st.markdown("""
    <style>
    /* 强制透明背景以显示动态效果 */
    .stApp, .stAppViewContainer, .stMain { background-color: transparent !important; }

    /* --- 动态背景样式 --- */
    .background-container {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        z-index: -2; background: linear-gradient(135deg, #F9FAFB 0%, #F0F4F8 100%);
        overflow: hidden;
    }
    .blob {
        position: absolute; width: 600px; height: 600px;
        background: radial-gradient(circle, rgba(49, 130, 206, 0.08) 0%, rgba(255, 255, 255, 0) 70%);
        border-radius: 50%; animation: float 25s infinite alternate ease-in-out;
    }
    .blob-1 { top: -10%; left: -5%; }
    .blob-2 { bottom: -10%; right: -5%; animation-delay: -5s; }
    .blob-3 { top: 40%; right: 10%; animation-delay: -10s; width: 400px; height: 400px; }
    .grid-overlay {
        position: absolute; width: 100%; height: 100%;
        background-image: radial-gradient(rgba(49, 130, 206, 0.04) 1px, transparent 1px);
        background-size: 50px 50px; z-index: -1;
    }
    @keyframes float { 0% { transform: translate(0, 0) scale(1); } 100% { transform: translate(60px, 80px) scale(1.1); } }

    /* 隐藏导航栏 */
    [data-testid="stSidebar"], [data-testid="collapsedControl"] { display: none; }
    .stMain { margin-left: 0px; }

    /* --- 欢迎屏 --- */
    #welcome-screen {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        background-color: white; display: flex; flex-direction: column;
        justify-content: center; align-items: center; z-index: 9999;
        animation: fadeOut 1.5s ease-in-out forwards; animation-delay: 1.5s;
    }
    .welcome-text { font-size: 100px; font-weight: 800; color: #1A202C; opacity: 0; animation: fadeInText 1s ease-in-out forwards; }
    .welcome-sub { font-size: 50px; color: #3182CE; margin-top: 10px; opacity: 0; animation: fadeInText 1s ease-in-out forwards; animation-delay: 0.5s; }
    @keyframes fadeInText { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes fadeOut { 0% { opacity: 1; } 90% { opacity: 1; transform: translateY(0); } 100% { opacity: 0; transform: translateY(-100vh); visibility: hidden; } }

    /* --- 标题与特大方框卡片 --- */
    .section-title { 
        font-size: 42px; /* 进一步增大标题 */
        font-weight: 800; 
        color: #1A202C; 
        padding-left: 20px; 
        border-left: 12px solid #3182CE; 
        margin: 70px 0 40px 0; 
    }

    .info-card {
        background: white; 
        padding: 50px 40px; /* 超大内边距 */
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
        border-top: 6px solid #3182CE; 
        margin-bottom: 30px; 
        transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        min-height: 350px; /* 增加高度确保方形感 */
        display: flex;
        flex-direction: column;
        justify-content: center; 
        text-align: center;
    }
    .info-card:hover { transform: translateY(-15px); box-shadow: 0 25px 50px rgba(0, 0, 0, 0.1); }

    .card-title { font-size: 32px; font-weight: 800; color: #1A202C; margin-bottom: 15px; }
    .title-link { text-decoration: none; color: inherit; transition: 0.3s; }
    .title-link:hover { color: #3182CE; text-decoration: underline; }

    .card-subtitle { color: #3182CE; font-weight: 700; font-size: 24px; margin-bottom: 20px; }
    .card-text { color: #4A5568; font-size: 20px; line-height: 1.7; font-weight: 500; }

    /* --- 成果展示特大方框 --- */
    .stat-container {
        background: white; padding: 60px; border-radius: 24px;
        text-align: center; box-shadow: 0 6px 30px rgba(0,0,0,0.04);
        border: 1px solid #E2E8F0; transition: all 0.4s ease;
        min-height: 380px; 
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .stat-container:hover { transform: translateY(-15px); border-color: #3182CE; box-shadow: 0 30px 60px rgba(0,0,0,0.1); }
    .stat-link { font-size: 110px; font-weight: 800; color: #3182CE; text-decoration: none; line-height: 0.9; }
    .stat-link:hover { color: #1A202C; }
    .stat-lab { font-size: 36px; font-weight: 800; color: #2D3748; margin-top: 25px; }

    header, footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- 5. 渲染动态背景与欢迎屏 ---
st.markdown(
    '<div class="background-container"><div class="grid-overlay"></div><div class="blob blob-1"></div><div class="blob blob-2"></div><div class="blob blob-3"></div></div>',
    unsafe_allow_html=True)

if not st.session_state.animation_played:
    st.markdown(
        '<div id="welcome-screen"><div class="welcome-text">所 向</div><div class="welcome-sub">上海体育大学 · 智慧体育工程学院</div></div>',
        unsafe_allow_html=True)
    st.session_state.animation_played = True

# --- 6. 主内容展示 ---
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# A. 头部名片 (特大号)
img_path = "my_avatar.jpg"
img_base64 = get_image_base64(img_path)
if img_base64:
    st.markdown(f"""
        <div style="display: flex; align-items: center; justify-content: center; gap: 80px; margin: 80px 0;">
            <img src="data:image/jpeg;base64,{img_base64}" 
                 style="width: 250px; height: 250px; border-radius: 50%; object-fit: contain; 
                        background-color: white; border: 10px solid white; box-shadow: 0 20px 45px rgba(0,0,0,0.15);">
            <div style="text-align: left;">
                <h1 style="margin: 0; font-size: 72px; color: #1A202C; font-weight: 900;">所 向 (Xiang Suo)</h1>
                <h3 style="margin: 15px 0 25px 0; color: #3182CE; font-weight: 700; font-size: 32px;">上海体育大学 智慧体育工程学院 教师</h3>
                <p style="margin: 0; color: #4A5568; font-size: 22px; line-height: 1.8;">
                    🏃 <b>研究方向</b>：体育工程、运动表现分析、AI & 大模型应用<br>
                    📧 <b>电子邮箱</b>：<a href="mailto:xiang_suo@sus.edu.cn" style="color:#4A5568; text-decoration:none;">xiang_suo@sus.edu.cn</a><br>
                    📍 <b>办公地址</b>：上海市杨浦区清源环路588号
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# B. 教育背景
st.markdown('<div class="section-title">教育背景 (Education)</div>', unsafe_allow_html=True)
e1, e2, e3 = st.columns(3)
with e1: st.markdown(
    """<div class="info-card"><div class="card-title"><a href="教育与历程" target="_self" class="title-link">上海体育大学</a></div><div class="card-subtitle">博士 (2021-2025)</div><div class="card-text">体育教育训练学</div></div>""",
    unsafe_allow_html=True)
with e2: st.markdown(
    """<div class="info-card"><div class="card-title"><a href="教育与历程" target="_self" class="title-link">新南威尔士大学</a></div><div class="card-subtitle">硕士 (2018-2021)</div><div class="card-text">Engineering Science</div></div>""",
    unsafe_allow_html=True)
with e3: st.markdown(
    """<div class="info-card"><div class="card-title"><a href="教育与历程" target="_self" class="title-link">北京航空航天大学</a></div><div class="card-subtitle">学士 (2008-2012)</div><div class="card-text">机械工程及自动化</div></div>""",
    unsafe_allow_html=True)

# C. 工作经历
st.markdown('<div class="section-title">工作经历 (Work Experience)</div>', unsafe_allow_html=True)
w1, w2 = st.columns(2)
with w1: st.markdown(
    """<div class="info-card"><div class="card-title"><a href="教育与历程" target="_self" class="title-link">上海体育大学</a></div><div class="card-subtitle">教师 | 2025.08 - 至今</div><div class="card-text">负责智慧体育教学、视觉算法及大模型科研工作。</div></div>""",
    unsafe_allow_html=True)
with w2: st.markdown(
    """<div class="info-card"><div class="card-title"><a href="教育与历程" target="_self" class="title-link">中国航发北京长空</a></div><div class="card-subtitle">工艺工程师 | 2012-2016</div><div class="card-text">负责直升机发动机部件加工及总装设计。</div></div>""",
    unsafe_allow_html=True)

st.write("---")

# D. 核心成果概览 (巨型数字)
st.markdown('<div class="section-title">核心成果概览 (Research Summary)</div>', unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1: st.markdown(
    f"""<div class="stat-container"><a href="学术成果" target="_self" class="stat-link">{STATS['total_academic']}</a><div class="stat-lab">学术成果总数</div></div>""",
    unsafe_allow_html=True)
with c2: st.markdown(
    f"""<div class="stat-container"><a href="科研与项目" target="_self" class="stat-link">{STATS['projects']}</a><div class="stat-lab">核心科研项目</div></div>""",
    unsafe_allow_html=True)

st.write("")
st.caption("© 2024 所向 | 上海体育大学 智慧体育工程学院")
st.markdown('</div>', unsafe_allow_html=True)