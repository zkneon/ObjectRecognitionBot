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

### Build Docker image from Dockerfile

```bash
git clone https://github.com/zkneon/chatBot
cd /chatBot
```

```bash
docker build -t objdetect:latest .
```
### Create Docker image from Dockerfile

```bash
docker run -id -P -e TOKEN_TG=YOUR_TOKEN_TELEGRAM_BOT --name objdetect objdetect
```

### Local Run
Add login and password from TradingView account to /.env file.



