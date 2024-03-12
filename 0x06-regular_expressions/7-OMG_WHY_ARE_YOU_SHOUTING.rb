#!/usr/bin/env ruby
# A regular expression only matching in capital letters
puts ARGV[0].scan(/[A-Z]/).join
