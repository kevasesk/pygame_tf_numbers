import settings

class Drawing:

    def __init__(self, pygameObject, screenObject, font):
        self.pygameObject = pygameObject
        self.screenObject = screenObject
        self.font = font

    def drawButton(title, position):
        x, y = position
        self.pygameObject.draw.rect(self.screenObject, settings.BUTTON_BACKGROUND_COLOR,
            self.pygameObject.Rect(x, y, settings.BUTTON_WIDTH, settings.BUTTON_HEIGHT)
        )
        textsurface = self.font.render(title, False, settings.BUTTON_TEXT_COLOR)
        self.screenObject.blit(textsurface, (x + x/4, y))

    def drawText(title, position):
        x, y = position
        self.pygameObject.draw.rect(self.screenObject, settings.TEXT_COLOR, self.pygameObject.Rect(x, y, settings.TEXT_WIDTH, settings.TEXT_HEIGHT))

    def drawPixel(position):
        x, y = position
        self.pygameObject.draw.rect(screen, settings.PIXEL_COLOR, self.pygameObject.Rect(x, y, settings.PIXEL_SIZE, settings.PIXEL_SIZE))
