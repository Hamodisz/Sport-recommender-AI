
import csv
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

def save_to_csv(answers, recommendation):
    os.makedirs("data", exist_ok=True)
    with open("data/results.csv", "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().isoformat(), answers, recommendation])

def generate_image(text):
    img = Image.new("RGB", (800, 600), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((50, 50), text, fill=(0, 0, 0), font=font)
    path = "data/recommendation.png"
    img.save(path)
    return path
