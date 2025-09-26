import streamlit as st
import random
import string
from where2go import load_footer

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align:center; font-size: 48px; font-weight: bold;'>Welcome to Ayodhya- The Sacred City of Shree Ram</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size: 20px;'>Explore Ayodhya's top attractions, vibrant history, and colorful culture in this visual journey.</p>", unsafe_allow_html=True)

images = [
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Ayodhya/shree%20ram.jpg", "Shree Ram Janmabhoomi / Shree Ram Mandir", "The sacred birthplace of Shree Ram, a spiritual centerpiece attracting millions of pilgrims worldwide."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Ayodhya/Hanuman%20Garhi.jpg", "Hanuman Garhi", "Ancient hilltop temple dedicated to Lord Hanuman with panoramic city views."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Ayodhya/Kanak%20Bhawan%20Ayodhya.jpg", "Kanak Bhawan", "Beautiful palace-temple complex believed to have been gifted to Sita by her mother."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Ayodhya/Saryu%20Ghat.jpg", "Saryu Ghat", "A bustling riverfront where pilgrims perform sacred rituals and evening aartis on the holy Sarayu River."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Ayodhya/Mani%20Patvat.jpg", "Mani Parvat", "Sacred hill where Hanuman Ji fell after being struck by Bharat’s arrow and met him"),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Ayodhya/nageshwarnath%20temple%20ayodhya.jpg", "Nageshwarnath Temple", "Famous Lord Shiva temple built by Kush, Lord Rama’s son."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Ayodhya/Guptar%20Ghat.jpg", "Guptar Ghat", "Sacred spot on the Saryu river where Shree Ram took Jal Samadhi"),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Ayodhya/Sita%20ki%20rasoi.jpg", "Sita ki Rasoi", "he legendary kitchen where Goddess Sita is believed to have cooked during her stay in Ayodhya, reflecting royal culinary traditions of the Ramayana era."),

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

            
st.markdown("<h3 class='food-section' style='font-weight:bold; margin-top: 20px;'>🥘 Must-Try Foods in Ayodhya</h3>", unsafe_allow_html=True)

food_names = [
    "Kakori Kebabs",
    "Paneer Pasanda / Shahi Paneer",
    "Kachori & Samosa",
    "Aloo Tikki & Chaat",
    "Roomali Roti",
    "Dal Tadka & Khichdi",
    "Lassi(sweet)",
    "Malai Ghewar(sweet)",
    "Rabri & Jalebi (sweet)",
]


foods_line = " &nbsp; &#8226; &nbsp; ".join(food_names)

st.markdown(
    f"<div class='food-section'>{foods_line}</div>",
    unsafe_allow_html=True,
)

st.markdown("<h3 class='travel-section' style='font-weight:bold; margin-top: 40px;'>🚖 Best Ways to Travel Inside Ayodhya</h3>", unsafe_allow_html=True)

ayodhya_travel_text = """
<ul style='margin-top: 0; max-width: 700px; font-size: 18px;'>
<li>🛺 <strong>Auto Rickshaws & E-Rickshaws:</strong> Best for short distances like Hanuman Garhi, Ram Ki Paidi, and local temples. Fares are generally negotiable; e-rickshaws are eco-friendly and ideal for narrow lanes.</li>
<li>🚌 <strong>Local Buses:</strong> Available for main routes in Ayodhya and nearby towns. Budget-friendly but slower and less frequent than autos or cabs.</li>
<li>🚖 <strong>Private Cabs / App-Based Cabs (Ola, Uber):</strong> Available throughout the city for more comfortable and convenient travel, especially useful for longer distances or airport transfers.</li>
</ul>
"""

ayodhya_travel_tip = """
<div style='background-color: #f0f8ff; padding: 15px; border-radius: 8px; max-width: 700px; font-size: 18px; margin-top: 20px;'>
🌟 <strong>Travel Tip:</strong><br>
Auto and e-rickshaws are ideal for short visits to temples and local sightseeing.<br>
For longer journeys or night travel, private cabs and app-based taxis offer comfort and convenience.<br>
Local buses provide budget options but require patience and route familiarity.
</div>
"""

st.markdown(ayodhya_travel_text, unsafe_allow_html=True)
st.markdown(ayodhya_travel_tip, unsafe_allow_html=True)
st.markdown("<h3 class='travel-section' style='font-weight:bold; margin-top: 40px;'>📅 Best Months to Visit Ayodhya</h3>", unsafe_allow_html=True)

ayodhya_months_text = """
<ul style='margin-top: 0; max-width: 700px; font-size: 18px;'>
<li>🍂 <strong>October – March (Peak Season & Best Weather):</strong> Pleasant and cool weather (10°C to 25°C), ideal for exploring temples and cultural sites comfortably. Festivals include Deepotsav (Diwali), Ram Navami, Holi, and Vivah Panchami. The city is lively, especially during Ram Leela Mahotsav and other religious events.</li>
<li>☀️ <strong>April – June (Summer, Less Crowded):</strong> Hot temperatures (up to 40°C), fewer tourists, and budget-friendly accommodations. Best for travelers who prefer quieter experiences and can plan morning or evening sightseeing to avoid heat.</li>
<li>🌧️ <strong>July – September (Monsoon & Off-Season):</strong> Rainy season brings lush greenery but occasional heavy showers and slippery terrain. Fewer tourists and low prices but limited outdoor activities.</li>
</ul>
"""

travel_tip = """
<div style='background-color: #f0f8ff; padding: 15px; border-radius: 8px; max-width: 700px; font-size: 18px; margin-top: 20px;'>
🌟 <strong>Travel Tip:</strong><br>
For cultural immersion and pleasant weather, visit between October and March.<br>
Summer months offer off-peak benefits but require heat management.<br>
Monsoon travelers can enjoy greenery with packed rain gear and flexible plans.
</div>
"""

st.markdown(ayodhya_months_text, unsafe_allow_html=True)
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
    if st.button("Get Redeem Code for Ayodhya Hotels", key="redeem_code_ayodhya_btn", type="primary", use_container_width=True):
        code = generate_redeem_code()
        st.success(f"Congratulations! Use this redeem code '{code}' to get an exclusive discount on your hotel booking.")
        tripadvisor_url = "https://www.tripadvisor.in/Hotels-g1985445-Ayodhya_Ayodhya_District_Uttar_Pradesh-Hotels.html"
        st.markdown(f"[Click here to book hotels on Tripadvisor and apply your redeem code](<{tripadvisor_url}>)")


load_footer()