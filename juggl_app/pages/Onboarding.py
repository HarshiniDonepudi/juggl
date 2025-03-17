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

# Custom CSS to style the app exactly like the image
custom_css = """
<style>
body {
    font-family: sans-serif;
    background-color: #f5f5f5;
    margin: 0;
    padding: 0;
}

/* Hide default Streamlit components */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.block-container {padding-top: 0 !important; padding-bottom: 0 !important;}

/* Logo Style */
.logo {
    font-family: sans-serif;
    font-weight: bold;
    font-size: 18px;
    color: #333;
    padding: 20px 0 10px 20px;
}

/* Card Container */
.card-container {
    max-width: 500px;
    margin: 20px auto;
    background: white;
    border-radius: 8px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    padding: 30px;
}

/* Card Header */
.card-header {
    text-align: center;
    margin-bottom: 20px;
    border-bottom: 1px solid #f0f0f0;
    padding-bottom: 15px;
}

.card-title {
    font-weight: bold;
    font-size: 16px;
    margin-bottom: 5px;
}

.card-subtitle {
    color: #777;
    font-size: 13px;
}

/* Custom styling for Streamlit components */
div.stButton > button {
    border-radius: 20px !important;
    padding: 5px 20px !important;
    font-size: 14px !important;
    font-weight: normal !important;
}

.stButton button[data-testid="baseButton-secondary"] {
    background-color: #f5f5f5 !important;
    color: #666 !important;
    border: 1px solid #ddd !important;
}

.stButton button[data-testid="baseButton-primary"] {
    background-color: #000000 !important;
    color: white !important;
    border: none !important;
}

.stCheckbox {
    margin-bottom: 15px;
}

.stSelectbox > div > div {
    padding: 5px 10px !important;
}

.stRadio > div {
    display: flex !important;
    flex-direction: row !important;
}

.stRadio > div > div {
    margin-right: 15px !important;
}

/* Success message for final step */
.success-message {
    text-align: center;
    color: #4CAF50;
    font-weight: bold;
    font-size: 18px;
    margin: 20px 0;
}

.center-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 20px;
}
</style>
"""

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Define function to go to insights page
def go_to_insights():
    # Mark onboarding as complete
    st.session_state.onboarding_complete = True
    
    # Set Insights as the active page
    st.session_state.active_page = "Insights"
    
    # Redirect to the insights page using query parameters
    # This is a more reliable way to navigate between pages in Streamlit
    st.experimental_set_query_params(page="Insights")
    
    # Alternative direct link using HTML
    st.markdown("""
    <meta http-equiv="refresh" content="0; URL=Insights">
    """, unsafe_allow_html=True)

# Logo
st.markdown('<div class="logo">Juggl</div>', unsafe_allow_html=True)

# Step indicators (1, 2, 3, 5) with current step highlighted
step_indicators = """
<div style='display: flex; justify-content: center; margin: 10px 0 30px 0; gap: 40px;'>
"""

for i in range(1, 6):
    if i == 4:  # Skip step 4 as shown in the image
        continue
    
    if i == st.session_state.step:
        # Current step - blue
        indicator = f"<div style='color: #007bff; font-weight: bold;'>Onboarding {i}</div>"
    else:
        # Other steps - gray
        indicator = f"<div style='color: #ccc;'>Onboarding {i}</div>"
    
    step_indicators += indicator

step_indicators += "</div>"

# Display step indicators
st.markdown(step_indicators, unsafe_allow_html=True)

# Check if we need to go to insights page (coming back from final step)
if st.session_state.get('go_to_insights', False):
    go_to_insights()
    st.stop()

# Main card container
with st.container():
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    
    # STEP 1: How do you want Juggl to help you?
    if st.session_state.step == 1:
        st.markdown('''
        <div class="card-header">
            <div class="card-title">How do you want Juggl to help you?</div>
            <div class="card-subtitle">Select all that apply to your situation</div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Grid for selection options - using columns
        col1, col2, col3 = st.columns(3)
        
        with col1:
            detect_burnout = st.checkbox("Detect burnout signs", value=True)
            track_progress = st.checkbox("Track my progress")
        
        with col2:
            work_life_balance = st.checkbox("Work-life balance")
            time_mgmt = st.checkbox("Time management")
        
        with col3:
            improve_focus = st.checkbox("Improve focus")
            goals = st.checkbox("Set & achieve goals")
        
        # Save selections to session state
        st.session_state.onboarding_data['goals'] = {
            'detect_burnout': detect_burnout,
            'track_progress': track_progress,
            'work_life_balance': work_life_balance,
            'time_mgmt': time_mgmt,
            'improve_focus': improve_focus,
            'goals': goals
        }
        
        # Next button aligned to right
        cols = st.columns([3, 1])
        with cols[1]:
            if st.button("Next", key="next_1", use_container_width=True):
                st.session_state.step = 2
                st.experimental_rerun()
    
    # STEP 2: Let's understand you
    elif st.session_state.step == 2:
        st.markdown('''
        <div class="card-header">
            <div class="card-title">Let's understand you.</div>
            <div class="card-subtitle">Tell us about yourself to customize your experience</div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Form fields
        st.markdown("<label style='font-weight: 500; font-size: 14px; margin-bottom: 5px; display: block;'>What industry do you work in?</label>", unsafe_allow_html=True)
        industry = st.selectbox(
            "",
            ["", "Technology", "Healthcare", "Finance", "Education", "Other"],
            label_visibility="collapsed"
        )
        
        st.markdown("<label style='font-weight: 500; font-size: 14px; margin-bottom: 5px; margin-top: 15px; display: block;'>What best describes your job role?</label>", unsafe_allow_html=True)
        role = st.selectbox(
            "",
            ["", "Manager/Director", "Individual Contributor", "Executive", "Other"],
            label_visibility="collapsed"
        )
        
        st.markdown("<label style='font-weight: 500; font-size: 14px; margin-bottom: 5px; margin-top: 15px; display: block;'>What's your work set up like?</label>", unsafe_allow_html=True)
        setup = st.radio(
            "",
            ["Remote", "Hybrid", "In-office"],
            horizontal=True,
            label_visibility="collapsed"
        )
        
        # Save selections to session state
        st.session_state.onboarding_data['profile'] = {
            'industry': industry,
            'role': role,
            'setup': setup
        }
        
        # Previous and Next buttons
        cols1, cols2 = st.columns(2)
        with cols1:
            if st.button("Previous", key="prev_2", use_container_width=True):
                st.session_state.step = 1
                st.experimental_rerun()
        with cols2:
            if st.button("Next", key="next_2", use_container_width=True):
                st.session_state.step = 3
                st.experimental_rerun()
    
    # STEP 3: Let's understand your life
    elif st.session_state.step == 3:
        st.markdown('''
        <div class="card-header">
            <div class="card-title">Let's understand your life.</div>
            <div class="card-subtitle">Select all aspects that you want to manage better</div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Grid of life aspects
        col1, col2, col3 = st.columns(3)
        
        with col1:
            work = st.checkbox("Work & Career", value=True)
            hobbies = st.checkbox("Hobbies & Interests")
        
        with col2:
            health = st.checkbox("Health & Wellbeing", value=True)
            finances = st.checkbox("Finances")
        
        with col3:
            relationships = st.checkbox("Family & Relationships")
            personal = st.checkbox("Personal Growth")
        
        # Save selections to session state
        st.session_state.onboarding_data['life_aspects'] = {
            'work': work,
            'hobbies': hobbies,
            'health': health,
            'finances': finances,
            'relationships': relationships,
            'personal': personal
        }
        
        # Previous and Next buttons
        cols1, cols2 = st.columns(2)
        with cols1:
            if st.button("Previous", key="prev_3", use_container_width=True):
                st.session_state.step = 2
                st.experimental_rerun()
        with cols2:
            if st.button("Next", key="next_3", use_container_width=True):
                st.session_state.step = 5  # Skip to step 5 as shown in the image
                st.experimental_rerun()
    
    # STEP 5: Sync calendars (skip step 4 as per the image)
    elif st.session_state.step == 5:
        st.markdown('''
        <div class="card-header">
            <div class="card-title">Sync all your calendars in one place.</div>
            <div class="card-subtitle">Connect your calendars to get the most out of Juggl</div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Simple calendar connection UI
        st.image("https://via.placeholder.com/450x130?text=Calendar+UI", use_column_width=True)
        
        # Email input and button
        col1, col2 = st.columns([3, 1])
        with col1:
            email = st.text_input("", value="yourname@gmail.com", label_visibility="collapsed")
        with col2:
            add_calendar = st.button("Add Calendar", use_container_width=True)
        
        if add_calendar:
            st.success(f"Calendar for {email} connected successfully!")
        
        # Save selections to session state
        st.session_state.onboarding_data['calendar'] = {
            'email': email,
            'connected': add_calendar
        }
        
        # Previous and Next buttons
        cols1, cols2 = st.columns(2)
        with cols1:
            if st.button("Previous", key="prev_5", use_container_width=True):
                st.session_state.step = 3
                st.experimental_rerun()
        with cols2:
            # Complete onboarding button
            if st.button("Finish", key="complete", use_container_width=True):
                # Display success message
                st.success("Onboarding complete!")
                st.markdown("""
                <div class="center-content">
                    <a href="Insights" style="display: inline-block; background: #4CAF50; color: white; padding: 10px 30px; border-radius: 30px; text-decoration: none; font-weight: bold; margin-top: 20px;">Go to Insights Dashboard</a>
                </div>
                """, unsafe_allow_html=True)
                
                # Also add a streamlit button as a backup navigation method
                if st.button("View Your Insights", key="insights_button"):
                    # Set the flag to redirect on next load
                    st.session_state.go_to_insights = True
                    st.experimental_rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close card container

# Check if we have pages.py file and create one if needed
import os
pages_dir = "pages"
if not os.path.exists(pages_dir):
    os.makedirs(pages_dir)

# Check if Insights.py exists in the pages directory
insights_path = os.path.join(pages_dir, "Insights.py")
if not os.path.exists(insights_path):
    # Create a simple placeholder file that will show up in the sidebar
    with open(insights_path, "w") as f:
        f.write("""import streamlit as st
st.title("Insights")
st.write("The Insights page is being set up.")
""")