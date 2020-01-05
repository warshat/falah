#!/bin/sh
set -xe

PROJECT_NAME=$1

PROJECT_DIR=/vagrant
VIRTUALENV_DIR=/home/vagrant/.virtualenvs/$PROJECT_NAME

PYTHON=$VIRTUALENV_DIR/bin/python
PIP=$VIRTUALENV_DIR/bin/pip

# Install Virtualenv
apt-get update -y
apt-get install -y virtualenv

# Installing Apache 2 (setting up Apache2 and mod_wsgi for python 3)
# https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/modwsgi/
apt-get install -y apache2 libapache2-mod-wsgi-py3

# Virtualenv setup for project
su - vagrant -c "virtualenv --python=python3 $VIRTUALENV_DIR"

su - vagrant -c "echo $PROJECT_DIR > $VIRTUALENV_DIR/.project"


# Upgrade PIP itself
su - vagrant -c "$PIP install --upgrade pip"

# Upgrade setuptools (for example html5lib needs 1.8.5+)
su - vagrant -c "$PIP install --upgrade six setuptools"

# Install PIP requirements
su - vagrant -c "cd $PROJECT_DIR && $PIP install -r requirements.txt"


# Set execute permissions on manage.py as they get lost if we build from a zip file
chmod a+x $PROJECT_DIR/manage.py


# configure Apache and mod-wsgi
# Create a Django virtual host
touch /etc/apache2/sites-available/$PROJECT_NAME.conf

cat <<EOT >> /etc/apache2/sites-available/$PROJECT_NAME.conf
<VirtualHost *:80>

    WSGIDaemonProcess $PROJECT_NAME python-home=$VIRTUALENV_DIR python-path=$PROJECT_DIR
    WSGIProcessGroup $PROJECT_NAME

    Alias /media/ $PROJECT_DIR/media/
    Alias /static/ $PROJECT_DIR/static/

    <Directory $PROJECT_DIR/static>
    Require all granted
    </Directory>

    <Directory $PROJECT_DIR/media>
    Require all granted
    </Directory>

    WSGIScriptAlias / $PROJECT_DIR/$PROJECT_NAME/wsgi.py
    
    <Directory $PROJECT_DIR/$PROJECT_NAME>
    <Files wsgi.py>
    Require all granted
    </Files>
    </Directory>

</VirtualHost>
EOT

# Add a couple of aliases to manage.py into .bashrc
cat << EOF >> /home/vagrant/.bashrc
source $VIRTUALENV_DIR/bin/activate
cd $PROJECT_DIR
EOF

usermod -a -G vagrant www-data

# disable the default virtual host config file i.e 000.default.conf
a2dissite 000-default.conf

# Enable your $PROJECT_NAME virtual host
a2ensite $PROJECT_NAME

# Restart apache web server to take effect the changes
systemctl restart apache2
#systemctl reload apache2