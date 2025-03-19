import streamlit as st
import time

# Streamlit app configuration
st.set_page_config(page_title="Juggl - Onboarding", layout="wide", initial_sidebar_state="collapsed")

# Initialize session state for tracking progress
if 'step' not in st.session_state:
    st.session_state.step = 1

# Store onboarding data in session state
if 'onboarding_data' not in st.session_state:
    st.session_state.onboarding_data = {}

# Flag to indicate onboarding completion
if 'onboarding_complete' not in st.session_state:
    st.session_state.onboarding_complete = False

# Custom CSS to style the app exactly like the images
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

body {
    font-family: 'Inter', sans-serif;
    background-color: #f5f5f5;
    margin: 0;
    padding: 0;
    color: #333;
}

/* Hide default Streamlit components */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.block-container {padding-top: 0 !important; padding-bottom: 0 !important;}

/* Global page background */
.stApp {
    background: linear-gradient(to bottom, white 65%, #4CAF50 35%);
}

/* Logo Style */
.logo {
    font-family: 'Inter', sans-serif;
    font-weight: bold;
    font-size: 24px;
    color: #4CAF50;
    padding: 20px 0 10px 20px;
}

/* Progress bar */
.progress-container {
    max-width: 1140px;
    margin: 0 auto;
    padding: 0 20px;
}

.progress-bar {
    height: 6px;
    background-color: #E3EAF3;
    border-radius: 4px;
    margin-bottom: 10px;
}

.progress-fill {
    height: 100%;
    border-radius: 4px;
    background-color: #447BF4;
}

.progress-text {
    font-size: 14px;
    color: #666;
    display: flex;
    justify-content: space-between;
}

/* Card Container */
.card-container {
    max-width: 700px;
    margin: 20px auto 40px auto;
    background: white;
    border-radius: 16px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.06);
    padding: 40px;
}

/* Card Header */
.card-header {
    text-align: center;
    margin-bottom: 30px;
}

.card-title {
    font-weight: 600;
    font-size: 24px;
    margin-bottom: 10px;
}

.card-subtitle {
    color: #666;
    font-size: 14px;
}

/* Selection cards */
.selection-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 20px;
    margin: 30px 0;
}

.selection-card {
    background: white;
    border: 1px solid #eee;
    border-radius: 12px;
    padding: 20px 10px;
    text-align: center;
    cursor: pointer;
    position: relative;
}

.selection-card.selected {
    border-color: #447BF4;
}

.selection-radio {
    position: absolute;
    top: 10px;
    left: 10px;
    width: 20px;
    height: 20px;
    border: 2px solid #ccc;
    border-radius: 50%;
}

.selection-radio.selected {
    border-color: #447BF4;
}

.selection-radio.selected::after {
    content: "";
    position: absolute;
    top: 4px;
    left: 4px;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #447BF4;
}

.selection-icon {
    width: 60px;
    height: 60px;
    margin: 0 auto 10px auto;
}

.selection-title {
    font-size: 14px;
    font-weight: 500;
    margin-bottom: 5px;
}

.selection-subtitle {
    font-size: 12px;
    color: #666;
}

/* Form fields */
.stTextInput > div > div > input {
    font-size: 14px !important;
    padding: 12px 15px !important;
    border-radius: 8px !important;
    border: 1px solid #ddd !important;
}

.stSelectbox > div > div {
    font-size: 14px !important;
    padding: 12px 15px !important;
    border-radius: 8px !important;
    border: 1px solid #ddd !important;
}

.radio-horizontal {
    display: flex !important;
    justify-content: space-between !important;
    gap: 20px !important;
}

.radio-button {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 6px 15px;
    font-size: 14px;
    text-align: center;
    cursor: pointer;
}

.radio-button.selected {
    border-color: #447BF4;
    color: #447BF4;
}

/* Continue button */
.continue-button {
    display: inline-block;
    background: #447BF4;
    color: white;
    border: none;
    padding: 10px 30px;
    font-size: 14px;
    font-weight: 500;
    border-radius: 25px;
    margin-top: 20px;
    text-align: center;
    cursor: pointer;
    width: auto;
}

/* Industry selection cards */
.industry-cards {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 10px;
    margin: 20px 0;
}

.industry-card {
    border: 1px solid #eee;
    border-radius: 8px;
    padding: 10px;
    text-align: center;
    cursor: pointer;
}

.industry-card.selected {
    border-color: #447BF4;
    background-color: #f0f7ff;
}

/* Checkbox styling */
.stCheckbox > div {
    padding: 5px 0 !important;
}

.stCheckbox > div > div > label {
    font-size: 14px !important;
}

/* Layout for calendar sync screen */
.email-container {
    display: flex;
    align-items: center;
    margin: 30px 0;
    background: #f8f9fa;
    border-radius: 8px;
    padding: 15px;
}

.email-avatar {
    width: 40px;
    height: 40px;
    background: #4CAF50;
    border-radius: 50%;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    margin-right: 15px;
}

.email-label {
    flex-grow: 1;
}

.calendar-type {
    background: white;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 5px 15px;
    font-size: 14px;
    color: #666;
    display: flex;
    align-items: center;
}

.calendar-type::after {
    content: "▼";
    margin-left: 5px;
    font-size: 10px;
}

.add-calendar-button {
    display: flex;
    align-items: center;
    color: #447BF4;
    font-size: 14px;
    margin-top: 15px;
    cursor: pointer;
}

.add-calendar-button::before {
    content: "+";
    margin-right: 5px;
    font-size: 16px;
}

</style>
"""

# Define SVG icons
icons = {
    'burnout': """
    <svg width="60" height="60" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="30" cy="30" r="24" fill="#FFF3E0"/>
        <path d="M35 22C36.5 24 37 26 36 28C35 30 34 31 35 33C36 35 38 36 36 39C34 42 30 40 30 38C30 36 32 35 31 33C30 31 28 32 27 30C26 28 27 25 29 23C31 21 33.5 20 35 22Z" fill="#FF9800"/>
        <circle cx="29" cy="27" r="2" fill="#FFEB3B"/>
    </svg>
    """,
    'balance': """
    <svg width="60" height="60" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="20" y="40" width="20" height="3" rx="1.5" fill="#7986CB"/>
        <rect x="15" y="43" width="30" height="3" rx="1.5" fill="#7986CB"/>
        <rect x="27" y="20" width="6" height="20" fill="#7986CB"/>
        <circle cx="30" cy="20" r="6" fill="#9FA8DA"/>
        <path d="M20 30a10 5 0 0 1 20 0" fill="#9FA8DA"/>
    </svg>
    """,
    'goals': """
    <svg width="60" height="60" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M30 15 L30 30 L38 45 L22 45 Z" fill="#4CAF50"/>
        <path d="M20 20 L40 20 L40 25 L35 30 L25 30 L20 25 Z" fill="#81C784"/>
        <circle cx="30" cy="20" r="2" fill="#E8F5E9"/>
        <rect x="28" y="10" width="4" height="5" fill="#4CAF50"/>
    </svg>
    """,
    'time': """
    <svg width="60" height="60" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="30" cy="30" r="15" fill="#FFECB3" stroke="#FFA000" stroke-width="2"/>
        <path d="M30 20 L30 30 L38 35" stroke="#FFA000" stroke-width="2" stroke-linecap="round"/>
        <circle cx="30" cy="30" r="2" fill="#FFA000"/>
    </svg>
    """,
    'habits': """
    <svg width="60" height="60" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="30" cy="35" r="10" fill="#B39DDB"/>
        <path d="M25 25 C25 20 35 20 35 25" stroke="#673AB7" stroke-width="2"/>
        <path d="M25 32 L28 35 L35 28" stroke="white" stroke-width="2"/>
    </svg>
    """,
    'work': """
    <svg width="60" height="60" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="20" y="25" width="20" height="15" rx="2" fill="#90CAF9"/>
        <path d="M25 25 V20 C25 18.8954 25.8954 18 27 18 H33 C34.1046 18 35 18.8954 35 20 V25" stroke="#2196F3" stroke-width="2"/>
    </svg>
    """,
    'health': """
    <svg width="60" height="60" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M30 20 C25 15 15 20 20 30 C25 40 30 42 30 42 C30 42 35 40 40 30 C45 20 35 15 30 20Z" fill="#EF9A9A"/>
        <path d="M40 30 Q35 36 30 30 Q25 24 20 30" stroke="#E57373" stroke-width="2"/>
    </svg>
    """,
    'relationships': """
    <svg width="60" height="60" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M25 22 C20 17 10 22 15 32 C20 42 25 44 25 44 C25 44 30 42 35 32" fill="#EF9A9A"/>
        <path d="M35 22 C40 17 50 22 45 32 C40 42 35 44 35 44 C35 44 30 42 25 32" fill="#9FA8DA"/>
    </svg>
    """,
    'projects': """
    <svg width="60" height="60" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M30 15 L40 25 L30 35 L20 25 Z" fill="#FFE082"/>
        <path d="M30 25 L30 45" stroke="#FFC107" stroke-width="2"/>
        <circle cx="30" cy="45" r="4" fill="#FFC107"/>
    </svg>
    """,
    'hobbies': """
    <svg width="60" height="60" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="30" cy="30" r="12" fill="#FFCCBC"/>
        <path d="M25 25 L35 35 M25 35 L35 25" stroke="#FF5722" stroke-width="2"/>
    </svg>
    """,
    'adulting': """
    <svg width="60" height="60" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M25 20 L25 40 L35 40 L35 20 Z" fill="#B39DDB"/>
        <path d="M25 25 L35 25 M25 30 L35 30 M25 35 L35 35" stroke="#673AB7" stroke-width="1"/>
        <circle cx="30" cy="20" r="4" fill="#9575CD"/>
    </svg>
    """
}

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Logo
st.markdown('<div class="logo">Juggl<sup>™</sup></div>', unsafe_allow_html=True)

# Progress bar based on current step
progress_percentage = {
    1: 25,
    2: 50,
    3: 75,
    4: 100
}

st.markdown(f'''
<div class="progress-container">
    <div class="progress-bar">
        <div class="progress-fill" style="width: {progress_percentage[st.session_state.step]}%;"></div>
    </div>
    <div class="progress-text">
        <span>STEP {st.session_state.step} OF 4</span>
        <span>{progress_percentage[st.session_state.step]}%</span>
    </div>
</div>
''', unsafe_allow_html=True)

# Main card container
with st.container():
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    
    # STEP 1: How would you like Juggl to help you?
    if st.session_state.step == 1:
        st.markdown('''
        <div class="card-header">
            <div class="card-title">How would you like Juggl to help you?</div>
            <div class="card-subtitle">Select all that apply to you.</div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Selection cards using columns
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            burnout = st.checkbox("Prevent Burnout", value=False, label_visibility="collapsed")
            st.markdown(f'''
            <div class="selection-card {'selected' if burnout else ''}">
                <div class="selection-radio {'selected' if burnout else ''}"></div>
                {icons['burnout']}
                <div class="selection-title">Prevent<br>Burnout</div>
            </div>
            ''', unsafe_allow_html=True)
        
        with col2:
            balance = st.checkbox("Achieve Balance", value=False, label_visibility="collapsed")
            st.markdown(f'''
            <div class="selection-card {'selected' if balance else ''}">
                <div class="selection-radio {'selected' if balance else ''}"></div>
                {icons['balance']}
                <div class="selection-title">Achieve<br>Balance</div>
            </div>
            ''', unsafe_allow_html=True)
        
        with col3:
            goals = st.checkbox("Achieve Life Goals", value=False, label_visibility="collapsed")
            st.markdown(f'''
            <div class="selection-card {'selected' if goals else ''}">
                <div class="selection-radio {'selected' if goals else ''}"></div>
                {icons['goals']}
                <div class="selection-title">Achieve Life<br>Goals</div>
            </div>
            ''', unsafe_allow_html=True)
        
        with col4:
            time = st.checkbox("Reclaim Time", value=False, label_visibility="collapsed")
            st.markdown(f'''
            <div class="selection-card {'selected' if time else ''}">
                <div class="selection-radio {'selected' if time else ''}"></div>
                {icons['time']}
                <div class="selection-title">Reclaim<br>Time</div>
            </div>
            ''', unsafe_allow_html=True)
        
        with col5:
            habits = st.checkbox("Nurture Habits", value=False, label_visibility="collapsed")
            st.markdown(f'''
            <div class="selection-card {'selected' if habits else ''}">
                <div class="selection-radio {'selected' if habits else ''}"></div>
                {icons['habits']}
                <div class="selection-title">Nurture<br>Habits</div>
            </div>
            ''', unsafe_allow_html=True)
        
        # Save selections to session state
        st.session_state.onboarding_data['goals'] = {
            'prevent_burnout': burnout,
            'achieve_balance': balance,
            'achieve_life_goals': goals,
            'reclaim_time': time,
            'nurture_habits': habits
        }
        
        # Continue button
        col_space, col_btn = st.columns([4, 1])
        with col_btn:
            if st.button("Continue", key="continue_1", use_container_width=True):
                st.session_state.step = 2
                st.experimental_rerun()
    
    # STEP 2: Let's understand your burnout risk
    elif st.session_state.step == 2:
        st.markdown('''
        <div class="card-header">
            <div class="card-title">Let's understand your burnout risk.</div>
            <div class="card-subtitle">We understand that some industries and roles come with a higher risk and so, require more support.</div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Industry selection
        st.markdown("<div style='margin-top: 30px;'><label style='font-weight: 500; font-size: 16px;'>Which industry do you work in?</label></div>", unsafe_allow_html=True)
        industry = st.text_input("Industry placeholder", value="Education, Healthcare, Finance...", label_visibility="collapsed")
        
        # Job role selection
        st.markdown("<div style='margin-top: 20px;'><label style='font-weight: 500; font-size: 16px;'>What best describes your job role?</label></div>", unsafe_allow_html=True)
        role = st.text_input("Role placeholder", value="Data Scientist, Product Manager, Engineer", label_visibility="collapsed")
        
        # Work setup
        st.markdown("<div style='margin-top: 20px;'><label style='font-weight: 500; font-size: 16px;'>What's your work set up like?</label></div>", unsafe_allow_html=True)
        
        work_setup = st.radio(
            "Work setup",
            ["Fully Remote", "Hybrid", "In Office"],
            horizontal=True,
            label_visibility="collapsed"
        )
        
        # Save selections to session state
        st.session_state.onboarding_data['profile'] = {
            'industry': industry,
            'role': role,
            'work_setup': work_setup
        }
        
        # Continue button
        col_space, col_btn = st.columns([3, 1])
        with col_btn:
            if st.button("Continue", key="continue_2", use_container_width=True):
                st.session_state.step = 3
                st.experimental_rerun()
    
    # STEP 3: Let's understand all that you juggle
    elif st.session_state.step == 3:
        st.markdown('''
        <div class="card-header">
            <div class="card-title">Let's understand all that you juggle.</div>
            <div class="card-subtitle">We will help you reclaim time for what truly matters to you.</div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Life aspects selection using columns
        col1, col2, col3 = st.columns(3)
        
        with col1:
            work = st.checkbox("Work & Career", value=False, label_visibility="collapsed")
            st.markdown(f'''
            <div class="selection-card {'selected' if work else ''}">
                <div class="selection-radio {'selected' if work else ''}"></div>
                {icons['work']}
                <div class="selection-title">Work &<br>Career</div>
            </div>
            ''', unsafe_allow_html=True)
        
        with col2:
            health = st.checkbox("Physical & Mental Health", value=False, label_visibility="collapsed")
            st.markdown(f'''
            <div class="selection-card {'selected' if health else ''}">
                <div class="selection-radio {'selected' if health else ''}"></div>
                {icons['health']}
                <div class="selection-title">Physical &<br>Mental Health</div>
            </div>
            ''', unsafe_allow_html=True)
        
        with col3:
            relationships = st.checkbox("Relationships & Connection", value=False, label_visibility="collapsed")
            st.markdown(f'''
            <div class="selection-card {'selected' if relationships else ''}">
                <div class="selection-radio {'selected' if relationships else ''}"></div>
                {icons['relationships']}
                <div class="selection-title">Relationships<br>& Connection</div>
            </div>
            ''', unsafe_allow_html=True)
        
        col4, col5, col6 = st.columns(3)
        
        with col4:
            projects = st.checkbox("Passion Projects", value=False, label_visibility="collapsed")
            st.markdown(f'''
            <div class="selection-card {'selected' if projects else ''}">
                <div class="selection-radio {'selected' if projects else ''}"></div>
                {icons['projects']}
                <div class="selection-title">Passion<br>Projects</div>
            </div>
            ''', unsafe_allow_html=True)
        
        with col5:
            hobbies = st.checkbox("Recreation & Hobbies", value=False, label_visibility="collapsed")
            st.markdown(f'''
            <div class="selection-card {'selected' if hobbies else ''}">
                <div class="selection-radio {'selected' if hobbies else ''}"></div>
                {icons['hobbies']}
                <div class="selection-title">Recreation &<br>Hobbies</div>
            </div>
            ''', unsafe_allow_html=True)
        
        with col6:
            adulting = st.checkbox("Adulting & Chores", value=False, label_visibility="collapsed")
            st.markdown(f'''
            <div class="selection-card {'selected' if adulting else ''}">
                <div class="selection-radio {'selected' if adulting else ''}"></div>
                {icons['adulting']}
                <div class="selection-title">Adulting &<br>Chores</div>
            </div>
            ''', unsafe_allow_html=True)
        
        # Save selections to session state
        st.session_state.onboarding_data['life_aspects'] = {
            'work': work,
            'health': health,
            'relationships': relationships,
            'projects': projects,
            'hobbies': hobbies,
            'adulting': adulting
        }
        
        # Continue button
        col_space, col_btn = st.columns([3, 1])
        with col_btn:
            if st.button("Continue", key="continue_3", use_container_width=True):
                st.session_state.step = 4
                st.experimental_rerun()
    
    # STEP 4: Let's sync all your calendars in one place
    elif st.session_state.step == 4:
        st.markdown('''
        <div class="card-header">
            <div class="card-title">Let's sync all your calendars in one place.</div>
            <div class="card-subtitle">We will optimise your schedule across your calendars.</div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Email and calendar type display
        st.markdown('''
        <div class="email-container">
            <div class="email-avatar">J</div>
            <div class="email-label">johndoe@gmail.com</div>
            <div class="calendar-type">Personal</div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Add calendar button
        st.markdown('''
        <div class="add-calendar-button">Add Calendar</div>
        ''', unsafe_allow_html=True)
        
        # Placeholder for adding additional calendars
        add_more = st.checkbox("Add more calendars", value=False, label_visibility="hidden")
        
        # Continue button
        col_space, col_btn = st.columns([3, 1])
        with col_btn:
            if st.button("Continue", key="continue_4", use_container_width=True):
                # Mark onboarding as complete
                st.session_state.onboarding_complete = True
                st.session_state.show_insights_link = True
                st.experimental_rerun()
    
    # Show insights link after completing onboarding
    if st.session_state.get('show_insights_link', False):
        st.markdown("""
        <div style="text-align: center; margin-top: 20px;">
            <p style="color: #4CAF50; font-weight: bold; font-size: 18px;">Onboarding complete!</p>
            <p style="margin-bottom: 20px;">You're all set up and ready to start your Juggl journey!</p>
            <a href="/Insights" target="_self" style="display: inline-block; background: #4CAF50; color: white; padding: 10px 30px; border-radius: 30px; text-decoration: none; font-weight: bold;">Go to Insights Dashboard</a>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Continue to Insights", key="insights_direct_button"):
            # Create a Streamlit URL parameter to force navigation
            st.query_params.page = "insights"
            
            # Also try JavaScript redirect as fallback
            st.markdown("""
            <script>
                window.location.href = "/Insights";
            </script>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close card container

# Store onboarding completion in a session cookie to persist between pages
if st.session_state.get('onboarding_complete', False):
    st.markdown("""
    <script>
        // Store completion status in localStorage
        localStorage.setItem('onboarding_complete', 'true');
    </script>
    """, unsafe_allow_html=True)