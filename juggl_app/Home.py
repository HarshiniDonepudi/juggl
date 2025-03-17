import streamlit as st

def main():
    # Page config
    st.set_page_config(page_title="Juggl - Home", layout="wide", initial_sidebar_state="collapsed")
    
    # Hide Streamlit default elements
    hide_streamlit_style = """
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .css-18e3th9 {padding-top: 0; padding-bottom: 0;}
            .css-1d391kg {padding-top: 1rem;}
        </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    # Custom CSS for page styling
    custom_css = """
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');

    /* Global Styles */
    body {
        font-family: 'Roboto', sans-serif;
        background: #f5f7fa;
        color: #333;
        margin: 0;
        padding: 0;
    }

    /* Header */
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px;
        max-width: 1200px;
        margin: 0 auto;
    }

    .logo {
        font-size: 28px;
        font-weight: 700;
        color: #4CAF50;
    }

    .nav-links {
        display: flex;
        gap: 15px;
    }

    .nav-link {
        text-decoration: none;
        color: #666;
        padding: 8px 15px;
        border: 1px dashed #ccc;
        border-radius: 4px;
    }

    .auth-buttons {
        display: flex;
        gap: 15px;
    }

    .login-button {
        background: white;
        color: #333;
        border: 1px solid #ddd;
        padding: 8px 20px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 500;
    }

    .signup-button {
        background: #2196F3;
        color: white;
        border: none;
        padding: 8px 20px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 500;
    }

    /* Hero Section */
    .hero {
        text-align: center;
        max-width: 800px;
        margin: 60px auto;
    }

    .hero h1 {
        font-size: 40px;
        font-weight: 500;
        margin: 0;
        line-height: 1.2;
    }

    .hero .emphasis {
        font-style: italic;
    }

    .hero-subtitle {
        font-size: 20px;
        color: #555;
        margin: 30px 0 50px 0;
    }

    /* Feature Cards */
    .features {
        display: flex;
        justify-content: center;
        gap: 30px;
        margin: 50px 0;
        padding: 0 20px;
    }

    .feature-card {
        background: white;
        border-radius: 12px;
        padding: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        width: 300px;
        text-align: center;
    }

    .feature-card svg {
        width: 100px;
        height: 100px;
        margin-bottom: 20px;
    }

    .feature-title {
        font-size: 20px;
        font-weight: 600;
        margin-bottom: 15px;
    }

    .feature-text {
        color: #666;
        line-height: 1.5;
    }

    /* CTA Button */
    .cta-container {
        text-align: center;
        margin: 50px 0;
    }

    .cta-button {
        display: inline-block;
        background: #2196F3;
        color: white;
        padding: 12px 40px;
        font-size: 18px;
        font-weight: 600;
        border-radius: 50px;
        text-decoration: none;
        transition: all 0.3s ease;
    }

    .cta-button:hover {
        background: #1976D2;
        transform: translateY(-2px);
    }
    </style>
    """
    
    # Add SVG Icons
    icons = {
        "snow_globe": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
          <rect x="70" y="150" width="60" height="10" fill="#2196F3" rx="5" />
          <circle cx="100" cy="100" r="60" fill="#e0f7fa" stroke="#2196F3" stroke-width="3" />
          <circle cx="80" cy="70" r="3" fill="#2196F3" />
          <circle cx="120" cy="90" r="3" fill="#2196F3" />
          <circle cx="90" cy="110" r="3" fill="#2196F3" />
          <circle cx="110" cy="80" r="3" fill="#2196F3" />
          <circle cx="85" cy="95" r="2" fill="#2196F3" />
          <path d="M75 65 L78 72 L85 72 L80 77 L82 85 L75 80 L68 85 L70 77 L65 72 L72 72 Z" fill="#64B5F6" />
          <path d="M115 85 L117 90 L122 90 L118 93 L120 98 L115 95 L110 98 L112 93 L108 90 L113 90 Z" fill="#64B5F6" />
          <path d="M70 120 Q80 100 100 110 Q120 100 130 120" fill="#B3E5FC" stroke="#64B5F6" stroke-width="2" />
        </svg>
        """,
        
        "head_bulb": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
          <path d="M60 150 L60 110 C60 70 100 50 140 80 L140 150 Z" fill="#FF9800" />
          <path d="M75 110 C95 110 105 115 125 110" fill="none" stroke="#FFF3E0" stroke-width="2" />
          <circle cx="100" cy="75" r="20" fill="#FFEB3B" />
          <path d="M95 90 L95 100 L105 100 L105 90 Z" fill="#FFC107" />
          <line x1="100" y1="45" x2="100" y2="35" stroke="#FFEB3B" stroke-width="3" />
          <line x1="75" y1="75" x2="65" y2="75" stroke="#FFEB3B" stroke-width="3" />
          <line x1="125" y1="75" x2="135" y2="75" stroke="#FFEB3B" stroke-width="3" />
          <line x1="85" y1="60" x2="75" y2="50" stroke="#FFEB3B" stroke-width="3" />
          <line x1="115" y1="60" x2="125" y2="50" stroke="#FFEB3B" stroke-width="3" />
        </svg>
        """,
        
        "balance_stones": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
          <ellipse cx="100" cy="160" rx="60" ry="20" fill="#4CAF50" />
          <ellipse cx="100" cy="130" rx="45" ry="15" fill="#66BB6A" />
          <ellipse cx="100" cy="105" rx="35" ry="12" fill="#81C784" />
          <ellipse cx="100" cy="80" rx="25" ry="10" fill="#A5D6A7" />
          <ellipse cx="100" cy="60" rx="15" ry="8" fill="#C8E6C9" />
        </svg>
        """
    }
    
    # Build HTML structure with Streamlit components
    st.markdown(custom_css, unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div class="header">
        <div class="logo">Juggl</div>
        <div class="nav-links">
            <a href="About" class="nav-link">About</a>
            <a href="Pricing" class="nav-link">Pricing</a>
        </div>
        <div class="auth-buttons">
            <a href="Log_in" class="login-button">Log In</a>
            <a href="Sign_up" class="signup-button">Sign Up</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Hero section
    st.markdown("""
    <div class="hero">
        <h1>Create <span class="emphasis">time & mental space</span> for</h1>
        <h1>what <span class="emphasis">truly matters.</span></h1>
        <div class="hero-subtitle">Turn your calendar into a tool for your well-being.</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature cards
    st.markdown(f"""
    <div class="features">
        <div class="feature-card">
            {icons["snow_globe"]}
            <div class="feature-title">Know Burnout Risk</div>
            <div class="feature-text">Become aware of your likelihood of experiencing burnout</div>
        </div>
        
        <div class="feature-card">
            {icons["head_bulb"]}
            <div class="feature-title">Understand Yourself</div>
            <div class="feature-text">Become aware of your likelihood of experiencing burnout</div>
        </div>
        
        <div class="feature-card">
            {icons["balance_stones"]}
            <div class="feature-title">Create Balance</div>
            <div class="feature-text">Become aware of your likelihood of experiencing burnout</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # CTA button
    st.markdown("""
    <div class="cta-container">
        <a href="Sign_up" class="cta-button">Sign Up</a>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()