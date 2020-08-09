import pytesseract
from PIL import Image

# img = Image.open('phone_number.png')
# img = Image.open('eng_text.png')
img = Image.open('rus_text.jpg')
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

file_name = img.filename
file_name = file_name.split(".")[0]

# custom_config = r'--oem 3 --psm 13'
custom_config = r'--oem 3 --psm 6'

text = pytesseract.image_to_string(img, lang='rus', config=custom_config)
print(text)

with open(f'{file_name}.txt', 'w') as text_file:
    text_file.write(text)