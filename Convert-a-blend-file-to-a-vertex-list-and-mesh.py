import numpy as np
import tkinter as tk
from tkinter import filedialog
import os

def obj_to_text(obj_file):
    vertices = []
    faces = []

    with open(obj_file, 'r') as file:
        for line in file:
            if line.startswith('v '):  # Вершины начинаются с 'v '
                vertex = list(map(float, line.strip().split()[1:]))
                vertices.append(vertex)
            elif line.startswith('f '):  # Грани начинаются с 'f '
                face = [int(idx.split('/')[0]) - 1 for idx in line.strip().split()[1:]]
                faces.append(face)

    return f"Vertices: {vertices}\nFaces: {faces}"

def save_to_file(text):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "output.txt")
    with open(desktop_path, 'w') as file:
        file.write(text)
    print(f"Сохранено в {desktop_path}")

def select_obj_file():
    root = tk.Tk()
    root.withdraw()  # Скрываем корневое окно
    file_path = filedialog.askopenfilename(title="Выберите файл OBJ", filetypes=[("OBJ files", "*.obj")])
    if file_path:  # Проверяем, выбран ли файл
        text = obj_to_text(file_path)
        print(text)
        save_to_file(text)  # Сохраняем текст в файл
    else:
        print("Файл не выбран.")

# Запуск диалогового окна
select_obj_file()

