from game import Game

if __name__ == "__main__":
    game = Game()

    while game.is_running:
        game.update()

    game.quit()
