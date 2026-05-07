import streamlit as st
import random
import string
from where2go import load_footer

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align:center; font-size: 48px; font-weight: bold;'>Welcome to Varanasi – The Spiritual Heart of India</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size: 20px;'>Explore  Varanasi's top attractions, vibrant history, and colorful culture in this visual journey.</p>", unsafe_allow_html=True)

images = [
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Varanasi/Kashi%20%20Vishwanath%20Mandir.jpg", "Kashi Vishwanath Mandir", "One of India’s holiest Shiva temples, revered for its spiritual significance and golden spire."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Varanasi/Dashashwamedh%20Ghat.jpg", "Dashashwamedh Ghat", "The vibrant main ghat on the Ganga, famous for its evening Ganga Aarti ceremony."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Varanasi/Assi%20Ghat%20.jpg", "Assi Ghat", "A lively ghat at the confluence of the Ganga and Assi rivers, popular for morning rituals and boat rides."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Varanasi/Ganga%2C%20Varanasi%20.jpg", "Ganga River, Varanasi", "The sacred river of India, central to Varanasi’s rituals, boat rides, and spiritual experiences."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Varanasi/Bharat%20Mata%20Mandir.jpg", "Bharat Mata Mandir", "Unique temple dedicated to Mother India, featuring a relief map of the country carved in marble."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Varanasi/Sankat%20Mochan%20Mandir.jpg", "Sankat Mochan Hanuman Temple ", "Famous temple dedicated to Lord Hanuman, visited by thousands seeking protection and blessings."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Varanasi/Durga%20temple%2C%20Varanasi%20India.jpg", "Durga Temple", "Historic red sandstone temple honoring Goddess Durga, known for its architectural charm."),
    ("https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Varanasi/Kaal%20Bhairav%20Temple.jpg", "Kaal Bhairav Temple", "Ancient shrine dedicated to Kal Bhairav, considered the guardian deity of Varanasi."),
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

            
st.markdown("<h3 class='food-section' style='font-weight:bold; margin-top: 20px;'>🥘 Must-Try Foods in  Varanasi</h3>", unsafe_allow_html=True)

food_names = [
    "Kachori Sabzi",
    "Aloo Tikki",
    "Baati & Dal",
    "Chaat & Pani Puri",
    "Tamatar Chaat",
    "Banarasi Paan (sweet)",
    "Lassi & Rabri(sweet)",
    "Malaiyo (seasonal sweet)",
]

foods_line = " &nbsp; &#8226; &nbsp; ".join(food_names)

st.markdown(
    f"<div class='food-section'>{foods_line}</div>",
    unsafe_allow_html=True,
)

st.markdown("<h3 class='tourist-section' style='font-weight:bold; margin-top: 40px;'>🚖 Tourist Recommendation: How to Get Around Varanasi</h3>", unsafe_allow_html=True)

travel_text = """
<ul style='margin-top: 0; max-width: 700px; font-size: 18px;'>
<li><strong>For short trips between ghats and temples:</strong> Autos and E-rickshaws are convenient and popular for navigating Varanasi’s narrow lanes and local landmarks.</li>
<li><strong>For budget solo travel:</strong> Use local buses combined with short auto rides for an affordable way to explore the city’s highlights.</li>
<li><strong>✨ Tip:</strong> In the old city near Dashashwamedh & Assi Ghat, walking is often the easiest and most scenic way to get around, soaking in the spiritual vibe and vibrant street life.</li>
</ul>
"""

st.markdown(travel_text, unsafe_allow_html=True)
st.markdown("<h3 class='visit-section' style='font-weight:bold; margin-top: 40px;'>🗓️ Best Months to Visit Varanasi</h3>", unsafe_allow_html=True)

best_month_text = """
<ul style='max-width: 700px; margin-left: 20px; margin-right: auto; font-size: 18px;'>
<li><strong>October – March:</strong> Best overall for pleasant weather, vibrant festivals, and rich cultural experience. Ideal for sightseeing and attending major events like Diwali and Dev Deepawali.</li>
<li><strong>July – September:</strong> Cheapest travel period with fewer tourists. Suitable if you don’t mind occasional rains and enjoy lush green surroundings.</li>
<li><strong>✨ Tourist tip:</strong> Visit the ghats at sunrise for a serene view with fewer crowds. Don’t miss the evening Ganga Aarti at Dashashwamedh Ghat – a deeply spiritual and mesmerizing ceremony.</li>
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

col1, col2, col3 = st.columns([3, 2, 3])
with col2:
    if st.button("Get Redeem Code for Varanasi Hotels", key="redeem_code_varanasi_btn", type="primary", use_container_width=True):
        code = generate_redeem_code()
        st.success(f"Congratulations! Use this code '{code}' for exclusive discounts on Varanasi hotels.")
        


load_footer()
