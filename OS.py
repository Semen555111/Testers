import os
dir_path1 = "C:\\Users\\Семён\\Downloads\\Telegram Desktop"
dir_p1 = os.listdir(dir_path1)
for f in dir_p1:
    if f.endswith('.jpg') or f.endswith('.png') \
    or f.endswith('.pdf') or f.endswith('.docx') \
    or f.endswith('.mp4') or f.endswith('.mp3')\
    or f.endswith('.xls') or f.endswith('.xlsx')\
    or f.endswith('.rar') or f.endswith('.zip') or f.endswith('.HEIC')\
    or f.endswith('.PNG') or f.endswith('.JPG'):
        os.remove(os.path.join(dir_path1,f))
dir_path2 = 'C:\\Users\\Семён\\Desktop'
dir_p2 = os.listdir(dir_path2)
for f in dir_p2:
    if f.endswith('.jpg') or f.endswith('.pdf')\
    or f.endswith('.docx') or f.endswith('.webp') or f.endswith('.cpp')\
    or f.endswith('.mp4') or f.endswith('.mp3'):
        os.remove(os.path.join(dir_path2,f))
dir_path3 = 'C:\\WINDOWS\\Temp'
dir_p3 = os.listdir(dir_path3)
for f in dir_p3:
    if f.endswith('.tmp') or f.endswith('.ses')\
    or f.endswith('.json') or f.endswith('.xml')\
    or f.endswith('.cache') or f.endswith('.bak')\
    or f.endswith('.dat'):
        os.remove(os.path.join(dir_path3,f))


