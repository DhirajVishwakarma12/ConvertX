			practical 8

2. csf
import itertools

colors = ["Red", "Green", "Blue"]

# Variables
regions = ["A", "B", "C"]

# Generate all possible color combinations
for values in itertools.product(colors, repeat=3):

    A, B, C = values

    # Constraints:
    # A != B
    # B != C
    # A != C

    if A != B and B != C and A != C:
        print("Solution:")
        print("A =", A ,"B =", B ,"C =", C)


			practical 7


1. cards

import random

suits =["2","3","4","5","6","7","8","9","10","A","K","J","Q"]
ranks = ["diamond","spade","club","heart"]

cards =[
    rank +" of "+ suit
        for suit in suits
        for rank in ranks
        ]
random.shuffle(cards)
for card in cards[:4]:
    print(card)


2. tic -tac -to

board = ["" for _ in range(9)]
player = "X"


def show_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def winner(p):
    return (
        (board[0] == p and board[1] == p and board[2] == p) or
        (board[3] == p and board[4] == p and board[5] == p) or
        (board[6] == p and board[7] == p and board[8] == p) or
        (board[0] == p and board[4] == p and board[8] == p) or
        (board[2] == p and board[4] == p and board[6] == p)
    )


def tie():
    return "" not in board


def start():
    global player

    while True:
        show_board()

        try:
            move = int(input(f"Player {player}, enter your move (0-8): "))

            if 0 <= move <= 8 and board[move] == "":
                board[move] = player

                if winner(player):
                    show_board()
                    print(f"Player {player} is winner!")
                    break

                elif tie():
                    show_board()
                    print("Game is a tie.")
                    break

                if player == "X":
                    player = "O"
                else:
                    player = "X"

            else:
                print("Invalid move!")

        except ValueError:
            print("Please enter a number from 0 to 8.")


start()

			practical 6

1. 8-puzzle problem
 
from collections import deque

goal = input("Enter goal state: ")
start = input("Enter starting state: ")

moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

queue = deque([(start, [start])])
visited = {start}

while queue:
    state, path = queue.popleft()

    if state == goal:
        print("\nSteps to reach goal:\n")

        for i, s in enumerate(path):
            print("Step", i)
            print(s[0], s[1], s[2])
            print(s[3], s[4], s[5])
            print(s[6], s[7], s[8])
            print()

        break

    zero = state.index("0")

    for pos in moves[zero]:
        temp = list(state)

        temp[zero], temp[pos] = temp[pos], temp[zero]

        new_state = "".join(temp)

        if new_state not in visited:
            visited.add(new_state)
            queue.append((new_state, path + [new_state]))

else:
    print("No solution")


2. missionaries and cannibals 

from collections import deque

start = (3, 3, 0)
goal = (0, 0, 1)

moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

def valid(m, c):
    return 0 <= m <= 3 and 0 <= c <= 3 and (m == 0 or m >= c)

queue = deque([(start, [start])])
visited = {start}

while queue:
    state, path = queue.popleft()

    m, c, boat = state

    if state == goal:
        for m, c, boat in path:
            print(f"c = {c}, m = {m}, boat = {boat}")
        break

    for dm, dc in moves:

        if boat == 0:
            new = (m-dm, c-dc, 1)
        else:
            new = (m+dm, c+dc, 0)

        if valid(new[0], new[1]) and new not in visited:
            visited.add(new)
            queue.append((new, path + [new]))


		practical 5


1. jug problem
from collections import deque

jug1 = int(input("Enter first jug capacity: "))
jug2 = int(input("Enter second jug capacity: "))
goal = int(input("Enter goal: "))

start = (0, 0)

queue = deque([(start, [start])])
visited = {start}

while queue:
    (a, b), path = queue.popleft()

    if a == goal or b == goal:
        print("\nSteps:")
        for a, b in path:
            print("Jug1 =", a, "Jug2 =", b)
        break

    states = [
        (jug1, b),  # fill jug1
        (a, jug2),  # fill jug2
        (0, b),     # empty jug1
        (a, 0),     # empty jug2
    ]

    # jug1 -> jug2
    x = min(a, jug2 - b)
    states.append((a - x, b + x))

    # jug2 -> jug1
    x = min(b, jug1 - a)
    states.append((a + x, b - x))

    for new in states:
        if new not in visited:
            visited.add(new)
            queue.append((new, path + [new]))
else:
    print("No solution")


2.Travelling Salesman Problem

from itertools import permutations

n = int(input("Enter number of cities: "))

print("Enter distance matrix:")

distance = []

for i in range(n):
    row = list(map(int, input().split()))
    distance.append(row)

cities = range(1, n)

best_path = None
min_cost = float("inf")

for path in permutations(cities):
    route = (0,) + path + (0,)

    cost = 0

    for i in range(len(route) - 1):
        cost += distance[route[i]][route[i + 1]]

    if cost < min_cost:
        min_cost = cost
        best_path = route

print("Best path:", best_path)
print("Minimum cost:", min_cost)


		pratical 4
1. A* 

import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

h = {
    'A': 5,
    'B': 3,
    'C': 1,
    'D': 0
}

def astar(start, goal):
    queue = [(h[start], 0, start, [start])]
    visited = set()

    while queue:
        f, cost, node, path = heapq.heappop(queue)

        if node == goal:
            return path, cost

        if node in visited:
            continue

        visited.add(node)

        for next_node, edge_cost in graph[node].items():
            new_cost = cost + edge_cost
            new_f = new_cost + h[next_node]

            heapq.heappush(
                queue,
                (new_f, new_cost, next_node, path + [next_node])
            )

print(astar('A', 'D'))

2. greedy

import heapq

def greedy(start, goal):
    queue = [(h[start], start, [start])]
    visited = set()

    while queue:
        _, node, path = heapq.heappop(queue)

        if node == goal:
            return path

        if node in visited:
            continue

        visited.add(node)

        for next_node in graph[node]:
            if next_node not in visited:
                heapq.heappush(
                    queue,
                    (h[next_node], next_node, path + [next_node])
                )

print(greedy('A', 'D'))


		practical 3

1.hill climbing

hills = list(map(int, input("Enter hills: ").split()))

i = 0

while True:
    if i < len(hills) - 1 and hills[i + 1] > hills[i]:
        i = i + 1
    else:
        break

print("Hill climbed:", hills[i])
print("Position:", i + 1)

2. aplha and beta proning

def alpha_beta(values, alpha, beta):

    for i in range(len(values)):
        print("Node:", values[i], "Alpha:", alpha, "Beta:", beta)

        alpha = max(alpha, values[i])

        if alpha >= beta:
            print("Pruned at node:", values[i])
            break

    return alpha


values = [3, 5, 2, 9]

result = alpha_beta(values, -999, 999)

print("Best value:", result)

		
		practical 2
1. tower of hanoi
def hanoi(n, source, helper, destination):
    if n == 1:
        print("Move disk from", source, "to", destination)
        return

    hanoi(n-1, source, destination, helper)
    print("Move disk from", source, "to", destination)
    hanoi(n-1, helper, source, destination)


n = int(input("Enter number of disks: "))

hanoi(n, "A", "B", "C")

2. N queen problem
def solve(board, row, n):
    if row == n:
        for r in board:
            print(r)
        return True

    for col in range(n):
        if col not in board:
            board.append(col)

            if solve(board, row + 1, n):
                return True

            board.pop()

    return False


n = int(input("Enter N: "))

board = []

if solve(board, 0, n):
    print("\nQueen Matrix:")

    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


		practial 1


1.dfs
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}

visited = set()


def dfs(graph, visited, root):
    if root not in visited:
        visited.add(root)
        print(root)

        for neighbour in graph[root]:
            dfs(graph, visited, neighbour)


dfs(graph, visited, "A")

2.bfs
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

h = {
    'A': 5,
    'B': 3,
    'C': 2,
    'D': 1,
    'E': 4,
    'F': 0
}

start = 'A'
goal = 'F'

queue = [(h[start], [start])]

while queue:
    queue.sort()
    hv, path = queue.pop(0)

    node = path[-1]
    print("Node:", node, "Heuristic:", h[node])

    if node == goal:
        print("Path:", path)
        break

    for n in graph[node]:
        if n not in path:
            queue.append((h[n], path + [n]))



