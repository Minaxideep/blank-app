import pandas as pd

# Create sample data
data = {
    "url": [
        "https://google.com",
        "https://youtube.com",
        "https://openai.com",
        "https://github.com",
        "https://google.com"
    ],
    "website_name": [
        "Google",
        "YouTube",
        "OpenAI",
        "GitHub",
        "Google"
    ],
    "visitors": [120, 90, 75, 65, 110],
    "frequency": [12, 8, 5, 6, 14]
}

df = pd.DataFrame(data)
df.to_excel("sample_website_data.xlsx", index=False)
print("Sample Excel file created as 'sample_website_data.xlsx'.")
