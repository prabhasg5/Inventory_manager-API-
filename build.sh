#!/bin/bash
# Install system dependencies manually
echo "deb http://security.debian.org/debian-security buster/updates main" >> /etc/apt/sources.list
apt-get update
apt-get install -y libssl1.1
wget -O - https://packages.couchbase.com/clients/c/repos/deb/couchbase.key | apt-key add -
echo "deb https://packages.couchbase.com/clients/c/repos/deb/ubuntu2204 jammy jammy/main" > /etc/apt/sources.list.d/couchbase.list
apt-get update
apt-get install -y libcouchbase3 libcouchbase-dev

# Continue with normal build process
pip install -r requirements.txt