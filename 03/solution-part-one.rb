#!/usr/bin/env ruby

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

# convert input to list of coords and width/height pairs.
input = ARGF.map do |line|
  # Example: '#1024 @ 232,558: 13x11'
  m = /^\#\d+ @ (?<x>\d+),(?<y>\d+): (?<width>\d+)x(?<height>\d+)/.match(line)
  x, y = Integer(m['x']), Integer(m['y'])
  w, h = Integer(m['width']), Integer(m['height'])

  [[x, y], [w, h]]
end

grid = Hash.new(0)

coords_claimed = input.map do |claim|
  x, y = claim.first
  w, h = claim.last

  coords = coords_for_claim(x, y, w, h)

  coords.each do |coord|
    grid[coord] += 1
  end
end

overclaimed = grid.select { |_, count| count > 1 }.size
puts overclaimed
