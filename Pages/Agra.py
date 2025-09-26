import streamlit as st
import random
import string
from main import load_footer

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align:center; font-size: 48px; font-weight: bold;'>Welcome to Agra – Home of the Taj Mahal</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size: 20px;'>Explore Agra's top attractions, vibrant history, and colorful culture in this visual journey.</p>", unsafe_allow_html=True)

images = [
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Agra.jpg", "Taj Mahal", "The iconic white marble mausoleum and symbol of eternal love, admired worldwide for its beauty and symmetry."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Agra/Agra%20Fort.jpg", "Agra Fort", "A massive UNESCO World Heritage fort, showcasing Mughal grandeur with palaces, halls, and impressive gates."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Agra/Fatehpur%20Sikri.jpg", "Fatehpur Sikri", "A well-preserved Mughal ghost city built by Akbar, known for its stunning palaces, mosques, and courtyards."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Agra/Akbar%20%20Tomb.jpg", "Akbar's Tomb (Sikandra)", "Majestic Mughal tomb with impressive architecture and serene gardens, celebrating Emperor Akbar’s legacy."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Agra/Itimad-ud-Daulah.jpg","Itmad-Ud-Daulah Tomb", "Often called the “Baby Taj,” a delicate marble tomb with intricate pietra dura inlay work."),
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

            
st.markdown("<h3 class='food-section' style='font-weight:bold; margin-top: 20px;'>🥘 Must-Try Foods in Agra</h3>", unsafe_allow_html=True)

food_names = [
    "Dal Moth",
    "Mughlai Cuisine",
    "Paneer Tikka",
    "Veg Mughlai Dishes",
    "Raan / Seekh Kebabs",
    "Bedai & Jalebi (sweet)",
    "Petha (sweet)",
    "Agra Kulfi / Rabri (sweet)",
]

foods_line = " &nbsp; &#8226; &nbsp; ".join(food_names)

st.markdown(
    f"<div class='food-section'>{foods_line}</div>",
    unsafe_allow_html=True,
)

st.markdown("<h3 class='travel-section' style='font-weight:bold; margin-top: 40px;'>🚆 Best Ways to Travel Inside Agra</h3>", unsafe_allow_html=True)

travel_text = """
<ul style='margin-top: 0; max-width: 700px; font-size: 18px;'>
<li><strong>For short sightseeing trips / Taj Mahal to nearby attractions:</strong> Autos and E-rickshaws are convenient and inexpensive. They’re ideal for short distances and give a fun local experience.</li>
<li><strong>For full-day trips or Agra Fort + Fatehpur Sikri combo:</strong> Private cabs, Ola, or Uber provide comfort, flexibility, and air-conditioned travel for families or longer itineraries.</li>
<li><strong>For budget solo travel:</strong> Use city buses combined with autos for the most affordable and flexible option between major sites and neighborhoods.</li>
</ul>
"""

st.markdown(travel_text, unsafe_allow_html=True)

st.markdown("<h3 class='visit-section' style='font-weight:bold; margin-top: 40px;'>🗓️ Best Months to Visit Agra</h3>", unsafe_allow_html=True)

best_month_text = """
<ul style='max-width: 700px; margin-left: 20px; margin-right: auto; font-size: 18px;'>
<li><strong>Best Balance:</strong> <span style='color: #138808;'>October–March &#10004;</span> — Best overall for cool, pleasant weather and a festive atmosphere. Great for sightseeing, comfortable walks, and experiencing Diwali, Taj Mahotsav (February), and Holi.</li>
<li><strong>Budget-Friendly & Less Crowded:</strong><span style='color: #138808;'> July–September &#10004;</span>— Cheapest months to visit. Enjoy fewer tourists if you don’t mind the monsoon showers that give Agra a romantic vibe and lush look.</li>
<li><strong>✨ Tourist Tip:</strong> For the Taj Mahal, visit early morning to avoid both heat and peak crowds. February is extra special for the Taj Mahotsav festival, combining ideal weather with cultural performances.</li>
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
    if st.button("Get Redeem Code for Agra Hotels", key="redeem_code_agra_btn", type="primary", use_container_width=True):
        code = generate_redeem_code()
        st.success(f"Congratulations! Use this redeem code '{code}' to get an exclusive discount on your hotel booking.")
        tripadvisor_url = "https://www.tripadvisor.in/Hotels-g297683-Agra_Agra_District_Uttar_Pradesh-Hotels.html"
        st.markdown(f"[Click here to book hotels on Tripadvisor and apply your redeem code](<{tripadvisor_url}>)")

load_footer()