FROM python:3.10.2-alpine3.15

MAINTAINER Daniel Yanes

# Apk directory
ADD /apk /apk

# Coping keys
RUN cp /apk/.abuild/-58b83ac3.rsa.pub /etc/apk/keys

RUN apk --no-cache add xvfb openbox xfce4-terminal x11vnc supervisor \ 
  sudo python3-tkinter musl-dev linux-headers g++ build-base \
  && addgroup alpine \
  && adduser  -G alpine -s /bin/sh -D alpine \
  && echo "alpine:alpine" | /usr/sbin/chpasswd \
  # adding to sudoers file
  && echo "alpine    ALL=(ALL) ALL" >> /etc/sudoers \
  && rm -rf /apk /tmp/* /var/cache/apk/*

ADD etc /etc

WORKDIR /home/alpine/video-converter

# Port in 5900 for default
EXPOSE 5900

USER alpine

# Coping all code
COPY . .

# Dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Running the app
RUN python3 index.py

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]