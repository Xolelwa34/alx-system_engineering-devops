#install a specific version of flask
exec { 'flask':
  command =>  'pip3 install flask==2.1.0',
  path    =>  '/usr/bin/',
  unless  =>  'pip3 list | grep flask',
}

