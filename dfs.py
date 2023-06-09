def dfs(graph, start):
    visited = set()  # Множество посещенных вершин
    stack = [(start, 0)]  # Стек для обхода, включая длину шага

    while stack:
        vertex, distance = stack.pop()  # Извлекаем вершину и длину шага из стека

        if vertex not in visited:
            visited.add(vertex)  # Посещаем вершину
            print(vertex, distance)  # Можно изменить на сохранение в путь

            # Добавляем непосещенные соседние вершины с учетом расстояния в стек
            neighbors = graph[vertex]
            for neighbor, step in neighbors:
                if neighbor not in visited:
                    # Пример графа с  длиной шага  между вершинами
                    stack.append((neighbor, distance + step))

<<<<<<<<<<< HEAD
# Добавляем непосещенные соседние вершины с учетом расстояния в стек
 =======
# Пример графа с  длиной шага  между вершинами
>>>> Added comment
graph = {
    1: [(3, 2)],
    2: [(4, 1)],
    3: [],
    4: [(2, 3)]
}

# Запуск обхода в глубину
dfs(graph, 1)

