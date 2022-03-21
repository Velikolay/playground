from enum import Enum
from queue import PriorityQueue
from time import sleep
from bisect import bisect
from random import randrange
import math

Direction = Enum("Direction", "UP DOWN")


class Lift:
    def __init__(self, lift_id):
        self.id = lift_id
        self.floor = 0
        self.direction = Direction.UP

    def get_id(self) -> int:
        return self.id

    def get_direction(self) -> Direction:
        return self.direction

    def set_direction(self, direction: Direction):
        self.direction = direction

    def get_floor(self) -> int:
        return self.floor

    def move(self, floor: int):
        self.floor = floor


class LiftController:
    STOP_FACTOR = 10
    FLOOR_FACTOR = 1

    def __init(self, lift: Lift, min_floor: int, max_floor: int):
        self.lift = lift
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.upQueue = PriorityQueue()
        self.downQueue = PriorityQueue()
        self.__control_loop()

    def go_to_floor(self, floor: int):
        if self.lift.direction == Direction.UP:
            if self.lift.floor < floor:
                self.upQueue.put_nowait(floor)
            if self.lift.floor > floor:
                self.downQueue.put_nowait(-floor)

        if self.lift.direction == Direction.DOWN:
            if self.lift.floor > floor:
                self.downQueue.put_nowait(-floor)
            if self.lift.floor < floor:
                self.upQueue.put_nowait(floor)

    def estimate_going_down_from_floor(self, floor: int) -> int:
        return randrange(10)

    def estimate_going_up_from_floor(self, floor: int) -> int:
        return randrange(10)
        # up_moves = sorted(list(self.upQueue.queue))
        # down_moves = sorted(list(self.downQueue.queue))
        # estimate = 0
        #
        # def going_down_estimate():
        #     top_floor = up_moves[-1] if len(up_moves) > 0 else self.lift.floor
        #     move_pos = bisect(-floor, down_moves)
        #     if move_pos == len(down_moves):
        #         return (move_pos + 1) * self.STOP_FACTOR + \
        #                     (top_floor - floor) * self.FLOOR_FACTOR
        #     else:
        #         return (len(down_moves) + 1) * self.STOP_FACTOR + \
        #                     (top_floor + down_moves[-1] + floor + down_moves[-1]) * self.FLOOR_FACTOR
        #
        # if self.lift.direction == Direction.UP:
        #     if self.lift.get_floor() > floor:
        #         if len(up_moves) > 0:
        #             estimate += len(up_moves) * self.STOP_FACTOR + \
        #                         (up_moves[-1] - self.lift.get_floor()) * self.FLOOR_FACTOR
        #
        #         estimate += going_down_estimate()
        #     else:
        #         move_pos = bisect(floor, up_moves)
        #         estimate += (move_pos + 1) * self.STOP_FACTOR + \
        #                     (floor - self.lift.floor) * self.FLOOR_FACTOR
        #
        # if self.lift.direction == Direction.DOWN:
        #     return going_down_estimate()

    def __control_loop(self):
        while True:
            if self.lift.direction == Direction.UP:
                while not self.upQueue.empty():
                    floor = self.upQueue.get_nowait()
                    self.lift.move(floor)

                if not self.downQueue.empty():
                    self.lift.set_direction(Direction.DOWN)

            if self.lift.direction == Direction.DOWN:
                while not self.downQueue.empty():
                    floor = -self.downQueue.get_nowait()
                    self.lift.move(floor)

                if not self.upQueue.empty():
                    self.lift.set_direction(Direction.UP)

            sleep(0.1)


class CentralLiftController:
    def __init__(self, num_lifts: int, min_floor: int, max_floor: int):
        lifts = [Lift(lift_id) for lift_id in range(num_lifts)]
        self.controllers = [LiftController(lift, min_floor, max_floor) for lift in lifts]

    def go_up_from_floor(self, floor: int):
        return self.__go_direction_from_floor(Direction.UP, floor)

    def go_down_from_floor(self, floor: int):
        return self.__go_direction_from_floor(Direction.DOWN, floor)

    def __go_direction_from_floor(self, direction: Direction, floor: int):
        min_estimate = math.inf
        min_estimate_controller = None
        for controller in self.controllers:
            if direction == Direction.UP:
                estimate = controller.estimate_going_up_from_floor(floor)
            else:
                estimate = controller.estimate_going_down_from_floor(floor)

            if min_estimate > estimate:
                min_estimate = estimate
                min_estimate_controller = controller

        if min_estimate_controller:
            min_estimate_controller.go_to_floor(floor)

        return min_estimate, min_estimate_controller


def main():
    cc = CentralLiftController(3, -3, 10)
    estimate, controller = cc.go_down_from_floor(5)


if __name__ == "__main__":
    main()
