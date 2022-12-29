from collections import Counter


def min_cost_destroy_planets(cost, planets):
    total_cost = 0
    orbits = Counter(planets)
    for num_planets in orbits.values():
        if num_planets > 1:
            if cost < num_planets:
                total_cost += cost
            else:
                total_cost += num_planets
        else:
            total_cost += 1
    return total_cost

if __name__ == "__main__":
    number_of_test_cases = int(input())
    answers = []
    for test_case in range(number_of_test_cases):
        num_planets, cost = map(int, input().split())
        planets = map(int, input().split())
        answers.append(min_cost_destroy_planets(cost, planets))
    for answer in answers:
        print(answer)

