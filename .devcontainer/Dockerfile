FROM python:3.13.2-alpine

ARG USER_ID=1000
ARG GROUP_ID=1000
ARG USER_NAME=MY_USER
ARG GROUP_NAME=MY_GROUP

# Install necessary utilities
RUN apk add --no-cache git bash

# Create group and user properly in Alpine
# RUN <<EOF
#     addgroup -g ${GROUP_ID} ${GROUP_NAME}
#     adduser -D -u ${USER_ID} -G ${GROUP_NAME} -h /home/${USER_NAME} -s /bin/bash ${USER_NAME}
# EOF



# Install Python dependencies using heredoc
RUN <<EOF
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade setuptools gitpython pdm
EOF

# RUN mkdir -p /workspace
# RUN chown -R ${USER_NAME}:${GROUP_NAME} /home/${USER_NAME}

# WORKDIR /home/${USER_NAME}
