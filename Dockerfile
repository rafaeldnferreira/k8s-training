FROM alpine:3.15
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
WORKDIR /app
ADD static /app/static
ADD templates /app/templates
ADD app.py requirements.txt /app/
RUN pip3 install -r requirements.txt
ENV FLASK_APP=app
EXPOSE 5000
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
