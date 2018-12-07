#!/usr/bin/env ruby

twos = 0
threes = 0

ARGF.each do |id|
  letters = id.strip.split('')
  counts = letters.each_with_object(Hash.new(0)) do |character, h|
    h[character] += 1
  end

  has_twos = counts.find { |letter, count| count == 2 }
  has_threes = counts.find { |letter, count| count == 3 }

  twos += 1 if has_twos
  threes += 1 if has_threes
end

checksum = twos * threes
puts "checksum: #{checksum}"
