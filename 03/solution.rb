#!/usr/bin/env ruby

def parse_claim(claim)
  # Example: '#1024 @ 232,558: 13x11'
  m = /^\#(?<id>\d+) @ (?<x>\d+),(?<y>\d+): (?<width>\d+)x(?<height>\d+)/.match(claim)
  id = Integer(m['id'])
  x, y = Integer(m['x']), Integer(m['y'])
  w, h = Integer(m['width']), Integer(m['height'])

  [id, x, y, w, h]
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
claims_made = []

ARGF.each do |claim|
  id, x, y, w, h = parse_claim(claim)
  coords = coords_for_claim(x, y, w, h)
  coords.each do |coord|
    grid[coord] += 1
  end
  claims_made << [id, coords]
end

puts grid.select { |_, count| count > 1 }.size

# --- part two

good = claims_made.select do |id, coords|
  coords.map { |c| grid[c] }.all? { |x| x == 1 }
end

puts good.map(&:first)
