import vehictrl as vc
import pygame


def initt():
    vc.init()
    pygame.init()
    pygame.display.set_mode((320, 240))
    pass


if __name__ == '__main__':
    try:
        initt()
        loop = True
        while(loop):
            for event in pygame.event.get():
                if event.type ==  pygame.KEYDOWN:
                    key_input = pygame.key.get_pressed()
                    if key_input[pygame.K_w]:
                        print("W")
                        vc.moveFore()
                    elif key_input[pygame.K_s]:
                        print("S")
                        vc.moveBack()
                    elif key_input[pygame.K_a]:
                        print("A")
                        vc.moveLeft()
                    elif key_input[pygame.K_d]:
                        print("D")
                        vc.moveRight()
                    elif key_input[pygame.K_q]:
                        print("Q")
                        vc.turnLeft()
                    elif key_input[pygame.K_e]:
                        print("E")
                        vc.turnRight()
                    elif key_input[pygame.K_SPACE]:
                        print("Space")
                        vc.stop()
                    elif key_input[pygame.K_z]:
                        print("Z")
                        vc.stop()
                        loop = False
                    pass
    finally:
        print("End")
        vc.release()
        pass