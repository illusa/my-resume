import streamlit as st
import os

# --- 1. 页面配置 ---
st.set_page_config(page_title="科研项目 | 所向", layout="wide")

# --- 2. 统一视觉风格 CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #F9FAFB; }
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
    
    .project-card {
        background: white; padding: 25px; border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        border-top: 4px solid #3182CE; 
        margin-bottom: 20px; transition: 0.3s ease;
    }
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 20px -5px rgba(0, 0, 0, 0.1);
    }
    .project-level { color: #3182CE; font-weight: 700; font-size: 14px; margin-bottom: 10px; display: block; }
    .project-title { font-size: 20px; font-weight: 800; color: #1A202C; margin-bottom: 10px; }
    .project-desc { color: #4A5568; font-size: 15px; line-height: 1.6; }
    .stButton>button { border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 初始化 Session State ---
if 'view' not in st.session_state:
    st.session_state.view = 'list'
if 'pid' not in st.session_state:
    st.session_state.pid = None

# --- 4. 完整的项目详情数据 ---
PROJECT_DETAILS = {
    "olympic": {
        "title": "科技冬奥 - 跳台滑雪运动员技能优化专项",
        "level": "国家重点研发计划 (2022北京冬奥专项)",
        "content": """
            在备战2022北京冬奥会期间，作为国家跳台滑雪集训队随队服务人员，负责运动员技术指标的实时监测、数据采集与反馈工作。
            - **核心成果**：累计采集并分析 13,000+ 条技术指标，为教练员提供科学化训练依据。
            - **技术方案**：基于高速摄像的动作捕捉系统、运动生物力学建模、多维度数据可视化。
            - **荣誉证明**：获得国家体育总局冬季运动管理中心颁发的官方服务证明。
        """,
        "local_video": "videos/科技冬奥.mp4"
    },
    "soccer_sys": {
        "title": "足球训练辅助系统 (专利转化项目)",
        "level": "发明专利转化 / 智慧体育课题",
        "content": """
            基于已申请的专利《基于足球视频的足球训练辅助系统及方法》，开发了一套完整的智慧足球分析平台。
        """,
        "image": "https://via.placeholder.com/800x400?text=Soccer+System+Platform+Preview"
    },
    "soccer_tracking": {
        "title": "跨视域语义融合的足球技战术分析",
        "level": "国家自然科学基金项目",
        "content": """针对足球场多摄像机视角的复杂环境，研究跨视域下的目标关联与语义融合技术。""",
        "local_video": "videos/足球激光雷达.mp4"
    },
    "llm_sports": {
        "title": "体育垂直领域大模型研发",
        "level": "校企合作 / 前沿研发项目",
        "content": """构建国内领先的体育垂直领域大模型，实现运动科学知识的智能交互与辅助决策。""",
        "local_image": "videos/上体体育大模型.png"
    }
}

# --- 5. 视图逻辑展示 ---
st.markdown('<div class="main-content">', unsafe_allow_html=True)

if st.session_state.view == 'list':
    # --- 【新增开始】返回首页按钮 ---
    col_back, _ = st.columns([1, 5])
    with col_back:
        if st.button("🏠 返回首页", use_container_width=True):
            st.switch_page("Home.py")
    # --- 【新增结束】 ---

    st.markdown('<div class="section-title">参与科研项目与课题 (Research Projects)</div>', unsafe_allow_html=True)

    for key, p in PROJECT_DETAILS.items():
        st.markdown(f"""
            <div class="project-card">
                <span class="project-level">[{p['level']}]</span>
                <div class="project-title">{p['title']}</div>
                <div class="project-desc">{p['content'][:120].strip()}...</div>
            </div>
        """, unsafe_allow_html=True)

        if st.button(f"查看 {p['title']} 详细展示 →", key=f"btn_{key}"):
            st.session_state.pid = key
            st.session_state.view = 'detail'
            st.rerun()

else:
    # --- 三级：详情页面 ---
    p = PROJECT_DETAILS[st.session_state.pid]

    # 详情页原有的返回项目列表按钮
    if st.button("← 返回项目列表"):
        st.session_state.view = 'list'
        st.rerun()

    st.markdown(f'<div class="section-title">{p["title"]}</div>', unsafe_allow_html=True)
    col_text, col_media = st.columns([1, 1])

    with col_text:
        st.markdown(f"**项目级别/类别**：`{p['level']}`")
        st.write("---")
        st.markdown("### 项目详情介绍")
        st.markdown(p['content'])

    with col_media:
        st.markdown("### 演示与成果展示")

        # 1. 检查并播放本地视频
        if 'local_video' in p:
            video_path = p['local_video']
            if os.path.exists(video_path):
                with open(video_path, 'rb') as f:
                    video_bytes = f.read()
                st.video(video_bytes)
            else:
                st.error(f"找不到视频文件：{video_path}")

        # 2. 检查并显示本地图片 (这是你新增的逻辑)
        elif 'local_image' in p:
            img_path = p['local_image']
            if os.path.exists(img_path):
                st.image(img_path, use_column_width=True)
            else:
                st.error(f"找不到本地图片文件：{img_path}")

        # 3. 针对网络视频/图片的兼容逻辑
        elif 'video' in p:
            st.video(p['video'])
        if 'image' in p:
            st.image(p['image'], use_column_width=True)

st.write("---")
st.caption("© 2026 所向 | 上海体育大学 智慧体育工程学院")
st.markdown('</div>', unsafe_allow_html=True)