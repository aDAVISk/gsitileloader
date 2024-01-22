
# ref: https://qiita.com/studio_haneya/items/9aad8f9ede11e58b41a8
# ref: https://qiita.com/shonansurvivors/items/0fbcbfde129f2d26301c

from setuptools import setup, find_packages
import os

# long_description(後述)に、GitHub用のREADME.mdを指定
with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gsitileloader',  # パッケージ名（pip listで表示される）
    version="0.0.1",  # バージョン
    description="load tiles from GSI",  # 説明
    author='Akito Davis Kawamura',  # 作者名
    license='MIT',  # ライセンス
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=['numpy', 'xyztilefile'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='gsitileloader gsi gsi-tile xyz-tile xyztile',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)
