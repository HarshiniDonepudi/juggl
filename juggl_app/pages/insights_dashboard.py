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

custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Albert+Sans:ital,wght@0,100..900;1,100..900&display=swap');
/* Hide default Streamlit elements */
#MainMenu, footer, header {
    visibility: hidden;
}
body {
    margin: 0;
    padding: 0;
    font-family: 'Albert Sans', sans-serif;
    background: var(--Gray---10, #EEF1F1);
    letter-spacing: -0.01em;
}
/* Container for everything */
.block-container {
    margin-top:-30px;
    margin-left:120px;
    max-width: 1370px;
    padding: 20px;
    background: var(--Gray---10, #EEF1F1);
}

/* Sidebar */
.sidebar {
    position: fixed;
    left: 0;
    top: 0;
    width: 120px;
    height: 100vh;
    background: #ffffff;
    box-shadow: 2px 0 8px rgba(0,0,0,0.05);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.sidebar .top-links {
    margin-top: 40px;
}
.sidebar-logo {
    font-size: 28px;
    font-weight: 700;
    padding: 20px 20px 0;
    color: #333;
}
.sidebar-menu {
    list-style: none;
    padding: 0;
    margin: 20px 0;
}
.sidebar-menu li {
    padding: 10px 20px;
    font-size: 15px;
    color: #666;
    cursor: pointer;
}
.sidebar-menu li.active {
    color: #277DC6;
    font-weight: 600;
}
.sidebar-menu li:hover {
    background: #f5f5f5;
}
.sidebar-bottom {
    margin-bottom: 20px;
    padding: 0 20px;
    font-size: 13px;
    color: #999;
}

/* Main content */
.main-content {

    padding: 30px;
}
.header-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}
.header-bar h1 {
    font-size: 1.5rem;
    font-weight: 600;
    margin: 0;
}
.cards-row {
    display: flex;
    gap: 20px;
}
.card {
    border-radius: 16px;
    background: linear-gradient(180deg, #FFF 0%, rgba(255, 255, 255, 0.25) 100%);
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    padding: 20px;
    flex: 1;
    position: relative;
}
.card h2 {
    margin-top: 0;
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 10px;
}
.big-metric {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 5px;
}
.sub-metric {
    color: #999;
    font-size: 0.85rem;
    margin-bottom: 10px;
}
.arrow-icon {
    position: absolute;
    top: 10px;
    right: 10px;
    color: #999;
    cursor: pointer;
}
.arrow-icon:hover {
    color: #666;
}
.big-donut {
    text-align: center;
}
.big-donut .metric-value {
    font-size: 2rem;
    font-weight: 600;
}
.big-donut .change-text {
    font-size: 0.85rem;
    margin-bottom: 10px;
    color: #4caf50;
}
.small-card h2 {
    font-size: 0.9rem;
}
.small-card .description {
    font-size: 0.8rem;
    color: #666;
}

/* The search box and question pills */
.search-box {
    width: 100%;
    border: 1px solid #277DC6;
    border-radius: 20px;
    padding: 10px 15px;
    font-size: 0.9rem;
    outline: none;
    margin-bottom: 15px;
}
.question-pills {
    display: flex;
    gap: 10px;
    overflow-x: auto;
}
.question-pill {
    flex-shrink: 0;
    background: linear-gradient(180deg, #FFF 0%, rgba(255, 255, 255, 0.25) 100%);
    padding: 8px 15px;
    border-radius: 20px;
    font-size: 0.85rem;
    color: #277DC6;
    cursor: pointer;
    white-space: nowrap;
}
.question-pill:hover {
    background: #e0e0e0;
    color: #333;
}

/* Responsive tweaks */
@media (max-width: 768px) {
    .cards-row {
        flex-direction: column;
    }
    .main-content {
        margin-left: 0;
    }
    .sidebar {
        position: static;
        width: 100%;
        height: auto;
        box-shadow: none;
    }
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ------------- SIDEBAR -------------
st.markdown("""
<div class="sidebar">
    <div>
        <div class="sidebar-logo" style="margin-top:60px">
<svg width="60" height="40" viewBox="0 0 118 48" fill="none" xmlns="http://www.w3.org/2000/svg">
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
        <ul class="sidebar-menu top-links" style="margin-top:5px">
            <li>Today</li>
            <li class="active">Insights</li>
            <li>Habits</li>
            <li>Calendar</li>
        </ul>
    </div>
    <div class="sidebar-bottom">
        Settings
    </div>
</div>
""", unsafe_allow_html=True)

# ------------- MAIN CONTENT -------------
st.markdown("<div class='main-content'>", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-bar" style="margin-bottom: -25px;">
    <h1>Insights</h1>
</div>
""", unsafe_allow_html=True)
# Create the burnout donut chart
burnout_fig = go.Figure(data=[go.Pie(
    labels=["Risk", "Safe"],
    values=[62, 38],  # 62% risk, 38% safe
    hole=0.6,
    textinfo="none",
    marker=dict(colors=["#f77f51", "#ddd"])
)])
burnout_fig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0),
    height=200, width=200,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

# Create the work-life balance donut chart
worklife_fig = go.Figure(data=[go.Pie(
    labels=["Work", "Life"],
    values=[3, 4],  # Ratio 3:4
    hole=0.6,
    textinfo="none",
    marker=dict(colors=["#ffcc80", "#90caf9"])
)])
worklife_fig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0),
    height=200, width=200,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

# Create two main columns for the two cards
cols = st.columns(2)

with cols[0]:
    # Burnout Risk Card

    st.markdown("<div class='arrow-icon'>↗</div>", unsafe_allow_html=True)
    st.markdown("<h5>Burnout Risk</h5>", unsafe_allow_html=True)
    
    # Nested columns: chart on left, text content on right
    inner_cols = st.columns([1, 3])
    with inner_cols[0]:
        st.plotly_chart(burnout_fig, use_container_width=True)
    with inner_cols[1]:
        st.markdown("""
            <p class="sub-metric">Your burnout risk dropped by 9.7% this week.</p>
            <p class="big-metric">62% <span style="font-size:0.7rem;">This Week</span></p>
            <p class="sub-metric">Change: -8.5% from Last Week (71.5%)</p>
            <p class="sub-metric">Your burnout risk dropped by 8.5% this week. By scheduling consistent “Decompress” blocks and focusing on personal/wellness activities, you’ve created a healthier buffer around your demanding class and work schedule.</p>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with cols[1]:
    # Work & Life Balance Card

    st.markdown("<div class='arrow-icon'>↗</div>", unsafe_allow_html=True)
    st.markdown("<h5>Work & Life Balance</h5>", unsafe_allow_html=True)
    
    # Nested columns: chart on left, text content on right
    inner_cols = st.columns([1, 3])
    with inner_cols[0]:
        st.plotly_chart(worklife_fig, use_container_width=True)
    with inner_cols[1]:
        st.markdown("""
            <p class="sub-metric">
                Work: 45 H this week (down from 50 H last week) <span style="color:#4caf50;">-9.7%</span><br>
                Life: 70 H this week (up from 65 H last week) <span style="color:#4caf50;">-9.7%</span>
            </p>
            <p class="big-metric">3 : 4</p>
            <p class="sub-metric">Work : Life</p>
            <p class="sub-metric">You carved out more time for personal pursuits, weekend breaks, and occasional mid‐day breathers, improving your overall ratio.</p>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Row for the 3 small metrics
st.markdown("""
<div class="cards-row" style="margin-top:-15px; margin-bottom:20px;">
    <div class="card small-card" style="position:relative;">
        <div class="arrow-icon">↗</div>
            <div style="display:flex; align-items:center; margin-bottom:8px;">
      <!-- Example lightning bolt SVG icon -->
      <svg width="20" height="20" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M14.7943 0.600471C15.3987 -0.200157 16.6013 -0.200157 17.2058 0.600471L19.7327 3.94749C20.4842 4.94285 19.7742 6.36862 18.527 6.36862H13.473C12.2258 6.36862 11.5158 4.94285 12.2673 3.94748L14.7943 0.600471Z" fill="url(#paint0_linear_550_1222)"/>
        <path d="M17.2057 31.3995C16.6013 32.2002 15.3987 32.2002 14.7942 31.3995L12.2673 28.0525C11.5158 27.0572 12.2258 25.6314 13.473 25.6314L18.527 25.6314C19.7742 25.6314 20.4842 27.0572 19.7327 28.0525L17.2057 31.3995Z" fill="url(#paint1_linear_550_1222)"/>
        <path d="M0.60047 17.2057C-0.200157 16.6013 -0.200157 15.3987 0.600471 14.7942L3.94749 12.2673C4.94285 11.5158 6.36862 12.2258 6.36862 13.473L6.36862 18.527C6.36862 19.7742 4.94285 20.4842 3.94748 19.7327L0.60047 17.2057Z" fill="url(#paint2_linear_550_1222)"/>
        <path d="M31.3995 14.7943C32.2002 15.3987 32.2002 16.6013 31.3995 17.2058L28.0525 19.7327C27.0572 20.4842 25.6314 19.7742 25.6314 18.527L25.6314 13.473C25.6314 12.2258 27.0572 11.5158 28.0525 12.2673L31.3995 14.7943Z" fill="url(#paint3_linear_550_1222)"/>
        <path d="M4.25832 5.96343C4.11962 4.96987 4.96995 4.11954 5.96351 4.25825L10.117 4.8381C11.3523 5.01054 11.8584 6.52079 10.9765 7.40269L7.40276 10.9764C6.52087 11.8583 5.01061 11.3522 4.83817 10.117L4.25832 5.96343Z" fill="url(#paint4_linear_550_1222)"/>
        <path d="M27.7418 26.0365C27.8805 27.0301 27.0302 27.8804 26.0366 27.7417L21.8831 27.1618C20.6479 26.9894 20.1418 25.4791 21.0237 24.5972L24.5974 21.0236C25.4793 20.1417 26.9895 20.6478 27.162 21.883L27.7418 26.0365Z" fill="url(#paint5_linear_550_1222)"/>
        <path d="M5.96355 27.7417C4.97 27.8804 4.11967 27.03 4.25837 26.0365L4.83822 21.883C5.01066 20.6477 6.52091 20.1416 7.40281 21.0235L10.9765 24.5972C11.8584 25.4791 11.3523 26.9894 10.1171 27.1618L5.96355 27.7417Z" fill="url(#paint6_linear_550_1222)"/>
        <path d="M26.0364 4.25832C27.03 4.11962 27.8803 4.96995 27.7416 5.96351L27.1618 10.117C26.9893 11.3523 25.4791 11.8584 24.5972 10.9765L21.0235 7.40276C20.1416 6.52087 20.6477 5.01061 21.8829 4.83817L26.0364 4.25832Z" fill="url(#paint7_linear_550_1222)"/>
        <path d="M28.0864 16C28.0864 22.6752 22.6752 28.0864 16 28.0864C9.32486 28.0864 3.91357 22.6752 3.91357 16C3.91357 9.32486 9.32486 3.91357 16 3.91357C22.6752 3.91357 28.0864 9.32486 28.0864 16Z" fill="url(#paint8_linear_550_1222)"/>
        <path d="M19.5946 9.95679H13.603C13.453 9.95679 13.3171 10.0456 13.257 10.1831L10.9436 15.4709C10.8344 15.7205 11.0172 16 11.2896 16H14.1754C14.4269 16 14.6082 16.2412 14.5382 16.4827L13.028 21.6998C12.9182 22.0791 13.3906 22.3512 13.6636 22.066L20.4872 14.9393C20.7172 14.6991 20.5469 14.3004 20.2144 14.3004H17.8819C17.5718 14.3004 17.3939 13.9475 17.5781 13.6981L19.8984 10.559C20.0827 10.3097 19.9047 9.95679 19.5946 9.95679Z" fill="url(#paint9_linear_550_1222)"/>
        <defs>
        <linearGradient id="paint0_linear_550_1222" x1="16" y1="-0.996551" x2="16" y2="8.82368" gradientUnits="userSpaceOnUse">
        <stop stop-color="#F3A07F"/>
        <stop offset="1" stop-color="#ECC736"/>
        </linearGradient>
        <linearGradient id="paint1_linear_550_1222" x1="16" y1="32.9966" x2="16" y2="23.1763" gradientUnits="userSpaceOnUse">
        <stop stop-color="#F3A07F"/>
        <stop offset="1" stop-color="#ECC736"/>
        </linearGradient>
        <linearGradient id="paint2_linear_550_1222" x1="-0.996551" y1="16" x2="8.82368" y2="16" gradientUnits="userSpaceOnUse">
        <stop stop-color="#F3A07F"/>
        <stop offset="1" stop-color="#ECC736"/>
        </linearGradient>
        <linearGradient id="paint3_linear_550_1222" x1="32.9966" y1="16" x2="23.1763" y2="16" gradientUnits="userSpaceOnUse">
        <stop stop-color="#F3A07F"/>
        <stop offset="1" stop-color="#ECC736"/>
        </linearGradient>
        <linearGradient id="paint4_linear_550_1222" x1="3.98165" y1="3.98157" x2="10.9256" y2="10.9255" gradientUnits="userSpaceOnUse">
        <stop stop-color="#F3A07F"/>
        <stop offset="1" stop-color="#ECC736"/>
        </linearGradient>
        <linearGradient id="paint5_linear_550_1222" x1="28.0185" y1="28.0184" x2="21.0745" y2="21.0744" gradientUnits="userSpaceOnUse">
        <stop stop-color="#F3A07F"/>
        <stop offset="1" stop-color="#ECC736"/>
        </linearGradient>
        <linearGradient id="paint6_linear_550_1222" x1="3.9817" y1="28.0184" x2="10.9256" y2="21.0744" gradientUnits="userSpaceOnUse">
        <stop stop-color="#F3A07F"/>
        <stop offset="1" stop-color="#ECC736"/>
        </linearGradient>
        <linearGradient id="paint7_linear_550_1222" x1="28.0183" y1="3.98165" x2="21.0744" y2="10.9256" gradientUnits="userSpaceOnUse">
        <stop stop-color="#F3A07F"/>
        <stop offset="1" stop-color="#ECC736"/>
        </linearGradient>
        <linearGradient id="paint8_linear_550_1222" x1="16" y1="3.91357" x2="16" y2="28.0864" gradientUnits="userSpaceOnUse">
        <stop stop-color="#ECC736"/>
        <stop offset="1" stop-color="#FEF0CF"/>
        </linearGradient>
        <linearGradient id="paint9_linear_550_1222" x1="15.9055" y1="9.95679" x2="15.9055" y2="23.1763" gradientUnits="userSpaceOnUse">
        <stop stop-color="white"/>
        <stop offset="1" stop-color="#FEF0CF"/>
        </linearGradient>
        </defs>
        </svg>
      <h2 style="margin:5px;">Energy</h2>
    </div>
        <p class="description">
            Your daily energy has risen by approximately 12% this week<br><br>
            <b>Today:</b> 3.5 / 5<br>
            <b>Last Week:</b> 3.1 / 5<br><br>
            Regular yoga, gym sessions, and mental wellness breaks seem to be fueling higher energy levels throughout the day.
        </p>
    </div>
    <div class="card small-card" style="position:relative;">
        <div class="arrow-icon">↗</div>
         <div style="display:flex; align-items:center; margin-bottom:8px;">
      <!-- Example lightning bolt SVG icon -->
        <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="22.4762" cy="12.5238" r="9.52381" fill="url(#paint0_linear_550_1225)"/>
        <path fill-rule="evenodd" clip-rule="evenodd" d="M22.4762 13.1191C20.175 13.1191 18.3095 14.9845 18.3095 17.2857C18.3095 17.6145 18.043 17.881 17.7143 17.881C17.3855 17.881 17.119 17.6145 17.119 17.2857C17.119 14.3271 19.5175 11.9286 22.4762 11.9286C25.4348 11.9286 27.8333 14.3271 27.8333 17.2857C27.8333 17.6145 27.5668 17.881 27.2381 17.881C26.9093 17.881 26.6428 17.6145 26.6428 17.2857C26.6428 14.9845 24.7773 13.1191 22.4762 13.1191Z" fill="white"/>
        <circle cx="9.52381" cy="20.1428" r="9.52381" fill="url(#paint1_linear_550_1225)"/>
        <path fill-rule="evenodd" clip-rule="evenodd" d="M9.52384 24.3095C11.825 24.3095 13.6905 22.444 13.6905 20.1429C13.6905 19.8141 13.957 19.5476 14.2857 19.5476C14.6145 19.5476 14.881 19.8141 14.881 20.1429C14.881 23.1015 12.4825 25.5 9.52384 25.5C6.56517 25.5 4.1667 23.1015 4.1667 20.1429C4.1667 19.8141 4.43319 19.5476 4.76193 19.5476C5.09067 19.5476 5.35717 19.8141 5.35717 20.1429C5.35717 22.444 7.22265 24.3095 9.52384 24.3095Z" fill="white"/>
        <defs>
        <linearGradient id="paint0_linear_550_1225" x1="22.4762" y1="3" x2="22.4762" y2="22.0476" gradientUnits="userSpaceOnUse">
        <stop stop-color="#F3A07F"/>
        <stop offset="1" stop-color="#E97432"/>
        </linearGradient>
        <linearGradient id="paint1_linear_550_1225" x1="9.52381" y1="29.6666" x2="9.52381" y2="10.619" gradientUnits="userSpaceOnUse">
        <stop stop-color="#48CDEA"/>
        <stop offset="1" stop-color="#BEEDFC"/>
        </linearGradient>
        </defs>
        </svg>
        <h2 style="margin:5px;">Optimism</h2>
      </div>
        <p class="description">
            Your optimism improved by about 9% this week.<br><br>
            <b>Today:</b> 4.1 / 5<br>
            <b>Last Week:</b> 3.8 / 5<br><br>
            With fewer back‐to‐back obligations and a slight drop in overall work hours, you’re experiencing a more positive outlook.
        </p>
    </div>
    <div class="card small-card" style="position:relative;">
        <div class="arrow-icon">↗</div>
         <div style="display:flex; align-items:center; margin-bottom:8px;">
      <!-- Example lightning bolt SVG icon -->
        <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path fill-rule="evenodd" clip-rule="evenodd" d="M4.86814 25.4762C5.28892 25.4762 5.62713 25.1339 5.65766 24.7142C6.04772 19.3522 10.5215 15.1233 15.983 15.1233C21.4445 15.1233 25.9183 19.3522 26.3083 24.7142C26.3388 25.1339 26.677 25.4762 27.0978 25.4762H31.2211C31.6419 25.4762 31.9849 25.1345 31.9652 24.7142C31.5674 16.2315 24.5641 9.4762 15.983 9.4762C7.40188 9.4762 0.398547 16.2315 0.000808973 24.7142C-0.0188993 25.1345 0.324099 25.4762 0.744887 25.4762H4.86814Z" fill="url(#paint0_linear_550_1223)"/>
        <path d="M20.5545 25.4762C20.5545 28.0009 18.5078 30.0476 15.983 30.0476C13.4583 30.0476 11.4116 28.0009 11.4116 25.4762C11.4116 22.9515 13.4583 20.9048 15.983 20.9048C18.5078 20.9048 20.5545 22.9515 20.5545 25.4762Z" fill="url(#paint1_linear_550_1223)"/>
        <path fill-rule="evenodd" clip-rule="evenodd" d="M29.1833 16.4319L24.6777 19.8539C22.833 17.0069 19.6279 15.1233 15.983 15.1233C10.5215 15.1233 6.04771 19.3522 5.65765 24.7142C5.62712 25.1339 5.28891 25.4762 4.86813 25.4762H0.744886C0.324098 25.4762 -0.0188993 25.1345 0.000808971 24.7142C0.398546 16.2315 7.40186 9.4762 15.983 9.4762C21.4631 9.4762 26.2997 12.2313 29.1833 16.4319Z" fill="url(#paint2_linear_550_1223)"/>
        <path fill-rule="evenodd" clip-rule="evenodd" d="M26.3127 18.17C26.5608 18.5099 26.4863 18.9865 26.1464 19.2345L12.0512 29.5202C11.7113 29.7683 11.2346 29.6938 10.9866 29.3539C10.7385 29.014 10.813 28.5374 11.1529 28.2893L25.2482 18.0036C25.5881 17.7556 26.0647 17.83 26.3127 18.17Z" fill="url(#paint3_linear_550_1223)"/>
        <path d="M17.5068 25.4762C17.5068 26.3178 16.8246 27 15.983 27C15.1415 27 14.4592 26.3178 14.4592 25.4762C14.4592 24.6346 15.1415 23.9524 15.983 23.9524C16.8246 23.9524 17.5068 24.6346 17.5068 25.4762Z" fill="url(#paint4_linear_550_1223)"/>
        <rect y="5.4762" width="6.47619" height="1.52381" rx="0.761905" fill="url(#paint5_linear_550_1223)"/>
        <path fill-rule="evenodd" clip-rule="evenodd" d="M28.0001 8.71429C28.0001 9.13507 28.3412 9.47619 28.762 9.47619C29.1828 9.47619 29.5239 9.13507 29.5239 8.71429V7H31.2382C31.659 7 32.0001 6.65888 32.0001 6.2381C32.0001 5.81731 31.659 5.47619 31.2382 5.47619H29.5239V3.76191C29.5239 3.34112 29.1828 3 28.762 3C28.3412 3 28.0001 3.34112 28.0001 3.7619V5.47619H26.2858C25.865 5.47619 25.5239 5.81731 25.5239 6.2381C25.5239 6.65888 25.865 7 26.2858 7H28.0001V8.71429Z" fill="url(#paint6_linear_550_1223)"/>
        <defs>
        <linearGradient id="paint0_linear_550_1223" x1="31.966" y1="19.7619" x2="24.3542" y2="21.4727" gradientUnits="userSpaceOnUse">
        <stop stop-color="#EEF1F1"/>
        <stop offset="1" stop-color="#C5CCCA"/>
        </linearGradient>
        <linearGradient id="paint1_linear_550_1223" x1="15.983" y1="20.9048" x2="15.983" y2="30.0476" gradientUnits="userSpaceOnUse">
        <stop stop-color="#66BA86"/>
        <stop offset="1" stop-color="#8CE1AC"/>
        </linearGradient>
        <linearGradient id="paint2_linear_550_1223" x1="6.07822" y1="15.5714" x2="23.602" y2="15.9524" gradientUnits="userSpaceOnUse">
        <stop stop-color="#8CE1AC"/>
        <stop offset="1" stop-color="#4E9168"/>
        </linearGradient>
        <linearGradient id="paint3_linear_550_1223" x1="16.9354" y1="27.381" x2="15.2211" y2="24.5238" gradientUnits="userSpaceOnUse">
        <stop stop-color="#887EC4"/>
        <stop offset="1" stop-color="#ADA7D7"/>
        </linearGradient>
        <linearGradient id="paint4_linear_550_1223" x1="15.983" y1="23.9524" x2="15.983" y2="27" gradientUnits="userSpaceOnUse">
        <stop stop-color="#EEF1F1"/>
        <stop offset="1" stop-color="#C5CCCA"/>
        </linearGradient>
        <linearGradient id="paint5_linear_550_1223" x1="3.42857" y1="5.66667" x2="3.42857" y2="7.19048" gradientUnits="userSpaceOnUse">
        <stop stop-color="#887EC4"/>
        <stop offset="1" stop-color="#ADA7D7"/>
        </linearGradient>
        <linearGradient id="paint6_linear_550_1223" x1="27.2382" y1="6.42857" x2="30.0954" y2="6.42857" gradientUnits="userSpaceOnUse">
        <stop stop-color="#887EC4"/>
        <stop offset="1" stop-color="#ADA7D7"/>
        </linearGradient>
        </defs>
        </svg>
        <h2 style="margin:5px;">Productivity</h2>
      </div>
        <p class="description">
            Your productivity has climbed 7% this week.<br><br>
            <b>Today:</b> 3.4 / 5<br>
            <b>Last Week:</b> 3.2 / 5<br><br>
            Concentrated “deep‐work” pockets (fewer split by meetings) are helping you accomplish tasks more efficiently, despite spending slightly less total time “on the clock.”
        </p>
    </div>
        <div class="card small-card" style="position:relative;">
        <div class="arrow-icon">↗</div>
   <div style="display:flex; align-items:center; margin-bottom:8px;">
      <!-- Example lightning bolt SVG icon -->
    <svg width="30" height="30" viewBox="0 0 68 80" fill="none" xmlns="http://www.w3.org/2000/svg">
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
        <h2 style="margin:5px;">Focus Time</h2>
        </div>
        <p class="description">
            Focus time saw a modest increase of ~10%<br><br>
            <b>Today:</b> ~2.0 hrs of uninterrupted work<br>
            <b>Last Week:</b>  ~1.8 hrs<br><br>
            By batching your classes and meetings, you freed up longer stretches for design, planning, and creative tasks.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# Search box + question pills
st.markdown("""
<input class="search-box" type="text" placeholder="How much do meetings impact my mood?" />

<div class="question-pills">
    <div class="question-pill">How does movement impact my optimism?</div>
    <div class="question-pill">How does sleep impact my optimism?</div>
    <div class="question-pill">How does movement impact my productivity?</div>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # Close main-content



