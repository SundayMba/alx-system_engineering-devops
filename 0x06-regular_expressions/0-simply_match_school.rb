#!/usr/bin/env ruby
# The regular expression must match School
pattern = "School"
puts ARGV[0].scan(/#{pattern}/).join
