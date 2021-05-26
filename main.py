import pygame
import settings

pygame.init()
pygame.display.set_caption(settings.WINDOW_TITLE)
screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
screen.fill((50,200,50))
done = False

#field
pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(20, 20, settings.FIELD_SIZE, settings.FIELD_SIZE))

myfont = pygame.font.SysFont('sans-serif', 30)
#button1
pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(500, 20, 200, 50))
textsurface = myfont.render('Clear', False, (0, 0, 0))
screen.blit(textsurface, (580, 30))

#button2
pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(500, 80, 200, 50))
textsurface = myfont.render('Predict', False, (0, 0, 0))
screen.blit(textsurface, (580, 90))

#text
pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(500, 140, 200, 50))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, settings.PIXEL_SIZE, settings.PIXEL_SIZE))

    pygame.display.flip()