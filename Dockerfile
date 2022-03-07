FROM python:3.10.2-alpine3.15

MAINTAINER Daniel Yanes

# Adding the apk directory
ADD /build/apk /apk

# Coping keys
RUN cp /apk/.abuild/-58b83ac3.rsa.pub /etc/apk/keys

RUN apk --no-cache add xvfb openbox terminus-font xfce4-terminal x11vnc supervisor \ 
  sudo cython python3-tkinter musl-dev zlib py3-numpy linux-headers g++ make gcc build-base \
  && addgroup alpine \
  && adduser -G alpine -s /bin/sh -D alpine \
  && echo "alpine:alpine" | /usr/sbin/chpasswd \
  # Adding to sudoers file
  && echo "alpine    ALL=(ALL) ALL" >> /etc/sudoers \
  && rm -rf /apk /tmp/* /var/cache/apk/*

# Adding the configuration
ADD /build/etc /etc

# Port in 5900 for default
EXPOSE 5900

WORKDIR /home/alpine/video-converter
# Coping all code
COPY . .

USER root

RUN cd build/libs/moviepy \
    && mv * /usr/lib/python3.9

# Dependencies
# RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install --upgrade pip

# Running the app
# RUN python3 index.py

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]