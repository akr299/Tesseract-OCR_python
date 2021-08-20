import os
from PIL import Image
import pyocr
import sys

#バンドルから実行されているか判定
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    pass
else:
    print('running in a normal Python process')
    #インストールしたTesseract-OCRのパスを環境変数「PATH」へ追記する。
    #OS自体に設定してあれば以下は不要
    path=r'C:\\Program Files\\Tesseract-OCR'

    #PATHの区切り文字があるか確認する。無ければ追加
    if os.environ['PATH'][-1] != ';':
        os.environ['PATH']=os.environ['PATH']+';'

    #PATHに登録
    os.environ['PATH'] = os.environ['PATH'] + path
 
#pyocrへ利用するOCRエンジンをTesseractに指定する。
tools = pyocr.get_available_tools()
tool = tools[0]

#OCR対象の画像ファイルを読み込む
img = Image.open(sys.argv[1])

img_box = img.crop((252, 457, 360, 483))

#画像から文字を読み込む
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
text = tool.image_to_string(img_box, lang="lets", builder=builder)

#文字を出力
print(text)

 