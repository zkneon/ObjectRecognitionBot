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

RUN apt install -y python3.10 \
    cmake \
    libopencv-dev \
    python3.10-venv \
    python3-opencv

WORKDIR /home
RUN python3.10 -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN make darknet/Makefile
#RUN pip install --upgrade pip
RUN pip install -r requriments.txt

EXPOSE 8777

CMD ["python", "main.py"]