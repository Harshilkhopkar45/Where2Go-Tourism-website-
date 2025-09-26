import streamlit as st
import random
import string
from where2go import load_footer

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align:center; font-size: 48px; font-weight: bold;'>Welcome to Indore – The Food Capital of Madhya Pradesh</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size: 20px;'>Explore Indore's top attractions, vibrant history, and colorful culture in this visual journey.</p>", unsafe_allow_html=True)

images = [
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Indore/Rajwada%20Palace.jpg", "Rajwada Palace", "Historic 7-story palace showcasing Maratha architectural grandeur."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Indore/Lal%20Bagh%20Palace.jpg", "Lal Bagh Palace", "Lavish Holkar-era palace famous for European-style interiors and royal gardens."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Indore/Shri%20Khajrana%20Ganesh%2C%20Indore.jpg", "Khajrana Ganpati Temple", "Beloved 18th-century temple where devotees seek blessings from Lord Ganesha."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Indore/Sarafa%20Bazaar.jpg", "Sarafa Market (Night Food Market)", "A bustling street food haven offering iconic Indori delicacies after sunset."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Indore/Bade%20Ganpati%20Temple.jpg", "Bada Ganpati", "Home to one of India’s largest Lord Ganesha idols, standing 25 feet tall."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Indore/Indore%20zoo.jpg", "Indore Zoo", "Madhya Pradesh’s largest zoo with tigers, lions, birds, and greenery for families."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Indore/Waterfall%20-%20Patalpani.jpg", "Patalpani Waterfall", "Scenic waterfall and picnic spot, especially spectacular during monsoon."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Indore/Kanch%20Mandir.jpg", "Kanch Mandir", "Stunning Jain temple entirely made of glass and mirrors with intricate artwork."),

]

FIXED_HEIGHT = 400
FIXED_WIDTH = 600  # Pixels

for i in range(0, 10, 2):
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

            
st.markdown("<h3 class='food-section' style='font-weight:bold; margin-top: 20px;'>🥘 Must-Try Foods in Indore</h3>", unsafe_allow_html=True)

food_names = [
    "Poha-Jalebi",
    "Bhutte Ka Kees",
    "Indori Namkeen",
    "Vada Pav",
    "Dal Bafla",
    "Sabudana Khichdi",
    "Gulab Jamun & Malpua (sweet)",
    "Immarti Jalebi (sweet)",
    "Rabdi & Ice Cream",
]


foods_line = " &nbsp; &#8226; &nbsp; ".join(food_names)

st.markdown(
    f"<div class='food-section'>{foods_line}</div>",
    unsafe_allow_html=True,
)

st.markdown("<h3 class='travel-section' style='font-weight:bold; margin-top: 40px;'>🚖 Best Ways to Travel Inside Indore</h3>", unsafe_allow_html=True)

indore_travel_text = """
<ul style='margin-top: 0; max-width: 700px; font-size: 18px;'>
<li>🛺 <strong>Auto Rickshaws:</strong> Ideal for short distances like Rajwada, Khajrana Ganpati, or Sarafa Bazaar. Fares usually require bargaining; air-conditioned autos are available on some routes.</li>
<li>🚖 <strong>Cabs / App-Based Cabs (Ola, Uber):</strong> Comfortable and air-conditioned. Suitable for longer distances, family trips, and night travel. Reliable pricing ensures hassle-free rides around the city.</li>
<li>🚌 <strong>City Buses:</strong> Widespread and economical, connecting major localities and outskirts. Can be crowded and slower but excellent for budget travelers who know the routes.</li>
</ul>
"""

indore_travel_tip = """
<div style='background-color: #fff9e6; padding: 15px; border-radius: 8px; max-width: 700px; font-size: 18px; margin-top: 20px;'>
🌟 <strong>Travel Tip:</strong><br>
Use auto rickshaws for quick, short trips within crowded markets.<br>
Cabs and app-based taxis are best for comfort, convenience, and longer distances.<br>
City buses offer budget-friendly travel but plan ahead for route and timing.
</div>
"""

st.markdown(indore_travel_text, unsafe_allow_html=True)
st.markdown(indore_travel_tip, unsafe_allow_html=True)

st.markdown("<h3 class='travel-section' style='font-weight:bold; margin-top: 40px;'>📅 Best Months to Visit Indore</h3>", unsafe_allow_html=True)

indore_months_text = """
<ul style='margin-top: 0; max-width: 700px; font-size: 18px;'>
<li>🍂 <strong>October – March (Best Weather & Festivals):</strong> Pleasant winter weather (10–25°C) ideal for sightseeing, shopping, and walking around the city. Festivals include Diwali (Oct/Nov), Holi (March), Ganesh Chaturthi, and local fairs. Moderate to high crowd during festivals with slightly higher hotel prices.</li>
<li>☀️ <strong>April – June (Summer, Less Crowded):</strong> Hot temperatures (35–45°C), fewer tourists, and cheaper stays. Best for budget travelers and short trips, with sightseeing mostly in mornings and evenings.</li>
<li>🌧️ <strong>July – September (Monsoon Beauty, Budget-Friendly):</strong> Lush greenery and rivers at their best, with occasional rain restricting outdoor activities. Low tourist footfall, affordable hotels, and quieter markets and heritage sites.</li>
</ul>
"""

travel_tip = """
<div style='background-color: #fff9e6; padding: 15px; border-radius: 8px; max-width: 700px; font-size: 18px; margin-top: 20px;'>
🌟 <strong>Travel Tip:</strong><br>
Visit during October to March for comfortable weather and vibrant festivals.<br>
Summer months are suitable for budget travelers willing to avoid peak crowds.<br>
Monsoon offers natural beauty and low costs but pack rain gear.
</div>
"""

st.markdown(indore_months_text, unsafe_allow_html=True)
st.markdown(travel_tip, unsafe_allow_html=True)

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
    if st.button("Get Redeem Code for Indore Hotels", key="redeem_code_indore_btn", type="primary", use_container_width=True):
        code = generate_redeem_code()
        st.success(f"Congratulations! Use this redeem code '{code}' to get an exclusive discount on your hotel booking.")
        tripadvisor_url = "https://www.tripadvisor.in/Hotels-g494941-Indore_Indore_District_Madhya_Pradesh-Hotels.html"
        st.markdown(f"[Click here to book hotels on Tripadvisor and apply your redeem code](<{tripadvisor_url}>)")

load_footer()