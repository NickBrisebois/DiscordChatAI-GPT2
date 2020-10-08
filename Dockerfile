FROM tensorflow/tensorflow:1.15.4-gpu-py3

RUN mkdir /chat

RUN pip3 install discord gpt-2-simple

COPY ./Bot /chat/Bot
COPY ./main.py /chat/
COPY ./entrypoint.sh /chat/

RUN chmod +x /chat/entrypoint.sh

ENTRYPOINT ["/chat/entrypoint.sh"]
