FROM akihiro69/akihiro:buster

RUN git clone -b master https://github.com/akihiro69/AkihiroProject /home/master/ \
    && chmod 777 /home/master \
    && mkdir /home/master/bin/
RUN pip3 install -r https://raw.githubusercontent.com/akihiro69/AkihiroProject/master/requirements.txt

WORKDIR /home/master

CMD ["python3", "-m", "userbot"]
