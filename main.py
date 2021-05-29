import pygame
import settings
import numpy as np

from drawing import Drawing

pygame.init()
pygame.display.set_caption(settings.WINDOW_TITLE)
screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
screen.fill(settings.WINDOW_COLOR)
myfont = pygame.font.SysFont(settings.FONT_STYLE, settings.FONT_SIZE)
drawing = Drawing(pygame, screen, myfont)
done = False
drawing_processing = False

#init drawing
drawing.drawField()
drawing.drawButton('Clear', (500, 20))
drawing.drawButton('Predict', (500, 80))

#drawing numbers predictions

while not done:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing_processing = True
            if drawing.isClickOnButton(pos, (500, 20)):
                drawing.clear()
            if drawing.isClickOnButton(pos, (500, 80)):
                predictions = drawing.predict()
                print(predictions)
                print(np.argmax(predictions))

        if event.type == pygame.MOUSEBUTTONUP:
            drawing_processing = False
            drawing.drawPredictions()

    if drawing.isInField(pos) and drawing_processing:
        drawing.drawBrush(pos)

    pygame.display.flip()
