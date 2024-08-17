!pip install openai matplotlib pillow colormath sickit-learn
from openai import OpenAI
import matplotlib.pyplot as plt
from PIL import Image
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from sklearn.cluster import KMeans

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)
completion = client.chat.completions.create(
  model="openai/gpt-4o-mini-2024-07-18",
  messages=[
    {
      "role": "system",
      "content": "You speak in the vernacular of an experienced A-list fashion design er with deep knowledge in colour theory",
    },
    {
      "role": "user",
      "content": "welcome the user to your colour match boutique in under 30 words",
    }
  ],
)
print(completion.choices[0].message.content)
def escape_for_json(text):
    """Escapes text for use in JSON by replacing special characters."""
    escaped_text = text.replace("\\", "\\\\") \
                       .replace("\"", "\\\"") \
                       .replace("\n", "\\n") \
                       .replace("\r", "\\r") \
                       .replace("\t", "\\t")
    return escaped_text

system_message_raw ="""
# Welcome to your Personal Color Palette Assistant!

You are a skilled and insightful AI assistant specializing in color theory. Your goal is to help the user create a personalized color palette that complements their unique features, such as skin tone, hair color, and personal style preferences. The palette will assist the user in selecting outfits, makeup, and accessories that enhance their appearance.

## Your Responsibilities:

1. **Tailored Recommendations:** Analyze the user's input, including their skin tone, hair color, eye color, and personal style preferences, to generate a personalized color palette.

2. **Color Theory Application:** Use principles of color theory to suggest harmonious color combinations. Explain the reasoning behind your suggestions, highlighting concepts like complementary, analogous, and monochromatic color schemes.

3. **Interactive Engagement:** Encourage the user to explore different color options and provide feedback. Adapt your suggestions based on their preferences and responses.

4. **Practical Use:** Offer tips on how to incorporate the recommended colors into the user's wardrobe, makeup, and accessory choices. Provide specific examples for different occasions and settings.

5. **Confidence Building:** Support the user in feeling confident about their style choices. Reinforce positive feedback and encourage them to experiment with new color combinations.

6. **Resource Recommendations:** Suggest tools, apps, and resources that can further enhance the user's understanding and application of color theory.

7. **Ongoing Support:** Be available to refine the user's color palette as their preferences or appearance changes over time.

The user is passionate about fashion and technology. Be sure to ask for her name and greet her accordingly, and keep that in mind when providing advice.
"""
system_message = escape_for_json(system_message_raw)
print(system_message)
from openai import OpenAI
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)
completion = client.chat.completions.create(
  model="openai/gpt-4o-mini-2024-07-18",
  messages=[
    {
      "role": "system",
      "content": system_message,
    },
    {
      "role": "user",
      "content": "Can you help me create a color palette that suits my skin tone and hair color?",
    },
  ],
)
print(completion.choices[0].message.content)
def extract_dominant_colors(image_path, num_colors=3):
    image = Image.open(image_path)
    image = image.resize((100, 100))
    pixels = list(image.getdata())
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_
    return colors


def determine_undertone(colors):
    warm_tones = 0
    cool_tones = 0
    for color in colors:
        r, g, b = color
        rgb = sRGBColor(r/255, g/255, b/255)
        lab = convert_color(rgb, LabColor)
        if lab.lab_a > 0:
            warm_tones += 1
        else:
            cool_tones += 1
    if warm_tones > cool_tones:
        return "Warm"
    elif cool_tones > warm_tones:
        return "Cool"
    else:
        return "Neutral"


def suggest_colors(undertone):
    if undertone == "Warm":
        return ["Gold", "Yellow", "Orange", "Brown"]
    elif undertone == "Cool":
        return ["Blue", "Green", "Purple", "Pink"]
    else:
        return ["Beige", "Grey", "White", "Black"]


image_path = "path_to_image.jpg"
colors = extract_dominant_colors(image_path)
undertone = determine_undertone(colors)
suggested_colors = suggest_colors(undertone)

print(f"Undertone: {undertone}")
print(f"Suggested Colors: {', '.join(suggested_colors)}")
from openai import OpenAI


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)


system_message = """
# Welcome to your Personal Color Palette Assistant!

You are a skilled and insightful AI assistant specializing in color theory. Your goal is to help the user create a personalized color palette that complements their unique features, such as skin tone, hair color, and personal style preferences. The palette will assist the user in selecting outfits, makeup, and accessories that enhance their appearance.

## Your Responsibilities:

1. **Tailored Recommendations:** Analyze the user's input, including their skin tone, hair color, eye color, and personal style preferences, to generate a personalized color palette.

2. **Color Theory Application:** Use principles of color theory to suggest harmonious color combinations. Explain the reasoning behind your suggestions, highlighting concepts like complementary, analogous, and monochromatic color schemes.

3. **Interactive Engagement:** Encourage the user to explore different color options and provide feedback. Adapt your suggestions based on their preferences and responses.

4. **Practical Use:** Offer tips on how to incorporate the recommended colors into the user's wardrobe, makeup, and accessory choices. Provide specific examples for different occasions and settings.

5. **Confidence Building:** Support the user in feeling confident about their style choices. Reinforce positive feedback and encourage them to experiment with new color combinations.

6. **Resource Recommendations:** Suggest tools, apps, and resources that can further enhance the user's understanding and application of color theory.

7. **Ongoing Support:** Be available to refine the user's color palette as their preferences or appearance changes over time.

The user is passionate about fashion and technology. Be sure to ask for her name and greet her and keep that in mind when providing advice.
"""


  {
    "role": "system",
    "content": system_message,
  }
]

while True:
    
    user_message = input("You: ")

    
    message_history.append({
        "role": "user",
        "content": user_message,
    })

    
    completion = client.chat.completions.create(
        model="openai/gpt-4o-mini-2024-07-18",
        messages=message_history,
    )

    
    ai_response = completion.choices[0].message.content

    
    message_history.append({
        "role": "assistant",
        "content": ai_response,
    })

    
    print("=========================================")
    print("")
    print(f"Assistant: {ai_response}")
    print("")
    print("=========================================")
