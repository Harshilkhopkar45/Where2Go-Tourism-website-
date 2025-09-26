import streamlit as st
import random
import string
from where2go import load_footer

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align:center; font-size: 48px; font-weight: bold;'>Welcome to Kolkata – The Cultural Capital of India</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size: 20px;'>Explore Kolkata's top attractions, vibrant history, and colorful culture in this visual journey.</p>", unsafe_allow_html=True)

images = [
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Kolkata/victoria%20memorial.jpg", " Victoria Memorial", "A grand marble monument blending British and Mughal styles, the Victoria Memorial is Kolkata’s most iconic landmark surrounded by lush gardens."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Kolkata/Howrah%20Bridge%20Kolkata.jpg", "Howrah Bridge", "Howrah Bridge, an engineering marvel over the Hooghly, is the city’s lifeline and a dazzling sight when lit up at night."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Kolkata/Dakshineswar%20Maa%20Kali.jpg", "Dakshineswar Kali Temple", "The riverside Dakshineswar Kali Temple, dedicated to Goddess Kali, is a sacred spiritual hub with stunning nine-spired architecture."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Kolkata/science%20city%20kolkata.jpg", " Science City, Kolkata", "Science City, one of the world’s largest science centers, offers interactive exhibits, a space theater, and family-friendly fun."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Kolkata/Eden%20Gardens.jpg", "Eden Gardens", "Eden Gardens, the “Mecca of Indian Cricket,” is a bucket-list destination for cricket fans worldwide."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Kolkata/Explore%20Sundarban.jpg", "Sunderban National Park", "Sundarban National Park, a UNESCO World Heritage Site, enchants visitors with boat safaris, mangroves, and the Royal Bengal Tiger."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Kolkata/Indian%20Museum.jpg", "Indian Museum, Kolkata", "The Indian Museum, India’s oldest and largest, houses rare treasures like Egyptian mummies, Mughal paintings, and ancient fossils."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Kolkata/Belur%20Math.jpg", "Belur Math", "Belur Math, spiritual home of the Ramakrishna Mission, symbolizes unity of religions with its unique architecture."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Kolkata/Marble%20Palace.jpg", "Marble Palace", "Marble Palace, a 19th-century mansion, dazzles with marble grandeur, European art, and exquisite sculptures."),
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

            
st.markdown("<h3 class='food-section' style='font-weight:bold; margin-top: 20px;'>🥘 Must-Try Foods in Kolkata</h3>", unsafe_allow_html=True)

food_names = [
    "Kathi Rolls",
    "Puchkas (pani puri)",
    "Chow Mein & Momos",
    "Jhalmuri",
    "Machher Jhol(sea food)",
    "Shutki (Dry Fish Curry)",
    "Ras Gulla (sweet)",
    "Misti Doi (sweet)",
    "Sandesh(sweet)",
]

foods_line = " &nbsp; &#8226; &nbsp; ".join(food_names)

st.markdown(
    f"<div class='food-section'>{foods_line}</div>",
    unsafe_allow_html=True,
)

# Section Heading
st.markdown("<h3 class='travel-section' style='font-weight:bold; margin-top: 40px;'>🚖 Best Ways to Travel Inside Kolkata</h3>", unsafe_allow_html=True)

# Travel Options Content
kolkata_travel_text = """
<ul style='margin-top: 0; max-width: 700px; font-size: 18px;'>
<li>🚇 <strong>Kolkata Metro:</strong> Fastest way to cover long distances across the city. Air-conditioned, avoids traffic jams, economical, and safe.</li>
<li>🛺 <strong>Auto Rickshaws:</strong> Convenient for short distances and areas not served by the metro. Fares usually require bargaining; AC autos are available.</li>
<li>🚖 <strong>Cabs / App Cabs (Ola/Uber):</strong> Comfortable for longer trips or traveling with family. Avoid haggling and get reliable pricing; ideal for night travel.</li>
<li>🚌 <strong>City Buses:</strong> Cheap, cover almost every part of the city. Can be crowded; better for budget travelers familiar with routes.</li>
<li>🚶 <strong>Walking:</strong> Best in heritage areas like College Street, Park Street, Kumartuli, and near Victoria Memorial. Narrow lanes and local markets are easier to explore on foot.</li>
</ul>
"""

# Tourist Tip Section
kolkata_tip = """
<div style='background-color: #f9f9ed; padding: 15px; border-radius: 8px; max-width: 700px; font-size: 18px; margin-top: 20px;'>
🌟 <strong>Tourist Tip:</strong><br>
Use metro for long distances, autos for short hops, and walk in compact heritage areas.<br>
For comfort and convenience, app cabs are ideal, especially if traveling with luggage or family.
</div>
"""

# Display Text
st.markdown(kolkata_travel_text, unsafe_allow_html=True)
st.markdown(kolkata_tip, unsafe_allow_html=True)

# Section Heading
st.markdown("<h3 class='travel-section' style='font-weight:bold; margin-top: 40px;'>📅 Best Months to Travel in Kolkata</h3>", unsafe_allow_html=True)

# Best Months Content
kolkata_months_text = """
<ul style='margin-top: 0; max-width: 700px; font-size: 18px;'>
<li>🍂 <strong>September – October (Durga Puja Season):</strong> The absolute best time to visit Kolkata. The entire city comes alive with grand pandals, lights, cultural events, and traditional festivities. Perfect to experience Kolkata’s cultural heart.</li>
<li>🌞 <strong>November – February (Winter):</strong> Pleasant, cool weather ideal for sightseeing, exploring heritage streets, and enjoying Bengali cuisine. Great for Victoria Memorial, Howrah Bridge, College Street, and riverfront walks.</li>
<li>🌼 <strong>March – April:</strong> Warm but manageable weather. Fewer tourists compared to winter, good for visiting gardens, markets, and cultural trails.</li>
<li>🌧️ <strong>June – August (Monsoon):</strong> Heavy showers with waterlogging in some parts. Not the best for travel, but the city looks beautiful in the rains with lush greenery.</li>
<li>🔥 <strong>May:</strong> Very hot and humid, generally avoided by tourists unless visiting for specific reasons.</li>
</ul>
"""

# Tourist Tip Section
kolkata_months_tip = """
<div style='background-color: #fff3e6; padding: 15px; border-radius: 8px; max-width: 700px; font-size: 18px; margin-top: 20px;'>
🌟 <strong>Travel Tip:</strong><br>
If you want to experience the soul of Kolkata, visit during <strong>Durga Puja (September–October)</strong> when the city is at its most vibrant.<br>
For comfortable sightseeing and cultural exploration, <strong>November to February</strong> is the best season.
</div>
"""

# Display Text
st.markdown(kolkata_months_text, unsafe_allow_html=True)
st.markdown(kolkata_months_tip, unsafe_allow_html=True)

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
    if st.button("Get Redeem Code for Kolkata Hotels", key="redeem_code_kolkata_btn", type="primary", use_container_width=True):
        code = generate_redeem_code()
        st.success(f"Congratulations! Use this redeem code '{code}' to get an exclusive discount on your hotel booking.")
        tripadvisor_url = "https://www.tripadvisor.in/Hotels-g304558-Kolkata_Calcutta_Kolkata_District_West_Bengal-Hotels.html"
        st.markdown(f"[Click here to book hotels on Tripadvisor and apply your redeem code](<{tripadvisor_url}>)")


load_footer()