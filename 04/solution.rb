#!/usr/bin/env ruby

def parse(line)
  # Example: "[1518-11-17 00:02] Guard #1069 begins shift"
  minute, text = line.scan(/ \d\d:(\d\d)\] (.+)/).first
  guard_id = text.scan(/Guard \#(\d+)/).first
  minute = minute.to_i

  if guard_id
    action = :begin
    guard_id = Integer(guard_id.first)
  elsif text == 'falls asleep'
    action = :sleep
  elsif text == 'wakes up'
    action = :wake
  else
    raise "Bad input"
  end

  [action, minute, guard_id]
end

sleep_times = []
guard_on_duty = nil
asleep_at = nil

ARGF.sort.each do |line|
  action, minute, guard_id = parse(line)

  case action
  when :begin
    guard_on_duty = guard_id if action == :begin
  when :sleep
    asleep_at = minute
  when :wake
    (asleep_at..(minute-1)).each do |m|
      sleep_times << [guard_on_duty, m]
    end
  end
end

minutes_per_guard = Hash.new(0)

sleep_times.each do |guard_id, minute|
  minutes_per_guard[guard_id] += 1
end

sleepiest_guard = minutes_per_guard.sort_by { |guard_id, minutes| -minutes }.first.first

most_slept_minute = sleep_times
  .select { |guard_id, _| guard_id == sleepiest_guard }.map(&:last)
  .sort.chunk { |n| n }
  .map { |n, ns| [n, ns.size] }
  .sort_by { |n, size| -size }
  .first.first


puts "sleepiest: #{sleepiest_guard}"
puts "most slept minute: #{most_slept_minute}"
puts "=> #{most_slept_minute * sleepiest_guard}"


# -- part two

guard_minutes = Hash.new(0)

sleep_times.each do |guard_id, minute|
  guard_minutes[[guard_id, minute]] += 1
end

most_slept_minute = guard_minutes.sort_by { |key, count|  -count }.first

(guard_id, minute), count = most_slept_minute

puts "#{guard_id} slept #{count} during minute #{minute}"
puts "=> #{guard_id * minute}"
