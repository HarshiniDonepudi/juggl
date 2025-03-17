import streamlit as st

custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

html, body {
    margin: 0;
    padding: 0;
    font-family: 'Roboto', sans-serif;
    background: url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80') no-repeat center center fixed;
    background-size: cover;
    color: #333;
}
.overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(255, 255, 255, 0.9);
    z-index: -1;
}
.main-container {
    max-width: 900px;
    margin: 3rem auto;
    padding: 2rem;
    background: rgba(255,255,255,0.95);
    border-radius: 12px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.15);
}
h1, h2, h3 {
    text-align: center;
    font-weight: 700;
    color: #1a202c;
    margin-bottom: 1.5rem;
}
.card {
    background: #fff;
    border-radius: 12px;
    padding: 2rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 24px rgba(0,0,0,0.1);
}
button, .stButton > button {
    background: #2b6cb0;
    border: none;
    color: #fff;
    padding: 0.75rem 1.5rem;
    border-radius: 50px;
    font-size: 1rem;
    font-weight: 700;
    cursor: pointer;
    transition: background 0.3s ease, transform 0.2s ease;
}
.stButton > button:hover {
    background: #2c5282;
    transform: translateY(-2px);
}
.metric-card {
    background: #fff;
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
    margin: 0.5rem;
}
.metric-card h4 {
    font-size: 0.9rem;
    color: #718096;
    margin-bottom: 0.5rem;
}
.metric-card p {
    font-size: 2rem;
    font-weight: 700;
    color: #2b6cb0;
}
.slider-section {
    background: #fff;
    padding: 2rem;
    border-radius: 12px;
    margin-top: 1.5rem;
    box-shadow: 0 8px 24px rgba(0,0,0,0.1);
}
.footer {
    text-align: center;
    margin-top: 1.5rem;
    font-size: 0.9rem;
    color: #718096;
}
div.row-widget.stRadio > div {
    flex-direction: row;
}
</style>
<div class="overlay"></div>
"""

def calculate_burnout_score():
    score = 0
    if "Prevent Burnout" in st.session_state.get("onboarding_goals", []):
        score += 10
    if st.session_state.get("industry", "") in ["Finance", "Healthcare", "Tech"]:
        score += 5
    if len(st.session_state.get("life_aspects", [])) >= 4:
        score += 5
    return min(score * 5, 100)

def reset_session():
    for key in list(st.session_state.keys()):
        del st.session_state[key]

def app():
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.title("Juggl - Personalized Onboarding")

    if "step" not in st.session_state:
        st.session_state.step = 1

    # Step 1
    if st.session_state.step == 1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.header("Step 1: Your Goals")
        st.write("Select your top priorities:")
        st.session_state.onboarding_goals = st.multiselect(
            "Goals:",
            ["Prevent Burnout", "Work-Life Balance", "Self-Understanding",
             "Wellness Habits", "Reclaim Time", "Achieve Life Goals"],
            default=["Prevent Burnout"]
        )
        if st.button("Next"):
            st.session_state.step = 2
        st.markdown("</div>", unsafe_allow_html=True)

    # Step 2
    elif st.session_state.step == 2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.header("Step 2: Tell Us About Yourself")
        st.session_state.industry = st.selectbox(
            "Industry:", ["Education", "Healthcare", "Finance", "Tech", "Other"]
        )
        st.session_state.job_role = st.text_input("Job Role (e.g., Product Manager):")
        st.session_state.work_setup = st.radio(
            "Work Setup:", ["Remote", "Hybrid", "On-site"]
        )
        col1, col2 = st.columns(2)
        if col1.button("Previous"):
            st.session_state.step = 1
        if col2.button("Next"):
            st.session_state.step = 3
        st.markdown("</div>", unsafe_allow_html=True)

    # Step 3
    elif st.session_state.step == 3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.header("Step 3: What Do You Manage Daily?")
        st.session_state.life_aspects = st.multiselect(
            "Select all that apply:",
            ["Work & Career", "Physical & Mental Health", "Relationships",
             "Passion Projects", "Hobbies", "Adulting Tasks"],
            default=["Work & Career", "Physical & Mental Health"]
        )
        col1, col2 = st.columns(2)
        if col1.button("Previous"):
            st.session_state.step = 2
        if col2.button("Next"):
            st.session_state.step = 4
        st.markdown("</div>", unsafe_allow_html=True)

    # Step 4
    elif st.session_state.step == 4:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.header("Step 4: Sync Your Calendars")
        st.session_state.calendar_email = st.text_input("Email", "you@example.com")
        if st.button("Add Calendar"):
            st.info("Calendar integration goes here.")
        col1, col2 = st.columns(2)
        if col1.button("Previous"):
            st.session_state.step = 3
        if col2.button("Next"):
            st.session_state.step = 5
        st.markdown("</div>", unsafe_allow_html=True)

    # Step 5
    elif st.session_state.step == 5:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.header("Your Personalized Insights")
        burnout_score = calculate_burnout_score()
        st.subheader("Time Insights & Burnout Risk")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            st.write("Total Hours Analyzed")
            st.write("48")
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            st.write("Meetings This Week")
            st.write("20")
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            st.write("Appointments")
            st.write("5")
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
            st.write("Burnout Score")
            st.write(f"{burnout_score}%")
            st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='slider-section'>", unsafe_allow_html=True)
        st.subheader("Create Your Ideal Week")
        st.session_state.ideal_work = st.slider("Work & Career (hours/week)", 0, 60, 32)
        st.session_state.ideal_health = st.slider("Physical & Mental Health (hours/week)", 0, 40, 8)
        st.session_state.ideal_relationships = st.slider("Relationships (hours/week)", 0, 40, 10)
        st.session_state.ideal_passion = st.slider("Passion Projects (hours/week)", 0, 40, 6)
        st.session_state.ideal_chores = st.slider("Adulting Tasks (hours/week)", 0, 40, 5)
        st.session_state.ideal_sleep = st.slider("Sleep & Recovery (hours/week)", 0, 70, 56)
        st.markdown("</div>", unsafe_allow_html=True)

        if st.button("View Role & Detailed Insights"):
            st.session_state.step = 6

    # Step 6
    elif st.session_state.step == 6:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.header("Detailed Role Insights")
        st.write(f"Based on your role as a {st.session_state.job_role}, here are tailored recommendations:")
        if st.session_state.industry in ["Tech", "Finance", "Healthcare"]:
            st.write("Consider scheduling focused work blocks and regular mindfulness breaks.")
        else:
            st.write("A mix of creative breaks and focused work can help balance your day.")
        st.markdown("</div>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        if col1.button("Back to Overview"):
            st.session_state.step = 5
        if col2.button("Finish"):
            st.success("Thank you for using Juggl!")

    # Footer / Start Over
    st.markdown("<div class='footer'>", unsafe_allow_html=True)
    if st.button("Start Over"):
        reset_session()
        st.experimental_rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Juggl - Onboarding", layout="wide")
    app()

if __name__ == "__main__":
    main()
