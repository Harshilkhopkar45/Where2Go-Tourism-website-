import streamlit as st
import random
import string
from where2go import load_footer

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align:center; font-size: 48px; font-weight: bold;'>Welcome to New Chennai - Health capital of India</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size: 20px;'>Explore Chennai's top attractions, vibrant history, and colorful culture in this visual journey.</p>", unsafe_allow_html=True)

images = [
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Chennai/Kapaleeshwarar%20Temple%2Cchennai.jpg", "Kapaleeshwarar Temple", "A stunning Dravidian-style temple located in Mylapore, known for its intricate architecture and vibrant sculptures."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Chennai/Marina%20Beach.jpg", "Marina Beach", "The second longest urban beach in the world, Marina Beach stretches for about 13 kilometers along the Bay of Bengal"),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Chennai/San%20Thome%20Church.jpg", "San Thome Church", "A significant landmark in Chennai, this church is built over the tomb of St. Thomas, one of the twelve apostles of Jesus."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Chennai/Snow%20Kingdom.jpg", "Snow Kingdom", "CHENNAI'S VERY OWN SNOW-CAPPED DESTINATION! Beat the city’s heat and come on over for a snow adventure like no other, right here in the heart of Chennai."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Chennai/VGP%20Marine%20Kingdom.jpg", "VGP Marine Kingdom", "India’s Largest & Coolest Walk-In Aquarium Dive into a mesmerizing 70-meter underwater tunnel surrounded by exotic marine life from five aquatic zones."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Chennai/museum.jpg", "Government Museum, Chennai", "Established in 1851, this museum is one of the oldest in India and houses a rich collection of art, archaeology, and numismatics."),
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

            
st.markdown("<h3 class='food-section' style='font-weight:bold; margin-top: 20px;'>🥘 Must-Try Foods in Chennai</h3>", unsafe_allow_html=True)

food_names = [
    "Idli",
    "Dosa Varieties",
    "Mendu Vada",
    "Kothu Parotta",
    "Chicken 65",
    "Mysore Pak",
    "Filter Coffee",
    "Seafood Delights",
    "Jigarthanda(sweet)",
]

foods_line = " &nbsp; &#8226; &nbsp; ".join(food_names)

st.markdown(
    f"<div class='food-section'>{foods_line}</div>",
    unsafe_allow_html=True,
)

st.markdown("<h3 class='visit-section' style='font-weight:bold; margin-top: 40px;'>🚗 Best Travelling Options in Chennai</h3>", unsafe_allow_html=True)

travel_options_text = """
<p style='font-size: 18px;'>
Chennai offers diverse transport modes for comfortable and convenient travel across the city:
</p>
<ul style='font-size: 18px;'>
<li><strong>Chennai Metro:</strong> A fast, safe, and affordable network connecting major parts of the city including the airport, central business districts, and residential areas.</li>
<li><strong>Suburban Trains:</strong> Connect the city with its suburban areas and nearby towns, ideal for daily commuters.</li>
<li><strong>Public Buses:</strong> Operated by MTC (Metropolitan Transport Corporation), offering extensive coverage and economical fares across the city.</li>
<li><strong>Auto Rickshaws:</strong> Widely available and convenient for short trips. Metered rickshaws are recommended to avoid fare disputes.</li>
<li><strong>App-based Cabs:</strong> Services like Ola and Uber are popular for hassle-free rides, offering upfront fare estimates and cashless payments.</li>
<li><strong>Radio Taxis and Prepaid Cabs:</strong> Available at airports and major railway stations for safe and reliable transportation.</li>
<li><strong>Car Rentals:</strong> Both self-drive and chauffeur-driven car rentals are available for tourists who prefer private travel.</li>
</ul>
<p style='font-size: 18px;'>
Tips: Use Metro for long-distance intra-city travel. Auto rickshaws and app cabs are best for convenient and short-distance trips. Plan ahead during festivals and peak hours due to traffic congestion.
</p>
"""

st.markdown(travel_options_text, unsafe_allow_html=True)

st.markdown("<h3 class='visit-section' style='font-weight:bold; margin-top: 40px;'>🗓️ Best Month(s) to Visit Chennai</h3>", unsafe_allow_html=True)

best_month_text = """
<p style='margin-top: 0; font-size: 18px; max-width: auto;'>
The best months to visit Chennai are from <strong>November to February</strong> (Winter Season). During these months:
</p>
<ul style='margin-top: 0; max-width: auto; font-size: 18px;'>
<li><strong>Weather:</strong> Pleasant and cooler, with temperatures ranging from 20°C to 28°C, providing comfortable conditions for sightseeing and outdoor activities.</li>
<li><strong>Festivals:</strong> Enjoy vibrant cultural events like the Chennai Music & Dance Season (December–January), Pongal (January), and other local festivities.</li>
<li><strong>Activities:</strong> Ideal for beach outings, food walks, and exploring heritage sites without the discomfort of the intense summer heat or monsoon rains.</li>
<li><strong>Tourism Season:</strong> The peak tourist season, providing a lively atmosphere with plenty of events and open attractions.</li>
</ul>
<p style='font-size: 18px;'>
Avoid the hot summer months (March to May) with high temperatures often exceeding 38°C and the monsoon season (June to September) which brings heavy rains and occasional flooding.
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

col1, col2, col3 = st.columns([3, 2, 3])
with col2:
    if st.button("Get Redeem Code for Chennai Hotels", key="redeem_code_chennai_btn", type="primary", use_container_width=True):
        code = generate_redeem_code()
        st.success(f"Congratulations! Use this code '{code}' for exclusive discounts on Chennai hotels.")
       

load_footer()
