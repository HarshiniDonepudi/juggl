import streamlit as st

# ---------------------
# Advanced Aesthetic Custom CSS
# ---------------------
custom_css = """
<style>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

/* Global Styles */
html, body {
    margin: 0;
    padding: 0;
    font-family: 'Roboto', sans-serif;
    background: url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80') no-repeat center center fixed;
    background-size: cover;
    color: #333;
}

/* Overlay to dim the background image */
.overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(255, 255, 255, 0.9);
    z-index: -1;
}

/* Main Container */
.main-container {
    max-width: 900px;
    margin: 3rem auto;
    padding: 2rem;
    background: rgba(255,255,255,0.95);
    border-radius: 12px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.15);
    text-align: center;
}

/* Headings */
h1, h2, h3 {
    text-align: center;
    font-weight: 700;
    color: #1a202c;
    margin-bottom: 1.5rem;
}

/* Feature Card Container */
.features {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 2rem;
    margin-bottom: 2rem;
}

/* Feature Card */
.feature-card {
    background: #fff;
    border-radius: 12px;
    padding: 2rem;
    box-shadow: 0 8px 24px rgba(0,0,0,0.1);
    width: 240px;
}
.feature-card img {
    width: 80px;
    margin-bottom: 1rem;
}
.feature-card h3 {
    margin-bottom: 0.5rem;
    color: #1a202c;
}
.feature-card p {
    color: #4a5568;
    font-size: 0.95rem;
    line-height: 1.4;
}

/* Buttons */
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
</style>
<div class="overlay"></div>
"""

def main():
    st.set_page_config(page_title="Juggl - Home", layout="wide")

    # Inject CSS
    st.markdown(custom_css, unsafe_allow_html=True)

    # Main container
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.title("Create time & mental space for what truly matters.")
    st.write("Turn your calendar into a tool for your well-being.")

    # Features
    st.markdown("<div class='features'>", unsafe_allow_html=True)

    # Feature 1
    st.markdown(
        """
        <div class='feature-card'>
            <img src='https://via.placeholder.com/80.png?text=Icon+1' alt='Icon 1' />
            <h3>Know Burnout Risk</h3>
            <p>Become aware of your likelihood of experiencing burnout.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Feature 2
    st.markdown(
        """
        <div class='feature-card'>
            <img src='https://via.placeholder.com/80.png?text=Icon+2' alt='Icon 2' />
            <h3>Understand Yourself</h3>
            <p>Gain insights into your habits, schedule, and mental well-being.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Feature 3
    st.markdown(
        """
        <div class='feature-card'>
            <img src='https://via.placeholder.com/80.png?text=Icon+3' alt='Icon 3' />
            <h3>Create Balance</h3>
            <p>Discover how to allocate time for work, rest, and personal growth.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)  # close .features

    # Sign Up Button
    if st.button("Sign Up"):
        st.experimental_set_query_params(page="Sign_Up")

    st.markdown("</div>", unsafe_allow_html=True)  # close .main-container


if __name__ == "__main__":
    main()
