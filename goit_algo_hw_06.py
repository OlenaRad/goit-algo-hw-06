# -*- coding: utf-8 -*-
"""goit-algo-hw-06

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hRp4nSYrm7-qcbsE4ByobOcm9g_RmUz-

Завдання 1.
Створіть граф за допомогою бібліотеки networkX для моделювання певної реальної мережі (наприклад, транспортної мережі міста, соціальної мережі, інтернет-топології). Візуалізуйте створений граф, проведіть аналіз основних характеристик (наприклад, кількість вершин та ребер, ступінь вершин).
"""

import networkx as nx
import matplotlib.pyplot as plt

# Створення пустого графа
G = nx.Graph()

# Додавання вершин (міст)
cities = ['Київ', 'Львів', 'Одеса', 'Харків', 'Дніпро', 'Запоріжжя']
for city in cities:
    G.add_node(city)

# Додавання ребер (дороги) та їх ваг (відстань або час подорожі)
# Наприклад, список ребер та їх ваг може бути у форматі (місто_1, місто_2, відстань_або_час)
roads = [('Київ', 'Львів', 550),
         ('Київ', 'Одеса', 480),
         ('Київ', 'Харків', 480),
         ('Харків', 'Львів', 1010),
         ('Харків', 'Дніпро', 220),
         ('Дніпро', 'Одеса', 480),
         ('Дніпро', 'Запоріжжя', 80),
         ('Одеса', 'Запоріжжя', 470),
         ('Львів', 'Запоріжжя', 960)]

for road in roads:
    G.add_edge(road[0], road[1], weight=road[2])

# Малювання графа
pos = nx.spring_layout(G)  # Позиціонування вершин
nx.draw(G, pos, with_labels=True)  # Малювання графа з мітками вершин
labels = nx.get_edge_attributes(G, 'weight')  # Отримання ваг ребер
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  # Додавання ваг ребер
plt.show()

import networkx as nx
import matplotlib.pyplot as plt

# Створення графа (код створення графа із попереднього відповіді)

# Візуалізація графа
pos = nx.spring_layout(G)  # Позиціонування вершин
nx.draw(G, pos, with_labels=True)  # Малювання графа з мітками вершин
labels = nx.get_edge_attributes(G, 'weight')  # Отримання ваг ребер
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  # Додавання ваг ребер
plt.title("Транспортна мережа міста")
plt.show()

# Аналіз основних характеристик графа
print("Кількість вершин (міст):", G.number_of_nodes())
print("Кількість ребер (доріг):", G.number_of_edges())

# Розрахунок та вивід ступенів вершин
degrees = dict(G.degree())
print("\nСтупені вершин:")
for city, degree in degrees.items():
    print(f"{city}: {degree}")

"""Завдання 2

Напишіть програму, яка використовує алгоритми DFS і BFS для знаходження шляхів у графі, який було розроблено у першому завданні.

Далі порівняйте результати виконання обох алгоритмів для цього графа, висвітлить різницю в отриманих шляхах. Поясніть, чому шляхи для алгоритмів саме такі.
"""

def dfs(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = dfs(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def bfs(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next_node in set(graph[vertex]) - set(path):
            if next_node == end:
                yield path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))

# Граф (код створення графа із попереднього завдання)

# Знаходження шляхів за допомогою DFS та BFS
start_city = 'Київ'
end_city = 'Запоріжжя'

dfs_paths = dfs(G, start_city, end_city)
bfs_paths = list(bfs(G, start_city, end_city))

# Вивід результатів
print("DFS шляхи:")
for path in dfs_paths:
    print(path)

print("\nBFS шляхи:")
for path in bfs_paths:
    print(path)

"""Порівнюємо шляхи алгоритмів.

DFS (Depth First Search) проходить глибше в глибину, шукаючи шлях від початкової вершини до кінцевої. Таким чином, він може зайти далеко у глибокі гілки графа, перш ніж повернутися назад, що призводить до того, що він може знайти шлях, який, хоч і існує, але не є найкоротшим.

BFS (Breadth First Search), навпаки, просувається в ширину, розглядаючи всі сусідні вершини одного рівня перед переходом до вершин наступного рівня. Такий підхід забезпечує знаходження найкоротшого шляху між вершинами.

Отже, різниця полягає в тому, що DFS може знайти будь-який шлях, але він не завжди є найкоротшим, тоді як BFS знаходить найкоротший шлях.

Завдання 3

Реалізуйте алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі: додайте у граф ваги до ребер та знайдіть найкоротший шлях між всіма вершинами графа.
"""

import networkx as nx
import matplotlib.pyplot as plt

# Створення графа (код створення графа із попереднього завдання)

# Додавання ваг до ребер
edge_weights = {('Київ', 'Львів'): 550,
                ('Київ', 'Одеса'): 480,
                ('Київ', 'Харків'): 480,
                ('Харків', 'Львів'): 1010,
                ('Харків', 'Дніпро'): 220,
                ('Дніпро', 'Одеса'): 480,
                ('Дніпро', 'Запоріжжя'): 80,
                ('Одеса', 'Запоріжжя'): 470,
                ('Львів', 'Запоріжжя'): 960}

nx.set_edge_attributes(G, edge_weights, 'weight')

# Алгоритм Дейкстри для знаходження найкоротшого шляху між усіма парами вершин
all_pairs_shortest_paths = dict(nx.all_pairs_dijkstra_path(G, weight='weight'))

# Вивід результатів
for start_city in G.nodes():
    print(f"Найкоротші шляхи з {start_city}:")
    for end_city, path in all_pairs_shortest_paths[start_city].items():
        if start_city != end_city:
            print(f"  {end_city}: {path}, Вага: {nx.shortest_path_length(G, start_city, end_city, weight='weight')}")