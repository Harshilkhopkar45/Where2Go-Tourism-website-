import streamlit as st
import random
import string
from main import load_footer

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align:center; font-size: 48px; font-weight: bold;'>Welcome to Hyderabad - City of Nizams</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size: 20px;'>Explore Hyderbad's top attractions, vibrant history, and colorful culture in this visual journey.</p>", unsafe_allow_html=True)

images = [
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Hyderbad/Golconda%20Fort.jpg", "Golconda Fort", "A historic fort known for its impressive architecture and acoustics. Don't miss the light and sound show that narrates its fascinating history. "),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Hyderbad/Ramoji%20Film%20City.jpg", "Ramoji Film City", " One of the largest film studio complexes in the world, offering guided tours, live shows, and various attractions. It's a great place for families and movie enthusiasts."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Hyderbad/Charminar%2C%20Hyderabad.jpg", "Charminar", " An iconic symbol of Hyderabad, this 16th-century mosque features stunning architecture and is surrounded by bustling markets. "),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Hyderbad/Salar%20Jung%20museum%20.jpg", "Salar Jung Museum", "Home to a vast collection of art and artifacts, including the famous Veiled Rebecca. "),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Hyderbad/Birla.jpg", "Birla Mandir", "A beautiful temple made of white marble, dedicated to Lord Venkateshwara, offering serene views of the city. "),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Hyderbad/nehru%20zoological%20park.jpg",  "Nehru Zoological Park","A well-maintained zoo that is home to a variety of animals and is perfect for a family outing."),
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

            
st.markdown("<h3 class='food-section' style='font-weight:bold; margin-top: 20px;'>🥘 Must-Try Foods in Hyderabad</h3>", unsafe_allow_html=True)

food_names = [
    "Hyderabadi Biryani",
    "Mutton Haleem",
    "Butter Chicken",
    "Osmania Biscuits",
    "Chicken 65",
    "Char Koni Naan with Mutton Paya",
    "Qubani Ka Meetha (sweet)",
    "Jouzi Halwa (sweet)",
]

foods_line = " &nbsp; &#8226; &nbsp; ".join(food_names)

st.markdown(
    f"<div class='food-section'>{foods_line}</div>",
    unsafe_allow_html=True,
)
st.markdown("<h3 class='visit-section' style='font-weight:bold; margin-top: 40px;'>🚗 Best Travelling Options in Hyderabad</h3>", unsafe_allow_html=True)

travel_options_text = """
<p style='font-size: 18px;'>
Hyderabad offers a variety of transportation modes to suit different preferences and budgets:
</p>
<ul style='font-size: 18px;'>
<li><strong>Metro Rail:</strong> The Hyderabad Metro is a fast, affordable, and comfortable option covering major parts of the city including Hitech City, Ameerpet, and Secunderabad.</li>
<li><strong>Public Buses:</strong> Operated by TSRTC, buses run frequently with options including ordinary, deluxe, and air-conditioned services, ideal for budget travellers.</li>
<li><strong>Auto Rickshaws:</strong> Convenient for short distances and available throughout the city. Prefer prepaid or app-based autos for fair pricing.</li>
<li><strong>App-Based Cabs:</strong> Services like Ola and Uber provide easy, safe, and comfortable rides with fare estimates upfront and cashless payment options.</li>
<li><strong>Local Trains (MMTS):</strong> Suitable for commuters traveling between key railway stations like Secunderabad, Kacheguda, and Falaknuma.</li>
<li><strong>Airport Transfers:</strong> Various taxi services including prepaid taxis, app-based cabs, and airport shuttles operate to and from Rajiv Gandhi International Airport.</li>
</ul>
<p style='font-size: 18px;'>
Tips: For short city sightseeing use autos or app-based autos. Use metro or buses for longer city travels, and opt for Ola/Uber for airport transfers or outstation trips.
</p>
"""

st.markdown(travel_options_text, unsafe_allow_html=True)


st.markdown("<h3 class='visit-section' style='font-weight:bold; margin-top: 40px;'>🗓️ Best Month(s) to Visit Hyderabad</h3>", unsafe_allow_html=True)

best_month_text = """
<p style='margin-top: 0; font-size: 18px; max-width: auto;'>
The best time to visit Hyderabad is during the <strong>Winter season from October to February</strong>, when temperatures range from 13°C to 30°C with clear skies and cool evenings. This period is ideal for exploring Hyderabad's rich history, cultural landmarks, and festivals.
</p>
<ul style='margin-top: 0; max-width: auto; font-size: 18px;'>
<li><strong>Winter (October to February):</strong> Perfect weather for sightseeing and outdoor activities with pleasant, cool evenings.</li>
<li><strong>Monsoon (July to September):</strong> Temperatures between 22°C and 31°C, with moderate to heavy rainfall making travel less convenient but adding lush greenery to the city.</li>
<li><strong>Festivals & Events:</strong></li>
<ul>
<li><strong>Bathukamma Festival (September/October):</strong> A vibrant floral festival celebrated by women, featuring colorful floral decorations and cultural performances.</li>
<li><strong>Bonalu Festival (July/August):</strong> A traditional festival honoring the goddess Mahakali, celebrated with grand processions, rituals, and offerings.</li>
</ul>
</ul>
<p style='font-size: 18px;'>
Avoid the extremely hot summer months from March to June, when temperatures often rise above 40°C, making outdoor activities uncomfortable.
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
    if st.button("Get Redeem Code for Hyderabad Hotels", key="redeem_code_hyderabad_btn", type="primary", use_container_width=True):
        code = generate_redeem_code()
        st.success(f"Congratulations! Use this code '{code}' for exclusive discounts on Hyderabad hotels.")
        tripadvisor_url = "https://www.tripadvisor.in/Hotels-g297586-Hyderabad-Hotels.html"
        st.markdown(f"[Book Hyderabad hotels here on Tripadvisor](<{tripadvisor_url}>)")


load_footer()