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
    margin: 3px;
    padding: 10px 5px;
    border-radius: 8px;
    border: 1px solid #e0e0e0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    transition: all 0.3s;
    cursor: pointer;
    height: 100%;
    width: 90%; /* Reduced width */
    max-width: 210px; /* Maximum width */
    margin: 0 auto; /* Center in column */


.selection-radio {
    width: 16px;
    height: 16px;
    border-radius: 50%;
    border: 2px solid #e0e0e0;
    margin-bottom: 8px;
    position: relative;
}

.selection-radio.selected {
    border-color: #4E9168;
}

.selection-radio.selected::after {
    content: "";
    position: absolute;
    width: 8px;
    height: 8px;
    background: #4E9168;
    border-radius: 50%;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.selection-title {
    font-size: 14px;
    margin-top: 6px;
    font-weight: 500;
    line-height: 1.2;
}

.selection-card.selected {
    border-color: #4E9168;
    box-shadow: 0 0 0 1px #4E9168;
}

.selection-card svg {
    width: 36px;
    height: 36px;
}

/* Reduce column gaps */
div.row-widget.stHorizontal > div {
    gap: 8px !important;
    padding: 0 !important;
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
    margin-top: 50px;
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





/* Container styling */
    .calendar-page {
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
        text-align: center;
}
    


/* Email container */
    .email-container {
        display: flex;
        align-items: center;
        padding: 15px;
        border-radius: 10px;
        background-color: white;
        margin-bottom: 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    .email-avatar {
        width: 40px;
        height: 40px;
        background-color: #4E9168;
        color: white;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        font-weight: 500;
        margin-right: 15px;
    }
    
    .email-label {
        flex-grow: 1;
        text-align: left;
        font-size: 16px;
    }
    
    .calendar-type {
        padding: 8px 15px;
        border: 1px solid #e0e0e0;
        border-radius: 5px;
        color: #666;
        font-size: 14px;
        position: relative;
    }
    
    .calendar-type::after {
        content: "▼";
        font-size: 10px;
        margin-left: 5px;
    }
    
    /* Add calendar button */
    .add-calendar-button {
        display: flex;
        align-items: center;
        justify-content: center;
        color: #2196F3;
        font-size: 16px;
        font-weight: 500;
        cursor: pointer;
        padding: 10px;
        margin-bottom: 40px;
    }
    
    .add-calendar-button::before {
        content: "+";
        margin-right: 5px;
        font-size: 18px;
    }
    
    /* Continue button */
    .continue-button {
        background-color: #2196F3;
        color: white;
        padding: 12px 30px;
        border-radius: 50px;
        font-size: 16px;
        font-weight: 500;
        border: none;
        cursor: pointer;
        margin-top: 40px;
        transition: background-color 0.3s;
    }
    
    .continue-button:hover {
        background-color: #1976D2;
    }
/* Improved input styling */
.stTextInput > div > div > input {
    padding: 12px 15px;
    border-radius: 8px;
    border: 1px solid #e0e0e0;
    font-size: 15px;
    transition: all 0.3s ease;
    margin-top: 8px;
    margin-bottom: 15px;
}

.stTextInput > div > div > input:focus {
    border-color: #4E9168;
    box-shadow: 0 0 0 1px #4E9168;
}

/* Add label margin if you have visible labels */
.stTextInput > label {
    margin-bottom: 5px;
    font-weight: 500;
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
    <path fill-rule="evenodd" clip-rule="evenodd" d="M57 46C57 46.768 56.3372 47.3528 55.5705 47.3071L53.0586 47.1573C52.456 47.1214 52 46.6036 52 46C52 45.3964 52.456 44.8786 53.0586 44.8427L55.5705 44.6929C56.3372 44.6472 57 45.232 57 46ZM53.9209 34.4963C54.3053 35.1606 54.0247 35.9998 53.3384 36.3432L51.082 37.4723C50.545 37.741 49.8941 37.5204 49.5933 37.0007C49.2926 36.481 49.4272 35.8091 49.9279 35.4776L52.0315 34.0844C52.6714 33.6607 53.5365 33.8321 53.9209 34.4963ZM45.5037 26.0791C46.1679 26.4635 46.3393 27.3286 45.9156 27.9685L44.5224 30.0721C44.1909 30.5728 43.519 30.7074 42.9993 30.4067C42.4795 30.1059 42.259 29.455 42.5277 28.918L43.6568 26.6616C44.0002 25.9753 44.8394 25.6947 45.5037 26.0791ZM35.3071 24.4295C35.3528 23.6628 34.768 23 34 23C33.232 23 32.6472 23.6628 32.6929 24.4295L32.8427 26.9414C32.8786 27.544 33.3964 28 34 28C34.6036 28 35.1214 27.544 35.1573 26.9414L35.3071 24.4295ZM22.4963 26.0791C23.1606 25.6947 23.9998 25.9753 24.3432 26.6616L25.4723 28.918C25.741 29.455 25.5204 30.1059 25.0007 30.4067C24.481 30.7074 23.8091 30.5728 23.4776 30.0721L22.0844 27.9685C21.6607 27.3286 21.8321 26.4635 22.4963 26.0791ZM14.0791 34.4963C14.4635 33.8321 15.3286 33.6607 15.9685 34.0844L18.0721 35.4776C18.5728 35.8091 18.7074 36.481 18.4067 37.0007C18.1059 37.5205 17.455 37.741 16.918 37.4723L14.6616 36.3432C13.9753 35.9998 13.6947 35.1606 14.0791 34.4963ZM12.4295 44.6929C11.6628 44.6472 11 45.232 11 46C11 46.768 11.6628 47.3528 12.4295 47.3071L14.9414 47.1573C15.544 47.1214 16 46.6036 16 46C16 45.3964 15.544 44.8786 14.9414 44.8427L12.4295 44.6929ZM14.0791 57.5037C13.6947 56.8394 13.9753 56.0002 14.6616 55.6568L16.918 54.5277C17.455 54.259 18.1059 54.4796 18.4067 54.9993C18.7074 55.519 18.5728 56.1909 18.0721 56.5224L15.9685 57.9156C15.3286 58.3393 14.4635 58.1679 14.0791 57.5037ZM22.4963 65.9209C21.8321 65.5365 21.6607 64.6714 22.0844 64.0315L23.4776 61.9279C23.8091 61.4272 24.481 61.2926 25.0007 61.5933C25.5205 61.8941 25.741 62.545 25.4723 63.082L24.3432 65.3384C23.9998 66.0247 23.1606 66.3053 22.4963 65.9209ZM34 69C33.232 69 32.6472 68.3372 32.6929 67.5705L32.8427 65.0586C32.8786 64.456 33.3964 64 34 64C34.6036 64 35.1214 64.456 35.1573 65.0586L35.3071 67.5705C35.3528 68.3372 34.768 69 34 69ZM45.5037 65.9209C44.8394 66.3053 44.0002 66.0247 43.6568 65.3384L42.5277 63.082C42.259 62.545 42.4795 61.8941 42.9993 61.5933C43.519 61.2926 44.1909 61.4272 44.5224 61.9279L45.9156 64.0315C46.3393 64.6714 46.1679 65.5365 45.5037 65.9209ZM53.9209 57.5037C53.5365 58.1679 52.6714 58.3393 52.0315 57.9156L49.9279 56.5224C49.4272 56.1909 49.2926 55.519 49.5933 54.9993C49.8941 54.4795 50.545 54.259 51.082 54.5277L53.3384 55.6568C54.0247 56.0002 54.3053 56.8394 53.9209 57.5037Z" fill="url(#paint5_linear_507_1180)"/>
    <path d="M31.2247 38.8679L33.5187 30.7114C33.6554 30.2252 34.3446 30.2252 34.4813 30.7114L36.7753 38.8679C36.9192 39.3793 36.8536 39.9269 36.5932 40.3899L34.8716 43.4505C34.4893 44.1302 33.5107 44.1302 33.1284 43.4505L31.4068 40.3899C31.1464 39.9269 31.0808 39.3793 31.2247 38.8679Z" fill="url(#paint6_linear_507_1180)"/>
    <circle cx="34" cy="46" r="3" fill="url(#paint7_linear_507_1180)"/>
    <rect x="24" width="20" height="6" rx="3" fill="url(#paint8_linear_507_1180)"/>
    <defs>
    <linearGradient id="paint0_linear_507_1180" x1="10" y1="23" x2="10" y2="33.025" gradientUnits="userSpaceOnUse">
    <stop stop-color="#A4C7FB"/>
    <stop offset="1" stop-color="#4BA3F7"/>
    </linearGradient>
    <linearGradient id="paint1_linear_507_1180" x1="62.2085" y1="10" x2="62.2085" y2="20.025" gradientUnits="userSpaceOnUse">
    <stop stop-color="#A4C7FB"/>
    <stop offset="1" stop-color="#4BA3F7"/>
    </linearGradient>
    <linearGradient id="paint2_linear_507_1180" x1="34" y1="0" x2="34" y2="20" gradientUnits="userSpaceOnUse">
    <stop stop-color="#A4C7FB"/>
    <stop offset="1" stop-color="#4BA3F7"/>
    </linearGradient>
    <linearGradient id="paint3_linear_507_1180" x1="34" y1="12" x2="34" y2="80" gradientUnits="userSpaceOnUse">
    <stop stop-color="#F3A07F"/>
    <stop offset="1" stop-color="#E97432"/>
    </linearGradient>
    <linearGradient id="paint4_linear_507_1180" x1="34" y1="18" x2="34" y2="74" gradientUnits="userSpaceOnUse">
    <stop stop-color="#F9D4C9"/>
    <stop offset="1" stop-color="white"/>
    </linearGradient>
    <linearGradient id="paint5_linear_507_1180" x1="34" y1="23" x2="34" y2="69" gradientUnits="userSpaceOnUse">
    <stop stop-color="#4BA3F7"/>
    <stop offset="1" stop-color="#A4C7FB"/>
    </linearGradient>
    <linearGradient id="paint6_linear_507_1180" x1="34" y1="29" x2="34" y2="45" gradientUnits="userSpaceOnUse">
    <stop stop-color="#F3A07F"/>
    <stop offset="1" stop-color="#E97432"/>
    </linearGradient>
    <linearGradient id="paint7_linear_507_1180" x1="34" y1="43" x2="34" y2="49" gradientUnits="userSpaceOnUse">
    <stop stop-color="#ECC736"/>
    <stop offset="1" stop-color="#F3A07F"/>
    </linearGradient>
    <linearGradient id="paint8_linear_507_1180" x1="34" y1="0" x2="34" y2="6" gradientUnits="userSpaceOnUse">
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
    <linearGradient id="paint0_linear_507_1183" x1="55.2" y1="29.76" x2="55.2" y2="43.52" gradientUnits="userSpaceOnUse">
    <stop stop-color="#887EC4"/>
    <stop offset="1" stop-color="#6556AC"/>
    </linearGradient>
    <linearGradient id="paint1_linear_507_1183" x1="29.44" y1="54.4" x2="29.44" y2="24.32" gradientUnits="userSpaceOnUse">
    <stop stop-color="#887EC4"/>
    <stop offset="1" stop-color="#6556AC"/>
    </linearGradient>
    <linearGradient id="paint2_linear_507_1183" x1="29.44" y1="9.28" x2="13.44" y2="9.28" gradientUnits="userSpaceOnUse">
    <stop stop-color="#ECC736"/>
    <stop offset="1" stop-color="white" stop-opacity="0.5"/>
    </linearGradient>
    <linearGradient id="paint3_linear_507_1183" x1="38.7198" y1="9.28" x2="22.7198" y2="9.28" gradientUnits="userSpaceOnUse">
    <stop stop-color="#ECC736"/>
    <stop offset="1" stop-color="white" stop-opacity="0.5"/>
    </linearGradient>
    <linearGradient id="paint4_linear_507_1183" x1="48.0001" y1="9.28" x2="32.0001" y2="9.28" gradientUnits="userSpaceOnUse">
    <stop stop-color="#ECC736"/>
    <stop offset="1" stop-color="white" stop-opacity="0.5"/>
    </linearGradient>
    <linearGradient id="paint5_linear_507_1183" x1="2.62451" y1="67.36" x2="77.1845" y2="67.36" gradientUnits="userSpaceOnUse">
    <stop stop-color="#D4D1EA"/>
    <stop offset="1" stop-color="#F1F0F8"/>
    </linearGradient>
    <linearGradient id="paint6_linear_507_1183" x1="40.8391" y1="56.0653" x2="40.8391" y2="76.3102" gradientUnits="userSpaceOnUse">
    <stop stop-color="#66BA86"/>
    <stop offset="1" stop-color="#224630"/>
    </linearGradient>
    </defs>
    </svg>

    """,
    'work': """
    <svg width="68" height="60" viewBox="0 0 68 60" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M3.66406 14.0197C3.66406 11.5422 5.55286 9.53384 7.88281 9.53384H60.6172C62.9471 9.53384 64.8359 11.5422 64.8359 14.0197V55.5141C64.8359 57.9916 62.9471 60 60.6172 60H7.88281C5.55286 60 3.66406 57.9916 3.66406 55.5141V14.0197Z" fill="url(#paint0_linear_508_1853)"/>
    <path fill-rule="evenodd" clip-rule="evenodd" d="M41.775 5.71304C36.9663 4.07683 31.7973 4.07683 26.9886 5.71305L26.6035 5.84409V14.3001C26.6035 15.5388 25.6591 16.543 24.4941 16.543C23.3292 16.543 22.3848 15.5388 22.3848 14.3001V5.02547C22.3848 3.56239 23.274 2.26703 24.5845 1.82112L25.2274 3.95735L24.5845 1.82112L25.7029 1.44058C31.3479 -0.480194 37.4158 -0.480195 43.0608 1.44058L44.1792 1.82112C45.4897 2.26703 46.3789 3.56239 46.3789 5.02547V14.3001C46.3789 15.5388 45.4345 16.543 44.2695 16.543C43.1046 16.543 42.1602 15.5388 42.1602 14.3001V5.84409L41.775 5.71304Z" fill="url(#paint1_linear_508_1853)"/>
    <path d="M0.5 14.0197C0.5 11.5422 2.3888 9.53384 4.71875 9.53384H63.7812C66.1112 9.53384 68 11.5422 68 14.0197V24.9645C68 28.8478 65.6504 32.2903 62.1783 33.4942L42.0974 40.457C36.9979 42.2252 31.5021 42.2252 26.4026 40.457L6.3217 33.4942C2.84958 32.2903 0.5 28.8478 0.5 24.9645V14.0197Z" fill="url(#paint2_linear_508_1853)"/>
    <path d="M30.5586 38.9724C30.5586 38.3531 31.0308 37.851 31.6133 37.851H37.9414C38.5239 37.851 38.9961 38.3531 38.9961 38.9724V42.3368C38.9961 44.8143 37.1073 46.8227 34.7773 46.8227C32.4474 46.8227 30.5586 44.8143 30.5586 42.3368V38.9724Z" fill="url(#paint3_linear_508_1853)"/>
    <defs>
    <linearGradient id="paint0_linear_508_1853" x1="34.25" y1="9.53384" x2="34.25" y2="60" gradientUnits="userSpaceOnUse">
    <stop stop-color="#4BA3F7"/>
    <stop offset="1" stop-color="#A4C7FB"/>
    </linearGradient>
    <linearGradient id="paint1_linear_508_1853" x1="34.3818" y1="0.842438" x2="34.3818" y2="14.3001" gradientUnits="userSpaceOnUse">
    <stop stop-color="#ECC736"/>
    <stop offset="1" stop-color="#FEF0CF"/>
    </linearGradient>
    <linearGradient id="paint2_linear_508_1853" x1="34.25" y1="9.53384" x2="34.25" y2="43.178" gradientUnits="userSpaceOnUse">
    <stop stop-color="#4BA3F7"/>
    <stop offset="1" stop-color="#A4C7FB"/>
    </linearGradient>
    <linearGradient id="paint3_linear_508_1853" x1="34.7773" y1="46.8227" x2="34.7773" y2="37.851" gradientUnits="userSpaceOnUse">
    <stop stop-color="#ECC736"/>
    <stop offset="1" stop-color="#FEF0CF"/>
    </linearGradient>
    </defs>
    </svg>

    """,
    'health': """
    <svg width="68" height="60" viewBox="0 0 68 60" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M29.1231 2.92551L33.6547 5.81804C34.0081 6.04362 34.462 6.04362 34.8154 5.81804L38.9567 3.17461C47.381 -2.20269 58.6082 0.180086 64.0698 8.50441C69.4904 16.7663 68.3946 27.6491 61.4334 34.6873L37.9732 58.407C35.9068 60.4963 32.5237 60.5355 30.4085 58.4947L6.53201 35.4586C-1.10939 28.0861 -2.17664 16.2923 4.01925 7.69084C9.7619 -0.281381 20.8127 -2.37909 29.1231 2.92551Z" fill="url(#paint0_linear_508_1852)"/>
    <path fill-rule="evenodd" clip-rule="evenodd" d="M3.42084 31.6877C2.64709 30.4946 2.00278 29.2389 1.48975 27.9413C1.52848 27.939 1.56753 27.9377 1.60687 27.9377H17.7984L21.5046 22.5279C22.7558 20.7017 25.4988 20.8559 26.5374 22.8109L33.4504 35.8237L44.1178 15.2001C45.236 13.0382 48.3447 13.0876 49.3937 15.284L55.437 27.9377H65.8926C65.901 27.9377 65.9094 27.9378 65.9179 27.9379C65.3801 29.2403 64.7066 30.4975 63.8996 31.6877H54.9303C53.795 31.6877 52.7608 31.0355 52.2715 30.0111L46.7062 18.3583L36.077 38.9081C34.9853 41.0186 31.9727 41.0352 30.8579 38.9367L23.8483 25.7421L20.6527 30.4066C20.1033 31.2084 19.1939 31.6877 18.2219 31.6877H3.42084Z" fill="url(#paint1_linear_508_1852)"/>
    <defs>
    <linearGradient id="paint0_linear_508_1852" x1="33.2974" y1="-6.55041" x2="33.2974" y2="62.1866" gradientUnits="userSpaceOnUse">
    <stop stop-color="#E97432"/>
    <stop offset="1" stop-color="#887EC4"/>
    </linearGradient>
    <linearGradient id="paint1_linear_508_1852" x1="33.7038" y1="13.6073" x2="33.7038" y2="40.5008" gradientUnits="userSpaceOnUse">
    <stop stop-color="white"/>
    <stop offset="1" stop-color="white" stop-opacity="0.5"/>
    </linearGradient>
    </defs>
    </svg>

    """,
    'relationships': """
    <svg width="68" height="60" viewBox="0 0 68 60" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M41.0019 2.01129L44.1308 3.9999C44.3748 4.15499 44.6882 4.15499 44.9323 3.99991L47.7917 2.18254C53.6085 -1.51435 61.3607 0.123809 65.1317 5.84678C68.8746 11.5268 68.1179 19.0087 63.3114 23.8475L47.1127 40.1548C45.6859 41.5912 43.3499 41.6182 41.8894 40.2151L25.4033 24.3778C20.1271 19.3092 19.3901 11.2009 23.6683 5.28745C27.6334 -0.193449 35.2637 -1.63563 41.0019 2.01129Z" fill="url(#paint0_linear_508_1854)"/>
    <path d="M18.4909 23.8189L21.368 25.6525C21.5924 25.7955 21.8806 25.7955 22.105 25.6525L24.7344 23.9768C30.0832 20.5679 37.2116 22.0785 40.6792 27.3555C44.1209 32.5929 43.4252 39.4918 39.0053 43.9536L24.11 58.9902C22.798 60.3146 20.65 60.3395 19.307 59.0458L4.14731 44.4425C-0.704374 39.7689 -1.38199 32.2924 2.55191 26.8397C6.19803 21.7859 13.2144 20.4561 18.4909 23.8189Z" fill="url(#paint1_linear_508_1854)"/>
    <defs>
    <linearGradient id="paint0_linear_508_1854" x1="43.8841" y1="-4.50341" x2="43.8841" y2="42.7533" gradientUnits="userSpaceOnUse">
    <stop stop-color="#E97432"/>
    <stop offset="1" stop-color="#F3A07F"/>
    </linearGradient>
    <linearGradient id="paint1_linear_508_1854" x1="21.1412" y1="17.8118" x2="21.1412" y2="61.3861" gradientUnits="userSpaceOnUse">
    <stop stop-color="#887EC4"/>
    <stop offset="1" stop-color="#ADA7D7"/>
    </linearGradient>
    </defs>
    </svg>

    """,
    'projects': """
    <svg width="60" height="60" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M3.21694 44.5566C5.67202 39.2132 12.3118 37.3146 17.2206 40.5523L-nan -nanL17.2206 40.5523C18.3048 41.2674 19.2326 42.1952 19.9477 43.2794L-nan -nanL19.9477 43.2794C23.1854 48.1882 21.2868 54.828 15.9434 57.2831L10.1253 59.9563C9.7202 60.1424 9.31541 59.6981 9.53833 59.312L11.2912 56.2765C11.9561 55.1251 10.6956 53.8233 9.52337 54.4509L3.97083 57.4234C3.39447 57.732 2.76802 57.1055 3.07657 56.5292L6.04914 50.9766C6.67668 49.8044 5.3749 48.5439 4.2235 49.2088L1.18797 50.9617C0.801935 51.1846 0.357633 50.7798 0.543744 50.3747L3.21694 44.5566Z" fill="url(#paint0_linear_508_1855)"/>
    <path d="M11.8771 23.2751L20.4762 22.4506L13.3627 31.3802L12.3885 30.4059C11.5788 29.5963 10.4181 29.2448 9.29527 29.4694L4.78432 30.3716C3.95367 30.5377 3.41202 29.5256 4.01101 28.9266L7.68769 25.25C8.81247 24.1252 10.2937 23.427 11.8771 23.2751Z" fill="url(#paint1_linear_508_1855)"/>
    <path d="M36.4513 47.8496L37.2758 39.2505L28.3462 46.3639L29.3204 47.3382C30.1301 48.1478 30.4816 49.3086 30.257 50.4314L29.3548 54.9424C29.1887 55.773 30.2008 56.3146 30.7997 55.7157L34.4764 52.039C35.6012 50.9142 36.2994 49.433 36.4513 47.8496Z" fill="url(#paint2_linear_508_1855)"/>
    <path d="M43.804 0.986697L57.7164 0.0337925C58.7525 -0.037172 59.6127 0.823048 59.5418 1.85912L58.5889 15.7715C58.3166 19.7467 56.4266 23.4364 53.3597 25.98L28.3291 46.74C27.1382 47.7277 25.3912 47.6464 24.2972 46.5524L13.0232 35.2783C11.9292 34.1843 11.8479 32.4373 12.8356 31.2465L33.5956 6.21585C36.1392 3.14897 39.8289 1.25897 43.804 0.986697Z" fill="url(#paint3_linear_508_1855)"/>
    <circle cx="41.9678" cy="17.6074" r="7.70547" transform="rotate(45 41.9678 17.6074)" fill="url(#paint4_linear_508_1855)"/>
    <circle cx="41.9678" cy="17.6074" r="5.56506" transform="rotate(45 41.9678 17.6074)" fill="url(#paint5_linear_508_1855)"/>
    <path d="M23.1375 31.3017L26.4744 30.1287C28.5077 29.4139 30.4641 31.3704 29.7493 33.4037L28.5763 36.7405C28.0428 38.258 26.9923 39.5393 25.6088 40.36L13.5219 47.5293C12.7593 47.9816 11.8964 47.1188 12.3487 46.3562L19.5181 34.2692C20.3387 32.8857 21.62 31.8352 23.1375 31.3017Z" fill="url(#paint6_linear_508_1855)"/>
    <path d="M58.5408 12.2137C55.5651 11.6831 52.9423 10.4199 50.8975 8.37518C48.9337 6.41137 47.6909 3.91445 47.1255 1.08369C48.6269 0.765994 50.1574 0.551542 51.707 0.445406L58.1637 0.00316291C58.9632 -0.0515969 59.627 0.612192 59.5723 1.41168L59.13 7.86842C59.0294 9.33682 58.8316 10.7881 58.5408 12.2137Z" fill="url(#paint7_linear_508_1855)"/>
    <defs>
    <linearGradient id="paint0_linear_508_1855" x1="18.8636" y1="41.6362" x2="2.04595" y2="58.4538" gradientUnits="userSpaceOnUse">
    <stop stop-color="#E97432"/>
    <stop offset="1" stop-color="#ECC736"/>
    </linearGradient>
    <linearGradient id="paint1_linear_508_1855" x1="18.4329" y1="20.4074" x2="4.96279" y2="33.8775" gradientUnits="userSpaceOnUse">
    <stop stop-color="#FEF0CF"/>
    <stop offset="1" stop-color="#ECC736"/>
    </linearGradient>
    <linearGradient id="paint2_linear_508_1855" x1="39.319" y1="41.2936" x2="25.8489" y2="54.7638" gradientUnits="userSpaceOnUse">
    <stop stop-color="#FEF0CF"/>
    <stop offset="1" stop-color="#ECC736"/>
    </linearGradient>
    <linearGradient id="paint3_linear_508_1855" x1="59.6759" y1="-0.100523" x2="18.6601" y2="40.9153" gradientUnits="userSpaceOnUse">
    <stop stop-color="#4BA3F7"/>
    <stop offset="1" stop-color="#A4C7FB"/>
    </linearGradient>
    <linearGradient id="paint4_linear_508_1855" x1="49.6732" y1="17.6074" x2="34.2623" y2="17.6074" gradientUnits="userSpaceOnUse">
    <stop stop-color="#ECC736"/>
    <stop offset="1" stop-color="#FEF0CF"/>
    </linearGradient>
    <linearGradient id="paint5_linear_508_1855" x1="41.9678" y1="12.0423" x2="41.9678" y2="23.1725" gradientUnits="userSpaceOnUse">
    <stop stop-color="#ECC736"/>
    <stop offset="1" stop-color="#FEF0CF"/>
    </linearGradient>
    <linearGradient id="paint6_linear_508_1855" x1="10.6381" y1="49.2395" x2="31.5244" y2="28.3532" gradientUnits="userSpaceOnUse">
    <stop stop-color="#ECC736"/>
    <stop offset="1" stop-color="#FEF0CF"/>
    </linearGradient>
    <linearGradient id="paint7_linear_508_1855" x1="59.2849" y1="0.483494" x2="51.7618" y2="8.00662" gradientUnits="userSpaceOnUse">
    <stop stop-color="white"/>
    <stop offset="1" stop-color="white" stop-opacity="0.5"/>
    </linearGradient>
    </defs>
    </svg>

    """,
    'hobbies': """
    <svg width="67" height="60" viewBox="0 0 67 60" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M51.4181 25.7491C55.488 23.6579 60.5752 25.4243 60.5752 30C60.5752 46.5685 47.1437 60 30.5752 60C14.0067 60 0.575195 46.5685 0.575195 30C0.575195 13.4315 14.0067 0 30.5752 0C37.2522 0 37.3328 5.93416 31.6535 9.44541C28.0094 11.6984 26.0273 14.6256 26.3564 19.4531C26.9246 27.7864 39.2773 31.9875 51.4181 25.7491ZM48.3877 42.6562C50.9765 42.6562 53.0752 40.5576 53.0752 37.9688C53.0752 35.3799 50.9765 33.2812 48.3877 33.2812C45.7989 33.2812 43.7002 35.3799 43.7002 37.9688C43.7002 40.5576 45.7989 42.6562 48.3877 42.6562Z" fill="url(#paint0_linear_508_1856)"/>
    <circle cx="14.6377" cy="18.2812" r="4.6875" fill="url(#paint1_linear_508_1856)"/>
    <circle cx="11.3564" cy="32.8125" r="4.6875" fill="url(#paint2_linear_508_1856)"/>
    <circle cx="19.3252" cy="45.4688" r="4.6875" fill="url(#paint3_linear_508_1856)"/>
    <circle cx="35.2627" cy="48.75" r="4.6875" fill="url(#paint4_linear_508_1856)"/>
    <path d="M47.4558 29.044C47.2 25.7681 49.7893 22.9688 53.0752 22.9688C56.3611 22.9688 58.9504 25.7681 58.6946 29.044L56.7241 54.2811C56.5754 56.1862 54.9861 57.6562 53.0752 57.6562C51.1643 57.6562 49.575 56.1862 49.4263 54.2811L47.4558 29.044Z" fill="url(#paint5_linear_508_1856)"/>
    <path d="M50.6064 6.3707L51.4372 3.8068C51.9927 2.0923 54.1814 1.59842 55.4194 2.90822L58.1103 5.75528C63.0032 10.9321 63.2868 18.9385 58.7724 24.4485C58.3243 24.9954 57.6546 25.3125 56.9476 25.3125H48.6718C48.1313 25.3125 47.6203 25.0657 47.2843 24.6423L44.924 21.6683C42.0754 18.079 43.1327 12.7907 47.1424 10.5726C48.7883 9.66214 50.0266 8.16006 50.6064 6.3707Z" fill="url(#paint6_linear_508_1856)"/>
    <defs>
    <linearGradient id="paint0_linear_508_1856" x1="30.5752" y1="0" x2="30.5752" y2="60" gradientUnits="userSpaceOnUse">
    <stop stop-color="#DEDCDB"/>
    <stop offset="1" stop-color="#B9B3B2"/>
    </linearGradient>
    <linearGradient id="paint1_linear_508_1856" x1="14.6377" y1="13.5938" x2="14.6377" y2="22.9688" gradientUnits="userSpaceOnUse">
    <stop stop-color="#F3A07F"/>
    <stop offset="1" stop-color="#E97432"/>
    </linearGradient>
    <linearGradient id="paint2_linear_508_1856" x1="11.3564" y1="28.125" x2="11.3564" y2="37.5" gradientUnits="userSpaceOnUse">
    <stop stop-color="#4BA3F7"/>
    <stop offset="1" stop-color="#A4C7FB"/>
    </linearGradient>
    <linearGradient id="paint3_linear_508_1856" x1="19.3252" y1="40.7812" x2="19.3252" y2="50.1562" gradientUnits="userSpaceOnUse">
    <stop stop-color="#66BA86"/>
    <stop offset="1" stop-color="#8CE1AC"/>
    </linearGradient>
    <linearGradient id="paint4_linear_508_1856" x1="35.2627" y1="44.0625" x2="35.2627" y2="53.4375" gradientUnits="userSpaceOnUse">
    <stop stop-color="#ECC736"/>
    <stop offset="1" stop-color="#FEF0CF"/>
    </linearGradient>
    <linearGradient id="paint5_linear_508_1856" x1="53.0752" y1="57.6562" x2="53.0752" y2="22.9688" gradientUnits="userSpaceOnUse">
    <stop stop-color="#F3A07F"/>
    <stop offset="1" stop-color="#E97432"/>
    </linearGradient>
    <linearGradient id="paint6_linear_508_1856" x1="53.0752" y1="0" x2="53.0752" y2="25.3125" gradientUnits="userSpaceOnUse">
    <stop stop-color="#4BA3F7"/>
    <stop offset="1" stop-color="#A4C7FB"/>
    </linearGradient>
    </defs>
    </svg>

    """,
    'adulting': """
    <svg width="54" height="60" viewBox="0 0 54 60" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M0.668945 35.7125C0.668945 35.1882 0.773772 34.6691 0.977265 34.1858L1.27791 33.4717C3.47692 28.2491 6.59818 23.465 10.4923 19.3483L13.2099 16.4754H23.2919L23.8284 21.4378C24.1177 24.1144 25.3134 26.6117 27.2171 28.5154L32.4674 33.7657C33.2052 34.5035 33.6198 35.5042 33.6198 36.5477V56.0656C33.6198 58.2385 31.8583 60 29.6853 60H4.60337C2.43045 60 0.668945 58.2385 0.668945 56.0656V35.7125Z" fill="url(#paint0_linear_508_1857)"/>
    <rect x="27.4067" y="9.83606" width="11.8033" height="3.93443" rx="1.96721" transform="rotate(42.1294 27.4067 9.83606)" fill="url(#paint1_linear_508_1857)"/>
    <path d="M4.11182 12.7869C4.11182 6.26812 9.39632 0.983612 15.9151 0.983612H27.7184V14.7541C27.7184 15.8406 26.8376 16.7213 25.7512 16.7213H6.07903C4.99257 16.7213 4.11182 15.8406 4.11182 14.7541V12.7869Z" fill="url(#paint2_linear_508_1857)"/>
    <path d="M27.7183 0.983612H28.6363C30.8454 0.983612 32.6363 2.77447 32.6363 4.98361V6.81967C32.6363 9.02881 30.8454 10.8197 28.6363 10.8197H27.7183V0.983612Z" fill="url(#paint3_linear_508_1857)"/>
    <circle cx="38.538" cy="8.36065" r="1.96721" fill="url(#paint4_linear_508_1857)"/>
    <circle cx="46.8986" cy="2.95082" r="2.95082" fill="url(#paint5_linear_508_1857)"/>
    <circle cx="48.6195" cy="14.0164" r="5.16393" fill="url(#paint6_linear_508_1857)"/>
    <circle cx="17.1443" cy="41.5574" r="9.09836" fill="url(#paint7_linear_508_1857)"/>
    <circle cx="17.1442" cy="41.5574" r="6.63934" fill="url(#paint8_linear_508_1857)"/>
    <defs>
    <linearGradient id="paint0_linear_508_1857" x1="17.1444" y1="16.4754" x2="17.1444" y2="60" gradientUnits="userSpaceOnUse">
    <stop stop-color="#887EC4"/>
    <stop offset="1" stop-color="#ADA7D7"/>
    </linearGradient>
    <linearGradient id="paint1_linear_508_1857" x1="33.3084" y1="9.83606" x2="33.3084" y2="13.7705" gradientUnits="userSpaceOnUse">
    <stop stop-color="#66BA86"/>
    <stop offset="1" stop-color="#8CE1AC"/>
    </linearGradient>
    <linearGradient id="paint2_linear_508_1857" x1="15.9151" y1="0.983612" x2="15.9151" y2="16.7213" gradientUnits="userSpaceOnUse">
    <stop stop-color="#887EC4"/>
    <stop offset="1" stop-color="#ADA7D7"/>
    </linearGradient>
    <linearGradient id="paint3_linear_508_1857" x1="30.1773" y1="0.983612" x2="30.1773" y2="10.8197" gradientUnits="userSpaceOnUse">
    <stop stop-color="#887EC4"/>
    <stop offset="1" stop-color="#ADA7D7"/>
    </linearGradient>
    <linearGradient id="paint4_linear_508_1857" x1="38.538" y1="6.39343" x2="38.538" y2="10.3279" gradientUnits="userSpaceOnUse">
    <stop stop-color="#D3FADF"/>
    <stop offset="1" stop-color="#8CE1AC"/>
    </linearGradient>
    <linearGradient id="paint5_linear_508_1857" x1="46.8986" y1="0" x2="46.8986" y2="5.90164" gradientUnits="userSpaceOnUse">
    <stop stop-color="#D3FADF"/>
    <stop offset="1" stop-color="#8CE1AC"/>
    </linearGradient>
    <linearGradient id="paint6_linear_508_1857" x1="48.6195" y1="8.85245" x2="48.6195" y2="19.1803" gradientUnits="userSpaceOnUse">
    <stop stop-color="#D3FADF"/>
    <stop offset="1" stop-color="#8CE1AC"/>
    </linearGradient>
    <linearGradient id="paint7_linear_508_1857" x1="17.1443" y1="32.459" x2="17.1443" y2="50.6557" gradientUnits="userSpaceOnUse">
    <stop stop-color="#8CE1AC"/>
    <stop offset="1" stop-color="#D3FADF"/>
    </linearGradient>
    <linearGradient id="paint8_linear_508_1857" x1="17.1442" y1="48.1967" x2="17.1442" y2="34.918" gradientUnits="userSpaceOnUse">
    <stop stop-color="#8CE1AC"/>
    <stop offset="1" stop-color="#D3FADF"/>
    </linearGradient>
    </defs>
    </svg>

    """
}

def create_selection_card(icon, title, is_selected):
    """Generate HTML for a selection card."""
    html = f"""
    <div class="selection-card{"" if not is_selected else " selected"}">
      <div class="selection-radio{"" if not is_selected else " selected"}"></div>
      {icon}
      <div class="selection-title">{title}</div>
    </div>
    """
    return html

# Replace line breaks with space
def format_title(title):
    """Format title to replace <br> with spaces"""
    return title.replace("<br>", " ")


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
st.markdown("""
<div style="text-align: left; margin-bottom: 5px;">
  <svg width="118" height="48" viewBox="0 0 118 48" fill="none" xmlns="http://www.w3.org/2000/svg">
  <g id="Group 28">
  <g id="TM">
  <path id="Vector" d="M113.051 5C112.944 5 112.861 4.96987 112.8 4.9096C112.745 4.84933 112.717 4.76588 112.717 4.65925V0.340751C112.717 0.229485 112.747 0.146036 112.807 0.090403C112.868 0.0301343 112.949 0 113.051 0C113.148 0 113.222 0.0185442 113.273 0.0556325C113.329 0.0880851 113.38 0.148354 113.426 0.236439L115.248 3.637H115.033L116.848 0.236439C116.894 0.148354 116.943 0.0880851 116.994 0.0556325C117.045 0.0185442 117.119 0 117.216 0C117.318 0 117.397 0.0301343 117.453 0.090403C117.508 0.146036 117.536 0.229485 117.536 0.340751V4.65925C117.536 4.76588 117.508 4.84933 117.453 4.9096C117.402 4.96987 117.323 5 117.216 5C117.11 5 117.029 4.96987 116.973 4.9096C116.917 4.84933 116.89 4.76588 116.89 4.65925V1.07093H117.043L115.429 4.05424C115.392 4.12378 115.353 4.17478 115.311 4.20723C115.269 4.23969 115.211 4.25591 115.137 4.25591C115.063 4.25591 115.003 4.23969 114.956 4.20723C114.91 4.17014 114.868 4.11915 114.831 4.05424L113.204 1.06398H113.371V4.65925C113.371 4.76588 113.343 4.84933 113.287 4.9096C113.236 4.96987 113.157 5 113.051 5Z" fill="#4E9168"/>
  <path id="Vector_2" d="M110.149 4.99991C110.033 4.99991 109.943 4.96745 109.878 4.90255C109.817 4.83764 109.787 4.74724 109.787 4.63134V0.653591H108.313C108.216 0.653591 108.139 0.628093 108.083 0.577096C108.028 0.521463 108 0.444968 108 0.34761C108 0.250253 108.028 0.176076 108.083 0.125079C108.139 0.0740825 108.216 0.048584 108.313 0.048584H111.978C112.08 0.048584 112.159 0.0740825 112.214 0.125079C112.27 0.176076 112.298 0.250253 112.298 0.34761C112.298 0.444968 112.27 0.521463 112.214 0.577096C112.159 0.628093 112.08 0.653591 111.978 0.653591H110.504V4.63134C110.504 4.74724 110.473 4.83764 110.413 4.90255C110.358 4.96745 110.269 4.99991 110.149 4.99991Z" fill="#4E9168"/>
  </g>
  <g id="Vector_3">
  <path d="M95.7947 12.5941C95.9565 10.7448 95.69 9.02572 94.9926 7.47566C95.4286 7.32527 95.8512 7.1454 96.2589 6.93454C97.936 6.06716 98.9766 4.60175 99.1432 2.69776C99.1745 2.33956 99.1656 1.98706 99.1161 1.64406L101.114 1.4341C102.275 1.31202 103.091 1.34721 103.56 1.53967C103.995 1.73571 104.245 2.1412 104.309 2.75611C104.363 3.26855 104.287 3.69106 104.08 4.02365C103.873 4.35624 103.612 4.66006 103.295 4.9351C102.979 5.21014 102.685 5.53463 102.413 5.90857C102.107 6.2861 101.876 6.88029 101.72 7.69115C101.559 8.46785 101.54 9.43696 101.663 10.5985L103.268 25.8689C103.817 31.0957 105.236 33.5889 107.525 33.3483C108.481 33.2478 109.173 32.7606 109.599 31.8869C109.991 31.0167 110.234 29.7132 110.328 27.9764C110.353 26.903 110.656 26.0076 111.237 25.2903C111.814 24.5389 112.667 24.1039 113.794 23.9854C114.819 23.8777 115.726 24.1278 116.515 24.7356C117.304 25.3434 117.765 26.2794 117.898 27.5434C118.153 29.9689 117.467 32.1479 115.839 34.0805C114.208 35.9789 111.753 37.1004 108.474 37.4451C106.321 37.6713 104.448 37.5919 102.853 37.2069C101.255 36.7877 99.9648 36.1807 98.9832 35.3859C98.2195 34.7674 97.552 33.9714 96.981 32.9981C97.1944 32.3358 97.3358 31.6327 97.4009 30.8891C97.6105 28.4933 96.9611 26.331 95.3444 24.6136C95.0507 24.3016 94.7355 24.0182 94.4007 23.7619C94.364 23.4562 94.3289 23.1431 94.2952 22.8227L93.808 17.9765C94.9429 16.445 95.6156 14.6414 95.7947 12.5941Z" fill="#4E9168"/>
  <path d="M71.3376 8.39011C72.339 7.53877 73.5678 7.03613 74.9783 7.15955C76.1517 7.26222 77.1614 7.80198 77.9103 8.69446C78.0544 8.86616 78.1831 9.04469 78.2964 9.22917C78.4886 8.30166 78.8495 7.5307 79.379 6.9163C80.0698 6.1147 80.9114 5.75731 81.9037 5.84413C83.3752 5.97286 84.437 6.8416 85.0894 8.45034C85.7759 10.0621 86.0384 11.7919 85.8767 13.6397C85.748 15.1112 85.3397 16.2306 84.6519 16.998C83.9983 17.7683 83.1924 18.1116 82.2343 18.0278C80.6944 17.8931 79.5953 17.0555 78.937 15.5152C78.6951 14.9905 78.5064 14.4308 78.3707 13.8362C77.8783 14.8123 77.0764 15.5922 76.0239 16.1366C75.6161 16.3474 75.1936 16.5273 74.7576 16.6777C75.2514 17.7752 75.5291 18.9576 75.5917 20.2108C75.7013 20.1054 75.8262 20.0052 75.9663 19.9104C77.4019 20.4497 78.9922 20.7957 80.7374 20.9484L81.1481 20.9844C84.6132 21.1841 87.5187 20.49 89.8644 18.9022C92.2101 17.3144 93.5027 15.1517 93.7423 12.4141C93.9638 9.8819 93.2195 7.74789 91.5094 6.01212C92.9616 5.96677 94.2294 5.66391 95.3129 5.10355C96.3963 4.5432 96.9889 3.68128 97.0907 2.51782C97.1476 1.86765 96.9731 1.30067 96.5672 0.816902C96.1612 0.333127 95.6503 0.0642941 95.0343 0.0104052C94.1446 -0.0674342 93.3202 0.291454 92.5609 1.08707C90.7969 2.72577 89.0594 3.47028 87.3484 3.32059C87.0062 3.29065 86.5629 3.23462 86.0184 3.1525C85.5111 3.03916 85.1547 2.9735 84.9494 2.95554L83.3069 2.81184C79.8417 2.61212 76.8589 3.40284 74.3583 5.18399C73.033 6.12799 72.0261 7.1967 71.3376 8.39011Z" fill="#4E9168"/>
  <path fill-rule="evenodd" clip-rule="evenodd" d="M75.4665 22.5707C75.0023 25.5903 73.4046 28.0373 70.7838 29.8113C70.0893 30.2813 69.3591 30.6814 68.5954 31.014L68.598 31.0142C71.2157 31.2432 73.4889 32.0945 75.1091 33.8156C76.3339 35.1167 77.0034 36.673 77.165 38.3928C77.8869 38.5141 78.6297 38.6082 79.3934 38.675C83.842 39.0642 87.5441 38.5261 90.4998 37.0606C93.4867 35.6323 95.1029 33.5152 95.3484 30.7092C95.5131 28.8271 95.0117 27.2661 93.8444 26.026C92.6771 24.786 90.9471 24.0657 88.6544 23.8651C87.9015 23.7993 86.3013 23.7627 83.8538 23.7555C81.4092 23.714 79.6737 23.6484 78.6471 23.5586C77.0838 23.4218 76.0236 23.0925 75.4665 22.5707ZM81.1315 35.3617C76.5461 34.9605 74.3402 33.7676 74.5139 31.7828C74.6246 30.5167 75.45 29.951 76.9899 30.0857L78.1704 30.189C79.1286 30.2729 80.3992 30.3323 81.9823 30.3673C83.5624 30.4366 84.7972 30.5102 85.687 30.588L85.841 30.6015C87.4493 30.7422 88.1995 31.4285 88.0918 32.6604C87.9002 34.8505 85.5801 35.7509 81.1315 35.3617Z" fill="#4E9168"/>
  <path fill-rule="evenodd" clip-rule="evenodd" d="M49.2801 35.1864C49.748 35.9207 50.4575 36.5631 51.4085 37.1137C50.4174 37.4063 49.5995 37.8864 48.9549 38.5541C48.3445 39.2248 48.0034 39.9708 47.9316 40.7921C47.8118 42.1609 48.3259 43.3782 49.474 44.4442C50.6563 45.5131 52.0693 46.3091 53.7132 46.8323C55.3912 47.3584 57.2055 47.7068 59.156 47.8775C63.6045 48.2667 67.3066 47.7286 70.2624 46.2632C73.2493 44.8349 74.8655 42.7178 75.1111 39.9118C75.2757 38.0297 74.7744 36.4687 73.6071 35.2286C72.4398 33.9886 70.7098 33.2683 68.4171 33.0677C67.6643 33.0018 66.0641 32.9652 63.6165 32.958C61.172 32.9165 59.4364 32.8508 58.4098 32.761C55.9179 32.5429 54.7043 31.8357 54.769 30.6393C54.7074 30.7674 54.6406 30.89 54.5707 31.0065C54.1705 31.6728 53.5945 32.2675 52.9611 32.8L52.9507 32.8087L52.9402 32.8173C52.029 33.5631 50.8916 34.3019 49.5614 35.0394L49.5409 35.0508L49.5201 35.0617C49.4397 35.1039 49.3597 35.1455 49.2801 35.1864ZM60.8941 44.5642C56.3087 44.1629 54.1028 42.9699 54.2765 40.9852C54.3873 39.7191 55.2126 39.1534 56.7525 39.2881L57.9331 39.3914C58.8912 39.4753 60.1618 39.5347 61.7449 39.5698C63.325 39.6391 64.5599 39.7127 65.4496 39.7905L65.6036 39.804C67.2119 39.9447 67.9622 40.6311 67.8544 41.863C67.6627 44.053 65.3427 44.9534 60.8941 44.5642Z" fill="#4E9168"/>
  <path fill-rule="evenodd" clip-rule="evenodd" d="M55.0768 29.7379C55.1585 29.3374 55.1737 28.9054 55.0855 28.452C54.8806 27.3975 54.1982 26.6544 53.3717 26.2355C52.8889 25.9909 52.3803 25.8051 51.8512 25.6741C51.8175 25.6503 51.7515 25.5972 51.6571 25.4951C51.5393 25.3484 51.3821 25.0619 51.277 24.5208L50.3006 19.4977C50.8525 17.5113 52.1261 15.8075 54.1213 14.3864C56.6218 12.6052 59.6047 11.8146 63.0699 12.0143L64.7124 12.158C64.9177 12.176 65.274 12.2417 65.7813 12.355C66.3259 12.4371 66.7692 12.4932 67.1114 12.5231C68.8224 12.6728 70.5599 11.9283 72.3239 10.2897C73.0832 9.49406 73.9076 9.13518 74.7973 9.21303C75.4133 9.26693 75.9242 9.53577 76.3302 10.0195C76.7361 10.5033 76.9106 11.0703 76.8537 11.7205C76.7519 12.8839 76.1593 13.7458 75.0758 14.3062C73.9923 14.8665 72.7245 15.1694 71.2723 15.2147C72.9824 16.9505 73.7267 19.0845 73.5051 21.6168C73.2656 24.3543 71.9729 26.517 69.6272 28.1048C67.2814 29.6926 64.376 30.3866 60.9108 30.1868L60.5002 30.1509C58.755 29.9982 57.1646 29.6521 55.7291 29.1127C55.4518 29.3005 55.2343 29.5089 55.0768 29.7379ZM61.9971 27.2302C60.4572 27.0955 59.3581 26.258 58.6998 24.7177C58.0043 23.2086 57.7479 21.4104 57.9305 19.323C58.0473 17.9884 58.4511 16.9203 59.1419 16.1187C59.8327 15.3171 60.6743 14.9598 61.6667 15.0466C63.1381 15.1753 64.2 16.0441 64.8523 17.6528C65.5388 19.2646 65.8012 20.9944 65.6395 22.8422C65.5108 24.3137 65.1025 25.4331 64.4147 26.2005C63.7611 26.9708 62.9552 27.3141 61.9971 27.2302Z" fill="#4E9168"/>
  <path d="M0.0517875 27.5434C0.184639 26.2794 0.645673 25.3435 1.43489 24.7357C2.22411 24.1278 3.13114 23.8778 4.15601 23.9855C5.28336 24.104 6.13567 24.5389 6.71294 25.2904C7.29379 26.0077 7.59689 26.9031 7.62223 27.9764C7.716 29.7133 7.95893 31.0168 8.35103 31.8869C8.77729 32.7607 9.46869 33.2478 10.4252 33.3484C12.7141 33.5889 14.1332 31.0958 14.6826 25.869L16.2875 10.5985C16.4096 9.43703 16.3906 8.46792 16.2305 7.69122C16.0739 6.88036 15.8428 6.28617 15.5371 5.90864C15.2655 5.5347 14.9715 5.21021 14.655 4.93517C14.3385 4.66013 14.0769 4.35631 13.87 4.02372C13.6632 3.69113 13.5867 3.26861 13.6406 2.75618C13.7052 2.14126 13.9551 1.73578 14.3902 1.53973C14.8594 1.34728 15.6748 1.31209 16.8363 1.43417L26.265 2.42517C27.3582 2.54007 28.1143 2.74042 28.5333 3.02624C28.9522 3.31205 29.1294 3.76241 29.0648 4.37733C29.0109 4.88976 28.8483 5.28714 28.5768 5.56947C28.3054 5.85179 27.9863 6.09457 27.6195 6.2978C27.2528 6.50103 26.8806 6.7555 26.5031 7.06122C26.1256 7.36693 25.7759 7.90009 25.4542 8.66068C25.1361 9.38711 24.916 10.3311 24.7939 11.4926L23.6549 22.8227C23.4466 24.8041 23.1817 26.5033 22.8601 27.9201C22.5726 29.3406 22.0973 30.7413 21.434 32.1222C20.7708 33.5032 19.9484 34.5911 18.9668 35.3859C17.9853 36.1808 16.6953 36.7878 15.097 37.207C13.5022 37.592 11.6288 37.6714 9.47654 37.4452C6.19697 37.1005 3.74166 35.9789 2.1106 34.0805C0.483127 32.148 -0.203144 29.9689 0.0517875 27.5434Z" fill="#4E9168"/>
  <path d="M24.964 27.9466C25.2653 26.5239 25.5103 24.8844 25.7044 23.0383L25.7048 23.0336L26.7582 12.5557C27.7702 12.0005 28.4416 11.6907 28.7723 11.6264C29.6153 11.4626 30.1482 11.9539 30.371 13.1003L31.6674 20.0394L32.8177 25.9572C33.1781 27.8117 33.703 29.1619 34.3923 30.0077C35.1088 30.8133 36.0909 31.0948 37.3385 30.8523C38.5861 30.6098 39.5471 29.7931 40.2216 28.4022C40.9232 26.9711 41.0872 25.2945 40.7136 23.3725L39.76 18.4664C39.5896 17.5897 39.2529 16.9378 38.7499 16.5106C38.2404 16.0498 37.7539 15.7069 37.2902 15.4821C36.8538 15.217 36.5962 14.8822 36.5176 14.4775C36.3931 13.8369 36.8211 13.1588 37.8018 12.4433C38.7554 11.768 40.0531 10.9733 41.6951 10.0593C43.3642 9.10497 44.4011 8.58848 44.8058 8.50983C45.6487 8.34597 46.1816 8.83727 46.4045 9.98372L47.7008 16.9228L49.2542 24.9143C49.4115 25.7236 49.6943 26.3684 50.1027 26.849C50.5045 27.2958 50.9072 27.5674 51.3109 27.6639C51.7146 27.7604 52.0911 27.8972 52.4404 28.0742C52.7898 28.2513 52.9972 28.5084 53.0628 28.8456C53.1939 29.52 52.718 30.3123 51.6352 31.2227C50.8503 31.8651 49.826 32.5366 48.5625 33.2372C47.2923 33.904 46.3032 34.3062 45.5951 34.4438C44.8196 34.5946 44.2005 34.47 43.7378 34.07C43.3023 33.6298 42.9394 32.843 42.6491 31.7096L42.4314 30.8596C41.7363 32.3245 40.7664 33.5453 39.5215 34.5221C38.2767 35.499 36.9799 36.1185 35.6311 36.3806C32.765 36.9378 30.4131 36.4501 28.5756 34.9177C26.7985 33.4016 25.5947 31.0779 24.964 27.9466Z" fill="#4E9168"/>
  </g>
  </svg>
</div>
""", unsafe_allow_html=True)

# --- Start card container ---

st.markdown('<div class="card-content">', unsafe_allow_html=True)

st.write("")  # Adds a small amount of vertical space


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
    # Create 5 columns with small gap
    col1, col2, col3, col4, col5 = st.columns(5, gap="small")

    with col1:
        burnout = st.checkbox("Prevent Burnout", value=False, label_visibility="collapsed")
        st.markdown(
            create_selection_card(
                icons['burnout'], 
                "Prevent Burnout", 
                burnout
            ), 
            unsafe_allow_html=True
        )

    with col2:
        balance = st.checkbox("Achieve Balance", value=False, label_visibility="collapsed")
        st.markdown(
            create_selection_card(
                icons['balance'], 
                "Achieve Balance", 
                balance
            ), 
            unsafe_allow_html=True
        )

    with col3:
        goals = st.checkbox("Achieve Life Goals", value=False, label_visibility="collapsed")
        st.markdown(
            create_selection_card(
                icons['goals'], 
                "Achieve Life Goals", 
                goals
            ), 
            unsafe_allow_html=True
        )

    with col4:
        time = st.checkbox("Reclaim Time", value=False, label_visibility="collapsed")
        st.markdown(
            create_selection_card(
                icons['time'], 
                "Reclaim Time", 
                time
            ), 
            unsafe_allow_html=True
        )

    with col5:
        habits = st.checkbox("Nurture Habits", value=False, label_visibility="collapsed")
        st.markdown(
            create_selection_card(
                icons['habits'], 
                "Nurture Habits", 
                habits
            ), 
            unsafe_allow_html=True
        )
    # Save them into session state
    st.session_state.onboarding_data['goals'] = {
        'prevent_burnout': burnout,
        'achieve_balance': balance,
        'achieve_life_goals': goals,
        'reclaim_time': time,
        'nurture_habits': habits
    }
        
    # Add vertical space above the continue button
    st.write("")  # Adds a small amount of vertical space
    st.write("")  # Add multiple for more space
    st.write("")  # Add multiple for more space

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
    container = st.container()

    # Add custom CSS to adjust input element margins
    st.markdown("""
    <style>
        /* Remove default margins from Streamlit elements */
        .stSelectbox, .stRadio {
            margin-top: 0 !important;
            padding-top: 0 !important;
            padding-left: 30px !important;
            padding-right: 30px !important;
        }
        
        /* Style for form labels */
        .form-label {
            font-weight: 500;
            font-size: 16px;
            margin-left: 30px;
            margin-top: 20px;
            margin-bottom: 5px;
            display: block;
        }
    </style>
    """, unsafe_allow_html=True)

    # Industry field
    st.markdown("<div class='form-label'>Which industry do you work in?</div>", unsafe_allow_html=True)
    industry = st.selectbox(
        "Industry placeholder",
        options=["Education", "Healthcare", "Finance", "Technology", "Manufacturing", "Retail", "Other"],
        index=0,
        label_visibility="collapsed"
    )

    # Job role field
    st.markdown("<div class='form-label'>What best describes your job role?</div>", unsafe_allow_html=True)
    role = st.selectbox(
        "Role placeholder",
        options=["Data Scientist", "Product Manager", "Engineer", "Designer", "Marketing", "Sales", "Executive", "Other"],
        index=0,
        label_visibility="collapsed"
    )

    # Work setup field
    st.markdown("<div class='form-label'>What's your work set up like?</div>", unsafe_allow_html=True)
    work_setup = st.radio(
        "Work setup",
        ["Fully Remote", "Hybrid", "In Office"],
        horizontal=True,
        label_visibility="collapsed"
    )
        
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
        st.markdown(
            create_selection_card(
                icons['work'], 
                "Work & Career", 
                work
            ), 
            unsafe_allow_html=True
        )

    with col2:
        health = st.checkbox("Physical & Mental Health", value=False, label_visibility="collapsed")
        st.markdown(
            create_selection_card(
                icons['health'], 
                "Physical & Mental Health", 
                health
            ), 
            unsafe_allow_html=True
        )

    with col3:
        relationships = st.checkbox("Relationships & Connection", value=False, label_visibility="collapsed")
        st.markdown(
            create_selection_card(
                icons['relationships'], 
                "Relationships & Connection", 
                relationships
            ), 
            unsafe_allow_html=True
        )

    # Second row
    col4, col5, col6 = st.columns(3)
    with col4:
        projects = st.checkbox("Passion Projects", value=False, label_visibility="collapsed")
        st.markdown(
            create_selection_card(
                icons['projects'], 
                "Passion Projects", 
                projects
            ), 
            unsafe_allow_html=True
        )

    with col5:
        hobbies = st.checkbox("Recreation & Hobbies", value=False, label_visibility="collapsed")
        st.markdown(
            create_selection_card(
                icons['hobbies'], 
                "Recreation & Hobbies", 
                hobbies
            ), 
            unsafe_allow_html=True
        )

    with col6:
        adulting = st.checkbox("Adulting & Chores", value=False, label_visibility="collapsed")
        st.markdown(
            create_selection_card(
                icons['adulting'], 
                "Adulting & Chores", 
                adulting
            ), 
            unsafe_allow_html=True
        )
    # Save them
    st.session_state.onboarding_data['life_aspects'] = {
        'work': work,
        'health': health,
        'relationships': relationships,
        'projects': projects,
        'hobbies': hobbies,
        'adulting': adulting
    }
    st.write("")  # Adds a small amount of vertical space
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
    # Then add a centered container for all your content
    container = st.container()


        # Email container - use a simpler HTML structure
    st.markdown("""
    <div style="margin: 20px; display: flex; align-items: center; padding: 15px; border-radius: 10px; background-color: white; margin-bottom: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); width: 1300px;">
        <div style="width: 40px; height: 40px; background-color: #4E9168; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 18px; font-weight: 500; margin-right: 15px; text-align: center; line-height: 40px;">J</div>
        <div style="flex-grow: 1; text-align: left; font-size: 16px;">johndoe@gmail.com</div>
        <div style="padding: 8px 15px; border: 1px solid #e0e0e0; border-radius: 5px; color: #666; font-size: 14px;">Personal ▼</div>
    </div>
    """, unsafe_allow_html=True)

    # Add calendar button with inline styling
    st.markdown("""
    <div style="display: flex; align-items: center; justify-content: center; color: #2196F3; font-size: 16px; font-weight: 500; cursor: pointer; padding: 10px; margin: 15px 0;">
        <span style="margin-right: 5px; font-size: 18px;">+</span> Add Calendar
    </div>
    """, unsafe_allow_html=True)
    # Continue button
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

# --- Close the .card-content and .card-container ---
st.markdown('</div>', unsafe_allow_html=True)  # close .card-content


# If needed, store onboarding completion in localStorage
if st.session_state.get('onboarding_complete', False):
    st.markdown("""
    <script>
        localStorage.setItem('onboarding_complete','true');
    </script>
    """, unsafe_allow_html=True)