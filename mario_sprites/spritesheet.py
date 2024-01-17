import pygame

class SprteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, action, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha()

        if action == 0:
            image.blit(self.sheet, (0, 0), ((frame * width), 8, width, height))
        elif action == 1:
            image.blit(self.sheet, (0, 0), (((frame * width) + 2 + (frame * 2)), 8, width, height))
        elif action == 2:
            image.blit(self.sheet, (0, 0), ((frame * width) + 32, 8, width, height))

        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)

        return image
