from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests

print("Loading model... (this may take a few seconds)")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


image = Image.open("c:/Users/cpava/OneDrive/Desktop/Project/CodSoft/Image Captioning/img.png")

inputs = processor(images=image, return_tensors="pt")
out = model.generate(**inputs, max_length=50)

caption = processor.decode(out[0], skip_special_tokens=True)
print("\n📝 Generated Caption:")
print(caption)
