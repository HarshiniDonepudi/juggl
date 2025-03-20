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

# Flag to show the "Go to Insights" link after final step
if 'show_insights_link' not in st.session_state:
    st.session_state.show_insights_link = False

# Custom CSS to style the app exactly like the images, including hill background styling
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

/* Remove default app background so our SVG is visible */
.stApp {
    background: none;
}

/* Hill background styling */
.hill-background {
    position: fixed;      /* Fixed so it stays in place */
    bottom: 0;            /* Anchored to the bottom */
    left: 0;
    width: 100%;
    max-height: 392px;    /* Adjust based on your SVG height */
    z-index: -1;
    overflow: hidden;
}
.card-background {
    margin-top: 100px;
    position: fixed;      /* Fixed so it stays in place */
    z-index: -1;
    border-radius: 40px;
background: linear-gradient(0deg, rgba(255, 255, 255, 0.75) 0%, rgba(255, 255, 255, 0.25) 100%);
box-shadow: 0px 0px 8px 0px rgba(0, 0, 0, 0.16);
backdrop-filter: blur(10px);
}

/* Logo Style */
.logo {
    font-family: 'Inter', sans-serif;
    font-weight: bold;
    font-size: 24px;
    color: #4CAF50;
    padding: 20px 0 10px 20px;
}

/* Progress bar container */
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

/* Main container wrapper for all content */
.main-content-wrapper {
    position: relative;
    max-width: 1140px;
    margin: 0 auto;
    z-index: 2;
   }





/* Content layer: positioned above the card */
.card-content {
    position: relative;
    z-index: 3;
    padding: 20px;
    max-width: 1080px;
    margin-top: 20px
    border-radius: 40px;


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
 display: flex;
flex-direction: column;
align-items: center;
gap: 2px;
}

.selection-card {
    height: 250px;
    width: 220px;
    background: white;
    border: 1px solid #eee;
    border-radius: 24px;
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

# Define SVG ico
icons = {
'burnout': """
    <svg width="68" height="80" viewBox="0 0 68 80" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M0 23.7804L5.0467e-06 40.7647C0.000198313 48.5294 1.75727 55.2683 8.26618 59.8652C14.3826 64.1849 22.0189 66.352 29.7473 65.9534C37.9556 65.53 45.6718 62.2528 51.3025 56.7985C56.604 51.663 59.6871 44.9432 59.982 37.9005C60.2958 30.4059 56.4904 23.248 49.8319 18.8323L34.9257 8.94682C33.4428 7.9634 31.4255 9.22213 31.8978 10.8362L35.5007 23.1502C36.0466 25.0159 25.8553 15.111 24.5513 13.5882L11.5269 0.690615C10.2556 -0.793957 7.65469 0.310683 8.08719 2.1515L15.0808 31.918C15.5244 33.8061 16.3002 33.4977 15.0808 31.918L3.93044 23.191C3.66829 22.9859 3.44605 22.731 3.18174 22.5286C2.02979 21.6466 0.112654 22.2815 0 23.7804Z" fill="url(#paint0_linear_507_1184)"/>
      <path d="M21.5718 55.5179H33.7146V71.1122L26.5582 79.0496C24.8094 80.9891 21.5718 79.7616 21.5718 77.159V55.5179Z" fill="url(#paint1_linear_507_1184)"/>
      <rect x="15.1436" y="56.2267" width="12.1428" height="17.7208" rx="6.07141" fill="url(#paint2_linear_507_1184)"/>
      <path fill-rule="evenodd" clip-rule="evenodd" d="M67.9496 53.3914C67.983 53.041 68 52.6864 68 52.3282C68 46.9064 64.0943 42.2971 58.6519 40.61C56.1744 36.786 51.849 34.253 46.9275 34.253C44.5864 34.253 42.3803 34.8261 40.4437 35.8388C37.9206 32.3058 33.7676 30 29.072 30C22.2166 30 16.518 34.9148 15.3589 41.3874C10.979 43.4778 8 47.5932 8 52.3282C8 52.6864 8.01704 53.041 8.05045 53.3914H8C8 59.6551 13.0777 64.7328 19.3413 64.7328H21.0456C24.9916 64.7328 28.7255 66.5188 31.202 69.5908L31.8088 70.3435C34.6959 73.9248 40.424 72.7394 41.6525 68.3063L41.8312 67.6615C42.3108 65.9308 43.886 64.7328 45.6819 64.7328H56.6586C62.9222 64.7328 67.9999 59.6551 67.9999 53.3914H67.9496Z" fill="url(#paint3_linear_507_1184)"/>
      <path fill-rule="evenodd" clip-rule="evenodd" d="M57.6431 51.9737C57.6431 50.995 58.4426 50.2017 59.4288 50.2017C61.3679 50.2017 63.4802 50.5723 64.8065 52.4003C66.0317 54.0889 66.2093 56.5515 65.8451 59.6235C65.7299 60.5955 64.8424 61.2908 63.863 61.1764C62.8835 61.0621 62.1829 60.1814 62.2981 59.2094C62.6482 56.2564 62.2901 54.9976 61.9082 54.4711C61.6273 54.084 61.0611 53.7458 59.4288 53.7458C58.4426 53.7458 57.6431 52.9524 57.6431 51.9737Z" fill="url(#paint4_linear_507_1184)"/>
      <path fill-rule="evenodd" clip-rule="evenodd" d="M29.3768 60.4981C26.908 59.7868 23.4526 59.7709 19.4283 59.7709C18.4421 59.7709 17.6426 58.9775 17.6426 57.9988C17.6426 57.0202 18.4421 56.2268 19.4283 56.2268C19.4947 56.2268 19.5612 56.2268 19.6277 56.2268C23.401 56.2265 27.3589 56.2262 30.3726 57.0945C31.945 57.5475 33.436 58.281 34.5323 59.5221C35.6584 60.797 36.214 62.4323 36.214 64.3783C36.214 65.357 35.4145 66.1504 34.4283 66.1504C33.442 66.1504 32.6425 65.357 32.6425 64.3783C32.6425 63.1346 32.3053 62.3776 31.8466 61.8583C31.358 61.3051 30.5722 60.8425 29.3768 60.4981Z" fill="url(#paint5_linear_507_1184)"/>
      <path fill-rule="evenodd" clip-rule="evenodd" d="M32.2857 30.3544C33.272 30.3544 34.0714 31.1478 34.0714 32.1264C34.0714 32.7939 34.0963 33.397 34.1224 34.031C34.1422 34.5124 34.1628 35.0117 34.1738 35.5707C34.1966 36.7327 34.1679 38.0079 33.8758 39.173C33.5745 40.3744 32.9608 41.584 31.7344 42.4255C30.5361 43.2479 29.001 43.547 27.2047 43.4659C26.2195 43.4215 25.4571 42.5929 25.5019 41.6152C25.5467 40.6375 26.3816 39.881 27.3668 39.9254C28.7134 39.9862 29.3747 39.7359 29.7031 39.5105C30.0036 39.3043 30.2469 38.9677 30.41 38.3173C30.5822 37.6306 30.6248 36.7483 30.603 35.6398C30.5955 35.254 30.5777 34.8003 30.5591 34.3229C30.5306 33.5936 30.5 32.8091 30.5 32.1264C30.5 31.1478 31.2995 30.3544 32.2857 30.3544Z" fill="url(#paint6_linear_507_1184)"/>
      <path fill-rule="evenodd" clip-rule="evenodd" d="M15.3998 41.7548C16.3532 41.5043 17.3307 42.0681 17.5832 43.0142C17.8196 43.9003 18.5497 45.3352 19.9445 46.4447C21.2861 47.5118 23.3238 48.3453 26.3645 47.9936C27.3441 47.8803 28.2308 48.5765 28.3449 49.5486C28.4591 50.5208 27.7575 51.4007 26.7779 51.514C22.8056 51.9734 19.8109 50.8805 17.7109 49.2102C15.6642 47.5822 14.5436 45.4687 14.1307 43.9215C13.8783 42.9754 14.4465 42.0053 15.3998 41.7548Z" fill="url(#paint7_linear_507_1184)"/>
      <path fill-rule="evenodd" clip-rule="evenodd" d="M42.8591 43.2714C43.3293 42.4111 44.4132 42.092 45.2801 42.5586C46.2515 43.0815 48.2281 43.61 50.3698 43.0069C51.8219 42.598 53.4461 41.6446 54.9548 39.6331C55.5437 38.8481 56.6624 38.6853 57.4535 39.2697C58.2446 39.8541 58.4086 40.9642 57.8197 41.7493C56.3203 43.7483 54.6312 45.0563 52.909 45.8425C53.1902 47.7033 53.2024 50.0098 52.4747 52.1121C51.9866 53.5222 51.1463 54.8904 49.7859 55.923C48.4196 56.9599 46.6574 57.5607 44.4974 57.6431C43.5119 57.6807 42.6822 56.9184 42.6443 55.9404C42.6064 54.9625 43.3746 54.1392 44.3601 54.1016C45.9144 54.0422 46.9318 53.6273 47.6162 53.1078C48.3064 52.584 48.7874 51.8552 49.097 50.9608C49.5466 49.6617 49.5913 48.1276 49.4318 46.7725C47.0204 46.9992 44.8951 46.3834 43.5773 45.674C42.7104 45.2074 42.3888 44.1317 42.8591 43.2714Z" fill="url(#paint8_linear_507_1184)"/>
      <defs>
        <linearGradient id="paint0_linear_507_1184" x1="9.77585" y1="1.15271" x2="42.4814" y2="77.6956" gradientUnits="userSpaceOnUse">
          <stop stop-color="#ECC736"/>
          <stop offset="1" stop-color="#F3A07F"/>
        </linearGradient>
        <linearGradient id="paint1_linear_507_1184" x1="28.7146" y1="55.5179" x2="28.7146" y2="82.4536" gradientUnits="userSpaceOnUse">
          <stop stop-color="#E97432"/>
          <stop offset="1" stop-color="#BA5922"/>
        </linearGradient>
        <linearGradient id="paint2_linear_507_1184" x1="21.215" y1="56.2267" x2="21.215" y2="73.9475" gradientUnits="userSpaceOnUse">
          <stop stop-color="#F3A07F"/>
          <stop offset="1" stop-color="#E97432"/>
        </linearGradient>
        <linearGradient id="paint3_linear_507_1184" x1="38" y1="30" x2="38" y2="77.9169" gradientUnits="userSpaceOnUse">
          <stop stop-color="#F9D4C9"/>
          <stop offset="1" stop-color="#F3A07F"/>
        </linearGradient>
        <linearGradient id="paint4_linear_507_1184" x1="61.66" y1="53.4274" x2="61.66" y2="58.3951" gradientUnits="userSpaceOnUse">
          <stop stop-color="#F3A07F"/>
          <stop offset="1" stop-color="#E97432"/>
        </linearGradient>
        <linearGradient id="paint5_linear_507_1184" x1="26.1269" y1="59.0453" x2="26.1269" y2="63.8325" gradientUnits="userSpaceOnUse">
          <stop stop-color="#F3A07F"/>
          <stop offset="1" stop-color="#E97432"/>
        </linearGradient>
        <linearGradient id="paint6_linear_507_1184" x1="29.4983" y1="30" x2="29.4983" y2="41.7031" gradientUnits="userSpaceOnUse">
          <stop stop-color="#F3A07F"/>
          <stop offset="1" stop-color="#E97432"/>
        </linearGradient>
        <linearGradient id="paint7_linear_507_1184" x1="21.2141" y1="43.4678" x2="21.2141" y2="49.8473" gradientUnits="userSpaceOnUse">
          <stop stop-color="#F3A07F"/>
          <stop offset="1" stop-color="#E97432"/>
        </linearGradient>
        <linearGradient id="paint8_linear_507_1184" x1="48.1035" y1="40.2479" x2="52.7476" y2="44.6593" gradientUnits="userSpaceOnUse">
          <stop stop-color="#F3A07F"/>
          <stop offset="1" stop-color="#E97432"/>
        </linearGradient>
      </defs>
    </svg>
    """,
    'balance': """
    <svg width="64" height="80" viewBox="0 0 64 80" fill="none" xmlns="http://www.w3.org/2000/svg">
      <rect y="64.4019" width="70" height="6" rx="3" transform="rotate(-30 0 64.4019)" fill="url(#paint0_linear_507_1181)"/>
      <path d="M29.2733 52.9112C30.0265 51.6963 31.8631 51.6963 32.6164 52.9112L47.6694 77.1881C48.4388 78.429 47.5049 80 45.9978 80H15.8918C14.3847 80 13.4508 78.429 14.2202 77.1881L29.2733 52.9112Z" fill="url(#paint1_linear_507_1181)"/>
      <circle cx="13.9448" cy="45" r="10" fill="url(#paint2_linear_507_1181)"/>
      <circle cx="49.9448" cy="10" r="10" fill="url(#paint3_linear_507_1181)"/>
      <circle cx="30.9448" cy="52" r="4" fill="url(#paint4_linear_507_1181)"/>
      <defs>
        <linearGradient id="paint0_linear_507_1181" x1="0" y1="67.4019" x2="70" y2="67.4019" gradientUnits="userSpaceOnUse">
          <stop stop-color="#ADA7D7"/>
          <stop offset="1" stop-color="#887EC4"/>
        </linearGradient>
        <linearGradient id="paint1_linear_507_1181" x1="30.9448" y1="52" x2="30.9448" y2="80" gradientUnits="userSpaceOnUse">
          <stop stop-color="#ADA7D7"/>
          <stop offset="1" stop-color="#887EC4"/>
        </linearGradient>
        <linearGradient id="paint2_linear_507_1181" x1="13.9448" y1="35" x2="13.9448" y2="55" gradientUnits="userSpaceOnUse">
          <stop stop-color="#4BA3F7"/>
          <stop offset="1" stop-color="#277DC6"/>
        </linearGradient>
        <linearGradient id="paint3_linear_507_1181" x1="49.9448" y1="0" x2="49.9448" y2="20" gradientUnits="userSpaceOnUse">
          <stop stop-color="#38A4BB"/>
          <stop offset="1" stop-color="#48CDEA"/>
        </linearGradient>
        <linearGradient id="paint4_linear_507_1181" x1="30.9448" y1="48" x2="30.9448" y2="56" gradientUnits="userSpaceOnUse">
          <stop stop-color="#C5CCCA"/>
          <stop offset="1" stop-color="white"/>
        </linearGradient>
      </defs>
    </svg>
    """,
    'goals': """
    <svg width="68" height="80" viewBox="0 0 68 80" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M32.4024 26.665C33.1184 25.2725 34.8808 25.2725 35.5969 26.665L61.3823 76.8113C62.1078 78.2223 61.2173 80 59.785 80H8.21418C6.78189 80 5.89142 78.2223 6.61695 76.8113L32.4024 26.665Z" fill="url(#paint0_linear_507_1182)"/>
      <path fill-rule="evenodd" clip-rule="evenodd" d="M42.1822 39.4716L35.8929 46.6574C34.9283 47.7595 33.3644 47.7595 32.3998 46.6574L25.9258 39.2606L32.4025 26.665C33.1186 25.2725 34.8809 25.2725 35.597 26.665L42.1822 39.4716Z" fill="url(#paint1_linear_507_1182)"/>
      <path d="M13.1776 53.0133C13.5399 52.3087 14.4316 52.3087 14.7939 53.0133L27.8409 78.3865C28.208 79.1005 27.7575 80 27.0328 80H0.93875C0.214034 80 -0.23653 79.1005 0.130574 78.3865L13.1776 53.0133Z" fill="url(#paint2_linear_507_1182)"/>
      <path fill-rule="evenodd" clip-rule="evenodd" d="M18.1264 59.493L14.9438 63.1292C14.4557 63.6868 13.6644 63.6868 13.1764 63.1292L9.90088 59.3868L13.1781 53.0133C13.5405 52.3087 14.4322 52.3087 14.7945 53.0133L18.1264 59.493Z" fill="url(#paint3_linear_507_1182)"/>
      <path d="M54.8224 53.0133C54.4601 52.3087 53.5684 52.3087 53.2061 53.0133L40.1591 78.3865C39.792 79.1005 40.2425 80 40.9672 80H67.0612C67.786 80 68.2365 79.1005 67.8694 78.3865L54.8224 53.0133Z" fill="url(#paint4_linear_507_1182)"/>
      <path fill-rule="evenodd" clip-rule="evenodd" d="M49.8736 59.493L53.056 63.1292C53.544 63.6868 54.3354 63.6868 54.8234 63.1292L58.0991 59.3866L54.822 53.0133C54.4597 52.3087 53.5679 52.3087 53.2056 53.0133L49.8736 59.493Z" fill="url(#paint5_linear_507_1182)"/>
      <rect x="32.6401" y="5.28687" width="2.72" height="24.1686" rx="1.36" fill="url(#paint6_linear_507_1182)"/>
      <path d="M40.7998 6.28686C40.7998 5.73458 41.2475 5.28687 41.7998 5.28687H54.8739C55.7397 5.28687 56.1964 6.31249 55.617 6.95597L52.2822 10.6599C51.9398 11.0403 51.9398 11.6178 52.2822 11.9981L55.617 15.7021C56.1964 16.3456 55.7397 17.3712 54.8739 17.3712H41.7998C41.2475 17.3712 40.7998 16.9235 40.7998 16.3712V6.28686Z" fill="url(#paint7_linear_507_1182)"/>
      <path d="M32.6401 1C32.6401 0.447715 33.0879 0 33.6401 0H47.9601C48.5124 0 48.9601 0.447715 48.9601 1V11.0843C48.9601 11.6366 48.5124 12.0843 47.9601 12.0843H33.6401C33.0879 12.0843 32.6401 11.6366 32.6401 11.0843V1Z" fill="url(#paint8_linear_507_1182)"/>
      <defs>
        <linearGradient id="paint0_linear_507_1182" x1="33.9996" y1="25.6206" x2="33.9996" y2="80" gradientUnits="userSpaceOnUse">
          <stop stop-color="#66BA86"/>
          <stop offset="1" stop-color="#4E9168"/>
        </linearGradient>
        <linearGradient id="paint1_linear_507_1182" x1="34.054" y1="25.6206" x2="34.054" y2="47.484" gradientUnits="userSpaceOnUse">
          <stop stop-color="white"/>
          <stop offset="1" stop-color="white" stop-opacity="0.5"/>
        </linearGradient>
        <linearGradient id="paint2_linear_507_1182" x1="27.9715" y1="66.2424" x2="0" y2="66.2424" gradientUnits="userSpaceOnUse">
          <stop stop-color="#66BA86"/>
          <stop offset="1" stop-color="#4E9168"/>
        </linearGradient>
        <linearGradient id="paint3_linear_507_1182" x1="14.0136" y1="52.4849" x2="14.0136" y2="63.5474" gradientUnits="userSpaceOnUse">
          <stop stop-color="white"/>
          <stop offset="1" stop-color="white" stop-opacity="0.5"/>
        </linearGradient>
        <linearGradient id="paint4_linear_507_1181" x1="30.9448" y1="48" x2="30.9448" y2="56" gradientUnits="userSpaceOnUse">
          <stop stop-color="#C5CCCA"/>
          <stop offset="1" stop-color="white"/>
        </linearGradient>
        <linearGradient id="paint5_linear_507_1182" x1="2.62451" y1="67.36" x2="77.1845" y2="67.36" gradientUnits="userSpaceOnUse">
          <stop stop-color="#D4D1EA"/>
          <stop offset="1" stop-color="#F1F0F8"/>
        </linearGradient>
        <linearGradient id="paint6_linear_507_1182" x1="40.8391" y1="56.0653" x2="40.8391" y2="76.3102" gradientUnits="userSpaceOnUse">
          <stop stop-color="#66BA86"/>
          <stop offset="1" stop-color="#224630"/>
        </linearGradient>
        <linearGradient id="paint7_linear_507_1182" x1="40.7998" y1="11.329" x2="57.1198" y2="11.329" gradientUnits="userSpaceOnUse">
          <stop stop-color="#4BA3F7"/>
          <stop offset="1" stop-color="#A4C7FB"/>
        </linearGradient>
        <linearGradient id="paint8_linear_507_1182" x1="32.6401" y1="0" x2="32.6401" y2="6" gradientUnits="userSpaceOnUse">
          <stop stop-color="#4BA3F7"/>
          <stop offset="1" stop-color="#A4C7FB"/>
        </linearGradient>
      </defs>
    </svg>
    """,
    'time': """
    <svg width="68" height="80" viewBox="0 0 68 80" fill="none" xmlns="http://www.w3.org/2000/svg">
      <rect y="23" width="20" height="10.025" rx="5.01248" transform="rotate(-40 0 23)" fill="url(#paint0_linear_507_1180)"/>
      <rect x="52.2085" y="10" width="20" height="10.025" rx="5.01248" transform="rotate(40 52.2085 10)" fill="url(#paint1_linear_507_1180)"/>
      <rect x="28" width="12" height="20" rx="6" fill="url(#paint2_linear_507_1180)"/>
      <circle cx="34" cy="46" r="34" fill="url(#paint3_linear_507_1180)"/>
      <circle cx="34" cy="46" r="28" fill="url(#paint4_linear_507_1180)"/>
      <path fill-rule="evenodd" clip-rule="evenodd" d="M57 46C57 46.768 56.3372 47.3528 55.5705 47.3071L53.0586 47.1573C52.456 47.1214 52 46.6036 52 46C52 45.3964 52.456 44.8786 53.0586 44.8427L55.5705 44.6929C56.3372 44.6472 57 45.232 57 46ZM53.9209 34.4963C54.3053 35.1606 54.0247 35.9998 53.3384 36.3432L51.082 37.4723C50.545 37.741 49.8941 37.5204 49.5933 37.0007C49.2926 36.481 49.4272 35.8091 49.9279 35.4776L52.0315 34.0844C52.6714 33.6607 53.5365 33.8321 53.9209 34.4963ZM45.5037 26.0791C46.1679 26.4635 46.3393 27.3286 45.9156 27.9685L44.5224 30.0721C44.1909 30.5728 43.519 30.7074 42.9993 30.4067C42.4795 30.1059 42.259 29.455 42.5277 28.918L43.6568 26.6616C44.0002 25.9753 44.8394 25.6947 45.5037 26.0791ZM35.3071 24.4295C35.3528 23.6628 34.768 23 34 23C33.232 23 32.6472 23.6628 32.6929 24.4295L32.8427 26.9414C32.8786 27.544 33.3964 28 34 28C34.6036 28 35.1214 27.544 35.1573 26.9414L35.3071 24.4295ZM22.4963 26.0791C23.1606 25.6947 23.9998 25.9753 24.3432 26.6616L25.4723 28.918C25.741 29.455 25.5204 30.1059 25.0007 30.4067C24.481 30.7074 23.8091 30.5728 23.4776 30.0721L22.0844 27.9685C21.6607 27.3286 21.8321 26.4635 22.4963 26.0791ZM14.0791 34.4963C14.4635 33.8321 14.244 33 13.5577 32.6566L11.3013 31.5275C10.7643 31.2588 10.1134 31.4794 9.8126 32C9.51182 32.5207 9.73233 33.1716 10.2683 33.44L12.3719 34.8332C12.8807 35.0783 13.6657 34.9069 14.0491 34.2427ZM22.4963 65.9209C21.8321 65.5365 21.6607 64.6714 22.0844 64.0315L23.4776 61.9279C23.8091 61.4272 24.481 61.2926 25.0007 61.5933C25.5205 61.8941 25.741 62.545 25.4723 63.082L24.3432 65.3384C23.9998 66.0247 23.1606 66.3053 22.4963 65.9209ZM34 69C33.232 69 32.6472 68.3372 32.6929 67.5705L32.8427 65.0586C32.8786 64.456 33.3964 64 34 64C34.6036 64 35.1214 64.456 35.1573 65.0586L35.3071 67.5705C35.3528 68.3372 34.768 69 34 69ZM45.5037 65.9209C44.8394 66.3053 44.0002 66.0247 43.6568 65.3384L42.5277 63.082C42.259 62.545 42.4795 61.8941 42.9993 61.5933C43.519 61.2926 44.1909 61.4272 44.5224 61.9279L45.9156 64.0315C46.3393 64.6714 46.1679 65.5365 45.5037 65.9209ZM53.9209 57.5037C53.5365 58.1679 52.6714 58.3393 52.0315 57.9156L49.9279 56.5224C49.4272 56.1909 49.2926 55.519 49.5933 54.9993C49.8941 54.4795 50.545 54.259 51.082 54.5277L53.3384 55.6568C54.0247 56.0002 54.3053 56.8394 53.9209 57.5037Z" fill="url(#paint5_linear_507_1180)"/>
      <path d="M31.2247 38.8679L33.5187 30.7114C33.6554 30.2252 34.3446 30.2252 34.4813 30.7114L36.7753 38.8679C36.9192 39.3793 36.8536 39.9269 36.5932 40.3899L34.8716 43.4505C34.4893 44.1302 33.5107 44.1302 33.1284 43.4505L31.4068 40.3899C31.1464 39.9269 31.0808 39.3793 31.2247 38.8679Z" fill="url(#paint6_linear_507_1180)"/>
      <circle cx="34" cy="46" r="3" fill="url(#paint7_linear_507_1180)"/>
      <rect x="24" width="20" height="6" rx="3" fill="url(#paint8_linear_507_1180)"/>
      <defs>
        <linearGradient id="paint0_linear_507_1180" x1="0" y1="67.4019" x2="70" y2="67.4019" gradientUnits="userSpaceOnUse">
          <stop stop-color="#ADA7D7"/>
          <stop offset="1" stop-color="#887EC4"/>
        </linearGradient>
        <linearGradient id="paint1_linear_507_1180" x1="30.9448" y1="52" x2="30.9448" y2="80" gradientUnits="userSpaceOnUse">
          <stop stop-color="#ADA7D7"/>
          <stop offset="1" stop-color="#887EC4"/>
        </linearGradient>
        <linearGradient id="paint2_linear_507_1180" x1="30.9448" y1="35" x2="30.9448" y2="55" gradientUnits="userSpaceOnUse">
          <stop stop-color="#4BA3F7"/>
          <stop offset="1" stop-color="#4BA3F7" stop-opacity="0.5"/>
        </linearGradient>
        <linearGradient id="paint3_linear_507_1180" x1="30.9448" y1="0" x2="30.9448" y2="20" gradientUnits="userSpaceOnUse">
          <stop stop-color="#38A4BB"/>
          <stop offset="1" stop-color="#48CDEA"/>
        </linearGradient>
        <linearGradient id="paint4_linear_507_1180" x1="30.9448" y1="48" x2="30.9448" y2="56" gradientUnits="userSpaceOnUse">
          <stop stop-color="#C5CCCA"/>
          <stop offset="1" stop-color="white"/>
        </linearGradient>
        <linearGradient id="paint5_linear_507_1180" x1="30.9448" y1="23" x2="30.9448" y2="69" gradientUnits="userSpaceOnUse">
          <stop stop-color="#4BA3F7"/>
          <stop offset="1" stop-color="#A4C7FB"/>
        </linearGradient>
        <linearGradient id="paint6_linear_507_1180" x1="30.9448" y1="29" x2="30.9448" y2="45" gradientUnits="userSpaceOnUse">
          <stop stop-color="#F3A07F"/>
          <stop offset="1" stop-color="#E97432"/>
        </linearGradient>
        <linearGradient id="paint7_linear_507_1180" x1="30.9448" y1="43" x2="30.9448" y2="49" gradientUnits="userSpaceOnUse">
          <stop stop-color="#ECC736"/>
          <stop offset="1" stop-color="#F3A07F"/>
        </linearGradient>
        <linearGradient id="paint8_linear_507_1180" x1="30.9448" y1="0" x2="30.9448" y2="6" gradientUnits="userSpaceOnUse">
          <stop stop-color="#A4C7FB"/>
          <stop offset="1" stop-color="#4BA3F7"/>
        </linearGradient>
      </defs>
    </svg>
    """,
    'habits': """
    <svg width="68" height="80" viewBox="0 0 68 80" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path fill-rule="evenodd" clip-rule="evenodd" d="M53.4384 32.64H48V26.88H53.4384C56.8014 26.88 59.9418 28.5607 61.8072 31.3589L62.0742 31.7593C64.3975 35.2443 64.1399 39.845 61.4419 43.0488C59.6526 45.1736 57.0165 46.4 54.2387 46.4H48V40.64H54.2387C55.3175 40.64 56.3412 40.1637 57.036 39.3386C58.0838 38.0944 58.1838 36.3078 57.2816 34.9544L57.0146 34.554C56.2175 33.3582 54.8755 32.64 53.4384 32.64Z" fill="url(#paint0_linear_507_1183)"/>
      <path d="M8 26.88C8 25.4662 9.14615 24.32 10.56 24.32H48.32C49.7338 24.32 50.88 25.4662 50.88 26.88V39.04C50.88 47.5231 44.0031 54.4 35.52 54.4H23.36C14.8769 54.4 8 47.5231 8 39.04V26.88Z" fill="url(#paint1_linear_507_1183)"/>
      <path fill-rule="evenodd" clip-rule="evenodd" d="M25.8581 0.611496C26.7575 1.46093 26.798 2.87864 25.9485 3.77804L22.6391 7.28216C22.3199 7.62017 22.3374 8.15359 22.678 8.46995C24.7968 10.4374 24.955 13.7373 23.0341 15.8984L19.9142 19.4082C19.0923 20.3328 17.6765 20.4161 16.7518 19.5942C15.8272 18.7723 15.7439 17.3565 16.5658 16.4318L19.6857 12.922C19.988 12.5819 19.9631 12.0625 19.6296 11.7529C17.465 9.74283 17.3538 6.35366 19.3821 4.20609L22.6915 0.701969C23.5409 -0.197432 24.9587 -0.237938 25.8581 0.611496Z" fill="url(#paint2_linear_507_1183)"/>
      <path fill-rule="evenodd" clip-rule="evenodd" d="M35.1378 0.611496C36.0372 1.46093 36.0778 2.87864 35.2283 3.77804L31.9189 7.28216C31.5996 7.62017 31.6171 8.15359 31.9578 8.46995C34.0766 10.4374 34.2348 13.7373 32.3138 15.8984L29.194 19.4082C28.3721 20.3328 26.9563 20.4161 26.0316 19.5942C25.107 18.7723 25.0237 17.3565 25.8456 16.4318L28.9654 12.922C29.2678 12.5819 29.2429 12.0625 28.9094 11.7529C26.7448 9.74283 26.6336 6.35366 28.6619 4.20609L31.9713 0.701969C32.8207 -0.197432 34.2384 -0.237938 35.1378 0.611496Z" fill="url(#paint3_linear_507_1183)"/>
      <path fill-rule="evenodd" clip-rule="evenodd" d="M44.4181 0.611496C45.3175 1.46093 45.358 2.87864 44.5086 3.77804L41.1991 7.28216C40.8799 7.62017 40.8974 8.15359 41.2381 8.46995C43.3569 10.4374 43.515 13.7373 41.5941 15.8984L38.4743 19.4082C37.6524 20.3328 36.2365 20.4161 35.3119 19.5942C34.3873 18.7723 34.304 17.3565 35.1259 16.4318L38.2457 12.922C38.5481 12.5819 38.5232 12.0625 38.1897 11.7529C36.025 9.74283 35.9139 6.35366 37.9421 4.20609L41.2516 0.701969C42.101 -0.197432 43.5187 -0.237938 44.4181 0.611496Z" fill="url(#paint4_linear_507_1183)"/>
      <path d="M61.1947 62.0238L63.5 58.24H9.02451L2.62451 67.36L9.02451 76.48H63.5L61.1947 72.9614C59.058 69.6376 59.1109 65.3811 61.1947 62.0238Z" fill="url(#paint5_linear_507_1183)"/>
      <path fill-rule="evenodd" clip-rule="evenodd" d="M3.05794 59.3561C5.54441 56.225 9.32406 54.4 13.3224 54.4L65.12 54.3937C66.7106 54.3937 68 55.6832 68 57.2737C68 58.8643 66.7106 60.1537 65.12 60.1537L13.3224 60.16C11.0811 60.16 8.96245 61.183 7.56866 62.9381L7.21124 63.3882C5.12558 66.0146 5.30657 69.7793 7.63455 72.1935C8.89559 73.5012 10.6342 74.24 12.4509 74.24L65.12 74.2337C66.7106 74.2337 68 75.5232 68 77.1137C68 78.7043 66.7106 79.9937 65.12 79.9937L12.4509 80C9.07024 80 5.8349 78.6253 3.48824 76.1917C-0.84383 71.6992 -1.18062 64.6935 2.70052 59.8062L3.05794 59.3561Z" fill="url(#paint6_linear_507_1183)"/>
      <defs>
        <linearGradient id="paint0_linear_507_1180" x1="0" y1="67.4019" x2="70" y2="67.4019" gradientUnits="userSpaceOnUse">
          <stop stop-color="#ADA7D7"/>
          <stop offset="1" stop-color="#887EC4"/>
        </linearGradient>
        <linearGradient id="paint1_linear_507_1180" x1="30.9448" y1="52" x2="30.9448" y2="80" gradientUnits="userSpaceOnUse">
          <stop stop-color="#ADA7D7"/>
          <stop offset="1" stop-color="#887EC4"/>
        </linearGradient>
        <linearGradient id="paint2_linear_507_1180" x1="30.9448" y1="35" x2="30.9448" y2="55" gradientUnits="userSpaceOnUse">
          <stop stop-color="#4BA3F7"/>
          <stop offset="1" stop-color="#277DC6"/>
        </linearGradient>
        <linearGradient id="paint3_linear_507_1180" x1="30.9448" y1="0" x2="30.9448" y2="20" gradientUnits="userSpaceOnUse">
          <stop stop-color="#38A4BB"/>
          <stop offset="1" stop-color="#48CDEA"/>
        </linearGradient>
        <linearGradient id="paint4_linear_507_1180" x1="30.9448" y1="48" x2="30.9448" y2="56" gradientUnits="userSpaceOnUse">
          <stop stop-color="#C5CCCA"/>
          <stop offset="1" stop-color="white"/>
        </linearGradient>
        <linearGradient id="paint5_linear_507_1180" x1="30.9448" y1="23" x2="30.9448" y2="69" gradientUnits="userSpaceOnUse">
          <stop stop-color="#4BA3F7"/>
          <stop offset="1" stop-color="#A4C7FB"/>
        </linearGradient>
        <linearGradient id="paint6_linear_507_1180" x1="30.9448" y1="29" x2="30.9448" y2="45" gradientUnits="userSpaceOnUse">
          <stop stop-color="#F3A07F"/>
          <stop offset="1" stop-color="#E97432"/>
        </linearGradient>
        <linearGradient id="paint7_linear_507_1180" x1="30.9448" y1="43" x2="30.9448" y2="49" gradientUnits="userSpaceOnUse">
          <stop stop-color="#ECC736"/>
          <stop offset="1" stop-color="#F3A07F"/>
        </linearGradient>
        <linearGradient id="paint8_linear_507_1180" x1="30.9448" y1="0" x2="30.9448" y2="6" gradientUnits="userSpaceOnUse">
          <stop stop-color="#A4C7FB"/>
          <stop offset="1" stop-color="#4BA3F7"/>
        </linearGradient>
      </defs>
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



# --- Apply custom CSS ---
st.markdown(custom_css, unsafe_allow_html=True)

# --- Hill background (SVG) ---
st.markdown('''
<div class="hill-background">
  <svg xmlns="http://www.w3.org/2000/svg" width="1512" height="392" viewBox="0 0 1512 392" fill="none">
    <path d="M68.0462 68.5076L0 106.188V392H1512V2.06735L1294.71 106.576C1176.22 163.562 1041.1 175.71 914.355 140.771L476.14 19.975C338.996 -17.8293 192.499 -0.407143 68.0462 68.5076Z" 
          fill="url(#paint0_linear_508_2326)"/>
    <defs>
      <linearGradient id="paint0_linear_508_2326" x1="756" y1="-74.2599" x2="756" y2="392" gradientUnits="userSpaceOnUse">
        <stop stop-color="#8CE1AC"/>
        <stop offset="1" stop-color="#4E9168"/>
      </linearGradient>
    </defs>
  </svg>
</div>
''', unsafe_allow_html=True)
st.markdown('''
<div class="card-background">
<svg width="1350" height="620" xmlns="http://www.w3.org/2000/svg">
</svg>
</div>
''', unsafe_allow_html=True)
# --- Juggl logo (INSIDE the card) ---
st.markdown('<div class="logo">Juggl<sup>™</sup></div>', unsafe_allow_html=True)

# --- Start card container ---

st.markdown('<div class="card-content">', unsafe_allow_html=True)



# --- Progress bar ---
progress_percentage = {1: 25, 2: 50, 3: 75, 4: 100}
current_step = st.session_state.step
st.markdown(f"""
<div class="progress-container">
  <div class="progress-bar">
    <div class="progress-fill" style="width:{progress_percentage[current_step]}%;"></div>
  </div>
  <div class="progress-text">
    <span>STEP {current_step} OF 4</span>
    <span>{progress_percentage[current_step]}%</span>
  </div>
</div>
""", unsafe_allow_html=True)

# =====================
# STEP 1
# =====================
if st.session_state.step == 1:
    st.markdown('''
    <div class="card-header">
        <div class="card-title">How would you like Juggl to help you?</div>
        <div class="card-subtitle">Select all that apply to you.</div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Use columns (5 across) for the first set of checkboxes
    col1, col2, col3, col4, col5 = st.columns(5, gap="small")
    
    with col1:
        # The actual checkbox
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

    # Save them into session state
    st.session_state.onboarding_data['goals'] = {
        'prevent_burnout': burnout,
        'achieve_balance': balance,
        'achieve_life_goals': goals,
        'reclaim_time': time,
        'nurture_habits': habits
    }
    
    # "Continue" button
    col_space, col_btn = st.columns([4,1])
    with col_btn:
        if st.button("Continue", key="continue_1", use_container_width=True):
            st.session_state.step = 2
            st.experimental_rerun()

# =====================
# STEP 2
# =====================
elif st.session_state.step == 2:
    st.markdown('''
    <div class="card-header">
        <div class="card-title">Let's understand your burnout risk.</div>
        <div class="card-subtitle">We understand that some industries and roles come with a higher risk and so, require more support.</div>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown("<div style='margin-top:30px;'><label style='font-weight:500;font-size:16px;'>Which industry do you work in?</label></div>", 
                unsafe_allow_html=True)
    industry = st.text_input("Industry placeholder", 
                             value="Education, Healthcare, Finance...", 
                             label_visibility="collapsed")
    
    st.markdown("<div style='margin-top:20px;'><label style='font-weight:500;font-size:16px;'>What best describes your job role?</label></div>", 
                unsafe_allow_html=True)
    role = st.text_input("Role placeholder", 
                         value="Data Scientist, Product Manager, Engineer", 
                         label_visibility="collapsed")
    
    st.markdown("<div style='margin-top:20px;'><label style='font-weight:500;font-size:16px;'>What's your work set up like?</label></div>", 
                unsafe_allow_html=True)
    work_setup = st.radio("Work setup",
                          ["Fully Remote", "Hybrid", "In Office"],
                          horizontal=True,
                          label_visibility="collapsed")
    
    # Save to session
    st.session_state.onboarding_data['profile'] = {
        'industry': industry,
        'role': role,
        'work_setup': work_setup
    }
    
    # Continue button
    col_space, col_btn = st.columns([3,1])
    with col_btn:
        if st.button("Continue", key="continue_2", use_container_width=True):
            st.session_state.step = 3
            st.experimental_rerun()

# =====================
# STEP 3
# =====================
elif st.session_state.step == 3:
    st.markdown('''
    <div class="card-header">
        <div class="card-title">Let's understand all that you juggle.</div>
        <div class="card-subtitle">We will help you reclaim time for what truly matters to you.</div>
    </div>
    ''', unsafe_allow_html=True)
    
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
    
    # Save them
    st.session_state.onboarding_data['life_aspects'] = {
        'work': work,
        'health': health,
        'relationships': relationships,
        'projects': projects,
        'hobbies': hobbies,
        'adulting': adulting
    }
    
    # Continue button
    col_space, col_btn = st.columns([3,1])
    with col_btn:
        if st.button("Continue", key="continue_3", use_container_width=True):
            st.session_state.step = 4
            st.experimental_rerun()

# =====================
# STEP 4
# =====================
elif st.session_state.step == 4:
    st.markdown('''
    <div class="card-header">
        <div class="card-title">Let's sync all your calendars in one place.</div>
        <div class="card-subtitle">We will optimise your schedule across your calendars.</div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Example email & calendar
    st.markdown('''
    <div class="email-container">
        <div class="email-avatar">J</div>
        <div class="email-label">johndoe@gmail.com</div>
        <div class="calendar-type">Personal</div>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown('''
    <div class="add-calendar-button">Add Calendar</div>
    ''', unsafe_allow_html=True)
    
    # Example: checkbox to add more
    add_more = st.checkbox("Add more calendars", value=False, label_visibility="hidden")
    
    # Final continue
    col_space, col_btn = st.columns([3,1])
    with col_btn:
        if st.button("Continue", key="continue_4", use_container_width=True):
            # Mark onboarding as complete
            st.session_state.onboarding_complete = True
            st.session_state.show_insights_link = True
            st.experimental_rerun()

# =====================
# Show "Insights" link if completed
# =====================
if st.session_state.get('show_insights_link', False):
    st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <p style="color: #4CAF50; font-weight: bold; font-size: 18px;">Onboarding complete!</p>
        <p style="margin-bottom: 20px;">You're all set up and ready to start your Juggl journey!</p>
        <a href="/Insights" target="_self" 
           style="display: inline-block; background: #4CAF50; color: white; 
                  padding: 10px 30px; border-radius: 30px; 
                  text-decoration: none; font-weight: bold;">
           Go to Insights Dashboard
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Continue to Insights", key="insights_direct_button"):
        # Optionally attempt a direct redirect
        st.query_params.update({'page': 'insights'})  # Not always necessary
        st.markdown("""
        <script>
            window.location.href = "/Insights";
        </script>
        """, unsafe_allow_html=True)

# --- Close the .card-content and .card-container ---
st.markdown('</div>', unsafe_allow_html=True)  # close .card-content


# If needed, store onboarding completion in localStorage
if st.session_state.get('onboarding_complete', False):
    st.markdown("""
    <script>
        localStorage.setItem('onboarding_complete','true');
    </script>
    """, unsafe_allow_html=True)