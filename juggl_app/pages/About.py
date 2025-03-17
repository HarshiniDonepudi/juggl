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
}
h1 {
    text-align: center;
    color: #1a202c;
    margin-bottom: 1.5rem;
}
</style>
"""

def app():
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.title("About Juggl")
    st.write("""
        This is the About page. 
        Provide information on how Juggl helps users prevent burnout, 
        manage their time effectively, and improve well-being.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Juggl - About", layout="centered")
    app()

if __name__ == "__main__":
    main()
