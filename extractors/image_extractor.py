import pytesseract
from PIL import Image
from pathlib import Path

SUPPORTED_FORMATS = [".png", ".jpg", ".jpeg"]

def check_image_quality(text: str) -> dict:
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    total_lines = len(lines)
    if total_lines == 0:
        return {"quality": "bad", "score": 0}
    valid_lines = sum(1 for line in lines if '@' in line or line.count(',') >= 2)
    if total_lines == 0:
        score = 0
    else:
        score = round((valid_lines / total_lines) * 100)

    #counting suspiciously shorter lines
    short_lines = sum(1 for line in lines if len(line) < 10)
    short_ratio = short_lines / total_lines if total_lines > 0 else 0

    if short_ratio > 0.4:
        return {"quality": "poor", "score": score}
    elif short_ratio > 0.2:
        return {"quality": "fair", "score": score}
    else:
        return {"quality": "good", "score": score}

def extract_text_from_image(file_path: str) -> str:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix.lower() not in SUPPORTED_FORMATS:
        raise ValueError(f"Unsupported image format: {path.suffix}. Supported: {SUPPORTED_FORMATS}")

    print(f"Opening image: {file_path}")

    image = Image.open(file_path)

    print(f"Image size: {image.size}, Mode: {image.mode}")
    print(f"Running OCR...")

    text = pytesseract.image_to_string(image)

    if not text.strip():
        raise ValueError("OCR could not extract any text from the image — try anorher image")

    #check quality
    quality = check_image_quality(text)

    if quality["quality"] == "poor":
        print(f"\n WARNING: Image quality is poor (score: {quality['score']}/100)")
        print(f"Some data may be missing or replaced with null")
        print(f"For better results use a clearer, higher resolution image\n")
    elif quality["quality"] == "fair":
        print(f"\nWARNING: Image quality is fair (score: {quality['score']}/100)")
        print(f"Some data may be inaccurate, please verify the results\n")
    else:
        print(f"Image quality looks good (score: {quality['score']}/100)")

    print(f"Extracted {len(text)} characters from the image")
    return text