#!/usr/bin/env ruby

def parse_claim(claim)
  # Example: '#1024 @ 232,558: 13x11'
  m = /^\#\d+ @ (?<x>\d+),(?<y>\d+): (?<width>\d+)x(?<height>\d+)/.match(claim)
  x, y = Integer(m['x']), Integer(m['y'])
  w, h = Integer(m['width']), Integer(m['height'])

  [x, y, w, h]
end

def coords_for_claim(x, y, w, h)
  # return array of coordinates covered by this claim.
  coords = []
  w.times do |m|
    h.times do |n|
      coords << [x + m, y + n]
    end
  end
  coords
end

grid = Hash.new(0)

ARGF.each do |claim|
  x, y, w, h = parse_claim(claim)
  coords_for_claim(x, y, w, h).each do |coord|
    grid[coord] += 1
  end
end

puts grid.select { |_, count| count > 1 }.size
