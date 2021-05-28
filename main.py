import pygame
import settings

from drawing import Drawing

pygame.init()
pygame.display.set_caption(settings.WINDOW_TITLE)
screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
screen.fill(settings.WINDOW_COLOR)
myfont = pygame.font.SysFont(settings.FONT_STYLE, settings.FONT_SIZE)
drawing = Drawing(pygame, screen, myfont)
done = False
drawing_processing = False

#field
drawing.drawField()
drawing.drawButton('Clear', (500, 20))
drawing.drawButton('Predict', (500, 80))
drawing.drawText('123', (500, 140))

while not done:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing_processing = True
            drawing.clear(pos, (500, 20))


        if event.type == pygame.MOUSEBUTTONUP:
            drawing_processing = False

    if drawing.isInField(pos) and drawing_processing:
        drawing.drawPixel(pos)
    pygame.display.flip()
