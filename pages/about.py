import streamlit as st
from where2go import load_footer

# Page configuration - MUST be first Streamlit command
st.set_page_config(
    page_title="About Us - Where2Go Tourism",
    page_icon="ℹ️",
    layout="wide"
)

# Hide Streamlit branding (optional)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Page header
st.title("ℹ️ About Where2Go Tourism")
st.markdown("---")

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ## 🏢 Our Story
    
    Where2Go Tourism was founded with a passion for showcasing India's incredible diversity 
    to travelers from around the world. Our journey began with a simple belief: every traveler 
    deserves authentic, memorable experiences that go beyond the ordinary tourist trail.
    
    ## 🎯 Our Mission
    
    To make India's rich cultural heritage, stunning landscapes, and vibrant traditions 
    accessible to every traveler through carefully curated experiences and expert guidance.
    
    ## 💎 Our Values
    
    - **🏆 Authenticity**: We provide genuine cultural experiences
    - **⭐ Excellence**: We maintain the highest standards in service  
    - **🌱 Sustainability**: We promote responsible tourism
    - **🚀 Innovation**: We constantly improve our offerings
    """)

with col2:
    st.image(
        "https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/About_us.jpg",
        caption="About Us",
        use_container_width=True
    )

# Why choose us section
st.markdown("---")
st.markdown("## ✨ Why Choose Where2Go?")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 👨‍🏫 Expert Guidance
    - 10+ years of experience
    - Local expert guides
    - Personalized itineraries
    - Cultural insights
    """)

with col2:
    st.markdown("""
    ### 💎 Premium Quality
    - Handpicked destinations
    - Luxury accommodations
    - Authentic experiences
    - Safety guaranteed
    """)

with col3:
    st.markdown("""
    ### 🤝 Customer First
    - 24/7 support
    - Best price guarantee
    - 500+ happy customers
    - Flexible bookings
    """)

# Statistics section
st.markdown("---")
st.markdown("## 📊 Our Achievements")

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.metric("Happy Customers", "500+", "50 this month")

with metric_col2:
    st.metric("Destinations Covered", "50+", "5 new added")

with metric_col3:
    st.metric("Years of Experience", "10+", "Growing strong")

with metric_col4:
    st.metric("Customer Satisfaction", "98%", "2% increase")

# Team section
st.markdown("---")
st.markdown("## 👥 Meet Our Team")

st.markdown("""
Our team consists of passionate travel experts, local guides, and customer service 
professionals who are dedicated to making your Indian adventure unforgettable.

**Travel Experts**: Craft personalized itineraries  
**Local Guides**: Share authentic cultural insights  
**Support Team**: Available 24/7 for assistance  
**Safety Coordinators**: Ensure your wellbeing throughout the journey
""")

# FOOTER FUNCTION - This is the working footer
load_footer()
