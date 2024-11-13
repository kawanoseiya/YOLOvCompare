# 基本イメージの設定
FROM python:3.8

# 必要な依存パッケージをインストール
RUN apt-get update && apt-get install -y libgl1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# YOLOv5のリポジトリをクローン
RUN git clone https://github.com/ultralytics/yolov5.git && cd yolov5 && pip install -r requirements.txt
