#!/usr/bin/python3
import argparse
import random

parser = argparse.ArgumentParser(description='How many iterations should we run')
parser.add_argument('iterations', metavar='N', type=int, nargs='+',
                    help='an integer for the number of iterations')
args = parser.parse_args()


def main(iterations):
    guest_wins = 0
    for play in range(iterations):
        guest_wins += montey_hall_test()
    win_percentage = (guest_wins / iterations) * 100
    print('guest win percentage is', win_percentage)
    return


def montey_hall_test():
    doors = ['Door One', 'Door Two', 'Door Three']
    winning_door = choose_a_door(doors)
    guests_choice = choose_a_door(doors)
    hosts_reveal = host_opens_door(winning_door, guests_choice, doors)
    guests_choice = guest_changes_mind(guests_choice, hosts_reveal, doors)
    if guests_choice == winning_door:
        return 1
    else:
        return 0


def choose_a_door(doors: list) -> str:
    chosen = random.randint(0, len(doors) - 1)
    return doors[chosen]


def host_opens_door(winning_door: str, guests_choice: str, doors: list):
    candidates = doors[:]
    candidates = remove_choice_if_exists(winning_door, candidates)
    candidates = remove_choice_if_exists(guests_choice, candidates)
    return choose_a_door(candidates)


def guest_changes_mind(guests_choice: str, hosts_reveal: str, doors: list):
    doors.remove(guests_choice)
    doors.remove(hosts_reveal)
    return doors[0]


def remove_choice_if_exists(choice: str, doors: list) -> list:
    if choice in doors:
        doors.remove(choice)
    return doors


if __name__ == "__main__":
    main(args.iterations[0])
