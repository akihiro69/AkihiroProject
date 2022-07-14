FROM akihiro69/akihiro:buster

RUN git clone -b master https://github.com/akihiro69/AkihiroProject /home/akihiroprojects/ \
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot


RUN pip3 install -r https://raw.githubusercontent.com/akihiro69/AkihiroProject/master/requirements.txt

EXPOSE 80 443


CMD ["bash", "start"]
