FROM mcr.microsoft.com/azure-app-service/java:11-java11_stable

# Install OpenSSH and set the password for root to "Docker!".
RUN apk add openssh \
     && echo "root:Docker!" | chpasswd 

# Copy the sshd_config file to the /etc/ssh/ directory
COPY sshd_config /etc/ssh/

# Copy and configure the ssh_setup file
RUN mkdir -p /tmp
COPY ssh_setup.sh /tmp
RUN chmod +x /tmp/ssh_setup.sh \
    && (sleep 1;/tmp/ssh_setup.sh 2>&1 > /dev/null)

# Copy and configure the docker-entrypoint file
COPY docker-entrypoint.sh /tmp
RUN chmod +x /tmp/docker-entrypoint.sh 

# Open port 2222 for SSH access
ENV PORT 80
EXPOSE 80 2222

ENTRYPOINT ["/tmp/docker-entrypoint.sh"]
