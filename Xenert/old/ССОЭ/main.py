import pygame
from pygame.locals import *
import numpy as np
from PIL import Image

# Initialize Pygame
pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Topographic profile generator")

# Load height map
height_map = Image.open("heightmap.png")
height_map = height_map.convert("RGB")
height_map = np.array(height_map)

def get_height_color(x):
    if x < 0.001:
        return (0, 13, 80)
    elif x < 0.1:
        return blend((0, 80, 30), (43, 117, 0), norm(x, 0, 0.1))
    elif x < 0.3:
        return blend((43, 117, 0), (191, 139, 44), norm(x, 0.1, 0.3))
    elif x < 0.55:
        return blend((191, 139, 44), (89, 46, 34), norm(x, 0.3, 0.55))
    elif x < 0.8:
        return blend((89, 46, 34), (90, 90, 90), norm(x, 0.55, 0.8))
    else:
        return blend((90, 90, 90), (255, 255, 255), norm(x, 0.8, 1))

def blend(color1, color2, ratio):
    blended = [int((1 - ratio) * c1 + ratio * c2) for c1, c2 in zip(color1, color2)]
    return tuple(blended)

def norm(x, min_val, max_val):
    return (x - min_val) / (max_val - min_val)

def generate_palette_map_image():
    result = np.zeros_like(height_map)
    for y in range(height_map.shape[0]):
        for x in range(height_map.shape[1]):
            height = np.mean(height_map[y, x]) / 255.0

            up_height = np.mean(height_map[max(y - 1, 0), x]) / 255.0
            right_height = np.mean(height_map[y, min(x + 1, height_map.shape[1] - 1)]) / 255.0
            down_height = np.mean(height_map[min(y + 1, height_map.shape[0] - 1), x]) / 255.0
            left_height = np.mean(height_map[y, max(x - 1, 0)]) / 255.0

            hillshade = get_shading(height, left_height, right_height, up_height, down_height)
            result[y, x] = np.array(get_height_color(height)) * hillshade

    return result

def get_shading(middle, left, right, up, down):
    res = 1.0
    res *= np.clip(1.0 + ((right - middle) - (left - middle)) * (left > middle and middle > right and 6.0 or 1.0), 0.5, 2.0)
    res *= np.clip(1.0 + ((down - middle) - (up - middle)) * (up > middle and middle > down and 6.0 or 1.0), 0.5, 2.0)
    return res

def generate_image():
    result = generate_palette_map_image()
    return pygame.image.frombuffer(result.transpose(1, 0, 2), result.shape[:2][::-1], 'RGB')

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill((0, 0, 0))
    image = generate_image()
    if image:
        screen.blit(image, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
