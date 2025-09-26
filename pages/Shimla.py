import streamlit as st
import random
import string
from where2go import load_footer

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align:center; font-size: 48px; font-weight: bold;'>Welcome to Shimla – The Queen of Hills</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size: 20px;'>Explore Shimla's top attractions, vibrant history, and colorful culture in this visual journey.</p>", unsafe_allow_html=True)

images = [
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Shimla/Kufri.jpg", "Kufri, Shimla", "A popular hill station just 16 km from Shimla, known for snow sports like skiing, tobogganing, and snowboarding in winter, and nature walks and horse riding during summers.✅ Best spot for snow sports and beginner mountain trekking."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Shimla/Jakhu%20Temple%2C%20Shimla.jpg", "Jakhu Hanuman Temple","Located atop Jakhu Hill, the tallest point in Shimla, featuring a giant Hanuman statue and short trekking trails from the Ridge.✅ Great for hill climbing/trekking, but snow sports are limited."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Shimla/The%20Ridge.jpg", "The Ridge", "The heart of Shimla city, offering panoramic views of the surrounding hills, vibrant shops, cafes, and cultural events.✅ Great for walking and enjoying city views, not for snow sports or mountain climbing."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Shimla/Viceregal%20Lodge%20Shimla.jpg", "Viceregal Lodge,Shimla", "Majestic colonial-era building surrounded by lush gardens, offering a glimpse into British India and Shimla’s history.✅ Mostly for sightseeing; no snow sports or mountain climbing."),

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

            
st.markdown("<h3 class='food-section' style='font-weight:bold; margin-top: 20px;'>🥘 Must-Try Foods in Shimla</h3>", unsafe_allow_html=True)

food_names = [
    "Chana Madra",
    "Dham",
    "Babru(Stuffed bread for fish lovers)",
    "Aloo ke Gutke",
    "Momos & Thukpa",
    "Tikki / Chaat",
    "Apple-based Desserts(sweet)",
    "Hot Chocolate (sweet)",
    "Bal Mithai (famous Thickshakes)",
]

foods_line = " &nbsp; &#8226; &nbsp; ".join(food_names)

st.markdown(
    f"<div class='food-section'>{foods_line}</div>",
    unsafe_allow_html=True,
)

st.markdown("<h3 class='travel-section' style='font-weight:bold; margin-top: 40px;'>🚖 Best Ways to Travel Inside Shimla</h3>", unsafe_allow_html=True)

shimla_travel_text = """
<ul style='margin-top: 0; max-width: 700px; font-size: 18px;'>
<li>🚌 <strong>Himachal Pradesh Buses:</strong> State-run and private buses cover Shimla and nearby towns. Economical but slower and less frequent; ideal for budget travelers.</li>
<li>🚖 <strong>Cabs / Taxis:</strong> Comfortable for sightseeing and day trips to places like Kufri, Naldehra, and Mashobra. Best for small groups or families.</li>
<li>🛺 <strong>Auto Rickshaws / Shared Taxis:</strong> Convenient for short distances inside Shimla city. Shared autos are cheaper than private taxis.</li>
</ul>
"""

shimla_travel_tip = """
<div style='background-color: #f0f8ff; padding: 15px; border-radius: 8px; max-width: 700px; font-size: 18px; margin-top: 20px;'>
🌟 <strong>Travel Tip:</strong><br>
Use state buses for economical travel on longer routes.<br>
Cabs provide comfort and flexibility, ideal for sightseeing trips.<br>
Autos and shared taxis are great for quick and cheap travel within the city.
</div>
"""

st.markdown(shimla_travel_text, unsafe_allow_html=True)
st.markdown(shimla_travel_tip, unsafe_allow_html=True)


st.markdown("<h3 class='travel-section' style='font-weight:bold; margin-top: 40px;'>📅 Best Months to Visit Shimla</h3>", unsafe_allow_html=True)

shimla_months_text = """
<ul style='margin-top: 0; max-width: 700px; font-size: 18px;'>
<li>🌤️ <strong>March – June (Spring & Early Summer):</strong> Pleasant temperatures (15°C–30°C), ideal for sightseeing, trekking, and outdoor activities. Green hills, blooming flowers, and comfortable days for exploring Mall Road, Jakhoo Temple, and Kufri.</li>
<li>❄️ <strong>December – February (Winter & Snow Season):</strong> Temperatures range from -2°C to 15°C; snow often falls in January and February. Perfect for snow activities, photography, and cozy hill stays. Can be crowded during Christmas and New Year.</li>
</ul>
"""

travel_tip = """
<div style='background-color: #e6f0ff; padding: 15px; border-radius: 8px; max-width: 700px; font-size: 18px; margin-top: 20px;'>
🌟 <strong>Travel Tip:</strong><br>
Visit during spring (March-June) for beautiful greenery and pleasant weather.<br>
Winter (December-February) offers magical snowfall and festive experiences but expect crowds around holidays.
</div>
"""

st.markdown(shimla_months_text, unsafe_allow_html=True)
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
    if st.button("Get Redeem Code for Shimla Hotels", key="redeem_code_shimla_btn", type="primary", use_container_width=True):
        code = generate_redeem_code()
        st.success(f"Congratulations! Use this redeem code '{code}' to get exclusive discount on hotel bookings.")
        tripadvisor_url = "https://www.tripadvisor.in/Hotels-g304552-Shimla_Shimla_District_Himachal_Pradesh-Hotels.html"
        st.markdown(f"[Click here to book Shimla hotels on Tripadvisor with your redeem code](<{tripadvisor_url}>)")


load_footer()