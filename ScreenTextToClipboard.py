import pyautogui
import pytesseract
import pyperclip
from PIL import Image

while(0 == 0):
    input("Press Enter to Copy Screen Text")

    # Take a screenshot and save it as 'screenshot.png'
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')

    # Use pytesseract to extract text from the screenshot
    image = Image.open('screenshot.png')
    extracted_text = pytesseract.image_to_string(image)

    # Put the extracted text into the clipboard
    pyperclip.copy(extracted_text)

    print("Text extracted from the screenshot has been copied to the clipboard.\n")