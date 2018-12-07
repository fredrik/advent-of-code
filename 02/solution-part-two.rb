#!/usr/bin/env ruby

input = ARGF.map { |line| line.strip.split('') }

# returns list of characters that are identical in both ids
def shared_characters(a, b)
  raise unless a.size == b.size
  a.zip(b).select {|x,y| x == y }.map(&:first)
end

while !input.empty?
  id = input.pop
  input.each do |other_id|
    shared = shared_characters(id, other_id)
    if shared.size == (id.size - 1)
      puts shared.join('')
    end
  end
end
