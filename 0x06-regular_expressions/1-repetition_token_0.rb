#!/usr/bin/env ruby
# Repetition Token #0

pattern = "hbt{2,5}n"
puts ARGV[0].scan(/#{pattern}/).join

