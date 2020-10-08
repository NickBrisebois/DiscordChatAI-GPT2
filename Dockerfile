FROM tensorflow/tensorflow:1.15.4

RUN mkdir /chat

RUN pip3 install discord gpt-2-simple

COPY ./Bot /chat/Bot
copy ./main.py /chat/

ENTRYPOINT ["python3", "/chat/main.py"]
