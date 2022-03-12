FROM python:3.10.2-alpine3.15

MAINTAINER Daniel Yanes

# Adding the apk directory
ADD /build/apk /apk

# Coping keys
RUN cp /apk/.abuild/-58b83ac3.rsa.pub /etc/apk/keys


RUN apk update \ 
  && apk --no-cache add xvfb openbox terminus-font xfce4-terminal x11vnc supervisor \ 
  sudo musl-dev linux-headers build-base py3-numpy-dev python3-tkinter \
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

# App directory
WORKDIR /home/alpine/video-converter

# Coping all code
COPY . .

# Coping the libs for moviepy
RUN cd build/libs/moviepy \
    && mv * /usr/lib/python3.9

USER root

# Cleaning build files
RUN rm -rf build

# RUN python3 index.py

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]