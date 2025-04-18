from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64

client = genai.Client(api_key="")

contents = ("'Two Jedi knights, one in her late 30s, is an East Asian woman who holds a blue lightsaber and pushes her left foot forward in a fierce position, and the other in her late 20s, is of Western descent, holding a red lightsaber and in a defensive position. The female Jedi have braided dark brown hair, have dark gray eyes and sharp expressions, and wore leather armor with dark blue and gold decorations. The male Jedi had short blonde hair, blue eyes, and a determined expression, wore light brown leather armor and a dark gray cape. The red planet's surface, where lava flows, cracked black rocks, and hot orange lava are set in the background. With low-angle shots that capture very dynamic moments, the movement of the two Jedi and the trajectory of the lightsaber are dynamically expressed. The dramatic lighting is focused on the female Jedi, and the intense red and blue contrast catches the eye. It maintains the style of science fiction fantasy genres like Star Wars, and must express surreal atmospheres and dynamic actions. It vividly expresses the Jedi's movements and facial expressions by using high resolution, 8k, detailed textural expressions, and rich colors.  It expresses a very dynamic and grand atmosphere.'")

response = client.models.generate_content(
    model="gemini-2.0-flash-exp-image-generation",
    contents=contents,
    config=types.GenerateContentConfig(
      response_modalities=['TEXT', 'IMAGE']
    )
)

for part in response.candidates[0].content.parts:
  if part.text is not None:
    print(part.text)
  elif part.inline_data is not None:
    image = Image.open(BytesIO((part.inline_data.data)))
    image.save('gemini-native-image.png')
    image.show()