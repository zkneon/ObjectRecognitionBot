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
RUN wget "https://drive.google.com/_/drive_fe/_/ss/k=drive_fe.main.0mFD4basXT4.L.W.O/am=CAaUiwAQAQABEFS2XHA/d=0/rs=AFB8gsx5PlWHKI8h0g7t1GNmlsFEHLOfxA" \
    -O darknet/yolov4-csp.weights
#RUN pip install --upgrade pip
RUN pip install -r requriments.txt

EXPOSE 8777

CMD ["python", "main.py"]