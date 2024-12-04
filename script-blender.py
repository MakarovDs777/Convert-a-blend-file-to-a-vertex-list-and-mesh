import bpy

def blend_to_text(blend_file):
    # Открываем файл Blender
    bpy.ops.wm.open_mainfile(name=blend_file)

    # Получаем список всех объектов в сцене
    objects = bpy.context.scene.objects

    # Инициализируем пустые массивы для вершин и граней
    vertices = []
    edges = []

    # Перебираем все объекты в сцене
    for obj in objects:
        # Получаем список всех вершин объекта
        for vertex in obj.data.vertices:
            # Добавляем координаты вершины в список
            vertices.append(vertex.co)

        # Получаем список всех граней объекта
        for edge in obj.data.edges:
            # Добавляем индексы вершин грани в список
            edges.append([edge.vertices[0], edge.vertices[1]])

    # Закрываем файл Blender
    bpy.ops.wm.quit_blender()

    # Возвращаем массивы вершин и граней в виде строки
    return "Vertices: " + str(vertices) + "\nEdges: " + str(edges)

# Пример использования функции
blend_file = "путь_к_файлу.blend"
text = blend_to_text(blend_file)
print(text)
