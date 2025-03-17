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
    max-width: 400px;
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
label {
    font-weight: 700;
    color: #1a202c;
}
</style>
"""

def app():
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.title("Log In")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Log In"):
        st.success(f"Logged in as {email}")
    st.markdown("</div>", unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Juggl - Log In", layout="centered")
    app()

if __name__ == "__main__":
    main()
