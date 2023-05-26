def dfs(graph, start):
    visited = set()  # Множество посещенных вершин
    stack = [start]  # Стек для обхода

    while stack:
        vertex = stack.pop()  # Извлекаем вершину из стека

        if vertex not in visited:
            visited.add(vertex)  # Посещаем вершину
            print(vertex)  # Можно изменить на сохранение в путь

            # Добавляем непосещенные соседние вершины в стек
            stack.extend([neighbor for neighbor in graph[vertex] if neighbor not in visited])

# Пример графа
graph = {
    1: [3],
    2: [4],
    3: [1],
    4: [2]
}

# Запуск обхода в глубину
dfs(graph, 1)
