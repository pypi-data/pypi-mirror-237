#!/usr/bin/env python
# coding: utf-8
import os
import pip
def update_software(package_name):
    # 检查当前安装的版本
    print("正在检查更新...") 
    pip.main(['install', package_name, '--upgrade'])
    print("\n更新操作完成，您可以开展工作。")

package_name="treadtools"

package_names=package_name+".py"
update_software(package_name)


current_directory =str (os .path .abspath (__file__ )).replace (str (__file__ ),"")#line:60
file_path = os.path.join(current_directory, package_names)

os.system(f"python {file_path}")
