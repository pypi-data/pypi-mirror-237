# -*- coding: utf-8 -*-
"""
@Author : zhang.yonggang
@File   : setup.py.py
@Project: pydlt_plus
@Time   : 2023-10-26 08:28:01
@Desc   : The file is ...
@Version: v1.0
"""
from setuptools import setup

setup(
    name='pydlt_plus',
    version='1.0.0',
    author='Arthur Nostmabole Zhang',
    author_email='nostmabole@sina.com',
    description='A class to read and filter DLT message from DLT file BASE ON DltFileReader.',
    long_description='''A class to read and filter DLT message from DLT file BASE ON DltFileReader.''',
    url='https://gitee.com/nostmabole/pydlt_plus',
    packages=['pydlt_plus'],
    install_requires=[
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
