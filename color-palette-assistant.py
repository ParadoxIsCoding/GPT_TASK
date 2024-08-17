import matplotlib.pyplot as plt
from PIL import Image
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from sklearn.cluster import KMeans
from openai import OpenAI

def extract_dominant_colors(image_path, num_colors=3):
    image = Image.open(image_path)
    image = image.resize((100, 100))
    pixels = list(image.getdata())
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_
    return colors

def determine_undertone(colors):
    warm_tones = sum(1 for color in colors if convert_color(sRGBColor(*(c/255 for c in color)), LabColor).lab_a > 0)
    cool_tones = len(colors) - warm_tones
    return "Warm" if warm_tones > cool_tones else "Cool" if cool_tones > warm_tones else "Neutral"

def suggest_colors(undertone):
    color_suggestions = {
        "Warm": ["Gold", "Yellow", "Orange", "Brown"],
        "Cool": ["Blue", "Green", "Purple", "Pink"],
        "Neutral": ["Beige", "Grey", "White", "Black"]
    }
    return color_suggestions[undertone]

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

system_message = """
You are a skilled AI assistant specializing in color theory. Help users create personalized color palettes based on their features and preferences. Provide tailored recommendations, apply color theory principles, engage interactively, offer practical use tips, build confidence, recommend resources, and provide ongoing support.
"""

message_history = [{"role": "system", "content": system_message}]

while True:
    user_message = input("You: ")
    message_history.append({"role": "user", "content": user_message})
    
    completion = client.chat.completions.create(
        model="openai/gpt-4o-mini-2024-07-18",
        messages=message_history
    )
    
    ai_response = completion.choices[0].message.content
    message_history.append({"role": "assistant", "content": ai_response})
    
    print("\n=========================================")
    print(f"Assistant: {ai_response}")
    print("=========================================\n")
