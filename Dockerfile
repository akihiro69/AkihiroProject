FROM vckyouubitch/geez:master

RUN git clone -b master https://github.com/akihiro69/AkihiroProject /home/geezprojects/ \
    && chmod 777 /home/geezprojects \
    && mkdir /home/geezprojects/bin/

CMD [ "bash", "start" ]

RUN pip3 install -r https://raw.githubusercontent.com/akihiro69/AkihiroProject/master/requirements.txt
