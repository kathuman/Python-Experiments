"""
This file will 
1.- contain the main drive file.
2.- Handle player input
3.- display the current gameplay object
"""
import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

'''
Initialize a global dictionary of images. This will be called exactly once in main
'''

def loadImages():
    pieces = ['wp','wR','wN','wB','wQ','wK','bp','bR','bN','bB','bQ','bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(piece+".png"), (SQ_SIZE, SQ_SIZE))
    # note that we can access a piece by saying IMAGES['wp'] for example

'''
This will be our main driver
1.- handle user imput
2.- Update the graphics
'''


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    sqSelected = () # no square is selected initially - one tuple:(row,col)
    playerClicks = [] # keep tracks of the player clicks - two tuples: [(6,4),(4,4)]
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
                p.quit()
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # (x, y) coordinates for the mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                #check if the user already selected this square, as it wqould be an undo
                if sqSelected = (row,col):
                    sqSelected = () #Unselect the square
                    playerClicks = [] #reset the clicks
                sqSelected = (row,col)
                playerClicks.append(sqSelected) # we append both the first and second clicks
            #was this the user's secodn click?
                if len(playerClicks)==2: #after the second click
                    
            
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


'''
Responsible for all the graphics within the cyurrent gamestate
'''
def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

'''
Will draw the board
'''
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("grey")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


'''
Will draw the pieces considering the current game state
'''
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece],p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()
