import streamlit as st
import plotly.graph_objects as go

# ---------------------------
# PAGE CONFIG & CUSTOM CSS
# ---------------------------
st.set_page_config(
    page_title="Juggl - Insights",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to remove scrollbars and style the two pages
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* Hide default Streamlit elements */
#MainMenu, footer, header {visibility: hidden;}
body {
  font-family: 'Inter', sans-serif;
  margin: 0; 
  padding: 0;
  height: 100vh;
  overflow: hidden; /* No scrolling */
  background-image: linear-gradient(to bottom, #ffffff 50%, #41a162 100%);
  letter-spacing: -0.01em;
}

/* Container for each "page" */
.block-container {
  padding-top: 0 !important; 
  padding-bottom: 0 !important;
  max-width: 1200px;
  margin: 0 auto;
}

/* Shared card style */
.insights-container {
  background-color: #fff;
  padding: 20px; 
  border-radius: 24px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
  margin-top: 5px;
}

/* Headings & text */
h1,h2 {
  margin-bottom: 8px;
  text-align: center;
  font-weight: 600;
  color: #282828;
}
h1 {
  font-size: 2.2rem;
}
h2 {
  font-size: 1.6rem;
}
.subtext {
  color: #6b7280; 
  font-size: 0.95rem;
  line-height: 1.5;
  margin-bottom: 15px;
  text-align: center;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
  font-weight: 400;
}

/* Buttons */
.stButton > button {
  background-color: #3a86d0;
  color: white;
  border-radius: 20px;
  font-weight: 500;
  padding: 0.5rem 2.5rem;
  border: none;
  box-shadow: 0 2px 5px rgba(58,134,208,0.2);
  transition: all 0.2s ease;
}
.stButton > button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(58,134,208,0.3);
}

/* Smaller headings */
h3 {
  margin-top: 0 !important;
  margin-bottom: 8px !important;
  font-size: 1.3rem !important;
  font-weight: 600 !important;
  color: #282828 !important;
}
.chart-description {
  font-size: 0.9rem;
  line-height: 1.5;
  color: #6b7280;
  margin: 0 0 10px 0;
  font-weight: 400;
}
.explanation {
  font-size: 0.9rem;
  line-height: 1.5;
  margin: 10px 0;
  color: #4b5563;
}

/* Next-steps text */
.next-steps-text {
  font-size: 0.9rem;
  line-height: 1.5;
  margin: 8px auto 10px auto;
  max-width: 800px;
  text-align: center;
  color: #4b5563;
}

/* For columns, etc. */
.css-ocqkz7, div[data-testid="stVerticalBlock"] {
  gap: 0.5rem !important;
}
 /* CTA Button */
    .cta-container {
        text-align: center;
        margin: 50px 0;
    }

    .cta-button {
  background-color: #3a86d0;
  color: white;
  border-radius: 20px;
  font-weight: 500;
  padding: 0.5rem 2.5rem;
  border: none;
  box-shadow: 0 2px 5px rgba(58,134,208,0.2);
  transition: all 0.2s ease;
    }

    .cta-button:hover {
        background: #1976D2;
        transform: translateY(-2px);
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ---------------------------
# DEMO DATA
# ---------------------------
time_data = {"Work Meetings": 15, "Deep Work": 10, "Appointments": 8, "Misc": 9}
burnout_risk = 62
top_5_factors = [
    ("Frequent Meetings & Context Switching", "25%"),
    ("Weekend/Evening Tasks", "20%"),
    ("High Expectations & Multi-Disciplinary Focus", "20%"),
    ("Over-Commitment to Side Projects", "20%"),
    ("Minimal Buffer Time/Breaks", "15%")
]

# Predefine "ideal week" categories + default hours
ideal_categories = {
    "Work & Career": 32,
    "Physical & Mental Health": 8,
    "Connection & Relationships": 8,
    "Passion Projects": 8,
    "Recreation & Hobbies": 8,
    "Adulting & Chores": 8,
    "Sleep & Recovery": 56,
}

# ---------------------------
# CHART FUNCTIONS
# ---------------------------
def create_time_donut(data_dict):
    labels = list(data_dict.keys())
    values = list(data_dict.values())
    colors = ['#62cc89','#f89e76','#6b9fe8','#a77fcc','#ffc107','#2ec4b6','#6dbe8b','#8c8c8c']
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.6,
        textinfo='none',
        marker=dict(colors=colors[:len(values)]),
    )])
    # Center text
    fig.add_annotation(dict(
        text=f"{sum(values)}<br>Hrs",
        x=0.5, y=0.5, font_size=14, showarrow=False
    ))
    fig.update_layout(margin=dict(l=0,r=0,t=0,b=0), height=180)
    return fig

def create_burnout_donut(value):
    risk_data = {"Risk": value, "Safe": 100-value}
    colors = ['#f89e76','#e0e0e0']
    fig = go.Figure(data=[go.Pie(
        labels=list(risk_data.keys()),
        values=list(risk_data.values()),
        hole=0.6,
        textinfo='none',
        marker=dict(colors=colors),
        showlegend=False
    )])
    fig.add_annotation(dict(
        text=f"{value}%", x=0.5, y=0.5, font_size=14, showarrow=False
    ))
    fig.update_layout(margin=dict(l=0,r=0,t=0,b=0), height=180)
    return fig

# ---------------------------
# STATE & PAGE FLOW
# ---------------------------
if "page" not in st.session_state:
    st.session_state.page = 1

# ---------------------------
# PAGE 1: INSIGHTS
# ---------------------------
def page_insights():
    st.markdown("<div class='insights-container'>", unsafe_allow_html=True)
    st.markdown("""
    <h1>Hi Joe</h1>
    <p class="subtext">
      We understand as a Product Manager in Tech, juggling career, health, relationships, 
      hobbies, chores, and passion projects, you need support that goes beyond productivity.
    </p>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<h3>Time Insights</h3>", unsafe_allow_html=True)
        st.markdown("<p class='chart-description'>We analyzed your calendar events.</p>", unsafe_allow_html=True)
        donut_fig = create_time_donut(time_data)
        st.plotly_chart(donut_fig, use_container_width=True)

    with c2:
        st.markdown("<h3>Burnout Risk</h3>", unsafe_allow_html=True)
        st.markdown(f"<p class='chart-description'>Current Burnout Risk: <b>{burnout_risk}%</b></p>", unsafe_allow_html=True)
        burn_fig = create_burnout_donut(burnout_risk)
        st.plotly_chart(burn_fig, use_container_width=True)

    st.markdown("""
    <p class='explanation'>
      Your burnout risk is based on scheduled hours and context switching 
      across multiple responsibilities.
    </p>
    """, unsafe_allow_html=True)

    # Top factors
    st.markdown("<h3 class='factors-heading'>Top 5 Contributing Factors</h3>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
        <div style="background:#f5f9ff;border-left:4px solid #3a86d0;padding:10px;border-radius:6px;margin-bottom:10px;">
          {top_5_factors[0][0]} <span style="float:right;">{top_5_factors[0][1]}</span>
        </div>
        <div style="background:#f5f9ff;border-left:4px solid #3a86d0;padding:10px;border-radius:6px;margin-bottom:10px;">
          {top_5_factors[2][0]} <span style="float:right;">{top_5_factors[2][1]}</span>
        </div>
        <div style="background:#f5f9ff;border-left:4px solid #3a86d0;padding:10px;border-radius:6px;">
          {top_5_factors[4][0]} <span style="float:right;">{top_5_factors[4][1]}</span>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div style="background:#f5f9ff;border-left:4px solid #3a86d0;padding:10px;border-radius:6px;margin-bottom:10px;">
          {top_5_factors[1][0]} <span style="float:right;">{top_5_factors[1][1]}</span>
        </div>
        <div style="background:#f5f9ff;border-left:4px solid #3a86d0;padding:10px;border-radius:6px;">
          {top_5_factors[3][0]} <span style="float:right;">{top_5_factors[3][1]}</span>
        </div>
        """, unsafe_allow_html=True)

    # Next Steps
    st.markdown("<h4 class='next-steps'>Next Steps</h4>", unsafe_allow_html=True)
    if st.button("Create Your Ideal Week"):
        st.session_state.page = 2
        st.experimental_rerun()
    st.markdown("""
    <p class='next-steps-text'>
      Reorganize your tasks and block out personal breaks or deep-work windows.
      Click above for recommendations tailored to your schedule!
    </p>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------
# PAGE 2: IDEAL WEEK
# ---------------------------
def page_ideal_week():
    st.markdown("<div class='insights-container'>", unsafe_allow_html=True)
    st.markdown("""
    <h2>Let's create your ideal week</h2>
    <p class="subtext">You can always change your preferences later.</p>
    """, unsafe_allow_html=True)

    # Store user slider data in session
    if "ideal_hours" not in st.session_state:
        st.session_state.ideal_hours = ideal_categories

    left_col, right_col = st.columns([1.1,1])

    with right_col:
        # Sliders for each category
        updated_hours = {}
        for cat, default_val in st.session_state.ideal_hours.items():
            hrs = st.slider(cat, 0, 60, default_val, step=1)
            updated_hours[cat] = hrs
            st.markdown(f"<span style='color:#999;font-size:0.8rem;'>~ {hrs} hours / week</span>", unsafe_allow_html=True)

        st.session_state.ideal_hours = updated_hours
        total_used = sum(updated_hours.values())
        st.write(f"**{total_used} of 168 hours** used")

    with left_col:
        # Build a donut based on these slider values
        cat_labels = list(st.session_state.ideal_hours.keys())
        cat_values = list(st.session_state.ideal_hours.values())
        donut_colors = ['#4285F4','#F77669','#9370DB','#FFB74D','#29B6F6','#66BB6A','#8D6E63','#BDBDBD']  
          # Or any color palette you prefer

        fig = go.Figure(data=[go.Pie(
            labels=cat_labels,
            values=cat_values,
            hole=0.5,
            marker=dict(colors=donut_colors[:len(cat_values)]),
            textinfo='none'
        )])
        pct = min(100, int((total_used/168)*100))
        fig.add_annotation(dict(
            text=f"{pct}%<br>{total_used} of 168 hours",
            x=0.5, y=0.5, showarrow=False, font_size=16
        ))
        fig.update_layout(margin=dict(l=10,r=10,t=10,b=10), height=320, width=320)
        st.plotly_chart(fig, use_container_width=True)

    # Save Preferences
    st.markdown("""
    <div class="cta-container" style="margin-top:10px">
        <a href="insights_dashboard" class="cta-button" style="color:white">Save Preferences</a>
    </div>
    """, unsafe_allow_html=True)


    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------
# MAIN APP LOGIC
# ---------------------------
if st.session_state.page == 1:
    page_insights()
else:
    page_ideal_week()

# Optionally auto-click any Plotly "Play" button after load
st.markdown("""
<script>
setTimeout(function(){
  const btns = document.querySelectorAll('button[data-testid="baseButton-secondary"]');
  btns.forEach(function(b, i){
    if(b.innerText === 'Play'){
      setTimeout(()=>b.click(), i*500);
    }
  });
}, 1000);
</script>
""", unsafe_allow_html=True)
