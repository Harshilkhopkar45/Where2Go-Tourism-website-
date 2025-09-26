import streamlit as st
import random
import string
from main import load_footer

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align:center; font-size: 48px; font-weight: bold;'>Welcome to Goa – The Pearl of the Orient</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size: 20px;'>Explore Goa's top attractions, vibrant history, and colorful culture in this visual journey.</p>", unsafe_allow_html=True)

images = [
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/GOA/Baga%20Beach%20Goa.jpg", "Baga Beach", "Famous for water sports, nightlife, and beach shacks."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/GOA/calangute%20beach.jpg", "Calangute Beach", "The “Queen of Beaches,” ideal for sunbathing and parasailing."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/GOA/Dudhsagar%20Waterfalls.jpg", "Dudhsagar Waterfalls", "Majestic four-tiered waterfall on the Goa–Karnataka border."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/GOA/Fort%20Aguda.jpg", "Fort Aguada", "17th-century Portuguese fort with panoramic sea views."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/GOA/Se%E2%80%99%20Cathedral%2C%20Goa.jpg", "Se' Cathedral", "One of Asia’s largest churches, showcasing Portuguese architecture"),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/GOA/Fort%20Chapora.jpg", "Chapora Fort", "Iconic sunset point, popular from the movie Dil Chahta Hai."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/GOA/Basilica%20of%20Bom%20Jesus.jpg", "Basilica of Bom Jesus", "UNESCO World Heritage church housing St. Francis Xavier’s relics."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/GOA/Palolem%20Beach%2C%20%23Goa.jpg", "Palolem Beach", "Peaceful crescent-shaped beach, perfect for dolphin watching."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/GOA/Anjuna%20Flea%20Market.jpg", "Anjuna Beach & Flea Market", "Known for hippie vibes, parties, and colorful street shopping.Pleas do bargain as well"),
    
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

            
st.markdown("<h3 class='food-section' style='font-weight:bold; margin-top: 20px;'>🥘 Must-Try Foods in Goa</h3>", unsafe_allow_html=True)

food_names = [
    "Chicken Cafreal",
    "Sannas",
    "Sorpotel",
    "Vindaloo",
    "Rava Fried Fish(sea food)",
    "Prawn Balchao (seafood)",
    "Goan Fish Curry & Rice (seafood)",
    "Bebinca (Goan sweet)",
]

foods_line = " &nbsp; &#8226; &nbsp; ".join(food_names)

st.markdown(
    f"<div class='food-section'>{foods_line}</div>",
    unsafe_allow_html=True,
)

st.markdown("<h3 class='travel-section' style='font-weight:bold; margin-top: 40px;'>🌴 Best Ways to Travel Inside Goa</h3>", unsafe_allow_html=True)

# Travel Options Content
goa_travel_text = """
<ul style='margin-top: 0; max-width: 700px; font-size: 18px;'>
<li>🛺 <strong>Auto Rickshaws / Taxis:</strong> Best for short distances, but fares often need bargaining. Air-conditioned taxis are available for longer rides.</li>
<li>🚖 <strong>App-Based Cabs (Uber/Ola):</strong> Convenient for medium to long distances. More reliable pricing than local autos.</li>
<li>🚌 <strong>Local Buses:</strong> Budget-friendly, cover major towns like Panjim, Mapusa, and Margao. Less frequent and slower; not ideal for tourists with tight schedules.</li>
<li>🏍️ <strong>Scooter / Bike Rentals:</strong> Most popular for tourists, gives freedom to explore beaches, forts, and waterfalls at your own pace. Affordable and perfect for narrow coastal roads.</li>
<li>🚶 <strong>Walking:</strong> Great for short distances near beaches, markets, and forts. Best way to explore places like Baga, Anjuna, and Panjim on foot.</li>
</ul>
"""

# Tourist Tip Section
goa_tip = """
<div style='background-color: #f0f8ff; padding: 15px; border-radius: 8px; max-width: 700px; font-size: 18px; margin-top: 20px;'>
🌟 <strong>Tourist Tip:</strong><br>
For sightseeing: Rent a scooter or bike.<br>
For comfort or long distances: App cabs/taxis.<br>
Short hops near beaches or markets: Walk or take autos.
</div>
"""

# Display Text
st.markdown(goa_travel_text, unsafe_allow_html=True)
st.markdown(goa_tip, unsafe_allow_html=True)


# Section Heading
st.markdown("<h3 class='travel-section' style='font-weight:bold; margin-top: 40px;'>📅 Best Months to Travel in Goa</h3>", unsafe_allow_html=True)

# Best Months Content
goa_months_text = """
<ul style='margin-top: 0; max-width: 700px; font-size: 18px;'>
<li>🌞 <strong>November – February:</strong> Peak tourist season with pleasant weather, perfect for beaches, parties, and sightseeing.</li>
<li>🌴 <strong>March – May:</strong> Hot and humid, fewer tourists, good for budget travel but not ideal for day sightseeing.</li>
<li>🌧️ <strong>June – September (Monsoon):</strong> Lush greenery, waterfalls at their best, but not great for swimming or water sports due to rough seas.</li>
<li>🍂 <strong>October:</strong> Transition season with moderate crowds and improving weather, a good pre-peak time to visit.</li>
</ul>
"""

# Tourist Tip Section
goa_months_tip = """
<div style='background-color: #fffae6; padding: 15px; border-radius: 8px; max-width: 700px; font-size: 18px; margin-top: 20px;'>
🌟 <strong>Travel Tip:</strong><br>
For the best experience, visit between <strong>November and February</strong> for beaches and nightlife.<br>
For greenery, monsoon vibes, and fewer crowds, choose <strong>June to September</strong>.
</div>
"""

# Display Text
st.markdown(goa_months_text, unsafe_allow_html=True)
st.markdown(goa_months_tip, unsafe_allow_html=True)

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
    if st.button("Get Redeem Code for Goa Hotels", key="redeem_code_goa_btn", type="primary", use_container_width=True):
        code = generate_redeem_code()
        st.success(f"Congratulations! Use this redeem code '{code}' to get an exclusive discount on your hotel booking.")
        tripadvisor_url = "https://www.tripadvisor.in/Hotels-g297604-Goa-Hotels.html"
        st.markdown(f"[Click here to book hotels on Tripadvisor and apply your redeem code](<{tripadvisor_url}>)")

load_footer()
