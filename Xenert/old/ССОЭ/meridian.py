from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Создаем изображение
width, height = 4500, 2250
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Задайте интервалы для ординат и меридиан
# Например, интервалы для широт от -90 до 90 и интервалы для долгот от -180 до 180
latitude_intervals = np.arange(-90, 91, 5)
longitude_intervals = np.arange(-175, 176, 5)

# Функция для преобразования географических координат в пиксели
def geo_to_pixel(latitude, longitude):
    x = (longitude + 180) * (width - 1) / 360
    y = (90 - latitude) * (height - 1) / 180
    return x, y

# Рисуем меридианы (вертикальные линии) и добавляем нумерацию
for longitude in longitude_intervals:
    if longitude != -180 and longitude != 180:
        x, _ = geo_to_pixel(0, longitude)
        draw.line([(x, 0), (x, height)], fill="gray", width=1)
        
        font = ImageFont.load_default()
        text = str(longitude)
        text_width, text_height = draw.textsize(text, font)
        draw.text((x - text_width // 2, height - text_height), text, fill="black", font=font)
        draw.text((x - text_width // 2, 0), text, fill="black", font=font)

# Рисуем ординаты (горизонтальные линии) и добавляем нумерацию
for latitude in latitude_intervals:
    if latitude != -90 and latitude != 90:
        _, y = geo_to_pixel(latitude, 0)
        draw.line([(0, y), (width, y)], fill="gray", width=1)
        
        font = ImageFont.load_default()
        text = str(latitude)
        text_width, text_height = draw.textsize(text, font)
        draw.text((0, y - text_height // 2), text, fill="black", font=font)
        draw.text((width - text_width, y - text_height // 2), text, fill="black", font=font)

# Добавляем центральную метку
center_x, center_y = geo_to_pixel(0, 0)
draw.ellipse([(center_x - 5, center_y - 5), (center_x + 5, center_y + 5)], fill="red")

# Сохраняем изображение
image.save("grid_image_with_labels.png")
image.show()
