# make changes to our configuration files

# private key config.
exec {'echo "    IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config':
path => '/usr/bin:/usr/bin/local',
}

# turn off password authentication
exec { 'sed -i "s/^# *PasswordAuthentication yes/    PasswordAuthentication no/" /etc/ssh/ssh_config':
path => '/usr/bin:/usr/bin/local'
}

