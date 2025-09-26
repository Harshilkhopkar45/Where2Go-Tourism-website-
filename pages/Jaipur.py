import streamlit as st
import random
import string
from where2go import load_footer

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align:center; font-size: 48px; font-weight: bold;'>Welcome to Jaipur - The Pink city</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size: 20px;'>Explore Jaipur's top attractions, vibrant history, and colorful culture in this visual journey.</p>", unsafe_allow_html=True)

images = [
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Jaipur/Amber%20Fort%2C%20Jaipur.jpg", "Amber Fort", "A majestic hilltop fort blending Rajput and Mughal architecture, known for its grand courtyards and Sheesh Mahal (Mirror Palace)"),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Jaipur.jpg", "Hawa Mahal", "The iconic “Palace of Winds,” with 953 windows built so royal ladies could watch street life unseen."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Jaipur/Jantar%20Mantar.jpg", "Jantar Mantar, Jaipur", "A UNESCO World Heritage site with the world’s largest stone sundial, showcasing India’s astronomical genius."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Jaipur/Jal%20Mahal.jpg", "Jal Mahal", "A dreamy palace floating in the middle of Man Sagar Lake, best admired at sunrise or sunset."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Jaipur/Moti%20Doongri%20Ganesh%20Temple.jpg", "Moti Doongri Ganesh Temple", "A beloved temple dedicated to Lord Ganesh, attracting devotees with its divine and festive atmosphere."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Jaipur/Birla%20Mandir%2C%20Jaipur.jpg", "Birla Mandir, Jaipur", "A stunning white marble temple glowing at night, dedicated to Lord Vishnu and Goddess Lakshmi."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Jaipur/Sisodia%20Rani%20ka%20Bagh.jpg", "Sisodia Rani ka Bagh", "A beautiful terraced garden with fountains and murals, built as a romantic retreat for a queen."),
]

FIXED_HEIGHT = 400
FIXED_WIDTH = 600  # Pixels

for i in range(0, 8, 2):
    cols = st.columns(2)
    for col, (img, heading, txt) in zip(cols, images[i:i+2]):
        with col:
            st.markdown(
                f"""
                <div class='image-container' style='text-align: center;'>
                    <img src='{img}' style='height:{FIXED_HEIGHT}px; width:{FIXED_WIDTH}px; display:block; margin-left:auto; margin-right:auto;'/>
                    <h3 style='font-weight: bold; margin-top: 10px;'>{heading}</h3>
                    <p style='margin-top: 5px;'>{txt}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            
st.markdown("<h3 class='food-section' style='font-weight:bold; margin-top: 20px;'>🥘 Must-Try Foods in Jaipur</h3>", unsafe_allow_html=True)

food_names = [
    "Dal Baati Churma",
    "Pyaaz Kachori",
    "Mawa Kachori",
    "Rajasthani Thali",
    "Ghevar (sweet)",
    "Malpua (sweet)",
]

foods_line = " &nbsp; &#8226; &nbsp; ".join(food_names)

st.markdown(
    f"<div class='food-section'>{foods_line}</div>",
    unsafe_allow_html=True,
)

st.markdown("<h3 class='tourist-section' style='font-weight:bold; margin-top: 40px;'>🚖 Best Way for Tourists in Jaipur</h3>", unsafe_allow_html=True)

tourist_text = """
<ul style='margin-top: 0; max-width: 700px; font-size: 18px;'>
<li><strong>For short city sightseeing:</strong> Autos or E-rickshaws are convenient, affordable and let you explore Jaipur’s key landmarks and local markets easily.</li>
<li><strong>For comfortable day trips & family:</strong> Ola/Uber cabs offer air-conditioned rides, flexible pickup/drop and extra comfort for families or larger groups.</li>
<li><strong>For budget solo travel:</strong> Buses combined with autos provide the best value, connecting main attractions at very low fares and allowing independent travel.</li>
</ul>
"""

st.markdown(tourist_text, unsafe_allow_html=True)
st.markdown("<h3 class='visit-section' style='font-weight:bold; margin-top: 40px;'>🗓️ Best Months to Visit Jaipur</h3>", unsafe_allow_html=True)

best_month_text = """
<ul style='max-width: 700px; margin-left: 20px; margin-right: auto; font-size: 18px;'>
<li><strong>Best Balance:</strong> <span style='color: #138808;'>March–April &#10004;</span> — The best mix of affordable hotels, thinner crowds, and festive vibes (Holi, Gangaur). Comfortable weather is ideal for sightseeing.</li>
<li><strong>Magical Festive Atmosphere:</strong> <span style='color: #138808;'>October–November &#10004;</span> — Diwali lights up Jaipur and the weather is pleasant. Expect some crowds and higher prices in popular areas.</li>
<li><strong>Premium Experience:</strong><span style='color: #138808;'> December–February &#10004;</span> —The most popular time for perfect weather and major festivals (Jaipur Literature Festival, Makar Sankranti), but the city sees peak tourism and higher costs.</li>
</ul>
"""

st.markdown(best_month_text, unsafe_allow_html=True)

# Inject CSS to style the button with primary color
st.markdown("""
<style>
    /* Make success message full width with readable line length */
    div[role="alert"] > div {
        max-width: 650px;
        white-space: normal !important;
        word-wrap: break-word !important;
        line-height: 1.5;
        font-size: 16px;
    }
    /* Make markdown links full width */
    div.markdown-text-container {
        max-width: 650px;
        font-size: 16px;
        word-wrap: break-word;
    }
</style>
""", unsafe_allow_html=True)


def generate_redeem_code(length=8):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

col1, col2, col3 = st.columns([3, 2, 3])
with col2:
    if st.button("Get Redeem Code for Jaipur Hotels", key="redeem_code_jaipur_btn", type="primary", use_container_width=True):
        code = generate_redeem_code()
        st.success(f"Congratulations! Use this code '{code}' for exclusive discounts on Jaipur hotels.")
        tripadvisor_url = "https://www.tripadvisor.in/Hotels-g304555-Jaipur_Jaipur_District_Rajasthan-Hotels.html"
        st.markdown(f"[Book Jaipur hotels here](<{tripadvisor_url}>)")

load_footer()