import streamlit as st
import random
import string
from main import load_footer

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align:center; font-size: 48px; font-weight: bold;'>Welcome to Mumbai – The City of Dreams</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size: 20px;'>Explore Mumbai's top attractions, vibrant history, and colorful culture in this visual journey.</p>", unsafe_allow_html=True)

images = [
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Mumbai/The%20Gateway%20of%20India.jpg", "Gateway of India", "Iconic arch monument overlooking the Arabian Sea, a symbol of Mumbai’s colonial history."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Mumbai/Marine%20Drive.jpg", "Marine Drive", "The famous “Queen’s Necklace,” a seafront boulevard perfect for evening walks."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Mumbai/Juhu%20beach%20.jpg", "Juhu Beach", "Popular seaside hangout known for sunsets and Mumbai’s street food like pav bhaji and bhel puri."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Mumbai/Shri%20Siddhivinayak%20Ganapati%20Mandir.jpg", "Shree Siddhivinayak Temple", "A richly adorned temple dedicated to Lord Ganesha, famed for fulfilling wishes, drawing millions of devotees and celebrities alike for its spiritual aura and architectural beauty."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Mumbai/Elephanta%20Caves.jpg", "Elephanta Caves", "UNESCO World Heritage site with rock-cut temples dedicated to Lord Shiva."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Mumbai/The%20Chhatrapati%20Shivaji%20Maharaj%20Vastu%20Sangrahalaya%2C%20%2C%20Mumbai%2C%20India.jpg", "Chhatrapati Shivaji Maharaj Vastu Sangrahalaya", "Mumbai’s premier museum showcasing art, history, and culture of Maratha Kingdom and Chhatrapati Shivaji Maharaj ."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Mumbai/Shree%20Mahalakshmi%20Temple%20Mumbai%20.jpg", "Mahalaxmi Temple", "Sacred temple dedicated to Goddess Mahalaxmi, blending spirituality with sea views."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Mumbai/Sanjay%20Gandhi%20National%20Park.jpg", "National Park", "A vast green escape within the city, home to Kanheri Caves and diverse wildlife."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Mumbai/Haji%20Ali%20Durgah%2C%20Mumbai.jpg", "Haji Ali Dargah", "Stunning mosque and tomb on the sea, accessible only during low tide."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Mumbai/kaneri%20caves.jpg", "Kanheri Caves", "An ancient complex of rock-cut Buddhist caves dating back over 2,000 years, showcasing monasteries, stupas, and carvings nestled in lush greenery."),
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

            
st.markdown("<h3 class='food-section' style='font-weight:bold; margin-top: 20px;'>🥘 Must-Try Foods in Mumbai</h3>", unsafe_allow_html=True)

food_names = [
    "Vada Pav",
    "Pav Bhaji",
    "Misal Pav",
    "Sev Puri & Bhel Puri",
    "Poha",
    "Puran Poli (sweet)",
    "Berry Pulao(parsi food)",
    "Bombil Fry (seafood)",
    "Pomfret Curry & Surmai Fry (seafood)",
    "Rabdi Falooda (sweet)",
    "Modak & Ladoo (sweet)",
    "Bombay Halwa (famous Thickshakes)",
]

foods_line = " &nbsp; &#8226; &nbsp; ".join(food_names)

st.markdown(
    f"<div class='food-section'>{foods_line}</div>",
    unsafe_allow_html=True,
)

st.markdown("<h3 class='travel-section' style='font-weight:bold; margin-top: 40px;'>🚖 Best Ways to Travel Inside Mumbai</h3>", unsafe_allow_html=True)

travel_text = """
<ul style='margin-top: 0; max-width: 700px; font-size: 18px;'>
<li>🚇 <strong>Mumbai Local Trains:</strong> The city’s lifeline, cheapest and fastest for long distances, but very crowded during peak hours.</li>
<li>🚊 <strong>Mumbai Metro & Monorail:</strong> Modern, air-conditioned, and great for avoiding traffic; expanding routes make it increasingly useful.</li>
<li>🚌 <strong>BEST Buses:</strong> Budget-friendly with a wide network, though slower due to traffic conditions.</li>
<li>🛺 <strong>Auto Rickshaws:</strong> Best for short distances in the suburbs; not allowed in South Mumbai.</li>
<li>🚖 <strong>Kaali Peeli Taxis & App Cabs (Uber/Ola):</strong> Convenient and comfortable for medium to long distances, but pricier during peak hours.</li>
<li>🚶 <strong>Walking / Marine Drive Strolls:</strong> Sometimes faster than traffic in busy areas, plus the best way to soak in local vibes.</li>
</ul>
"""

st.markdown(travel_text, unsafe_allow_html=True)

st.markdown("<h3 class='visit-section' style='font-weight:bold; margin-top: 40px;'>🗓️ Best Months to Visit Mumbai</h3>", unsafe_allow_html=True)

best_month_text = """
<ul style='max-width: 700px; margin-left: 20px; margin-right: auto; font-size: 18px;'>
<li><strong>August – September (Ganesha Chaturthi):</strong> The most vibrant time to visit Mumbai, when the city comes alive with grand celebrations, elaborate decorations, and cultural events honoring Lord Ganesha.</li>
<li><strong>October – February:</strong> Enjoy pleasant weather, ideal for sightseeing, attending other local festivals like Diwali, and exploring the city’s outdoor attractions.</li>
<li><strong>March – May:</strong> Hot and humid months with fewer tourists and attractive hotel deals, suitable for those who prefer quieter stays and indoor activities.</li>
<li><strong>June – September (Monsoon):</strong> Witness Mumbai during the lush monsoon season. The rains add a unique charm but can disrupt outdoor plans.</li>
<li><strong>✨ Tourist Tip:</strong> Plan to visit during Ganesha Chaturthi to experience Mumbai’s cultural heartbeat. Attend the grand processions and immerse in local traditions while enjoying evening walks along Marine Drive in the cooler months.</li>
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
    if st.button("Get Redeem Code for Mumbai Hotels", key="redeem_code_mumbai_btn", type="primary", use_container_width=True):
        code = generate_redeem_code()
        st.success(f"Congratulations! Use this redeem code '{code}' to get an exclusive discount on your hotel booking.")
        tripadvisor_url = "https://www.tripadvisor.in/Hotels-g304554-Mumbai_Maharashtra-Hotels.html"
        st.markdown(f"[Click here to book hotels on Tripadvisor and apply your redeem code](<{tripadvisor_url}>)")


load_footer()