import cmpt120image
import pygame
import random
pygame.display.set_mode((1, 1))


def recolor_image(img, color):
  height, width = len(img), len(img[0])
  new_img = cmpt120image.get_black_image(width, height)

  for y in range(height):
    for x in range(width):
      if img[y][x] != [0,0,0]:
        new_img[y][x] = color
      else:
        new_img[y][x] = img[y][x]

  return new_img

def minify(img):
  height, width = len(img), len(img[0])
  new_img = cmpt120image.get_black_image(height, width)

  for y in range(0, height, 2):
    for x in range(0, width, 2):
      pixel1 = img[y][x]
      pixel2 = img[y][x+1]
      pixel3 = img[y+1][x]
      pixel4 = img[y+1][x+1]

      average_r = (pixel1[0] + pixel2[0] + pixel3[0] + pixel4[0])
      average_g = (pixel1[1] + pixel2[1] + pixel3[1] + pixel4[1])
      average_b = (pixel1[2] + pixel2[2] + pixel3[2] + pixel4[2])

      new_img[y//2][x//2]  = [average_r, average_g, average_b]

    return new_img

def mirror(img):
  height, width = len(img), len(img[0])
  new_img = cmpt120image.get_black_image(width, height)

  for i in range(height):
    new_img[i] = img[i][::-1]

  return new_img
  
def draw_item(canvas, item, row, col):
  item_height, item_width = len(item), len(item[0])

  for i in range(item_height):
    for j in range(item_width):
      canvas_row = row + j
      canvas_col = col + j

      canvas[canvas_row][canvas_col] = item[i][j]

  return canvas
  
def distribute_items(canvas, item, n):
  for i in range(n):
    row = random.randint(0, len(canvas) - len(item))
    col = random.randint(0, len(canvas[0]) - len(item[0]))
    draw_item(canvas, item, row, col)

  return canvas
