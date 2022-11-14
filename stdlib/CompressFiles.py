import tarfile
import os
import time
backupDate = time.strftime('%Y-%m-%d')
backupString = '/tmp/' + backupDate + '.tar.gz'
# 创建压缩包名
tar = tarfile.open(backupString, "w:gz")
# 创建压缩包
for root, d, files in os.walk("/tmp/tarball"):
    for file in files:
        print(file)
        fullpath = os.path.join(root, file)
        tar.add(fullpath)
    tar.close()

