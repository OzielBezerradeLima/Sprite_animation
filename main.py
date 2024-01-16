import pygame
import spritesheet

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load('NES - Super Mario Bros - Mario & Luigi.png').convert_alpha()
sprite_sheet = spritesheet.SprteSheet(sprite_sheet_image)

BG = (50, 50, 50)
LIGHT_SLATE_BLUE = (146, 144, 255)

animation_list = []
animation_steps = [1, 3, 1]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 250
frame = 0
step_counter = 0

for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, action, 16, 16, 4, LIGHT_SLATE_BLUE))
        step_counter += 1
    animation_list.append(temp_img_list)
    action += 1

action = 0

run = True
while run:

    screen.fill(BG)

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0

    screen.blit(animation_list[action][frame], (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            frame = 0
            if event.key == pygame.K_DOWN:
                action = 0
            if event.key == pygame.K_RIGHT:
                action = 1
            if event.key == pygame.K_UP:
                action = 2

    pygame.display.update()

pygame.quit()
