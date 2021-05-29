import settings
from network.brain import *

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

    def drawBrush(self, position):
        x, y = self.calculatePixelPosition(position)

        if self.isInField((x, y + settings.PIXEL_SIZE)):
            self.pygameObject.draw.rect(self.screenObject, settings.BLACK,
                                        self.pygameObject.Rect(x, y + settings.PIXEL_SIZE, settings.PIXEL_SIZE, settings.PIXEL_SIZE))

        if self.isInField((x, y - settings.PIXEL_SIZE)):
            self.pygameObject.draw.rect(self.screenObject, settings.BLACK,
                                    self.pygameObject.Rect(x, y - settings.PIXEL_SIZE, settings.PIXEL_SIZE, settings.PIXEL_SIZE))

        if self.isInField((x + settings.PIXEL_SIZE, y)):
            self.pygameObject.draw.rect(self.screenObject, settings.BLACK,
                                    self.pygameObject.Rect(x + settings.PIXEL_SIZE, y, settings.PIXEL_SIZE, settings.PIXEL_SIZE))

        if self.isInField((x - settings.PIXEL_SIZE, y)):
            self.pygameObject.draw.rect(self.screenObject, settings.BLACK,
                                    self.pygameObject.Rect(x - settings.PIXEL_SIZE, y, settings.PIXEL_SIZE, settings.PIXEL_SIZE))

        self.pygameObject.draw.rect(self.screenObject, settings.BLACK,
                                    self.pygameObject.Rect(x, y, settings.PIXEL_SIZE, settings.PIXEL_SIZE))

    def isInField(self, position):
        x, y = self.calculatePixelPosition(position)
        return (x >= settings.FIELD_MARGIN_X and x < settings.FIELD_SIZE + settings.FIELD_MARGIN_X) \
               and (y >= settings.FIELD_MARGIN_Y and y < settings.FIELD_SIZE + settings.FIELD_MARGIN_X)

    def isClickOnButton(self, clickPosition, elementPosition):
        clickX, clickY = clickPosition
        elemX, elemY = elementPosition
        if (clickX > elemX and clickX < elemX + settings.BUTTON_WIDTH) \
                and (clickY > elemY and clickY < elemY + settings.BUTTON_HEIGHT):
            return True
        return False

    def calculatePixelPosition(self, position):
        x, y = position
        x = int( (x - settings.FIELD_MARGIN_X) / settings.PIXEL_SIZE) * settings.PIXEL_SIZE + settings.FIELD_MARGIN_X
        y = int( (y - settings.FIELD_MARGIN_X) / settings.PIXEL_SIZE) * settings.PIXEL_SIZE + settings.FIELD_MARGIN_X
        return (x,y)

    def clear(self):
        self.drawField()

    def predict(self):
        result = []
        for x in range(0, settings.CELLS) :
            for y in range(0, settings.CELLS):
                coordX = x * settings.PIXEL_SIZE + settings.FIELD_MARGIN_X + 2
                coordY = y * settings.PIXEL_SIZE + settings.FIELD_MARGIN_Y + 2
                if self.screenObject.get_at((coordY, coordX)) == settings.BLACK:
                    result.append(255)
                if self.screenObject.get_at((coordY, coordX)) == settings.GREY:
                    result.append(200)
                if self.screenObject.get_at((coordY, coordX)) == settings.WHITE:
                    result.append(0)

        return predict(result)

    def drawPredictions(self):
        self.predict()
