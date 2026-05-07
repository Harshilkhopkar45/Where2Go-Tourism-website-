import streamlit as st
import random
import string
from where2go import load_footer

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align:center; font-size: 48px; font-weight: bold;'>Welcome to Pune – The Oxford of the East</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size: 20px;'>Explore Pune's top attractions, vibrant history, and colorful culture in this visual journey.</p>", unsafe_allow_html=True)

images = [
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Pune/Shaniwar%20Wada%2C%20Pune.jpg", "Shaniwar Wada", " The grand fort palace of the Peshwas, famous for its architectural beauty and legends. This historic fortification, built in 1736, is a symbol of Pune's rich history."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Pune/Shreemant%20Dagadusheth%20Halwai%20Ganapati%20Temple.jpg", "Shreemant Dagadusheth Halwai Ganapati Temple", "One of the most famous Ganesh temples in Maharashtra."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Pune/Sinhagad%20fort.jpg", "Sinhagad Fort", "Located about 36 km from Pune, this fort is famous for its scenic views and trekking opportunities."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Pune/Pataleshwar%20Cave%20Temple.jpg", "Pataleshwar Cave Temple", "An ancient rock-cut cave temple dedicated to Lord Shiva."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Pune/Raja%20Dinkar%20Kelkar%20Museum%2C%20Pune.jpg", "Raja Dinkar Kelkar Museum", "Home to thousands of rare artifacts and art pieces."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Pune/Aga%20khan.jpg", "Aga Khan Palace", "A heritage site tied to Mahatma Gandhi’s freedom struggle."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Pune/Parvati%20Hill%20Pune.jpg", "Parvati Hill & Parvati Temple", "A serene hilltop temple complex  with 700 steps & panoramic views of Pune."),
    
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

            
st.markdown("<h3 class='food-section' style='font-weight:bold; margin-top: 20px;'>🥘 Must-Try Foods in Pune</h3>", unsafe_allow_html=True)

food_names = [
    "Vada Pav",
    "Pav Bhaji",
    "Misal Pav",
    "Bhakarwadi",
    "Keema Pav",
    "Poha",
    "Puran Poli",
    "Rabdi Falooda (sweet)",
    "Modak & Ladoo (sweet)",
    "Mastani(sweet)",
]

foods_line = " &nbsp; &#8226; &nbsp; ".join(food_names)

st.markdown(
    f"<div class='food-section'>{foods_line}</div>",
    unsafe_allow_html=True,
)

st.markdown("<h3 class='travel-section' style='font-weight:bold; margin-top: 40px;'>🚖 Best Ways to Travel Inside Pune</h3>", unsafe_allow_html=True)

travel_text = """
<ul style='margin-top: 0; max-width: 700px; font-size: 18px;'>
<li>🚇 <strong>Pune Metro:</strong> Fast, clean, and affordable option, though currently operational on limited routes; expanding soon.</li>
<li>🚌 <strong>PMT Buses:</strong> Cheapest way to travel; good connectivity but can be crowded and less punctual.</li>
<li>🚖 <strong>Autos (Rickshaws):</strong> Easily available, short-distance travel friendly, but mostly run without meters (fares need bargaining).</li>
<li>🚗 <strong>Cabs (Ola/Uber):</strong> Comfortable for longer distances or groups; costlier than autos but reliable.</li>
<li>🏍️ <strong>Two-Wheelers (Rentals):</strong> Popular with youngsters; convenient for exploring the city and nearby spots.</li>
<li>🚲 <strong>Cycles & E-bikes:</strong> Available on rent for short rides, eco-friendly, and pocket-friendly.</li>
</ul>
"""

tip_text = """
<div style='background-color: #f0f8ff; padding: 15px; border-radius: 8px; max-width: 700px; font-size: 18px; margin-top: 20px;'>
🌟 <strong>Travel Tip:</strong><br>
For daily city travel, Metro + Autos make a good combo.<br>
For comfort, choose Cabs.<br>
For flexibility, Two-Wheeler rentals are ideal.
</div>
"""

st.markdown(travel_text, unsafe_allow_html=True)
st.markdown(tip_text, unsafe_allow_html=True)

st.markdown("<h3 class='visit-section' style='font-weight:bold; margin-top: 40px;'>🗓️ Best Months to Visit Pune</h3>", unsafe_allow_html=True)

best_month_text = """
<ul style='max-width: 700px; margin-left: 20px; margin-right: auto; font-size: 18px;'>
<li><strong>August – September (Ganesha Chaturthi):</strong> The most vibrant time to visit Pune, when the city comes alive with grand celebrations, elaborate decorations, and cultural events honoring Lord Ganesha.</li>
<li><strong>October – February:</strong> Enjoy pleasant weather, ideal for sightseeing, attending other local festivals like Diwali, and exploring the city’s outdoor attractions.</li>
<li><strong>March – May:</strong> Hot and humid months with fewer tourists and attractive hotel deals, suitable for those who prefer quieter stays and indoor activities.</li>
<li><strong>June – September (Monsoon):</strong> Witness Pune during the lush monsoon season. The rains add a unique charm but can disrupt outdoor plans.</li>
<li><strong>✨ Tourist Tip:</strong> Plan to visit during Ganesha Chaturthi to experience Pune’s cultural heartbeat and wonderful decorations. Attend the grand processions and immerse in local traditions while enjoying evening walks along Marine Drive in the cooler months.</li>
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

# Create three columns with the middle significantly wider
col1, col2, col3 = st.columns([3, 2, 3])
with col2:
    if st.button("Get Redeem Code for Delhi Hotels", key="redeem_code_btn", type="primary", use_container_width=True):
        code = generate_redeem_code()
        st.success(f"Congratulations! Use this redeem code '{code}' to get an exclusive discount on your hotel booking.")
        tripadvisor_url = "https://www.tripadvisor.in/Hotels-g304551-New_Delhi_National_Capital_Territory_of_Delhi-Hotels.html"
        st.markdown(f"[Click here to book hotels on Tripadvisor and apply your redeem code](<{tripadvisor_url}>)")


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
    if st.button("Get Redeem Code for Pune Hotels", key="redeem_code_pune_btn", type="primary", use_container_width=True):
        code = generate_redeem_code()
        st.success(f"Congratulations! Use this redeem code '{code}' to get an exclusive discount on your hotel booking.")
  


load_footer()
