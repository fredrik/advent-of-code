from heapq import heappush, heappop
from dataclasses import dataclass
from functools import cache


@dataclass(frozen=True, order=True)
class State:
    x: int
    y: int
    time: int


class Astar:
    def __init__(self, grid_size, obstacles, start_time):
        self.width, self.height = grid_size, grid_size
        self.obstacles = obstacles
        self.start_time = start_time

        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    @cache
    def is_valid(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            return False
        return (x, y) not in self.obstacles

    @cache
    def manhattan_distance(self, x1, y1, x2, y2):
        """Calculate Manhattan distance heuristic"""
        return abs(x1 - x2) + abs(y1 - y2)

    def find_path(self, start, goal, max_time=100000):
        start_state = State(start[0], start[1], self.start_time)
        goal_x, goal_y = goal

        # priority queue
        open_set = [(0, start_state)]
        came_from = {start_state: None}
        g_score = {start_state: 0}

        while open_set:
            current_state = heappop(open_set)[1]

            if (current_state.x, current_state.y) == goal:
                return self._reconstruct_path(came_from, current_state)

            if current_state.time >= max_time:
                print("time limit hit!")
                continue

            for dx, dy in self.directions:
                next_x = current_state.x + dx
                next_y = current_state.y + dy
                next_time = current_state.time + 1

                if not self.is_valid(next_x, next_y):
                    continue

                next_state = State(next_x, next_y, next_time)
                tentative_g = g_score[current_state] + 1

                if next_state not in g_score or tentative_g < g_score[next_state]:
                    came_from[next_state] = current_state
                    g_score[next_state] = tentative_g
                    f_score = tentative_g + self.manhattan_distance(
                        next_x, next_y, goal_x, goal_y
                    )
                    heappush(open_set, (f_score, next_state))

        return None

    def _reconstruct_path(self, came_from, current):
        path = [(current.x, current.y)]
        while came_from[current] is not None:
            current = came_from[current]
            path.append((current.x, current.y))
        return path[::-1]
