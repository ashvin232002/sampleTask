FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN apt-get update \
 && apt-get install -y grep coreutils \
 && pip install pytest \
 && chmod +x solution.sh run-tests.sh

CMD ["./run-tests.sh"]
