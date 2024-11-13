# config.py

# 判定フラグ（1の時に処理を実行）
execute_detection = 1

# 設定パターンのリスト
settings_patterns = [
    {"conf": 0.001, "iou": 0.500, "agnostic_nms": False, "max_det": 1000, "use": 0},
    {"conf": 0.010, "iou": 0.500, "agnostic_nms": False, "max_det": 1000, "use": 1},
    {"conf": 0.100, "iou": 0.500, "agnostic_nms": False, "max_det": 1000, "use": 0},
    {"conf": 1.000, "iou": 0.500, "agnostic_nms": False, "max_det": 1000, "use": 0},
    {"conf": 0.100, "iou": 0.100, "agnostic_nms": False, "max_det": 1000, "use": 0},
    {"conf": 0.100, "iou": 0.300, "agnostic_nms": False, "max_det": 1000, "use": 0},
    {"conf": 0.100, "iou": 0.500, "agnostic_nms": False, "max_det": 1000, "use": 0},
    {"conf": 0.100, "iou": 0.800, "agnostic_nms": False, "max_det": 1000, "use": 0},
    {"conf": 0.100, "iou": 1.000, "agnostic_nms": False, "max_det": 1000, "use": 0},
]

# モデル名とモデルファイルの対応と使用フラグ
models = {
    "yolov5n": {"path": "models/yolov5n.pt", "use": 1},
    "yolov5s": {"path": "models/yolov5s.pt", "use": 0},
    "yolov5m": {"path": "models/yolov5m.pt", "use": 0},
    "yolov5l": {"path": "models/yolov5l.pt", "use": 0},
    "yolov5x": {"path": "models/yolov5x.pt", "use": 0},
    "yolov8n": {"path": "models/yolov8n.pt", "use": 1},
    "yolov8s": {"path": "models/yolov8s.pt", "use": 0},
    "yolov8m": {"path": "models/yolov8m.pt", "use": 0},
    "yolov8l": {"path": "models/yolov8l.pt", "use": 0},
    "yolov8x": {"path": "models/yolov8x.pt", "use": 0},
    "yolov10n": {"path": "models/yolov10n.pt", "use": 1},
    "yolov10s": {"path": "models/yolov10s.pt", "use": 0},
    "yolov10m": {"path": "models/yolov10m.pt", "use": 0},
    "yolov10l": {"path": "models/yolov10l.pt", "use": 0},
    "yolov10x": {"path": "models/yolov10x.pt", "use": 0}
}
