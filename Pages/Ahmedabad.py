import streamlit as st
import random
import string
from main import load_footer

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align:center; font-size: 48px; font-weight: bold;'>Welcome to Ahmedabad – The Manchester of India</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size: 20px;'>Explore Ahmedabad's top attractions, vibrant history, and colorful culture in this visual journey.</p>", unsafe_allow_html=True)

images = [
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Ahmedabad/kankaria%20lake%20ahmedabad.jpg", "Kankaria Lake, Ahmedabad", "A lively lakefront with boating, zoo, toy train, and evening lights."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Ahmedabad/Sabarmati%20Riverfront%2C%20Ahmedabad.jpg", "Sabarmati Riverfront, Ahmedabad", "A beautifully developed riverside promenade perfect for evening walks, leisure activities, and city views."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Ahmedabad/Sabarmati%20Ashram.jpg", "Sabarmati Ashram", "Mahatma Gandhi’s peaceful residence, full of history and inspiration."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Ahmedabad/ahmedabad%20step%20well.jpg", "Adalaj Stepwell", "A beautifully carved stepwell showcasing Indo-Islamic architecture."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Ahmedabad/Manek%20Chowk.jpg", "Manekchowk", "Ahmedabad’s bustling night market and street food hub, famous for delicious local snacks, sweets, and vibrant evening vibes."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Ahmedabad/ISKCON%20Temple%20Ahmedabad.jpg", "ISKCON Temple,Ahmedabad", "A serene and beautifully designed temple dedicated to Radha-Krishna, known for spiritual chants, prasadam, and vibrant Janmashtami celebrations."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Ahmedabad/Atal%20bridge.jpg", "Atal bridge", "A modern, elegant pedestrian bridge connecting two sides of the riverfront, offering stunning views of Sabarmati and Ahmedabad skyline."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Ahmedabad/Bhadra%20Fort%20And%20Teen%20Darwaza.jpg", "Bhadra Fort And Teen Darwaza", "A 15th-century fort with royal arches and Mughal charm."),
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

            
st.markdown("<h3 class='food-section' style='font-weight:bold; margin-top: 20px;'>🥘 Must-Try Foods in Ahmedabad</h3>", unsafe_allow_html=True)

food_names = [
    "Gujarati Thali",
    "Fafda–Jalebi",
    "Khaman, Khandvi, Patra",
    "Khakra & Thepla",
    "Undhiyu",
    "Dal Dhokli",
    "Handvo",
    "Shrikhand (sweet)",
    "Mohanthal(sweet)",
    "Basundi (sweet)",
    "Ice Cream Falooda(sweet)",
]

foods_line = " &nbsp; &#8226; &nbsp; ".join(food_names)

st.markdown(
    f"<div class='food-section'>{foods_line}</div>",
    unsafe_allow_html=True,
)
st.markdown("<h3 class='travel-section' style='font-weight:bold; margin-top: 40px;'>🚌 Best Ways to Travel Inside Ahmedabad</h3>", unsafe_allow_html=True)

ahmedabad_travel_text = """
<ul style='margin-top: 0; max-width: 700px; font-size: 18px;'>
<li>🚌 <strong>BRTS (Bus Rapid Transit System):</strong> Fast, eco-friendly buses running on dedicated lanes covering major corridors with frequent service.</li>
<li>🚍 <strong>AMTS Buses:</strong> Extensive fleet serving nearly all parts of Ahmedabad, economical and convenient for daily travel.</li>
<li>🚇 <strong>Ahmedabad Metro:</strong> Modern, efficient, and expanding network, ideal for quick travel across growing business and residential hubs.</li>
<li>🛺 <strong>Private Cabs & Auto Rickshaws:</strong> Widely available for flexible, short to medium distances; negotiate fares with autos, while app cabs offer reliable pricing.</li>
</ul>
"""

ahmedabad_travel_tip = """
<div style='background-color: #e0f7fa; padding: 15px; border-radius: 8px; max-width: 700px; font-size: 18px; margin-top: 20px;'>
🌟 <strong>Travel Tip:</strong><br>
Use BRTS for speedy transit on main routes, and AMTS buses for wider coverage.<br>
Metro is best for fast, comfortable rides on select corridors.<br>
For door-to-door travel, choose private cabs or autos – easy and flexible!
</div>
"""

st.markdown(ahmedabad_travel_text, unsafe_allow_html=True)
st.markdown(ahmedabad_travel_tip, unsafe_allow_html=True)

st.markdown("<h3 class='travel-section' style='font-weight:bold; margin-top: 40px;'>📅 Best Months to Visit Ahmedabad</h3>", unsafe_allow_html=True)

ahmedabad_months_text = """
<ul style='margin-top: 0; max-width: 700px; font-size: 18px;'>
<li>🍂 <strong>October - November (Navratri & Diwali):</strong> Experience Ahmedabad’s grand Navratri with vibrant Garba dances and festive Diwali celebrations lighting up the city.</li>
<li>❄️ <strong>November - February:</strong> Pleasant, cool weather (15°C to 30°C) ideal for sightseeing historical and cultural attractions comfortably.</li>
<li>🌧️ <strong>July - September (Monsoon):</strong> Lush green surroundings and cooler temperatures, though occasional heavy rains may limit outdoor plans.</li>
</ul>
"""

travel_tip = """
<div style='background-color: #fff4e6; padding: 15px; border-radius: 8px; max-width: 700px; font-size: 18px; margin-top: 20px;'>
🌟 <strong>Travel Tip:</strong><br>
Plan your visit around <strong>Navratri and Diwali</strong> (October-November) to enjoy the city’s rich culture.<br>
The winter months (<strong>November to February</strong>) offer the most comfortable weather for all activities.<br>
Monsoon season adds natural beauty but carry rain gear.
</div>
"""

st.markdown(ahmedabad_months_text, unsafe_allow_html=True)
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

# Create three columns with the middle significantly wider
col1, col2, col3 = st.columns([3, 2, 3])
with col2:
    if st.button("Get Redeem Code for Ahmedabad Hotels", key="redeem_code_ahmedabad_btn", type="primary", use_container_width=True):
        code = generate_redeem_code()
        st.success(f"Congratulations! Use this redeem code '{code}' to get an exclusive discount on your hotel booking.")
        tripadvisor_url = "https://www.tripadvisor.in/Hotels-g297608-Ahmedabad_Ahmedabad_District_Gujarat-Hotels.html"
        st.markdown(f"[Click here to book hotels on Tripadvisor and apply your redeem code](<{tripadvisor_url}>)")

load_footer()