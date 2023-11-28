#!/usr/bin/env ruby
# Repetition Token #0

matches = ARGV[0].scan(/\[from:(\w+|[+0-9]+)\] \[to:([+0-9]+)\] \[flags:([-+:0-9]+)\]/).join(",")
puts matches
