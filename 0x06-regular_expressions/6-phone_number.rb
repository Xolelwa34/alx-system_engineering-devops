#!/usr/bin/env ruby
#A regular expression that matches any string
puts ARGV[0].scan(/^\d{10}$/).join
