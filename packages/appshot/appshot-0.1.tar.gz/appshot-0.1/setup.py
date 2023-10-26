#!/usr/bin/env python
# coding:utf-8

from setuptools import find_packages, setup

setup(
name='appshot',
version='0.1',
description='ScreenShot for target window. Identy window by 1.front 2.title 3.clsname 4.hwnd. Based on win32api. Only screenshot the window not all screen and not crop.',
author_email='2229066748@qq.com',
maintainer="Eagle'sBaby",
maintainer_email='2229066748@qq.com',
packages=find_packages(),
platforms=["windows"],
license='Apache Licence 2.0',
classifiers=[
'Programming Language :: Python',
'Programming Language :: Python :: 3',
],
keywords = ['screenshot', 'utils'],
python_requires='>=3',
install_requires=[
    "pywin32"
],
)
