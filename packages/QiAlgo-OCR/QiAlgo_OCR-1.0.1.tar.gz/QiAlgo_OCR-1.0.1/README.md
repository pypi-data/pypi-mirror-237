# QiAlgo青祁

## About 关于

QiAlgo_OCR (青祁OCR)是基于 `QiAlgoML 青祁机器学习` 项目中的神经网络子项目分离开发的 Python 库，是一种对特定场景进行光学字符识别（Optical Character Recognition，简称OCR）的解决方案。

QiAlgo_OCR 擅长序列到序列（Sequence-to-Sequence）任务，或者说场景文本识别（Scene Text Recognition）任务，用于提取在复杂背景中的文本。 例如对验证码的识别、对车牌号码的识别等任务。

在此发布的版本将针对图形验证码的识别任务进行强化，用于快速检验图形验证码的可靠程度。通过对大批量的随机数据进行神经网络训练，以实现高效、快速的评估。

## 使用到的依赖

| 名称          | 版本     | 用途                       |
|-------------|--------|--------------------------|
| onnxruntime | 1.16.1 | ONNX 运行时，用于加载模型。         |
| Pillow      | 10.0.1 | Python 图像处理              |
| torch       | 2.1.0  | PyTorch 项目，用于实现硬件类型识别等功能 |
| torchvision | 0.16.0 | PyTorch 项目的一部分，用于图像预处理。  |
| PyYAML      | 6.0.1  | 读取配置文件。                  |

您可能需要安装不同的依赖以在不同的硬件下运行，例如在使用 GPU 进行推理时，可能需要安装对应的 GPU 版本依赖。

## 当前支持的验证码类型

| 库       | 样例                   |
|---------|----------------------|
| Captcha | ![](images/A5Sk.png) |
|         | ![](images/5X3D.jpg) |


## 使用

### 安装

#### 在线安装

```shell
pip install QiAlgo-OCR
```

#### 通过 whl 进行安装

1. 在 [Releases页面](https://github.com/Morton-L/QiAlgo_OCR/releases) 下载 whl 包
2. 安装 whl 包```pip install QiAlgo_OCR-1.0.0-py3-none-any.whl```

### 使用示例

```python
from QiAlgo_OCR import QiAlgo_OCR


def qi_ml_ocr():
    qi = QiAlgo_OCR()

    with open('1AGB.jpg', 'rb') as f:
        image_bytes = f.read()

    qi.load_image(
        image=image_bytes
    )

    is_successful, results = qi.onnx_predictor()
    if is_successful:
        print(results)  # 1AGB


if __name__ == '__main__':
    qi_ml_ocr()
```

除了使用字节串 (bytestring)外，QiAlgo_OCR 还可以识别Base64、路径、PIL（Pillow）库中的Image图像对象、PurePath路径

## 基于源码打包

1. 将 onnx 模型命名为 `model.onnx` 并放置在 `QiAlgo_OCR/model/` 目录下；
2. ```python setup.py sdist bdist_wheel```

## 声明

### 科学技术伦理道德

科技是把双刃剑， QiAlgo_OCR 的设计初衷是用于检验图形验证码的可靠程度，但不可避免的是这确实可以对图形验证码进行快速解析以实现某些违反伦理道德的事情。为此郑重声明：

1. 本项目 `仅可用于学习` 和 `在法律允许的范围内进行可靠性测试` 用途；
2. 使用本项目进行的 `一切违反法律法规的事项均是不被允许的` ，即不允许使用本项目进行违反法律法规的尝试。
