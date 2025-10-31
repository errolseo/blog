import os
from PIL import Image, ImageChops

def trim_whitespace(image):
    """
    Pillow Image 객체를 받아 흰색(#FFFFFF) 여백을 제거한 이미지를 반환합니다.

    :param image: Pillow Image 객체
    :return: 여백이 제거된 Pillow Image 객체
    """
    # 이미지를 RGBA 모드로 일관되게 변환하여 알파 채널을 보장합니다.
    image = image.convert("RGBA")
    
    # 이미지를 RGB 모드로 변환 (getbbox가 RGB/L 모드에서 작동)
    bg = Image.new("RGB", image.size, (255, 255, 255))
    bg.paste(image, mask=image.split()[3])  # 투명 배경을 흰색으로 채움

    # 색상 반전 후 경계 상자 찾기
    inverted_image = ImageChops.invert(bg)
    bbox = inverted_image.getbbox()
    
    # 경계 상자가 있으면 해당 영역으로 원본 이미지(알파 채널 포함)를 자름
    if bbox:
        return image.crop(bbox)
    else:
        # 이미지가 전체가 흰색인 경우 원본 반환
        return image

def convert_images_to_webp_recursive(root_dir, quality=90, delete_original=False):
    """
    지정된 디렉토리와 모든 하위 디렉토리를 탐색하며 
    이미지 파일의 흰 여백을 제거하고 WebP로 변환합니다.
    """
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".ico"}
    
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            name, extension = os.path.splitext(filename)
            if extension.lower() in image_extensions:
                original_path = os.path.join(dirpath, filename)
                webp_path = os.path.join(dirpath, name + ".webp")

                try:
                    with Image.open(original_path) as img:
                        
                        # ⭐ 흰색 여백 제거 기능 호출
                        trimmed_img = trim_whitespace(img)
                        
                        # 여백이 제거된 이미지를 RGBA로 변환 후 WebP로 저장
                        trimmed_img.convert("RGBA").save(webp_path, "webp", quality=quality)
                    
                    print(f"✅ 변환 및 자르기 성공: {original_path} -> {webp_path}")

                    if delete_original:
                        os.remove(original_path)
                        print(f"🗑️ 원본 삭제: {original_path}")

                except Exception as e:
                    print(f"❌ 처리 실패: {original_path} | 오류: {e}")


if __name__ == "__main__":
    target_directory = "static/images/NLP/4"
    
    # ⚠️ 주의: delete_original=True로 설정하면 원본 파일이 삭제되니, 먼저 백업 후 테스트하세요.
    convert_images_to_webp_recursive(target_directory, quality=90, delete_original=False)