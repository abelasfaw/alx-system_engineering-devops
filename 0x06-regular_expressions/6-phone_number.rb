#!/usr/bin/env ruby
#regular expression matching a 10 digit phone number
puts ARGV[0].scan(/[0-9]{10}/).join 
