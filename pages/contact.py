import streamlit as st
from where2go import load_footer

# Page setup
st.set_page_config(page_title="Contact Us - Where2Go Tourism", page_icon="📞", layout="wide")

# Title
st.title("📞 Contact Where2Go Tourism")
st.markdown("---")
st.markdown(
    """
    <style>
    .contact-banner {
        width: 100%;         /* full width */
        max-height: 800px;   /* adjust height */
        object-fit: cover;   /* crop nicely if too tall */
        border-radius: 10px; /* optional rounded corners */
    }
    </style>
    <img src="https://github.com/Harshilkhopkar45/Where2Go-Tourism-website-/raw/main/Photos/Conatact.jpg" 
         alt="Contact Banner" class="contact-banner">
    """,
    unsafe_allow_html=True
)


# Two column layout
col1, col2 = st.columns([1, 1])

# Left column - Contact info
with col1:
    st.markdown("""
    <div style="font-size:20px; line-height:1.9;">
    <strong>🌟 Why Choose Where2Go?</strong><br>
    ✅ Expert local guides<br>
    ✅ Authentic experiences<br>
    ✅ Best price guarantee<br>
    ✅ 24/7 customer support
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📧 Get in Touch")
    st.markdown("""
    - **Email**: contact@where2go.com  
    - **Phone**: +91 96627 XXXXX  
    - **Socials**: [Instagram](https://instagram.com) | [Facebook](https://facebook.com) | [Twitter](https://twitter.com)
    """)

# Right column - Interactive form
with col2:
    st.markdown("### ✍️ Send Us a Message")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        query = st.text_area("Your Message / Query")

        submitted = st.form_submit_button("Send Message")
        if submitted:
            if name and email and query:
                st.success(f"✅ Thank you, {name}! We have received your message. Our team will reply soon.")
            else:
                st.error("⚠️ Please fill in all fields before submitting.")

# Footer
st.markdown("---")
load_footer()


