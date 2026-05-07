import streamlit as st
import random
import string
from where2go import load_footer

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align:center; font-size: 48px; font-weight: bold;'>Welcome to New Delhi - Capital of India</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size: 20px;'>Explore New Delhi's top attractions, vibrant history, and colorful culture in this visual journey.</p>", unsafe_allow_html=True)

images = [
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Delhi.jpg", "Red Fort", "The Mughal-era fort with lots of cultural and historical significance."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Delhi/Chandni%20Chowk.jpg", "Chandni Chowk", "Chandni Chowk is Delhi’s bustling historic market, famous for its vibrant streets, traditional shops, and mouthwatering street food."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Delhi/India%20Gate.jpg", "India Gate", "Great for an evening walk, patriotically photogenic – India Gate, Rashtrapati Bhavan, the ceremonial boulevard."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Delhi/Qutb%20Minar.jpg", "Qutb Minar", "A UNESCO World Heritage site, this tall minaret and the surrounding ruins are beautiful examples of early Indo-Islamic architecture."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Delhi/Akshardham%20temple%20new%20delhi.jpg", "Akshardham Temple", "Akshardham Temple is a majestic spiritual and cultural complex in Delhi, renowned for its grand architecture, intricate carvings, and serene atmosphere."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Delhi/Humayu%27s%20Tomb.jpg", "Humayun's Tomb", "Another UNESCO site. Gorgeous gardens, peaceful ambiance, excellent architecture."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Delhi/jama%20masjid%20delhi.jpg", "Jama Masjid", "Jama Masjid is one of India’s largest mosques, known for its stunning Mughal architecture in the heart of Old Delhi."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Delhi/Lotus%20Temple.jpg", "Lotus Temple", "Very striking architecture (lotus-like shape), peaceful place."),
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

            
st.markdown("<h3 class='food-section' style='font-weight:bold; margin-top: 20px;'>🥘 Must-Try Foods in New Delhi</h3>", unsafe_allow_html=True)

food_names = [
    "Chole Bhature",
    "Parathas at Paranthe Wali Gali",
    "Butter Chicken",
    "Mughlai Biryani",
    "Kebabs & Rolls",
    "Street Momos",
    "Rajma Chawal",
    "Aloo Tikki & Chaat",
    "Kulfi Falooda",
]

foods_line = " &nbsp; &#8226; &nbsp; ".join(food_names)

st.markdown(
    f"<div class='food-section'>{foods_line}</div>",
    unsafe_allow_html=True,
)

st.markdown("<h3 class='travel-section' style='font-weight:bold; margin-top: 40px;'>🚆 Best Ways to Travel Inside New Delhi</h3>", unsafe_allow_html=True)

travel_text = """
<ul style='margin-top: 0;'>
<li><strong>Delhi Metro:</strong> The fastest, most affordable, and safest way to travel around Delhi. It covers most key areas and tourist spots with frequent trains and air-conditioned coaches.</li>
<li><strong>Auto Rickshaws and E-Rickshaws:</strong> Ideal for short distances or last-mile connectivity. E-rickshaws are eco-friendly and economical, while autos are faster for moderate distances.</li>
<li><strong>App-based Cabs (Ola, Uber):</strong> Convenient for personalized, door-to-door travel and useful during late hours or uncomfortable weather but costlier than public transport.</li>
<li><strong>Buses:</strong> Delhi Transport Corporation (DTC) operates AC and non-AC buses covering wide routes at very affordable fares, but buses may be crowded during peak hours.</li>
</ul>
"""

st.markdown(f"<div class='travel-section'>{travel_text}</div>", unsafe_allow_html=True)

st.markdown("<h3 class='visit-section' style='font-weight:bold; margin-top: 40px;'>🗓️ Best Month(s) to Visit Delhi</h3>", unsafe_allow_html=True)

best_month_text = """
<p style='margin-top: 0; font-size: 18px; max-width: auto;'>
The ideal time to visit Delhi is from <strong>February to March</strong> and <strong>September to November</strong>. During these months:
</p>
<ul style='margin-top: 0; max-width: auto; font-size: 18px;'>
<li><strong>Festivals:</strong> Experience vibrant events like Holi in March and Diwali in October-November for rich cultural immersion.</li>
<li><strong>Low Tourism:</strong> Avoid peak tourist rush affecting popular destinations, allowing peaceful exploration.</li>
<li><strong>Better Affordability:</strong> Enjoy more competitive rates on accommodations and travel during these off-peak months.</li>
<li><strong>Comfortable Weather:</strong> Mild temperatures make touring and sightseeing comfortable without extreme heat or cold.</li>
</ul>
<p style='font-size: 18px;'>
Avoid heavy smog months of December and January and intense summer heat from April to June. Monsoon season (July-August) brings fewer crowds but unpredictable rain.
</p>
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
       

load_footer()

