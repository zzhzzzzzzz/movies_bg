# 项目打包部署：
# pip freeze
# pip freeze > requirements
# python setup.py sdist

import  setuptools
import glob

print(setuptools.find_packages()) #打包所有*py文件
print(glob.glob('**/*.html',recursive=True)) #递归获取所有html文件模版
print(glob.glob('user/templates/*.html')) #获取html文件模版

setuptools.setup(
    # 基本信息
    name='movie',
    version='1.0.1',
    description='电影数据分析可视化系统',
    author='Zhang Zihao',
    author_email='1336029976@qq.com',
    url='http://47.113.180.127/',

    # 打包文件
    packages=setuptools.find_packages(), # ['movie','movie_list','user'], 直接打包包下的所有*.py文件,不会深入子文件包
    py_modules=['messages','manage'], #打包带上单独的py文件
    data_files=['requirements'],
    python_requires='>=3.6',
)