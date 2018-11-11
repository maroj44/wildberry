from WindowAndScreenStuff.Window import Window
from WindowAndScreenStuff.StartScreen import StartScreen
from WindowAndScreenStuff.GameScreen import GameScreen

GAME_TITLE = "Wildberry"
WIDTH = 1200
HEIGHT = 800


class Game:
    def __init__(self):
        self._wildberryWindow = Window(GAME_TITLE,WIDTH,HEIGHT)

    def getGameWindow(self):
        return self._wildberryWindow.getWindow()

    def run(self):
        StartScreen(self.getGameWindow())
        while(True):
            GameScreen(self.getGameWindow())







if __name__ == "__main__":
    game = Game()
    game.run()