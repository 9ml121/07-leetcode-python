# 批量修改某个文件夹下面的所有图片文件的结尾名称

import os
import random
import re
import uuid

# 指定文件夹路径
# 使用正斜杠表示文件路径，或者使用原始字符串
path = r"D:\BaiduNetdiskWorkspace\07-算法\10-图论&并查集\生成树&并查集"

# 遍历文件夹中的所有文件
for filename in os.listdir(path):
    # 判断文件名是否以"img"开头，".png"结尾
    if re.match(r'img_.*\.png$', filename):
        # 构造新的文件名
        new_filename = "img_" + uuid.uuid4().hex[:8] + ".png"
        # 重命名文件
        os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
