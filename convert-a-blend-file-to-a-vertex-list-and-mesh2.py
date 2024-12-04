def create_obj_file(vertex, edges, filename):
    """
    Создает OBJ-файл из заданных вершин и граней.

    :param vertex: Массив вершин в формате [(x, y, z),...]
    :param edges: Массив граней в формате [(v1, v2, v3),...], где v1, v2, v3 - индексы вершин
    :param filename: Имя файла OBJ
    """
    with open(filename, 'w') as f:
        # Записать вершины
        for i, v in enumerate(vertex):
            f.write(f"v {v[0]} {v[1]} {v[2]}\n")

        # Записать грани
        for edge in edges:
            f.write(f"f {edge[0] + 1} {edge[1] + 1} {edge[2] + 1}\n")

# Пример использования
vertex = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
edges = [(0, 1, 2), (0, 2, 3)]
create_obj_file(vertex, edges, "example.obj")
