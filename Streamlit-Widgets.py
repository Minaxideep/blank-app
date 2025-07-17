import streamlit as st
import pandas as pd

# App title
st.title("🌟 Streamlit Widgets Demo")

# Sidebar for mode switching
st.sidebar.title("🌓 Settings")

theme = st.sidebar.radio("Select Theme:", options=["Day", "Night"])

# Apply theme color
if theme == "Night":
    st.markdown(
        """
        <style>
            body {
                background-color: #0E1117;
                color: white;
            }
        </style>
        """, unsafe_allow_html=True)
    st.success("Night mode activated 🌙")
else:
    st.info("Day mode activated ☀️")

# File uploader widget
st.header("📁 Upload a File")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of Uploaded Data:")
    st.dataframe(df.head())
else:
    st.warning("Please upload a CSV file.")

# Scale / Slider
st.header("🎚️ Scale Control (Slider)")
value = st.slider("Select a value between 0 and 100", min_value=0, max_value=100, value=50)
st.write(f"Selected value: {value}")

# Checkbox
st.header("✅ Checkbox Example")
if st.checkbox("Show extra options"):
    st.write("Extra options are visible now!")

# Select box
st.header("🔽 Select Box Example")
option = st.selectbox("Choose an option:", ["Option A", "Option B", "Option C"])
st.write(f"You selected: {option}")

# Expander with Scrollbar
st.header("🧾 Scrollable Content in Expander")
with st.expander("Click to expand and scroll"):
    st.write("Below is a long text to show the scroll bar:")
    long_text = "This is a long text.\n" * 100
    st.text(long_text)

# Number input
st.header("🔢 Number Input Example")
number = st.number_input("Pick a number", 0, 100, step=1)
st.write(f"You entered: {number}")

# Footer
st.markdown("---")
st.markdown("✅ **Demo Complete! Try interacting with all widgets above.**")
