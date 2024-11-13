# main.py

from ultralytics import YOLO
from PIL import Image, ImageOps
import os
from config import execute_detection, settings_patterns, models

# 入力フォルダ
input_folder = "./input"

# 画像内の人物領域を検出して保存する関数
def detect_and_save(image_path, output_folder, model, settings):
    image = Image.open(image_path).convert("RGB")

    results = model.predict(image, conf=settings["conf"], iou=settings["iou"],
                            agnostic_nms=settings["agnostic_nms"], max_det=settings["max_det"])
    detections = results[0].boxes.data.cpu().numpy()

    for i, det in enumerate(detections):
        x1, y1, x2, y2, conf, cls = det[:6]
        if int(cls) == 0:  # COCOで人のクラスIDは0
            person_crop = image.crop((x1, y1, x2, y2))
            white_background = Image.new("RGB", (520, 520), (255, 255, 255))
            person_crop = ImageOps.fit(person_crop, (520, 520), centering=(0.5, 0.5))
            white_background.paste(person_crop, (0, 0))

            # 共通の出力フォルダに保存
            output_path = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(image_path))[0]}_{i + 1}.jpg")
            white_background.save(output_path)
            print(f"人物画像を保存: {output_path}")

if execute_detection == 1:
    for model_name, model_info in models.items():
        if model_info["use"] == 1:
            model = YOLO(model_info["path"])

            for idx, settings in enumerate(settings_patterns):
                if settings["use"] == 1:
                    output_folder = f"./output/{model_name}/pattern_{idx+1}"
                    os.makedirs(output_folder, exist_ok=True)

                    for filename in os.listdir(input_folder):
                        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
                            image_path = os.path.join(input_folder, filename)
                            detect_and_save(image_path, output_folder, model, settings)

                    print(f"{model_name}の設定パターン {idx+1} の処理が完了しました。")
