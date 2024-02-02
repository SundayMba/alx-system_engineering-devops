# Install Nginx web server (w/ Puppet)
# Nginx should be listening on port 80
# it must return a page that contains the string Hello World! when queried with
# curl in /
# The redirection must be a “301 Moved Permanently”

Exec { 'apt-update':
command     => '/usr/bin/apt-get update',
refreshonly => true,
}

# ensure nginx package resource is installed
package {'nginx':
ensure  => '1.18.0-0ubuntu1.4',
require => Exec['apt-update'],
}

# create a file resource for index html
file {'/var/www//html/index.html':
ensure  => present,
content => 'Hello World!',
}


# defines the content of the config file in an embedded ruby file .erb
file {'/etc/nginx/sites-enabled/default':
ensure  => present,
content => "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm;
        add_header X-Served-By $HOSTNAME;

        location /redirect_me {
                return 301 https://youtube.com/;
        }
    }",
require => Package['nginx'],
notify  => Service['nginx'],
}

service {'nginx':
ensure    => running,
enable    => true,
subscribe => File['/etc/nginx/sites-enabled/default'],
}
