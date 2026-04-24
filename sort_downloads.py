import os
import shutil
from pathlib import Path

# Определяем путь к папке загрузок (работает для Windows, macOS и Linux)
downloads_path = Path.home() / "Downloads"

# Словарь категорий и соответствующих им расширений
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx", ".csv", ".rtf"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Video": [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
    "Music": [".mp3", ".wav", ".flac", ".ogg"],
    "Programs": [".exe", ".msi", ".dmg", ".pkg", ".deb"],
}

def organize_downloads():
    # Проверяем, существует ли папка
    if not downloads_path.exists():
        print(f"Папка {downloads_path} не найдена.")
        return

    # Проходим по всем файлам в папке Загрузки
    for item in downloads_path.iterdir():
        # Пропускаем папки и сам скрипт, если он лежит в той же папке
        if item.is_dir() or item.name == "__file__":
            continue

        # Получаем расширение файла в нижнем регистре
        extension = item.suffix.lower()
        moved = False

        # Ищем подходящую категорию
        for category, extensions in FILE_CATEGORIES.items():
            if extension in extensions:
                dest_folder = downloads_path / category
                
                # Создаем папку категории, если её нет
                dest_folder.mkdir(exist_ok=True)
                
                # Перемещаем файл
                try:
                    shutil.move(str(item), str(dest_folder / item.name))
                    print(f"Перемещен: {item.name} -> {category}")
                except Exception as e:
                    print(f"Ошибка при перемещении {item.name}: {e}")
                
                moved = True
                break

        # Если расширение не найдено в списке, перемещаем в "Others"
        if not moved:
            others_folder = downloads_path / "Others"
            others_folder.mkdir(exist_ok=True)
            shutil.move(str(item), str(others_folder / item.name))
            print(f"Перемещен (прочее): {item.name} -> Others")

if __name__ == "__main__":
    print("Начинаю сортировку файлов...")
    organize_downloads()
    print("Готово!")
