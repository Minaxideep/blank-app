import streamlit as st
pip install openpyxl
import pandas as pd

st.set_page_config(page_title="Website Visitors Analysis", layout="centered")
st.title("Website Visitors Analysis")

st.write("This tool helps analyze website visit patterns. Upload an Excel file with columns: `url`, `website_name`, `visitors`, `frequency`.")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)

        st.subheader("Uploaded Data")
        st.dataframe(df)

        st.subheader("Summary Statistics")
        st.write(df.describe())

        # Identify the website(s) with the highest frequency
        max_frequency = df["frequency"].max()
        top_sites = df[df["frequency"] == max_frequency]

        st.subheader("Most Frequently Visited Website(s)")
        for _, row in top_sites.iterrows():
            st.write(f"{row['website_name']} ({row['url']}) - {row['frequency']} visits")
            st.markdown("**Badge: Top Visitor**")

        # Grouped analysis
        st.subheader("Grouped Statistics by Website Name")
        grouped_df = df.groupby("website_name")[["visitors", "frequency"]].sum().sort_values(by="frequency", ascending=False)
        st.dataframe(grouped_df)

        # Simple bar chart
        st.subheader("Frequency by Website")
        st.bar_chart(grouped_df["frequency"])

    except Exception as e:
        st.error(f"Error reading the file: {e}")
else:
    st.info("Upload an Excel file to begin.")
