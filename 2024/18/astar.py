from heapq import heappush, heappop
from functools import cache


class Astar:
    def __init__(self, grid_size, obstacles):
        self.width, self.height = grid_size, grid_size
        self.obstacles = obstacles

        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_valid(self, x, y):
        return self.is_inbounds(x, y) and self.no_obstacle(x, y)

    @cache
    def is_inbounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def no_obstacle(self, x, y):
        return (x, y) not in self.obstacles

    @cache
    def manhattan_distance(self, x1, y1, x2, y2):
        """Calculate Manhattan distance heuristic"""
        return abs(x1 - x2) + abs(y1 - y2)

    def find_path(self, start, goal):
        start_x, start_y = start
        goal_x, goal_y = goal

        min_time_to_goal = self.manhattan_distance(start_x, start_y, goal_x, goal_y)
        max_time = min_time_to_goal * 12 + max(self.width, self.height)

        open_set = [(0, 0, start_x, start_y, 0)]  # (f_score, step, x, y, time)
        came_from = {(start_x, start_y, 0): None}
        g_score = {(start_x, start_y, 0): 0}
        step = 0
        min_f_score_to_goal = float("inf")

        while open_set:
            f, _, x, y, time = heappop(open_set)
            current = (x, y, time)

            if (x, y) == goal:
                min_f_score_to_goal = min(min_f_score_to_goal, f)
                return self._reconstruct_path(came_from, current)

            if f >= min_f_score_to_goal:
                print("early termination")
                break

            # time limit check
            remaining_dist = self.manhattan_distance(x, y, goal_x, goal_y)
            if time + remaining_dist >= max_time:
                print(
                    f"distance limit reached: {time} + {remaining_dist} >= {max_time}"
                )
                continue

            for dx, dy in self.directions:
                next_x = x + dx
                next_y = y + dy
                next_time = time + 1

                if not self.is_valid(next_x, next_y):
                    continue

                next_state = (next_x, next_y, next_time)
                tentative_g = g_score[current] + 1

                if next_state not in g_score or tentative_g < g_score[next_state]:
                    came_from[next_state] = current
                    g_score[next_state] = tentative_g
                    f_score = tentative_g + self.manhattan_distance(
                        next_x, next_y, goal_x, goal_y
                    )
                    step += 1
                    heappush(open_set, (f_score, step, next_x, next_y, next_time))

        return None

    def _reconstruct_path(self, came_from, current):
        path = [(current[0], current[1])]
        while came_from[current] is not None:
            current = came_from[current]
            path.append((current[0], current[1]))
        return path[::-1]
