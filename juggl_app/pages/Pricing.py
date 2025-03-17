import streamlit as st

custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
body {
    margin: 0;
    padding: 0;
    font-family: 'Roboto', sans-serif;
    background: #f0f2f6;
    color: #333;
}
.main-container {
    max-width: 800px;
    margin: 3rem auto;
    padding: 2rem;
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.1);
    text-align: center;
}
h1 {
    color: #1a202c;
    margin-bottom: 1.5rem;
}
.plan-container {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-top: 2rem;
}
.plan {
    background: #ffffff;
    border-radius: 12px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.05);
    padding: 2rem;
    width: 200px;
}
.plan h2 {
    margin-bottom: 0.5rem;
    color: #2b6cb0;
}
.plan p {
    margin-bottom: 1rem;
    color: #555;
}
</style>
"""

def app():
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.title("Pricing")
    st.write("Choose a plan that fits your needs:")
    st.markdown("""
    <div class="plan-container">
        <div class="plan">
            <h2>Free</h2>
            <p>$0 / month</p>
            <ul>
                <li>Basic Features</li>
                <li>Limited Insights</li>
            </ul>
        </div>
        <div class="plan">
            <h2>Pro</h2>
            <p>$9.99 / month</p>
            <ul>
                <li>Full Insights</li>
                <li>Calendar Integrations</li>
                <li>Priority Support</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Juggl - Pricing", layout="centered")
    app()

if __name__ == "__main__":
    main()
