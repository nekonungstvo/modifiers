FROM python:3.6
ENV IS_PROD 1
RUN apt update && apt install -y gcc build-essential
WORKDIR /usr/src/app
COPY . .
RUN python -m pip install -U .
CMD ["modifiers"]
EXPOSE 8080