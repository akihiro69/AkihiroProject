FROM akihiro69/akihiroproject:master

RUN git clone -b master https://github.com/akihiro69/AkihiroProject /home/akihiroproject/ \
    && chmod 777 /home/akihiroproject \
    && mkdir /home/akihiroproject/bin/

WORKDIR /home/akihiroproject/

CMD [ "bash", "start" ]
