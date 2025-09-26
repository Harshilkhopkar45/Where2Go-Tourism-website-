import streamlit as st
from where2go import load_footer

# Page configuration - MUST be first Streamlit command
st.set_page_config(
    page_title="Destinations",
    page_icon="🌍",
    layout="wide"
)

# Hide Streamlit branding (optional)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Page header
st.title("🌍 Destinations")
st.markdown("---")
st.markdown("<h3 style='text-align:center; margin-bottom: 10px;'>Empowering tourism experiences across 20+ cities.</h3>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    img.destinations-banner {
        display: block;
        margin-left: auto;
        margin-right: auto;
        max-height: 450px;   /* adjust height */
        width: 900px;         /* keep natural width */
        border-radius: 10px; /* optional rounded corners */
    }
    </style>
    <img src="https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Mumbai.jpg" 
         alt="Destinations Banner" class="destinations-banner">
    """,
    unsafe_allow_html=True
)

cities = [
    "Delhi", "Agra", "Jaipur", "Mumbai", "Varanasi",
    "Kolkata", "Amritsar", "Pune", "Ahmedabad", "Shimla",
    "Ayodhya", "Chennai", "Goa", "Indore", "Udaipur","Hyderabad",
]

def go_to_city_page(city):
    st.switch_page(f"pages/{city}.py")

@st.dialog("🌍 Choose Your City", width="large")
def city_modal():
    num_columns = 4
    button_cols = st.columns(num_columns)
    for idx, city in enumerate(cities):
        with button_cols[idx % num_columns]:
            if st.button(city, key=f"city_btn_{city}", type="primary" ,  use_container_width=True):
                go_to_city_page(city)

col1, col2, col3 = st.columns([3, 2, 3])
with col2:
    if st.button("Choose your city", key="choose_city_btn", use_container_width=True, type="primary"):
        st.session_state["show_modal"] = True

if st.session_state.get("show_modal", False):
    city_modal()



load_footer()
