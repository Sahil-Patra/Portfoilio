import streamlit as st
from datetime import datetime

# ==================================================================================
# 📝 CONFIGURATION SECTION 
# ==================================================================================

# Personal Information
PERSONAL_INFO = {
    "name": "Sahil Patra",
    "title": "Data Scientist | ML Engineer | Aspiring AI Specialist",
    "email": "sahilpatra1004@gmail.com",
    "linkedin": "https://www.linkedin.com/in/sahil-patra10",
    "github": "https://github.com/Sahil-Patra",
    "profile_pic": "sahil.png",  # my image URL
    "bio": """
    Computer science graduate passionate about leveraging data science and machine learning to solve 
    real-world problems. During my learning journey, I've built multiple end-to-end projects 
    demonstrating proficiency in Python, ML algorithms, and deployment. Eager to apply my 
    technical skills and contribute to innovative data-driven solutions in a professional setting.
    """,
    "resume_link": "https://drive.google.com/file/d/1eC4YW_rAMBK3dUUluA3gNixO6VszRDM3/view?usp=sharing"  # my resume URL
}

# Core Competencies (displayed as tags on Home page)
COMPETENCIES = [
    "Machine Learning", "AI", "Python Programming", "Data Analysis", "Statistical Modeling",
    "SQL & Databases", "Data Visualization", "Problem Solving", "Quick Learner",
    "TensorFlow/PyTorch", "Git & Version Control", "End-to-End ML Projects", "Self-Motivated"
]

# Skills with proficiency levels (0-100)
SKILLS = {
    "Python": 95,
    "SQL": 85,
    "Machine Learning": 90,
    "Deep Learning": 85,
    "Data Visualization": 88,
    "NLP": 82,
    "Cloud Computing": 75,
    "MLOps": 78,
    "Statistics": 85,
    "AI": 50
}

# Projects Data Structure -
def get_projects():
    """
    Returns a list of project dictionaries.
    To add a new project, simply add a new dictionary to this list.
    
    Each project should have:
    - title: Project name
    - description: Brief description (2-3 sentences)
    - image: URL to project image/screenshot
    - github: GitHub repository link
    - demo: Live demo link (optional, use None if not available)
    - tags: List of technologies used
    """
    return [
        {
            "title": "Generative AI Data Analyst ('Talk to Your CSV')",
            "description": "Developed an NLP-driven data analysis tool allowing users to query CSV datasets using natural language. Leveraged LangChain agents to convert text into Python/Pandas logic, reducing manual analysis time by 40% for non-technical stakeholders.",
            "image": "https://via.placeholder.com/400x250/4A90E2/ffffff?text=Churn+Prediction",
            "github": "https://github.com/Sahil-Patra/Talk-To-Your-CSV",
            "demo": None,
            "tags": ["Python", "PandasAI", "Streamlit", "Hugging-face API"]
        },
        {
            "title": "End-to-End Market Sentiment & Trend Analyzer",
            "description": "Engineered a real-time NLP pipeline fetching financial news via NewsAPI to quantify market sentiment. Implemented FinBERT for specialized financial text classification and deployed an interactive Streamlit dashboard to visualize daily trend shifts and keyword frequency.",
            "image": "https://via.placeholder.com/400x250/50C878/ffffff?text=Sentiment+Analysis",
            "github": "https://github.com/Sahil-Patra/End-to-End-Market-sentiment-and-trend-analyzer",
            "demo": "https://end-to-end-market-sentiment-and-trend-analyzer-gfmrfwfwtbp4car.streamlit.app/",
            "tags": ["Python", "NLP (Transformers)", "Streamlit", "NewsAPI", "Matplotlib"]
        },
        {
            "title": "Sales Forecasting with Time Series",
            "description": "Created ARIMA and LSTM models for multi-step sales forecasting. Reduced MAPE by 15% compared to baseline models and deployed via AWS Lambda.",
            "image": "https://via.placeholder.com/400x250/9B59B6/ffffff?text=Sales+Forecasting",
            "github": "https://github.com/Sahil-Patra/Sales_Performance_analysis",
            "demo": None,
            "tags": ["Python", "LSTM", "Prophet", "Pandas", "AWS Lambda"]
        },
        {
            "title": "AI-Powered Credit Risk Assessment Model",
            "description": "Designed a robust classification system to evaluate loan eligibility and probability of default. Handled class imbalance using SMOTE and optimized an XGBoost classifier to achieve 0.89 AUC-ROC, deploying the solution via a Flask API for real-time scoring.",
            "image": "https://via.placeholder.com/400x250/F39C12/ffffff?text=Recommender+System",
            "github": "https://github.com/Sahil-Patra/AI_Powered_Credit_Risk_Analyzer",
            "demo": "https://aipoweredcreditriskanalyzer-rednfqu7pfy4rjyqx46ltt.streamlit.app/",
            "tags": ["Python", "SHAP", "XGBoost", "Streamlit"]
        },
        {
            "title": "RAG-Based Financial Document Assistant",
            "description": "Architected a Retrieval-Augmented Generation (RAG) system to query complex financial reports (10-Ks, PDFs). Integrated LlamaIndex with a ChromaDB vector store for semantic search, reducing information retrieval latency by 90% and ensuring context-aware responses.",
            "image": "https://via.placeholder.com/400x250/1ABC9C/ffffff?text=ETL+Pipeline",
            "github": "https://github.com/Sahil-Patra/RAG-Based-Financial-Document-Assistant",
            "demo": "https://rag-based-financial-document-assistant-neae5oyytdnjyrx7casacl.streamlit.app/",
            "tags": ["Langchain", "Hugging Face API", "Python", "Streamlit"]
        },
         {
            "title": "Interactive E-Commerce Performance Dashboard",
            "description": "Architected a Retrieval-Augmented Generation (RAG) system to query complex financial reports (10-Ks, PDFs). Integrated LlamaIndex with a ChromaDB vector store for semantic search, reducing information retrieval latency by 90% and ensuring context-aware responses.",
            "image": "https://via.placeholder.com/400x250/1ABC9C/ffffff?text=ETL+Pipeline",
            "github": "https://github.com/Sahil-Patra/E-Commerce-Dashboard",
            "demo": "https://app.powerbi.com/view?r=eyJrIjoiNjMyZGZiMGMtZTk3My00NThhLWFmOTEtNmU4MzNjNTBhNWMzIiwidCI6ImRiOThlOTIzLWQyZWEtNDY2MS1hZDE1LTI3YzUyNjA2MGEyYiJ9",
            "tags": ["Airflow", "SQL", "Python", "Docker", "AWS S3"]
        },
          {
            "title": "Mobile Device Price Prediction Model",
            "description": "Engineered a supervised machine learning model to estimate mobile device price ranges based on hardware specifications. Optimized Random Forest hyperparameters to achieve 94% classification accuracy, aiding in competitive market pricing analysis.",
            "image": "https://via.placeholder.com/400x250/1ABC9C/ffffff?text=ETL+Pipeline",
            "github": "https://github.com/Sahil-Patra/Mobile-Price-Prediction",
            "demo": None,
            "tags": ["ML Classification", "Python", "Neural Networks", "ReLU"]
        },
         {
            "title": "ESG Risk Analysis",
            "description": "Architected a Retrieval-Augmented Generation (RAG) system to query complex financial reports (10-Ks, PDFs). Integrated LlamaIndex with a ChromaDB vector store for semantic search, reducing information retrieval latency by 90% and ensuring context-aware responses.",
            "image": "https://via.placeholder.com/400x250/1ABC9C/ffffff?text=ETL+Pipeline",
            "github": "https://github.com/Sahil-Patra/ESG-Risk-Analysis",
            "demo": "https://app.powerbi.com/view?r=eyJrIjoiM2Y0MGVlM2ItNDJiZS00ZjViLWI3MzUtY2I2M2Q0YWNhMjljIiwidCI6ImRiOThlOTIzLWQyZWEtNDY2MS1hZDE1LTI3YzUyNjA2MGEyYiJ9",
            "tags": ["Power BI", "SQL", "Python","Data Analysis", "Jupyter Notebook"]
        }
    ]

# ==================================================================================
# 🎨 STYLING AND PAGE CONFIGURATION
# ==================================================================================

# Page configuration
st.set_page_config(
    page_title=f"{PERSONAL_INFO['name']} - Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    /* Main content styling */
    .main {
        padding-top: 2rem;
    }
    
    /* Project card styling */
    .project-card {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
        height: 100%;
        transition: transform 0.2s;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    /* Tag styling */
    .tag {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        margin: 0.25rem;
        background-color: #e7f3ff;
        color: #0066cc;
        border-radius: 15px;
        font-size: 0.85rem;
        font-weight: 500;
    }
    
    /* Skill bar container */
    .skill-container {
        margin-bottom: 1rem;
    }
    
    /* Profile picture */
    .profile-pic {
        border-radius: 50%;
        border: 3px solid #4A90E2;
    }
    
    /* Competency tags */
    .competency-tag {
        display: inline-block;
        padding: 0.5rem 1rem;
        margin: 0.3rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 500;
    }
    
    /* Social links */
    .social-link {
        text-decoration: none;
        color: #4A90E2;
        font-size: 1.1rem;
        margin: 0.5rem 0;
        display: block;
    }
    
    /* Section headers */
    .section-header {
        color: #2c3e50;
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        border-bottom: 3px solid #4A90E2;
        padding-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# ==================================================================================
# 📱 SIDEBAR - NAVIGATION & PROFILE
# ==================================================================================

with st.sidebar:
    # Profile Picture
    st.image(PERSONAL_INFO["profile_pic"], width=200)
    
    st.markdown(f"## {PERSONAL_INFO['name']}")
    st.markdown(f"*{PERSONAL_INFO['title']}*")
    
    st.markdown("---")
    
    # Navigation Menu
    st.markdown("### 📍 Navigation")
    page = st.radio(
        "Go to:",
        ["🏠 Home", "💼 Skills", "🚀 Projects", "📬 Contact"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Social Links
    st.markdown("### 🔗 Connect With Me")
    st.markdown(f"[📧 Email]({PERSONAL_INFO['email']})")
    st.markdown(f"[💼 LinkedIn]({PERSONAL_INFO['linkedin']})")
    st.markdown(f"[👨‍💻 GitHub]({PERSONAL_INFO['github']})")
    
    st.markdown("---")
    st.caption(f"© {datetime.now().year} {PERSONAL_INFO['name']}")

# ==================================================================================
# 🏠 HOME PAGE
# ==================================================================================

if page == "🏠 Home":
    # Hero Section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"# Hello! 👋 I'm {PERSONAL_INFO['name']}")
        st.markdown(f"## {PERSONAL_INFO['title']}")
        st.markdown(PERSONAL_INFO['bio'])
        
        # Download Resume Button
        st.markdown(f"""
            <a href="{PERSONAL_INFO['resume_link']}" target="_blank">
                <button style="
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 0.75rem 2rem;
                    border: none;
                    border-radius: 25px;
                    font-size: 1rem;
                    font-weight: 600;
                    cursor: pointer;
                    margin-top: 1rem;
                ">
                    📄 Download Resume
                </button>
            </a>
        """, unsafe_allow_html=True)
    
    with col2:
        st.image(PERSONAL_INFO["profile_pic"], width=250)
    
    st.markdown("---")
    
    # Core Competencies
    st.markdown('<div class="section-header">🎯 Core Competencies</div>', unsafe_allow_html=True)
    
    # Display competencies as styled tags
    competency_html = "".join([f'<span class="competency-tag">{comp}</span>' for comp in COMPETENCIES])
    st.markdown(f'<div style="margin: 1rem 0;">{competency_html}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick Stats
    st.markdown('<div class="section-header">📊 Highlights</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Projects Built", len(get_projects()))
    
    with col2:
        st.metric("Technologies Used", "15+")
    
    with col3:
        st.metric("Certifications", "5+")
    
    with col4:
        st.metric("Problem-Solving Hours", "500+")

# ==================================================================================
# 💼 SKILLS PAGE
# ==================================================================================

elif page == "💼 Skills":
    st.markdown('<div class="section-header">💼 Technical Skills</div>', unsafe_allow_html=True)
    
    st.markdown("""
        My technical expertise spans across various domains of Data Science and Machine Learning.
        Below is a breakdown of my proficiency levels in key technologies and tools.
    """)
    
    st.markdown("---")
    
    # Display skills in two columns
    col1, col2 = st.columns(2)
    
    skills_list = list(SKILLS.items())
    mid_point = len(skills_list) // 2
    
    with col1:
        for skill, level in skills_list[:mid_point]:
            st.markdown(f"**{skill}**")
            st.progress(level / 100)
            st.caption(f"{level}% Proficiency")
            st.markdown("<br>", unsafe_allow_html=True)
    
    with col2:
        for skill, level in skills_list[mid_point:]:
            st.markdown(f"**{skill}**")
            st.progress(level / 100)
            st.caption(f"{level}% Proficiency")
            st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Additional Skills Categories
    st.markdown("### 🛠️ Additional Technical Proficiencies")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Languages**")
        st.markdown("• Python\n• SQL\n• R\n• JavaScript\n• Bash")
    
    with col2:
        st.markdown("**Tools & Frameworks**")
        st.markdown("• TensorFlow/Keras\n• PyTorch\n• Scikit-learn\n• Pandas/NumPy\n• Docker")
    
    with col3:
        st.markdown("**Cloud & Deployment**")
        st.markdown("• AWS (S3, Lambda, EC2)\n• Azure ML\n• Git/GitHub\n• CI/CD\n• MLflow")

# ==================================================================================
# 🚀 PROJECTS PAGE (DYNAMIC)
# ==================================================================================

elif page == "🚀 Projects":
    st.markdown('<div class="section-header">🚀 Featured Projects</div>', unsafe_allow_html=True)
    
    st.markdown("""
        Here's a showcase of my recent data science and machine learning projects. 
        Each project demonstrates different aspects of the ML lifecycle, from data exploration 
        to model deployment.
    """)
    
    st.markdown("---")
    
    # Get projects from the data structure
    projects = get_projects()
    
    # Create a grid layout (2 columns)
    for i in range(0, len(projects), 2):
        col1, col2 = st.columns(2)
        
        # First project in the row
        with col1:
            project = projects[i]
            
            # Project image
            st.image(project["image"], use_container_width=True)
            
            # Project title
            st.markdown(f"### {project['title']}")
            
            # Project description
            st.markdown(project["description"])
            
            # Technology tags
            tags_html = "".join([f'<span class="tag">{tag}</span>' for tag in project["tags"]])
            st.markdown(tags_html, unsafe_allow_html=True)
            
            # Links
            link_col1, link_col2 = st.columns(2)
            with link_col1:
                st.markdown(f"[💻 View Code]({project['github']})")
            with link_col2:
                if project["demo"]:
                    st.markdown(f"[🌐 Live Demo]({project['demo']})")
            
            st.markdown("<br>", unsafe_allow_html=True)
        
        # Second project in the row (if exists)
        if i + 1 < len(projects):
            with col2:
                project = projects[i + 1]
                
                st.image(project["image"], use_container_width=True)
                st.markdown(f"### {project['title']}")
                st.markdown(project["description"])
                
                tags_html = "".join([f'<span class="tag">{tag}</span>' for tag in project["tags"]])
                st.markdown(tags_html, unsafe_allow_html=True)
                
                link_col1, link_col2 = st.columns(2)
                with link_col1:
                    st.markdown(f"[💻 View Code]({project['github']})")
                with link_col2:
                    if project["demo"]:
                        st.markdown(f"[🌐 Live Demo]({project['demo']})")
                
                st.markdown("<br>", unsafe_allow_html=True)

# ==================================================================================
# 📬 CONTACT PAGE
# ==================================================================================

elif page == "📬 Contact":
    st.markdown('<div class="section-header">📬 Get In Touch</div>', unsafe_allow_html=True)
    
    st.markdown("""
        I'm always interested in hearing about new opportunities, collaborations, 
        or just having a conversation about data science and AI. Feel free to reach out!
    """)
    
    st.markdown("---")
    
    # Contact form
    col1, col2 = st.columns([2, 1])
    
    with col1:
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your Name *")
            email = st.text_input("Your Email *")
            subject = st.text_input("Subject *")
            message = st.text_area("Message *", height=150)
            
            submitted = st.form_submit_button("Send Message 📤")
            
            if submitted:
                if name and email and subject and message:
                    st.success("✅ Message sent successfully! I'll get back to you soon.")
                    st.balloons()
                    
                    # NOTE: This is a placeholder. To make the form functional, I need to:
                    # 1. Use a service like Formspree (https://formspree.io/)
                    # 2. Use EmailJS (https://www.emailjs.com/)
                    # 3. Set up a backend API to handle form submissions
                    # 4. Use Streamlit's experimental connection features
                    
                    st.info("""
                        **Sorry, this form is not functional for now.**
                    """)
                else:
                    st.error("⚠️ Please fill in all required fields.")
    
    with col2:
        st.markdown("### 📍 Direct Contact")
        st.markdown(f"""
            **Email:**  
            [{PERSONAL_INFO['email']}](mailto:{PERSONAL_INFO['email']})
            
            **LinkedIn:**  
            [View Profile]({PERSONAL_INFO['linkedin']})
            
            **GitHub:**  
            [View Repositories]({PERSONAL_INFO['github']})
        """)
        
        st.markdown("---")
        
        st.markdown("### ⏰ Response Time")
        st.info("I typically respond within 24-48 hours on business days.")
        
        st.markdown("### 🌍 Location")
        st.info("Open to remote opportunities worldwide")
