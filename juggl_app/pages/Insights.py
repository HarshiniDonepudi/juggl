import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge
import matplotlib.gridspec as gridspec

# Check if coming from onboarding
def check_onboarding_status():
    # Check URL parameters first
    if 'page' in st.query_params and st.query_params.page.lower() == 'insights':
        return True
    
    # Then check session state
    if 'onboarding_complete' in st.session_state and st.session_state.onboarding_complete:
        return True
    
    return False

# Set page config
st.set_page_config(page_title="Juggl - Insights", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for the insights dashboard
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* Base Styles */
body {
    font-family: 'Inter', sans-serif;
    background-color: #f5f5f5;
    color: #333;
    margin: 0;
    padding: 0;
}

/* Hide Streamlit Elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.block-container {padding-top: 0 !important; padding-bottom: 0 !important;}

/* App Container */
.app-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* Top Header */
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
}

.logo {
    font-size: 24px;
    font-weight: 700;
    color: #333;
}

.logo-tm {
    font-size: 10px;
    vertical-align: super;
}

.page-title {
    font-size: 20px;
    font-weight: 600;
}

.check-in-button {
    background: #000;
    color: white;
    padding: 8px 16px;
    border-radius: 20px;
    text-decoration: none;
    font-size: 14px;
    font-weight: 500;
}

/* Sidebar Menu */
.sidebar {
    width: 150px;
    float: left;
    margin-right: 30px;
}

.sidebar-menu {
    list-style: none;
    padding: 0;
    margin: 0;
}

.sidebar-menu li {
    margin-bottom: 15px;
}

.sidebar-menu a {
    color: #666;
    text-decoration: none;
    font-size: 15px;
    font-weight: 500;
}

.sidebar-menu a.active {
    color: #000;
    font-weight: 600;
}

/* Main Content */
.main-content {
    margin-left: 180px;
}

/* Dashboard card */
.dashboard-card {
    background: white;
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    position: relative;
}

.card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}

.card-title {
    font-size: 16px;
    font-weight: 600;
}

.card-subtitle {
    font-size: 14px;
    color: #666;
    margin-top: 5px;
}

/* Stats and Charts */
.stats-container {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
}

.stat-item {
    text-align: center;
}

.stat-value {
    font-size: 24px;
    font-weight: 600;
    margin-bottom: 5px;
}

.stat-label {
    font-size: 12px;
    color: #666;
}

/* Progress Indicators */
.progress-circle {
    width: 150px;
    height: 150px;
    margin: 0 auto;
    position: relative;
}

.progress-value {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 24px;
    font-weight: 600;
}

.progress-label {
    position: absolute;
    top: 65%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 12px;
    color: #666;
    text-align: center;
    width: 100%;
}

/* Recommendation Card */
.recommendation-card {
    background: white;
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.recommendation-title {
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 10px;
}

.recommendation-text {
    font-size: 14px;
    color: #666;
    margin-bottom: 15px;
}

.recommendation-cta {
    color: #007bff;
    font-weight: 500;
    text-decoration: none;
}

/* Welcome Section */
.welcome-section {
    margin-bottom: 30px;
}

.welcome-heading {
    font-size: 24px;
    font-weight: 600;
    margin-bottom: 10px;
}

.welcome-text {
    font-size: 14px;
    color: #555;
    line-height: 1.5;
}

/* Insights Grid */
.insights-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
}

.big-metric {
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 5px;
}

.metric-label {
    font-size: 12px;
    color: #666;
    font-weight: 500;
}

.metric-comparison {
    font-size: 12px;
    color: #28a745;
    margin-top: 5px;
}

.metric-comparison.negative {
    color: #dc3545;
}

/* Small metrics row */
.small-metrics {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-top: 20px;
}

.small-metric-card {
    background: white;
    border-radius: 8px;
    padding: 15px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.small-metric-title {
    font-size: 14px;
    color: #999;
    margin-bottom: 10px;
    font-weight: 500;
}

.small-metric-chart {
    display: flex;
    margin-bottom: 10px;
}

.small-metric-values {
    display: flex;
    justify-content: space-between;
}

.small-metric-current, .small-metric-average {
    text-align: center;
}

.small-metric-value {
    font-size: 20px;
    font-weight: 600;
}

.small-metric-label {
    font-size: 12px;
    color: #999;
}

/* Questions Section */
.questions-section {
    margin-top: 30px;
}

.search-box {
    width: 100%;
    padding: 10px 15px;
    border: 1px solid #ddd;
    border-radius: 20px;
    font-size: 14px;
    margin-bottom: 15px;
}

.questions-row {
    display: flex;
    gap: 15px;
    overflow-x: auto;
    padding-bottom: 10px;
}

.question-pill {
    white-space: nowrap;
    padding: 8px 16px;
    background: #f0f0f0;
    border-radius: 20px;
    font-size: 14px;
    color: #666;
    cursor: pointer;
}

.question-pill.active {
    background: #000;
    color: white;
}

/* Helpful Feedback */
.helpful-feedback {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    margin-top: 20px;
    gap: 10px;
}

.helpful-text {
    font-size: 14px;
    color: #666;
}

.feedback-button {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background: #f0f0f0;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
}

.feedback-button:hover {
    background: #e0e0e0;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .insights-grid {
        grid-template-columns: 1fr;
    }
    
    .small-metrics {
        grid-template-columns: 1fr;
    }
}
</style>
"""

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Check for and clear navigation parameters
came_from_onboarding = check_onboarding_status()
# Clear query parameters by accessing the object directly
if 'page' in st.query_params:
    del st.query_params.page

# Also check localStorage for onboarding completion using JS
st.markdown("""
<script>
    // Check if we have onboarding_complete in localStorage
    const onboardingComplete = localStorage.getItem('onboarding_complete');
    if (onboardingComplete === 'true') {
        // Can communicate back to Python via Streamlit's componentValue
        window.parent.postMessage({
            type: 'streamlit:setComponentValue',
            value: true
        }, '*');
    }
</script>
""", unsafe_allow_html=True)

# Define some example data
user_name = "Rhea"
burnout_risk = 65
burnout_week = 57
burnout_prev_week = 73
work_hours_week = 48
work_hours_prev_week = 58
life_hours_week = 120
life_hours_prev_week = 110
productivity_today = 3.0
productivity_avg = 3.5
optimism_today = 3.2
optimism_avg = 3.5
energy_today = 3.4
energy_avg = 3.5

# Initialize session state for view if not already set
if 'view' not in st.session_state:
    st.session_state.view = 1

# Function to create a donut chart for burnout risk
def create_donut_chart(value, title, subtitle="", size_inches=(3, 3)):
    fig, ax = plt.subplots(figsize=size_inches)
    
    # Draw the background circle (gray)
    wedge = Wedge(center=(0, 0), r=0.8, theta1=0, theta2=360, width=0.2, facecolor='#e0e0e0')
    ax.add_patch(wedge)
    
    # Draw the progress circle (black)
    wedge = Wedge(center=(0, 0), r=0.8, theta1=90, theta2=90-value*3.6, width=0.2, facecolor='#000000')
    ax.add_patch(wedge)
    
    # Add text in the center
    ax.text(0, 0.1, f"{value}%", ha='center', va='center', fontsize=14, fontweight='bold')
    ax.text(0, -0.1, title, ha='center', va='center', fontsize=8, color='#666')
    if subtitle:
        ax.text(0, -0.25, subtitle, ha='center', va='center', fontsize=6, color='#999')
    
    # Set aspect ratio and remove axes
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    
    return fig

# Function to create a ratio donut chart
def create_ratio_chart(ratio_text, title, size_inches=(3, 3)):
    fig, ax = plt.subplots(figsize=size_inches)
    
    # Draw the background circle (gray)
    wedge = Wedge(center=(0, 0), r=0.8, theta1=0, theta2=360, width=0.2, facecolor='#e0e0e0')
    ax.add_patch(wedge)
    
    # Draw the progress circle (black) - for demonstration 75% complete
    wedge = Wedge(center=(0, 0), r=0.8, theta1=90, theta2=-270, width=0.2, facecolor='#000000')
    ax.add_patch(wedge)
    
    # Add text in the center
    ax.text(0, 0, ratio_text, ha='center', va='center', fontsize=14, fontweight='bold')
    ax.text(0, -0.25, title, ha='center', va='center', fontsize=8, color='#666')
    
    # Set aspect ratio and remove axes
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    
    return fig

# Function to create time insights chart
def create_time_insights_chart():
    fig = plt.figure(figsize=(4, 4))
    
    # Data
    labels = ['Meetings', 'Deep Work', 'Appointments', 'Other']
    sizes = [20, 7, 5, 6]
    colors = ['#000000', '#333333', '#666666', '#999999']
    
    # Create a pie chart
    wedges, texts = plt.pie(sizes, colors=colors, startangle=90, counterclock=False, wedgeprops={'width': 0.3, 'edgecolor': 'w'})
    
    # Create center circle to make it a donut chart
    centre_circle = plt.Circle((0, 0), 0.7, fc='white')
    fig.gca().add_artist(centre_circle)
    
    # Add Total Hours text in center
    plt.text(0, 0.1, "48", horizontalalignment='center', verticalalignment='center', fontsize=14, fontweight='bold')
    plt.text(0, -0.1, "TOTAL HOURS", horizontalalignment='center', verticalalignment='center', fontsize=6)
    
    # Add legend
    legend_elements = []
    for i, (label, size) in enumerate(zip(labels, sizes)):
        legend_elements.append(plt.Line2D([0], [0], marker='o', color='w', label=f'{label} {size}h', 
                          markerfacecolor=colors[i], markersize=8))
    
    plt.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1, 0.5), frameon=False)
    
    plt.axis('equal')
    plt.tight_layout()
    
    return fig

# App Layout
st.markdown('<div class="app-container">', unsafe_allow_html=True)

# Display welcome notification if coming from onboarding
if came_from_onboarding:
    st.success("🎉 Welcome to your Insights Dashboard! Onboarding complete!")
    # Store onboarding completion in session state for this session
    st.session_state.onboarding_complete = True

# Header with Logo and Check-In button
st.markdown('''
<div class="header">
    <div class="logo">Juggl<span class="logo-tm">™</span></div>
    <div class="page-title">Insights</div>
    <div><a href="#" class="check-in-button">Check In</a></div>
</div>
''', unsafe_allow_html=True)

# Two column layout for sidebar and main content
col1, col2 = st.columns([1, 6])

with col1:
    st.markdown('''
    <div class="sidebar">
        <ul class="sidebar-menu">
            <li><a href="#">Today</a></li>
            <li><a href="#" class="active">Insights</a></li>
            <li><a href="#">Habits</a></li>
            <li><a href="#">Calendar</a></li>
            <li><a href="#">Settings</a></li>
        </ul>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    # Main Content - View 1 (Analysis view from Image 1)
    if st.session_state.view == 1:
        # Welcome section with personalized greeting
        st.markdown(f'''
        <div class="welcome-section">
            <h1 class="welcome-heading">Hi {user_name}</h1>
            <p class="welcome-text">
                We understand as a Product Manager in Tech, juggling career, health, relationships, hobbies, 
                chores, and passion projects, you require true support that goes beyond productivity.
            </p>
        </div>
        ''', unsafe_allow_html=True)
        
        # Main insights card with time insights and burnout risk
        st.markdown('''
        <div class="dashboard-card">
        ''', unsafe_allow_html=True)
        
        # Two-column layout for time insights and burnout risk
        left_col, right_col = st.columns([1, 1])
        
        with left_col:
            st.markdown('''
            <div class="card-title">Time Insights</div>
            <p class="card-subtitle">
                Based on events in your calendar, we were able to assess your time use 
                and determine how you spend your time.
            </p>
            ''', unsafe_allow_html=True)
            
            # Time insights donut chart
            time_fig = create_time_insights_chart()
            st.pyplot(time_fig)
        
        with right_col:
            st.markdown('''
            <div class="card-title">Burnout Risk</div>
            <p class="card-subtitle">
                Based on your industry, job role, and everything you juggle, we were 
                able to determine your burnout risk.
            </p>
            ''', unsafe_allow_html=True)
            
            # Burnout risk donut chart
            burnout_fig = create_donut_chart(burnout_risk, "BURNOUT RISK")
            st.pyplot(burnout_fig)
        
        # Helpful feedback section
        st.markdown('''
        <div class="helpful-feedback">
            <div class="helpful-text">Was this helpful?</div>
            <div class="feedback-button">👎</div>
            <div class="feedback-button">👍</div>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)  # Close dashboard card
        
        # Recommendation card
        st.markdown('''
        <div class="recommendation-card">
            <div class="recommendation-title">Set Work & Life Boundaries</div>
            <p class="recommendation-text">
                Tell us how you'd ideally spend your time, we'll help you make it happen.
            </p>
            <a href="#" class="recommendation-cta">→</a>
        </div>
        ''', unsafe_allow_html=True)
        
        # Add button to switch to view 2
        if st.button("View Detailed Insights"):
            st.session_state.view = 2
            st.experimental_rerun()
    
    # Main Content - View 2 (Insights view from Image 2)
    elif st.session_state.view == 2:
        # Top insights grid with burnout risk, work hours, life hours
        st.markdown('<div class="insights-grid">', unsafe_allow_html=True)
        
        # Burnout Risk Card
        st.markdown('''
        <div class="dashboard-card">
            <div class="card-header">
                <div class="card-title">Burnout Risk</div>
                <div><a href="#" style="color: #999; text-decoration: none;">↗</a></div>
            </div>
            <div class="card-subtitle">Includes meetings, work hours, stress indicators</div>
            <div style="display: flex; justify-content: space-between; margin-top: 20px;">
                <div>
                    <div style="font-size: 12px; color: #666;">This Week</div>
                    <div style="font-size: 18px; font-weight: 600; margin-top: 5px;">57<span style="font-size: 14px;">%</span></div>
                </div>
                <div>
                    <div style="font-size: 12px; color: #666;">Last Week</div>
                    <div style="font-size: 18px; font-weight: 600; margin-top: 5px;">73<span style="font-size: 14px;">%</span></div>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        burnout_fig = create_donut_chart(57, "Burnout Risk", "-37%", (3, 3))
        st.pyplot(burnout_fig)
        
        # Work Hours Card
        st.markdown('''
        <div class="dashboard-card">
            <div class="card-header">
                <div class="card-title">Work</div>
                <div><a href="#" style="color: #999; text-decoration: none;">↗</a></div>
            </div>
            <div class="card-subtitle">Includes meetings, deep work, tasks</div>
            <div style="display: flex; justify-content: space-between; margin-top: 20px;">
                <div>
                    <div style="font-size: 12px; color: #666;">This Week</div>
                    <div style="font-size: 18px; font-weight: 600; margin-top: 5px;">48<span style="font-size: 14px;">h</span></div>
                </div>
                <div>
                    <div style="font-size: 12px; color: #666;">Last Week</div>
                    <div style="font-size: 18px; font-weight: 600; margin-top: 5px;">58<span style="font-size: 14px;">h</span></div>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Life Hours Card
        st.markdown('''
        <div class="dashboard-card">
            <div class="card-header">
                <div class="card-title">Life</div>
                <div><a href="#" style="color: #999; text-decoration: none;">↗</a></div>
            </div>
            <div class="card-subtitle">Includes sleep, personal time, leisure</div>
            <div style="display: flex; justify-content: space-between; margin-top: 20px;">
                <div>
                    <div style="font-size: 12px; color: #666;">This Week</div>
                    <div style="font-size: 18px; font-weight: 600; margin-top: 5px;">120<span style="font-size: 14px;">h</span></div>
                </div>
                <div>
                    <div style="font-size: 12px; color: #666;">Last Week</div>
                    <div style="font-size: 18px; font-weight: 600; margin-top: 5px;">110<span style="font-size: 14px;">h</span></div>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        ratio_fig = create_ratio_chart("2:5", "Work-Life\nRatio", (3, 3))
        st.pyplot(ratio_fig)
        
        st.markdown('</div>', unsafe_allow_html=True)  # Close insights grid
        
        # Small metrics - Productivity, Optimism, Energy
        st.markdown('<div class="small-metrics">', unsafe_allow_html=True)
        
        # Productivity Metric
        st.markdown('''
        <div class="small-metric-card">
            <div class="small-metric-title">Productivity</div>
            <div class="small-metric-text">Your productivity has been steadily increasing by 10% this week</div>
            <div class="small-metric-values">
                <div class="small-metric-current">
                    <div style="font-size: 12px; color: #666;">Today</div>
                    <div style="font-size: 18px; font-weight: 600;">3</div>
                </div>
                <div class="small-metric-average">
                    <div style="font-size: 12px; color: #666;">Average</div>
                    <div style="font-size: 18px; font-weight: 600;">3.5</div>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Optimism Metric
        st.markdown('''
        <div class="small-metric-card">
            <div class="small-metric-title">Optimism</div>
            <div class="small-metric-text">Your optimism has been steadily increasing by 7% this week</div>
            <div class="small-metric-values">
                <div class="small-metric-current">
                    <div style="font-size: 12px; color: #666;">Today</div>
                    <div style="font-size: 18px; font-weight: 600;">3.2</div>
                </div>
                <div class="small-metric-average">
                    <div style="font-size: 12px; color: #666;">Average</div>
                    <div style="font-size: 18px; font-weight: 600;">3.5</div>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Energy Metric
        st.markdown('''
        <div class="small-metric-card">
            <div class="small-metric-title">Energy</div>
            <div class="small-metric-text">Your energy has decreased slightly by 2% this week</div>
            <div class="small-metric-values">
                <div class="small-metric-current">
                    <div style="font-size: 12px; color: #666;">Today</div>
                    <div style="font-size: 18px; font-weight: 600;">3.4</div>
                </div>
                <div class="small-metric-average">
                    <div style="font-size: 12px; color: #666;">Average</div>
                    <div style="font-size: 18px; font-weight: 600;">3.5</div>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)  # Close small metrics
        
        # Questions section
        st.markdown('''
        <div class="questions-section">
            <input type="text" class="search-box" placeholder="How much do meetings impact my mood?">
            <div class="questions-row">
                <div class="question-pill active">How do meetings impact my mood?</div>
                <div class="question-pill">How do breaks impact my energy?</div>
                <div class="question-pill">What contributes to my productivity?</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Add button to switch back to view 1
        if st.button("View Summary Insights"):
            st.session_state.view = 1
            st.experimental_rerun()

st.markdown('</div>', unsafe_allow_html=True)  # Close app container