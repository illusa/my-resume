import streamlit as st

# --- 1. 页面配置 ---
st.set_page_config(page_title="学术成果 | 所向", layout="wide")

# --- 2. 统一视觉风格 CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #F9FAFB; }

    /* 页面渐显动画 */
    .main-content {
        animation: contentUp 1.2s cubic-bezier(0.22, 1, 0.36, 1) forwards;
        opacity: 0;
    }
    @keyframes contentUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .section-title {
        font-size: 28px; font-weight: 800; color: #1A202C;
        padding-left: 15px; border-left: 6px solid #3182CE;
        margin: 20px 0 30px 0;
    }
    /* 彻底隐藏左侧导航栏 */
    [data-testid="stSidebar"] {
        display: none;
    }

    /* 隐藏顶部的展开/收起按钮 */
    [data-testid="collapsedControl"] {
        display: none;
    }

    /* 修复由于侧边栏消失后，主内容区可能出现的左边距 */
    .stMain {
        margin-left: 0px;
    }
    /* 论文卡片：使用 HTML 渲染加粗 */
    .paper-card {
        background: white; padding: 22px; border-radius: 12px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        border-left: 4px solid #E2E8F0;
        margin-bottom: 15px; transition: 0.3s ease;
        color: #4A5568; font-size: 15px; line-height: 1.6;
    }
    .paper-card:hover {
        transform: translateX(5px);
        border-left: 4px solid #3182CE;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        color: #1A202C;
    }

    .featured-box {
        background: #FFFFFF; padding: 25px; border-radius: 15px;
        border: 1px solid #3182CE;
        box-shadow: 0 4px 12px rgba(49, 130, 206, 0.1);
        margin-bottom: 30px;
    }

    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px; font-size: 18px; font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-content">', unsafe_allow_html=True)
# --- 新增：返回首页按钮 ---
col_back, _ = st.columns([1, 5])
with col_back:
    if st.button("🏠 返回首页", use_container_width=True):
        st.switch_page("Home.py")

st.markdown('<div class="section-title">学术成果展示 (Academic Results)</div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📄 期刊论文 (Journal)", "🎤 会议论文 (Conference)", "💡 发明专利 (Patent)"])

with tab1:
    st.write("")
    st.markdown("""
        <div class="featured-box">
            <h4 style="color: #3182CE; margin-top:0;">🌟 代表性学术贡献 (Selected Works)</h4>
            <ul style="color: #4A5568; line-height: 1.8;">
                <li><b>Xiang Suo</b>, Weidi Tang, et al. "Digital human and embodied intelligence for sports science." <i>The Visual Computer</i> 24, 1-17. (2024).</li>
                <li><b>Xiang Suo</b>, Weidi Tang, et al. "Motion Capture Technology in Sports Scenarios: A Survey." <i>Sensors</i>, 24(9), 2947. (2024).</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # 列表中的名字改用 <b> 标签
    journal_papers = [
        "[1] <b>所向</b>, 唐伟棣, 李旭辉, 等. 现代足球智能监控技术前沿与应用[J]. 上海体育大学学报, 2024, 48(04).",
        "[2] 唐伟棣, <b>所向</b>, 杨宸灏等. 跳台滑雪助滑阶段计算流体动力学模拟及优化[J]. 体育科学, 2022, 42(10).",
        "[3] 曹峰锐, 伍勰, 唐伟棣, <b>所向</b>等. 跳台滑雪起跳和早期飞行阶段生物力学研究进展[J]. 北京体育大学学报, 2022, 45(01).",
        "[4] 唐伟棣, <b>所向</b>, 杨宸灏, 等. 基于因果推断的运动科学研究方法架构及应用[J]. 中国体育科技, 2024, 60(07).",
        "[5] <b>Xiang Suo</b>; Weidi Tang; et al. Digital human and embodied intelligence for sports science. The Visual Computer 24, 1-17 (2024).",
        "[6] <b>Xiang Suo</b>, Weidi Tang, Zhen Li. Motion Capture Technology in Sports Scenarios: A Survey. Sensors, 24(9), 2947 (2024).",
        "[7] Tang, W., <b>Suo, X.</b>, et al. SnowMotion: A Wearable Sensor-Based Mobile Platform for Alpine Skiing Technique Assistance. Sensors, 24(12), 3975 (2024).",
        "[8] Yang, C., Yang, M., Li, H., <b>Suo, X.</b> et al. A survey on soccer player detection and tracking with videos. Vis Comput (2024).",
        "[9] Yang, C., Yang, M., Li, H., Jiang, L., <b>Suo, X.</b> et al. Soccer player tracking and data correction based on attention with full-field videos. Vis Comput (2024).",
        "[10] Li H, Yang M, Yang C, Kang J, <b>Suo X</b>, MengW, et al. Soccer match broadcast video analysis method based on detection and tracking. Comput Anim VirtualWorlds. 2024;35(3).",
        "[11] Tan, X., <b>Suo, X.</b>, Li, W. et al. Data visualization in healthcare and medicine: a survey. Vis Comput (2024).",
        "[12] Yang, M., Kang, J., Li, H., YangC., <b>Suo X.</b> et al. Enhanced dual-model framework for precision player tracking and ball detection in soccer videos. Vis Comput 41, 11537–11553 (2025).",
        "[13] Li H, Yang M, Yang C, Kang J, <b>Suo X</b>, Meng W, et al. Soccer match broadcast video analysis method based on detection and tracking. Comput Anim Virtual Worlds. 2024;35(3):e2259."
    ]

    for paper in journal_papers:
        st.markdown(f'<div class="paper-card">{paper}</div>', unsafe_allow_html=True)

with tab2:
    st.write("")
    conference_papers = [
        "[1] <b>所向</b>, 唐伟棣, 李震, 等. 无监督学习方法在足球运动员个性化训练中的应用前景与挑战. 第十三届全国体育科学大会 (体育工程分会).",
        "[2] <b>所向</b>, 唐伟棣, 李震, 等. 基于计算机视觉的足球比赛智能监控系统. 第一届全国体育人工智能大会.",
        "[3] 唐伟棣, <b>所向</b>, 李兴洋, 等. 以 GPT-4 为例探讨多模态大语言模型对体育科研的影响. 第十三届全国体育科学大会 (体育工程分会).",
        "[4] 唐伟棣, <b>所向</b>, 李兴洋, 等. 基于可穿戴传感器与视觉识别的滑雪数字孪生. 第十三届全国体育科学大会 (体育工程分会).",
        "[5] 沈潇楠, 杨宸灏, 唐伟棣, <b>所向</b>, 等. 我国精英男子跳台滑雪运动员起跳技术特征分析. 第十三届全国体育科学大会 (运动生物力学分会).",
        "[6] 杜艺超, 杨宸灏, 唐伟棣, <b>所向</b>, 等. 影响我国跳台滑雪优秀运动员飞行距离的三维运动学因素分析. 第十三届全国体育科学大会 (运动生物力学分会).",
        "[7] 唐伟棣, <b>所向</b>, 林正根, 等. 基于可穿戴传感器的可移动数字滑雪人开发及应用. 第一届全国体育人工智能大会.",
        "[8] Weidi Tang, <b>Xiang Suo</b>, et al. Snowmotion A Wearable Sensor-based Mobile Platform for Alpine Skiing. ACSM 2024 Annual Meeting.",
        "[9] <b>所向</b>, 唐伟棣, 李震, 等. 人工智能驱动的足球训练决策支持系统研究——基于动作长短期价值建模与视频分析. 第十四届全国体育科学大会 (2025)."
    ]

    for conf in conference_papers:
        st.markdown(f'<div class="paper-card">{conf}</div>', unsafe_allow_html=True)

with tab3:
    st.write("")
    st.markdown(f"""
        <div class="info-card" style="border-top: 4px solid #3182CE; background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
            <h3 style="color: #1A202C; margin-top: 0;">基于足球视频的足球训练辅助系统及方法</h3>
            <p style="color: #3182CE; font-weight: bold; font-size: 18px;">✅ 申请公布号：202310744889.3</p>
            <p style="color: #718096;"><b>当前状态</b>：实审中 | <b>发明人</b>：<b>所向</b>, 毛丽娟, 李震</p>
            <hr style="border: 0; border-top: 1px solid #E2E8F0; margin: 20px 0;">
            <p style="color: #4A5568; line-height: 1.8;">
                <b>专利摘要</b>：<br>
                本发明涉及一种利用机器视觉分析足球视频，通过人工智能算法自动识别球员行为并提取训练指标。
                该系统能有效辅助教练员进行技战术分析，提升足球运动员个性化训练的科学性。
            </p>
        </div>
    """, unsafe_allow_html=True)

st.write("---")
st.caption("© 2026 所向 | 上海体育大学 智慧体育工程学院")
st.markdown('</div>', unsafe_allow_html=True)