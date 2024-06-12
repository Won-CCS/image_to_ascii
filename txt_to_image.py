from PIL import Image, ImageDraw, ImageFont

def txt_to_image(txt_file, image_file, font_path=None, font_size=6):
    # テキストファイルの読み込み
    with open("to_txt/" + txt_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # フォントの設定（デフォルトフォントを使用）
    if font_path is None:
        font = ImageFont.load_default()
    else:
        font = ImageFont.truetype(font_path, font_size)
    
    # 画像サイズの計算
    lines = text.split('\n')
    max_line_length = max(len(line) for line in lines)
    image_width = max_line_length * font_size
    image_height = len(lines) * font_size

    # 画像の作成
    image = Image.new('RGB', (image_width, image_height), color='white')
    draw = ImageDraw.Draw(image)

    # テキストを画像に描画
    for i, line in enumerate(lines):
        draw.text((0, i * font_size), line, font=font, fill='black')

    # 画像を保存
    image.save("to_image/" + image_file)
