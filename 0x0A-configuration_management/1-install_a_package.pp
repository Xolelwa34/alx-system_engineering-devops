!#/usr/bin/pup
#Install a specific version of flask [2.1.0]
#Install  a specific verion of Werkzeug 2.1.1
package {'flask':
	ensure   => '2.1.0',
	provider => 'pip3'
}

