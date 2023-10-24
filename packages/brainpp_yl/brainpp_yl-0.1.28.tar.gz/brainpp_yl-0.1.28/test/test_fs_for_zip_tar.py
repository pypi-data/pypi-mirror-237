import os
import time
import brainpp_yl.fs
import io

# 源码在 https://git-core.megvii-inc.com/yanglei/brainpp_yl/-/blob/master/brainpp_yl/fs.py
# 安装方式 pip install brainpp_yl

# 通过侵入式地替换标准库中的 path 操作为对应的 megfile smart 操作
# 在几乎不改动代码的情况下, 让 Python 程序兼容 oss
brainpp_yl.fs.compat_mode()
# io._io.open = open
# io.open = open
import tarfile
import importlib

importlib.reload(tarfile)

test_dir = "s3://yl-share/tmp/test_fs"

# test_dir = "/tmp/test_fs"


if os.path.exists(test_dir):
    # os.rmdir(test_dir)
    brainpp_yl.fs.smart_remove(test_dir)
    # megfile 没有 os.rmdir 和 shutil.rmtree 完全对齐的 smart 版本

sub_dir = os.path.join(test_dir, "sub_dir")
os.makedirs(sub_dir)
with open(os.path.join(test_dir, "foo.txt"), "w") as f:
    f.write("foo")

with open(os.path.join(sub_dir, "sub_file.txt"), "w") as f:
    f.write("sub_file")


def print_tree(path, indent=""):
    """
    Recursively prints the directory tree rooted at the given path.
    """
    if os.path.isdir(path):
        print(indent + (path) + "/")
        for filename in os.listdir(path):
            print_tree(os.path.join(path, filename), indent + "    ")
    else:
        print(indent + (path))


print_tree(test_dir)

with tarfile.open(test_dir + ".tar.gz", "w:gz") as tar:
    tar.add(test_dir, arcname="")


import zipfile

with zipfile.ZipFile(test_dir + ".zip", "w") as zipObj:
    for foldername, subfolders, filenames in os.walk(test_dir):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            zipObj.write(file_path, arcname=os.path.relpath(file_path, test_dir))
