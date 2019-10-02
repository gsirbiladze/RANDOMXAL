# Remove old versions
sudo apt-get remove docker docker-engine docker.io

# Just in case you're missing these
# sudo apt-get install apt-transport-https ca-certificates curl  software-properties-common

# Add Docker’s official GPG key:
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Verify PGP
# apt-key fingerprint 0EBFCD88


# For Mint find based on which Ubuntu release is it 
#   * cat /etc/upstream-release/lsb-release
# and sub "$(lsb_release -cs)" with that.

# For Mint
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(cat /etc/upstream-release/lsb-release | awk -F= '/DISTRIB_CODENAME/ {print($2)}') stable"
# Docker repository addition for Ubuntu
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"



# Update apt repository
sudo apt-get update

# Install Docker  CE(Community Edition)
sudo apt-get install docker-ce


# Docker composer and machine
URL_DMB="https://github.com/docker/machine/releases/download/v0.16.0/docker-machine-$(uname -s)-$(uname -m)"
URL_DCB="https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)"

DMB="/usr/local/bin/docker-machine"
DCB="/usr/local/bin/docker-compose"

sudo curl -L "$URL_DMB" -o "$DMB" && sudo chmod +x "$DMB"
sudo curl -L "$URL_DCB"  -o "$DCB" && sudo chmod +x "$DCB"


