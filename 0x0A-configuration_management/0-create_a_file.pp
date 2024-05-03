# 0-create_a_file.pp
 { '/tmp/school':
	mode     => '0744',
	owner    => 'www-data',
	group    => 'www-data',
	contains => 'I love puppet'
}
