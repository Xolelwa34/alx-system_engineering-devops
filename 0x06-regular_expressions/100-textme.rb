#!/usr/bin/env ruby
#Takes a phone number and a message arguments
puts ARGV[0].scan(/\[from:(.*)\]\s\[to:(.*)\]\s\[flags:(*)\]/).join(",")
