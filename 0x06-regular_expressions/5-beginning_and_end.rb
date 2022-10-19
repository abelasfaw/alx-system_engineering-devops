#!/usr/bin/env ruby
#regular expression matching a string that starts with h and ends with n and can have any single character in between
puts ARGV[0].scan(/h[a-zA-Z0-9]n/).join
