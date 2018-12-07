#!/usr/bin/env ruby
# usage: ./solution-part-two.rb < input.txt
require 'set'

frequency = 0
seen_frequencies = Set.new()

input = ARGF.map { |line| Integer(line) }

loop do
  input.each do |change|
    frequency = frequency + change
    if seen_frequencies.member?(frequency)
      puts frequency
      exit
    end
    seen_frequencies.add(frequency)
  end
end
