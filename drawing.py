import settings

class Drawing:

    def __init__(self, pygameObject, screenObject, font):
        self.pygameObject = pygameObject
        self.screenObject = screenObject
        self.font = font

    def drawField(self):
        self.pygameObject.draw.rect(self.screenObject, settings.FIELD_BACKGROUND_COLOR,
             self.pygameObject.Rect(
                 settings.FIELD_MARGIN_X,
                 settings.FIELD_MARGIN_Y,
                 settings.FIELD_SIZE,
                 settings.FIELD_SIZE
             )
        )

    def drawButton(self, title, position):
        x, y = position
        self.pygameObject.draw.rect(self.screenObject, settings.BUTTON_BACKGROUND_COLOR,
            self.pygameObject.Rect(x, y, settings.BUTTON_WIDTH, settings.BUTTON_HEIGHT)
        )
        textsurface = self.font.render(title, False, settings.BUTTON_TEXT_COLOR)
        self.screenObject.blit(textsurface, (x + 45, y + 15))

    def drawText(self, title, position):
        x, y = position
        self.pygameObject.draw.rect(self.screenObject, settings.TEXT_COLOR, self.pygameObject.Rect(x, y, settings.TEXT_WIDTH, settings.TEXT_HEIGHT))

    def drawPixel(self, position):
        x, y = self.calculatePixelPosition(position)
        self.pygameObject.draw.rect(self.screenObject, settings.PIXEL_COLOR, self.pygameObject.Rect(x, y, settings.PIXEL_SIZE, settings.PIXEL_SIZE))

    def isInField(self, position):
        x, y = self.calculatePixelPosition(position)
        return (x >= settings.FIELD_MARGIN_X and x < settings.FIELD_SIZE + settings.FIELD_MARGIN_X) \
               and (y >= settings.FIELD_MARGIN_Y and y < settings.FIELD_SIZE + settings.FIELD_MARGIN_X)

    def calculatePixelPosition(self, position):
        x, y = position
        x = int( (x - settings.FIELD_MARGIN_X) / settings.PIXEL_SIZE) * settings.PIXEL_SIZE + settings.FIELD_MARGIN_X
        y = int( (y - settings.FIELD_MARGIN_X) / settings.PIXEL_SIZE) * settings.PIXEL_SIZE + settings.FIELD_MARGIN_X
        return (x,y)

    def clear(self, clickPosition, elementPosition):
        clickX, clickY = clickPosition
        elemX, elemY = elementPosition
        if (clickX > elemX and clickX < elemX + settings.BUTTON_WIDTH) \
                and (clickY > elemY and clickY < elemY + settings.BUTTON_HEIGHT):
            self.drawField()
