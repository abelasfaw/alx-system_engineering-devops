#!/usr/bin/env ruby
#regular expression matching a 10 digit phone number
puts ARGV[0].scan(/^[0-9]{1}[0-9]{8}[0-9]{1}$/).join 
