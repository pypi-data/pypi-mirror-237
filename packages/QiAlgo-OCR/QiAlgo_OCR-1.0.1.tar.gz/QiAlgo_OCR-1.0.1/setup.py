from setuptools import setup, find_packages

setup(
    name='QiAlgo_OCR',
    version='1.0.1',
    packages=find_packages(),
    package_data={
        'QiAlgo_OCR': ['model/*.onnx']
    },
    install_requires=[
        # 项目需要的依赖项
        'onnxruntime~=1.16.1',
        'Pillow~=10.0.1',
        'torch==2.1.0',
        'torchvision==0.16.0',
        'PyYAML~=6.0.1',
    ],
    author='Morton Li',
    author_email='Morton.L@Outlook.com',
    description='QiAlgo_OCR(青祁OCR)是基于"QiAlgoML青祁机器学习项目"中的神经网络子项目分离开发的Python库，是一种对特定场景进行光学字符识别（Optical Character Recognition，简称OCR）的解决方案。',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Morton-L/QiAlgo_OCR',
    classifiers=[
        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3.11",
    ],
)
