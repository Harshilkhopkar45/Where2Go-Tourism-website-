import streamlit as st
import random
import string
from main import load_footer

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align:center; font-size: 48px; font-weight: bold;'>Welcome to Udaipur – The City of Lakes</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size: 20px;'>Explore Udaipur's top attractions, vibrant history, and colorful culture in this visual journey.</p>", unsafe_allow_html=True)

images = [
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Udaipur/Udaipur%20City%20Palace.jpg", "City Palace", "A majestic palace complex with stunning courtyards, balconies, and panoramic views of Lake Pichola."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Udaipur/Pichola%20Lake%2C%20Udaipur.jpg", "Lake Pichola", "Famous for boat rides with views of palaces, ghats, and the magical sunset skyline."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Udaipur/Jag%20Mandir%20Palace%2C%20Udaipur.jpg", "Jag Mandir", "An island palace in Lake Pichola, often called the “Lake Garden Palace.”"),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Udaipur/Sajjangarh%20palace.jpg", "Sajjangarh Palace (Monsoon Palace)", "Perched on a hilltop, offering panoramic sunset views of Udaipur."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Udaipur/Jagdish%20Temple%2C%20Udaipur.jpg", "Jagdish Temple", "A grand 17th-century Hindu temple with intricate carvings, dedicated to Lord Vishnu."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Udaipur/Lake%20Fateh%20Sagar.jpg", "Fateh Sagar Lake", "Popular for evening walks, boating, and the Nehru Garden in the middle of the lake."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Udaipur/Saheliyon%20ki%20Bari%2C%20Udaipur.jpg", "Saheliyon ki Bari", "A beautiful historic garden with fountains, lotus pools, and marble pavilions."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Udaipur/Bagore%20Ki%20Haveli%2C%20Udaipur.jpg", "Bagore ki Haveli", "A heritage haveli with cultural shows (folk dance, puppet shows) in the evening."),

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

            
st.markdown("<h3 class='food-section' style='font-weight:bold; margin-top: 20px;'>🥘 Must-Try Foods in Udaipur</h3>", unsafe_allow_html=True)

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

st.markdown("<h3 class='travel-section' style='font-weight:bold; margin-top: 40px;'>🚖 Best Ways to Travel Inside Udaipur</h3>", unsafe_allow_html=True)

udaipur_travel_text = """
<ul style='margin-top: 0; max-width: 700px; font-size: 18px;'>
<li>🛺 <strong>Auto Rickshaws & E-Rickshaws:</strong> Ideal for short distances around City Palace, Jagdish Temple, and the markets. Fares often require bargaining; e-rickshaws are eco-friendly and navigate narrow lanes well.</li>
<li>🚖 <strong>Cabs / App-Based Cabs (Ola, Uber):</strong> Convenient for longer distances, lakeside sightseeing, and trips to Kumbhalgarh, Sajjangarh, or Fatehsagar Lake. Comfortable, air-conditioned, and offer reliable pricing.</li>
<li>🚌 <strong>Local Buses / Shared Vans:</strong> Available for nearby towns and villages; budget-friendly but less convenient for tourists due to limited routes and timings.</li>
</ul>
"""

udaipur_travel_tip = """
<div style='background-color: #e7f4ff; padding: 15px; border-radius: 8px; max-width: 700px; font-size: 18px; margin-top: 20px;'>
🌟 <strong>Travel Tip:</strong><br>
Use autos and e-rickshaws for quick, eco-friendly short trips within the city.<br>
For comfort and longer journeys, app-based cabs are the best choice.<br>
Local buses and shared vans are economical but check schedules carefully.
</div>
"""

st.markdown(udaipur_travel_text, unsafe_allow_html=True)
st.markdown(udaipur_travel_tip, unsafe_allow_html=True)


st.markdown("<h3 class='travel-section' style='font-weight:bold; margin-top: 40px;'>📅 Best Months to Visit Udaipur</h3>", unsafe_allow_html=True)

udaipur_months_text = """
<ul style='margin-top: 0; max-width: 700px; font-size: 18px;'>
<li>🍂 <strong>October – March (Peak Season & Best Weather):</strong> Pleasant winter climate (10–25°C), perfect for exploring palaces, lakes, and markets. Festivals during this time include Diwali (Oct/Nov), Shilpgram Arts & Crafts Fair (Dec), and the vibrant Mewar Festival (March/April). Expect higher prices and more tourists, especially around Christmas and New Year.</li>
<li>🌧️ <strong>July – September (Monsoon Charm, Budget-Friendly):</strong> Rain fills the lakes and makes the surroundings lush and scenic. Festivals during this season include Teej (July/Aug) and Janmashtami (Aug). There are fewer tourists and more affordable hotels, though occasional heavy showers may limit outdoor activities.</li>
</ul>
"""

travel_tip = """
<div style='background-color: #f0f4f8; padding: 15px; border-radius: 8px; max-width: 700px; font-size: 18px; margin-top: 20px;'>
🌟 <strong>Travel Tip:</strong><br>
Visit during <strong>October to March</strong> for the best weather and festival experiences.<br>
Monsoon months <strong>July to September</strong> offer budget-friendly travel and lush scenery but be prepared for rain.<br>
Book accommodations in advance for peak seasons to get the best deals.
</div>
"""

st.markdown(udaipur_months_text, unsafe_allow_html=True)
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
    if st.button("Get Redeem Code for Udaipur Hotels", key="redeem_code_udaipur_btn", type="primary", use_container_width=True):
        code = generate_redeem_code()
        st.success(f"Congratulations! Use this redeem code '{code}' for exclusive discounts on Udaipur hotels.")
        tripadvisor_url = "https://www.tripadvisor.in/Hotels-g297672-Udaipur_Udaipur_District_Rajasthan-Hotels.html"
        st.markdown(f"[Book Udaipur hotels here](<{tripadvisor_url}>)")

load_footer()