#!/bin/sh

# Startup OpenSSH daemon
/usr/sbin/sshd

# Run the JAR file
java -Dserver.port=80 -jar /tmp/appservice/parkingpage.jar
