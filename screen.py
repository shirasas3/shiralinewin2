import pygame

def text():
    pygame.font.init()
background_colour = (9, 99, 0)
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("The Flag")
    font = pygame.font.SysFont("ariel", 20)
text1 = font.render("Welcome to The Flag game.", True, (255, 255, 255))
text2 = font.render("Have Fun!", True, (255, 255, 255))
screen.blit(text1, (20, 20))
screen.blit(text2, (20, 20))
screen.fill(background_colour)
textRect1 = text1.get_rect()
textRect2 = text2.get_rect()
textRect1.center = (100, 20)
textRect2.center = (45, 35)
pygame.display.flip()
running = True
while running:
    screen.blit(text1, textRect1.topleft)
    screen.blit(text2, textRect2.topleft)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.display.update()