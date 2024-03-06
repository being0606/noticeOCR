from PIL import Image
import pytesseract

def ocr_tesseract(img_path, lang='kor'):
    # 이미지 불러오기
    img = Image.open(img_path)
    
    # Tesseract로 이미지에서 텍스트 추출
    result = pytesseract.image_to_string(img, lang=lang)
    
    # 결과를 리스트로 변환
    result_list = result.split('\n')
    
    return result_list

img_path = '/asset/test01.jpeg'  # 이 부분에 이미지 경로를 입력해주세요.
print(ocr_tesseract(img_path))