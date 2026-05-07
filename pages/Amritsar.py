import streamlit as st
import random
import string
from where2go import load_footer

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align:center; font-size: 48px; font-weight: bold;'> Welcome to Amritsar – Home of the Golden Temple</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size: 20px;'>Explore Amritsar's top attractions, vibrant history, and colorful culture in this visual journey.</p>", unsafe_allow_html=True)

images = [
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Amritsar/Golden%20Temple%20.jpg", "Golden Temple", "The iconic Sikh shrine with stunning gold-plated architecture and a serene holy pond."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Amritsar/Jallianwala%20Bagh%20.jpg", "Jallianwala Bagh", "Historic memorial site commemorating the 1919 massacre, surrounded by preserved walls and monuments."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Amritsar/The%20Partition%20Museum%20%2C%20Amritsar.jpg", "Partition Museum", "Museum detailing the history of India’s partition with artifacts, stories, and photographs."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Amritsar/Wagah%20Border.jpg", "Wagah Border", "Witness the famous India-Pakistan border flag-lowering ceremony with military pageantry."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Amritsar/Gobindgarh%20Fort.jpg", "Gobindgarh Fort","A restored 18th-century fort offering cultural shows, museums, and light & sound experiences."),

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

            
st.markdown("<h3 class='food-section' style='font-weight:bold; margin-top: 20px;'>🥘 Must-Try Foods in Amritsar</h3>", unsafe_allow_html=True)

food_names = [
    "Amritsari Kulcha",
    "Chole Bhature",
    "Paneer Tikka / Tandoori Items",
    "Aloo Chaat / Papdi Chaat",
    "Dal Makhani",
    "Butter Chicken / Chicken Amritsari",
    "Lassi (sweet)",
    "Pinni & Laddu(Sweet)",
    "Gajar ka Halwa(sweet)",
    "Jalebi(sweet)",
]

foods_line = " &nbsp; &#8226; &nbsp; ".join(food_names)

st.markdown(
    f"<div class='food-section'>{foods_line}</div>",
    unsafe_allow_html=True,
)
st.markdown("<h3 class='travel-section' style='font-weight:bold; margin-top: 40px;'>🚖 Best Ways to Travel Inside Amritsar</h3>", unsafe_allow_html=True)

amritsar_travel_text = """
<ul style='margin-top: 0; max-width: 700px; font-size: 18px;'>
<li>🚌 <strong>Local Buses:</strong> Economical, covering most parts of Amritsar, including major corridors like Golden Temple to ISBT and Airport routes. Air-conditioned and frequent but can be crowded.</li>
<li>🛺 <strong>Auto Rickshaws:</strong> Convenient for short trips such as Golden Temple to Jallianwala Bagh. Fares usually require bargaining as most autos don’t have meters.</li>
<li>🚖 <strong>Cabs / App Cabs (Ola/Uber):</strong> Comfortable, safe and reliable for longer trips or groups. Ideal for travel to Wagah Border, Khalsa College, Gobindgarh Fort, and airport transfers.</li>
<li>🚶 <strong>Walking:</strong> Best in compact areas like Golden Temple complex, Hall Bazaar, and Katra Jaimal Singh Bazaar to soak in local culture closely.</li>
</ul>
"""

amritsar_travel_tip = """
<div style='background-color: #f0f8ff; padding: 15px; border-radius: 8px; max-width: 700px; font-size: 18px; margin-top: 20px;'>
🌟 <strong>Travel Tip:</strong><br>
Use BRTS buses for fast and cheap travel on main routes.<br>
Autos are best for last-mile connectivity but bargain the fare.<br>
Cabs and app-based taxis offer comfort and convenience.<br>
Walking is recommended in heritage and market areas for rich local experience.
</div>
"""

st.markdown(amritsar_travel_text, unsafe_allow_html=True)
st.markdown(amritsar_travel_tip, unsafe_allow_html=True)


st.markdown("<h3 class='travel-section' style='font-weight:bold; margin-top: 40px;'>📅 Best Months to Visit Amritsar</h3>", unsafe_allow_html=True)

amritsar_months_text = """
<ul style='margin-top: 0; max-width: 700px; font-size: 18px;'>
<li>🍂 <strong>October - March:</strong> The best time to visit Amritsar with cool, pleasant weather great for sightseeing. Festivals like Diwali, Baisakhi, Gurpurab (Guru Nanak Jayanti), and Lohri create a vibrant atmosphere.</li>
<li>❄️ <strong>December - February:</strong> Chilly but comfortable winter months, perfect to enjoy outdoor attractions like the Golden Temple and Wagah Border ceremony.</li>
<li>🌸 <strong>March - April:</strong> Spring season with mild temperatures and blooming flowers, ideal for cultural exploration and outdoor walks.</li>
<li>🌧️ <strong>July - September (Monsoon):</strong> Green and rejuvenated landscapes, but occasional heavy rains may interrupt plans.</li>
</ul>
"""

travel_tip = """
<div style='background-color: #f0f8ff; padding: 15px; border-radius: 8px; max-width: 700px; font-size: 18px; margin-top: 20px;'>
🌟 <strong>Travel Tip:</strong><br>
Plan visits during major festivals like <strong>Diwali, Baisakhi, and Guru Nanak Jayanti</strong> for cultural immersion.<br>
For comfortable sightseeing, the cooler months from <strong>October to March</strong> are ideal.<br>
Carry rain protection if traveling in monsoon season.
</div>
"""

st.markdown(amritsar_months_text, unsafe_allow_html=True)
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
    if st.button("Get Redeem Code for Amritsar Hotels", key="redeem_code_amritsar_btn", type="primary", use_container_width=True):
        code = generate_redeem_code()
        st.success(f"Congratulations! Use this code '{code}' for discounts on Amritsar hotels.")



load_footer()
