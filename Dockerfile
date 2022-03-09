FROM akihiro69/akihiroproject:master

RUN git clone -b master https://github.com/akihiro69/AkihiroProject /home/AkihiroProject/ \
    && chmod 777 /home/AkihiroProject \
    && mkdir /home/AkihiroProject/bin/

WORKDIR /home/AkihiroProject/

CMD [ "bash", "start" ]
