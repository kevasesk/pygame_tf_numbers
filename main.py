import pygame
import settings

pygame.init()
pygame.display.set_caption(settings.WINDOW_TITLE)
screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
screen.fill(settings.WINDOW_COLOR)
done = False

#field
pygame.draw.rect(screen, settings.FIELD_BACKGROUND_COLOR,
    pygame.Rect(
        settings.FIELD_MARGIN_X,
        settings.FIELD_MARGIN_Y,
        settings.FIELD_SIZE,
        settings.FIELD_SIZE
    )
 )

myfont = pygame.font.SysFont(settings.FONT_STYLE, settings.FONT_SIZE)

#button1
pygame.draw.rect(screen, settings.BUTTON_BACKGROUND_COLOR, pygame.Rect(500, 20, settings.BUTTON_WIDTH, settings.BUTTON_HEIGHT))
textsurface = myfont.render('Clear', False, settings.BUTTON_TEXT_COLOR)
screen.blit(textsurface, (580, 30))

#button2
pygame.draw.rect(screen, settings.BUTTON_BACKGROUND_COLOR, pygame.Rect(500, 80, settings.BUTTON_WIDTH, settings.BUTTON_HEIGHT))
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
            if
                (x > settings.FIELD_MARGIN_X and x < settings.FIELD_MARGIN_X + settings.FIELD_SIZE) and
                (y > settings.FIELD_MARGIN_Y and y < settings.FIELD_MARGIN_Y + settings.FIELD_SIZE)
            :
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, settings.PIXEL_SIZE, settings.PIXEL_SIZE))

    pygame.display.flip()
