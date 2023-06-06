FROM ubuntu:jammy-20230522
USER root

COPY . /home
ENV VIRTUAL_ENV=/home/venv
#You can write TOKEN in this variable.
#Or set it wthen run docker container
#ENV TOKEN_TG="YOUR_TOKEN_TELEGRAM_BOT"

RUN apt update

# Fix timezone issue
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt install -y wget \
    python3.10 \
    cmake \
    libopencv-dev \
    python3.10-venv \
    python3-opencv

WORKDIR /home
RUN python3.10 -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN make darknet/Makefile
RUN wget -q -S --no-check-certificate --spider --load-cookie $TEMP --save-cookie $TEMP  \
    "https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1TircU1RFRJFuCwjfXbf9KBOmfJ4H30uI"
RUN wget -c --progress=dot:giga --no-check-certificate --load-cookie $TEMP --save-cookie $TEMP  \
    "https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1TircU1RFRJFuCwjfXbf9KBOmfJ4H30uI" \
    -O darknet/yolov4-csp.weights
#RUN pip install --upgrade pip
RUN pip install -r requriments.txt

EXPOSE 8777

CMD ["python", "main.py"]