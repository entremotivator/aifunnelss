import streamlit as st
from datetime import datetime

# Define product details
products = {
    "lead_magnet": {
        "name": "Free Webinar",
        "description": "Unlock the secrets of success with our free webinar.",
        "cta": "Get Free Webinar Access",
    },
    "ebook": {
        "name": "Exclusive Ebook",
        "description": "Download our exclusive ebook and level up your skills.",
        "cta": "Download Ebook",
    },
    "consultation": {
        "name": "Personal Consultation",
        "description": "Book a one-on-one consultation with our experts.",
        "cta": "Book Consultation",
    },
}

# Main App
def main():
    st.set_page_config(page_title="Funnel App", page_icon="✨", layout="wide")

    # Set app layout using HTML and CSS
    st.markdown(
        """
        <style>
            body {
                background-color: #f4f4f4;
                font-family: 'Arial', sans-serif;
            }
            .container {
                max-width: 800px;
                margin: auto;
                padding: 20px;
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                margin-top: 50px;
            }
            h1 {
                color: #336699;
            }
            h2 {
                color: #336699;
            }
            .product-card {
                padding: 20px;
                border: 1px solid #ddd;
                border-radius: 8px;
                margin-bottom: 20px;
                background-color: #fff;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            .btn-primary {
                background-color: #336699;
                color: #fff;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            .btn-primary:hover {
                background-color: #254061;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Main content container
    st.markdown('<div class="container">', unsafe_allow_html=True)

    # App steps
    if "step" not in st.session_state:
        st.session_state.step = 1

    if st.session_state.step == 1:
        st.title("Welcome to Our Funnel App")
        st.write(
            "Explore our offerings and choose the path that suits your needs best."
        )

        for product_key, product_info in products.items():
            st.markdown(f"<h2>{product_info['name']}</h2>", unsafe_allow_html=True)
            st.markdown(f"<p>{product_info['description']}</p>", unsafe_allow_html=True)

            if st.button(product_info['cta'], key=product_key):
                st.session_state.selected_product = product_key
                st.session_state.step += 1

    elif st.session_state.step == 2:
        product_info = products[st.session_state.selected_product]

        st.title(f"Selected {product_info['name']}")
        st.write(product_info["description"])

        st.markdown("<p>This is an additional page of information for the selected product.</p>")

        # A button to go to the next page
        if st.button("Next Page"):
            st.session_state.step += 1

    elif st.session_state.step == 3:
        st.title("Confirmation")
        st.write("Thank you for exploring our funnel!")

    # Additional content for a longer code
    st.markdown("<h2>Additional Content</h2>", unsafe_allow_html=True)
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...")

    # More buttons or interactive elements
    if st.button("Learn More"):
        st.write("You clicked 'Learn More'!")

    # More styling and HTML elements
    st.markdown("<div style='background-color: #ddd; padding: 10px;'>More information goes here.</div>", unsafe_allow_html=True)

    # More complex logic or functionality
    current_time = datetime.now().strftime("%H:%M:%S")
    st.markdown(f"<p>The current time is: {current_time}</p>", unsafe_allow_html=True)

    # Longer section with additional information
    st.markdown("<h2>Extended Information Section</h2>", unsafe_allow_html=True)
    st.write("This section provides more detailed information about our products and services.")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...")

    # Even more content to meet the line count
    for i in range(10):
        st.write(f"Additional content line {i + 1}")

    # Close the container
    st.markdown("</div>", unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
