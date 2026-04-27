import streamlit as st

# --- 1. 页面配置 ---
st.set_page_config(page_title="教育与历程 | 所向", layout="wide")

# --- 2. 视觉风格统一与隐藏导航栏 CSS ---
st.markdown("""
    <style>
    /* 全局背景：与首页一致 */
    .stApp { background-color: #F9FAFB; }

    /* 彻底隐藏左侧导航栏及折叠控制按钮 */
    [data-testid="stSidebar"], [data-testid="collapsedControl"] {
        display: none;
    }
    .stMain {
        margin-left: 0px;
    }

    /* 页面渐显动画 */
    .main-content {
        animation: contentUp 1.2s cubic-bezier(0.22, 1, 0.36, 1) forwards;
        opacity: 0;
    }
    @keyframes contentUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* 标题装饰：与首页一致 */
    .section-title {
        font-size: 28px; font-weight: 800; color: #1A202C;
        padding-left: 15px; border-left: 6px solid #3182CE;
        margin: 20px 0 30px 0;
    }

    /* 调整分割线颜色 */
    hr { border-top: 1px solid #E2E8F0; }

    header, footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# 开始内容容器
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# --- 3. 返回首页按钮 ---
col_back, _ = st.columns([1, 6])
with col_back:
    if st.button("🏠 返回首页", use_container_width=True):
        st.switch_page("Home.py")

# --- 4. 页面大标题 ---
st.markdown('<div class="section-title">教育背景与职业历程 (Education & Experience)</div>', unsafe_allow_html=True)

# --- 5. 详细履历内容 (时间轴样式) ---

# 博士
col1, col2 = st.columns([1, 4])
with col1:
    st.write("### 2021.09 - 2025.06")
with col2:
    st.markdown("#### **上海体育大学** | 体育教育训练学 | **博士**")
    st.write("研究方向为体育工程化应用，重点攻克运动表现数字化建模与人工智能评估。")

st.markdown("---")

# 硕士
col3, col4 = st.columns([1, 4])
with col3:
    st.write("### 2018.03 - 2021.01")
with col4:
    st.markdown("#### **新南威尔士大学 (UNSW)** | Mechanical Engineering | **硕士**")
    st.write("主修机械工程与管理，深入学习 Ansys 流体力学分析、有限元分析及复合材料设计。")

st.markdown("---")

# 工作
col5, col6 = st.columns([1, 4])
with col5:
    st.write("### 2012.08 - 2016.06")
with col6:
    st.markdown("#### **中国航发北京长空机械有限公司** | 工艺技术工程师")
    st.write("""
    - **结构件工艺**：负责武装直升机发动机部件的钣金与结构件加工。
    - **调度管理**：负责车间生产计划，协调现场排故。
    - **总装工艺**：主导离心泵、齿轮泵的装配工艺文件设计及检验。
    """)

st.markdown("---")

# 本科
col7, col8 = st.columns([1, 4])
with col7:
    st.write("### 2008.09 - 2012.06")
with col8:
    st.markdown("#### **北京航空航天大学** | 机械工程及自动化 | **学士**")
    st.write("学院学生会主席团成员；北航交响乐团小提琴手（2008-2012 演出与比赛）。")

# 页脚
st.write("---")
st.caption("© 2024 所向 | 上海体育大学 智慧体育工程学院")

st.markdown('</div>', unsafe_allow_html=True)