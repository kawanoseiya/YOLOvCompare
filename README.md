# YOLO画像検出スクリプト

このスクリプトは、YOLOモデルを使用して画像内の人物領域を検出し、設定に基づいて検出結果を保存します。複数のモデルや設定パターンを柔軟に使用することが可能です。

## 使用方法

### 1. 入力フォルダの設定
`./input` フォルダ内に処理したい画像を配置してください。スクリプトは、拡張子が `.jpg`、`.jpeg`、`.png`、`.bmp` の画像を対象とします。

### 2. モデルの設定
`models` 辞書には、使用するYOLOモデルとそのファイルパス、使用フラグ `use` が含まれます。`"use": 1` に設定するとそのモデルが有効になり、`"use": 0` にすると無効になります。有効なモデルのみが処理されます。

#### モデル設定例：
```python
models = {
    "yolov5n": {"path": "models/yolov5n.pt", "use": 1},
    "yolov5s": {"path": "models/yolov5s.pt", "use": 1},
    # 他のモデルの設定
}
```

### 3. 検出パターンの設定
`settings_patterns` リストには、検出パターンごとの設定が辞書形式で含まれます。各パターンには以下の設定があります：

- `conf`: 検出の信頼度閾値。
- `iou`: 非最大抑制のIoU閾値。
- `agnostic_nms`: クラスに依存しないNMSを使用するかどうか。
- `max_det`: 最大検出数。
- `use`: パターンを有効にするには `1`、無効にするには `0` を設定。

#### パターン設定例：
```python
settings_patterns = [
    {"conf": 0.001, "iou": 0.500, "agnostic_nms": False, "max_det": 1000, "use": 1},
    {"conf": 0.005, "iou": 0.400, "agnostic_nms": True, "max_det": 500, "use": 0},
    {"conf": 0.01, "iou": 0.300, "agnostic_nms": False, "max_det": 2000, "use": 1}
]
```

### 4. 検出処理の実行
`execute_detection = 1` に設定して処理を開始します。スクリプトは有効なモデルとパターンを繰り返し処理し、入力フォルダ内の画像に対してYOLO検出を実行します。

```python
execute_detection = 1
```

### 5. 出力の構造
検出された人物は、以下の方法で保存されます：

- 検出領域のサイズに応じて `extra_large`、`large`、`medium`、`small` フォルダに分類。
- 各人物画像は、520x520ピクセルの白背景にリサイズされて保存。
- 画像は `./output/{model_name}/pattern_{pattern_index}/{size}` のディレクトリ構造で保存されます。

### 6. 実行コマンド

```bash
docker-compose up --build
```

## ディレクトリ構造の例

```plaintext
YOLOvCompare/
├── docker/               # dockerファイル
├── input/                # 入力画像を配置
├── models/               # YOLOモデルファイル（例: yolov5n.pt, yolov8s.pt）
└── output/               # モデルとパターンごとの出力
```

スクリプトを実行すると、指定したモデルと設定で画像処理が始まります。
