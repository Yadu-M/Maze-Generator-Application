import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

def main():      
    pygame.init()
    
    global screen
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()       
           
    running = True    
        
    row_count = 72
    col_count = 128    
    
    cell_width = SCREEN_WIDTH // col_count
    cell_height = SCREEN_HEIGHT // row_count
    
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #Clear screen
        screen.fill(pygame.Color(0,0,0))
        
        #-------------------------Maze logic(Recursive-DFS)----------------------------------#
        #TODO Call the


        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60


if (__name__ == "__main__"):
    main()