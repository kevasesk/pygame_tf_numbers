import settings

class Drawing:

    def __init__(self, pygameObject, screenObject, font):
        self.pygameObject = pygameObject
        self.screenObject = screenObject
        self.font = font

    def drawButton(title, position):
        self.pygameObject.draw.rect(self.screenObject, settings.BUTTON_BACKGROUND_COLOR,
            self.pygameObject.Rect(500, 20, settings.BUTTON_WIDTH, settings.BUTTON_HEIGHT)
        )
        textsurface = self.font.render(title, False, settings.BUTTON_TEXT_COLOR)
        self.screenObject.blit(textsurface, (580, 30))
