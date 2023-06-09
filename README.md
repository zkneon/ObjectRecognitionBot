<div align="center">

# Object Rcognition based on YOLO v4 and TelegramBot

[![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat&logo=python)]()
[![Darknet](https://github.com/AlexeyAB/darknet/workflows/Darknet%20Continuous%20Integration/badge.svg)](https://github.com/AlexeyAB/darknet/actions?query=workflow%3A%22Darknet+Continuous+Integration%22)
[![YOLOv4](https://img.shields.io/badge/YOLO-v4-red?style=flat&logo=yolo)](https://github.com/AlexeyAB/darknet)
[![CV2](https://img.shields.io/badge/OpenCV-red?style=flat&logo=opencv)](https://opencv.org/)
[![TelegramBot](https://img.shields.io/badge/pyTelegramBotAPI-4.10-blue?style=flat&logo=telegram)](https://pypi.org/project/pyTelegramBotAPI/4.10.0/)

</div>

## Information

Detecting object on foto from Telegram Bot.
![image](img/AQAD5MUxG8aq4Et--D.jpg)
### Build Docker image from Dockerfile

```shell
git clone https://github.com/zkneon/ObjectRecognitionBot
cd /ObjectRecognitionBot
```

```shell
docker build -t objdetect:latest .
```
### Create Docker container from Dockerfile

```shell
docker run -id -P -e TOKEN_TG=YOUR_TOKEN_TELEGRAM_BOT --name objdetect objdetect
```

### Local Run
Add TOKEN_TG variable with token form Telegram Bot to /.env file.
And uncomment in main.py:

```python
config = dotenv_values('.env')
token = config['TOKEN_TG']
```
Finally Download file yolov4-csp.weigths to the /darknet directory of project.

```shell
wget -q -S --no-check-certificate --spider --load-cookie $TEMP --save-cookie $TEMP  \
    "https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1TircU1RFRJFuCwjfXbf9KBOmfJ4H30uI"
wget -c --progress=dot:giga --no-check-certificate --load-cookie $TEMP --save-cookie $TEMP  \
    "https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1TircU1RFRJFuCwjfXbf9KBOmfJ4H30uI" \
    -O darknet/yolov4-csp.weights
```

