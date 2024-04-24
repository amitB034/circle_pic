import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw

def ciercle_pic():
    # ファイル選択ダイアログを表示して動画ファイルを選択
    file_path = filedialog.askopenfilename(title="画像ファイルを選択",
                                           filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpeg"), ("All files", "*.*")])
    if not file_path:
        return
    
    image = Image.open(file_path)

    # 新しい画像とマスクの作成
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)

    w, h = image.size
    print(image.size)
    center_x, center_y = w // 2, h // 2
    radius = min(h, w) // 4  # 幅と高さの最小値を基に半径を設定
    print(w,h)
    print(radius)
    print(center_x ,center_y)

    draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), fill=255)

    result = Image.new('RGBA', image.size)
    result.paste(image, mask=mask)

    result.show()

ciercle_pic()