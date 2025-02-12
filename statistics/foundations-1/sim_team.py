from itertools import permutations
import math
import random


def sim_team_random(people, team_size, chosen, attempts=1000):
    ok = 0

    for _ in range(attempts):
        outcome = [random.choice(people) for _ in range(team_size)]
        if all(person in outcome for person in chosen):
            ok += 1

    return 1.0 * ok / attempts


def sim_team_exact(people, team_size, chosen):
    ok = 0

    all_permutations = list(permutations(people, team_size))
    
    for outcome in all_permutations:
        if all(person in outcome for person in chosen):
            ok += 1

    return 1.0 * ok / len(all_permutations)


if __name__ == "__main__":
    people = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
    chosen = ["a", "c"]
    print(sim_team_random(people=people, team_size=4, chosen=chosen, attempts=100000))
    print(sim_team_exact(people=people, team_size=4, chosen=chosen))
