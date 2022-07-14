FROM akihiro69/akihiro:buster

RUN git clone -b master https://github.com/akihiro69/AkihiroProject /home/akihiroprojects/ \
    && chmod 777 /home/akihiroprojects \
    && mkdir /home/akihiroprojects/bin/

CMD [ "python3", "-m", "userbot" ]

RUN pip3 install -r https://raw.githubusercontent.com/akihiro69/AkihiroProject/master/requirements.txt
