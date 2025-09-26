import streamlit as st
import streamlit.components.v1 as components

# Make Streamlit full-width
st.set_page_config(layout="wide")


# Hide Streamlit default header/footer
st.markdown("""
    <style>
    /* Full-screen video container */
    .video-container {
        position: relative;
        width: 100vw;   /* full viewport width */
        height: 100vh;  /* full viewport height */
        margin-left: -50vw; /* shift left */
        left: 50%;        /* recenter */
        overflow: hidden;
    }
    .video-container video {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    /* Logo top-left inside video */
    .overlay-logo {
        position: absolute;
        top: 40px;
        left: 50px;
        width: 180px;
        z-index: 2;
    }
    /* Centered tagline */
    .overlay-content {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        color: white;
        z-index: 2;
    }
    .overlay-content h1 {
        font-size: 3em;
        font-weight: bold;
        text-shadow: 2px 2px 8px #000;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Video + overlays grouped in one hero container
video_url = "https://raw.githubusercontent.com/Harshilkhopkar45/Where2Go-Tourism-website-/main/video/Tourism%20in%20%20India.mp4"
logo_url = "https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Where2Go%20logo.png"

st.markdown(f"""
<div class="video-container">
    <video autoplay muted loop playsinline>
        <source src="{video_url}" type="video/mp4">
    </video>
    <img src="{logo_url}" alt="Where2Go Logo" class="overlay-logo">
    <div class="overlay-content">
        <h1>India's best experiences curated just for you</h1>
    </div>
</div>
""", unsafe_allow_html=True)

#Content below Video
st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
# Layout with columns (text left, image right)
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown(
    """
    <div style="height: 500px; display: flex; flex-direction: column; justify-content: text-align: left; padding-left: 40px;">
        <h1 style='font-size: 40px; color: #333; margin-bottom: 20px;'>Why Choose Where2Go?</h1>
        <h3 style='font-size: 24px; line-height: 1.8; color: #555;'>
            Only the <b>finest destinations</b>, curated for travelers.<br>
            <b>Best prices</b> with last-minute availability.<br>
            Experiences from culture to adventure, for every flavor.<br>
            100% satisfaction guarantee.<br><br>
            Flexible trip planning made simple.<br>
            Safe, secure, and trusted by thousands.<br>
            Your journey begins with just one click.<br>
        </h3>
    </div>
    """,
    unsafe_allow_html=True
)

with col2:
    st.image(
        "https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Frontend%20Img1.jpg",
        width=800
    )




st.markdown("<div style='height: 1px;'></div>", unsafe_allow_html=True)

st.markdown("## 🌏 Explore India's Top Destinations")
st.markdown(
    """
    <style>
    .image-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 20px;
        margin-bottom: 10px;
    }
    .image-grid img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 10px;
    }
    </style>
    <div class="image-grid">
        <img src="https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Delhi.jpg" alt="Delhi"/>
        <img src="https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Agra.jpg" alt="Agra"/>
        <img src="https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Jaipur.jpg" alt="Jaipur"/>
        <img src="https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Mumbai.jpg" alt="Mumbai"/>
        <img src="https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Varanasi.jpg" alt="Varanasi"/>
    </div>
    """,
    unsafe_allow_html=True,
)

cities = ["Delhi", "Agra", "Jaipur", "Mumbai", "Varanasi"]
cols = st.columns(len(cities))

for city, col in zip(cities, cols):
    with col:
        # Center the button inside the column using markdown div with style
        st.markdown("<div style='display:flex; justify-content:center;'>", unsafe_allow_html=True)
        if st.button(city, key=f"btn_{city}", type="primary",  use_container_width=True):
            st.switch_page(f"pages/{city}.py")
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div style='height: 3px;'></div>", unsafe_allow_html=True)
# Centered single button
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
            if st.button(city, key=f"city_btn_{city}", type="primary", use_container_width=True):
                go_to_city_page(city)


col1, col2, col3 = st.columns([3, 2, 3])
with col2:
    if st.button("Choose your city", key="choose_city_btn", use_container_width=True, type="primary"):
        st.session_state["show_modal"] = True

if st.session_state.get("show_modal", False):
    city_modal()

#footer code
def load_footer():
    st.markdown(
        """
        <style>
        .footer {
            background-color: #333333; /* Charcoal Gray */
            color: white;
            text-align: center;
            padding: 30px 10px;
            margin-top: 60px;
            border-radius: 10px;
        }
        .footer-top {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
            margin-bottom: 20px;
        }
        .footer-top img {
            height: 120px; /* Bigger logo */
        }
        .footer-top span {
            font-size: 32px; /* Bigger title text */
            font-weight: bold;
        }
        .footer-bottom {
            font-size: 18px; /* Bigger footer text */
            line-height: 2;
        }
        </style>

        <div class="footer">
            <div class="footer-top">
                <img src="https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Where2Go%20logo.png" alt="Where2Go Logo">
                <span>Where2Go</span>
            </div>
            <div class="footer-bottom">
                <p>© 2025 Where2Go Tourism. All Rights Reserved.</p>
                <p>Made with ❤️ for travelers exploring incredible India.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


    # 🔻 Your code unchanged below 🔻
    st.markdown("### 🧭 Quick Navigation")
    # Create columns for buttons
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button(
            "🏠 **Home**",
            key="footer_home_btn",
            use_container_width=True,
            type="primary"
            
        ):
            st.switch_page("main.py")
    
    with col2:
        if st.button(
            "ℹ️ **About Us**",
            key="footer_about_btn", 
            use_container_width=True,
            type="primary"
        ):
            st.switch_page("pages/about.py")
    
    with col3:
        if st.button(
            "🌍 **Destinations**",
            key="footer_dest_btn",
            use_container_width=True,
            type="primary"
        ):
            st.switch_page("pages/destinations.py")
    
    with col4:
        if st.button(
            "📞 **Contact**",
            key="footer_contact_btn",
            use_container_width=True,
            type="primary"
        ):
            st.switch_page("pages/contact.py")
            
load_footer()








