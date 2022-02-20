FROM alpine:3.15

# Updating and requireds packages
RUN apk update && apk add --no-cache x11vnc supervisor openssh-server \ 
    net-tools xvfb \
    openbox xterm terminus-font pwgen


# Adding the startup and configuration
ADD startup.sh /
ADD supervisord.conf /etc/supervisor/conf.d/

# Running in 5900
EXPOSE 5900
WORKDIR /root

# Commands for init in startup.sh
ENTRYPOINT ["/startup.sh"]