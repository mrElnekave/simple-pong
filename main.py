import sys, pygame
import random
import math
pygame.init()
clock = pygame.time.Clock()

size = width, height = 500, 500 # TODO: Decide on final window size

screen = pygame.display.set_mode(size) 

class Ball:
    def __init__(self):
        self.ball_rect = pygame.Rect(width/2, 233, 20, 30)
        # self.xmove = 5
        self.xmove = random.randint (-7, 7)
        if self.xmove == 0:
            self.xmove = 1
        # self.ymove = 5
        self.ymove = math.sqrt(50-(self.xmove**2))
    def move(self):
        self.ball_rect = self.ball_rect.move(self.xmove, self.ymove)
    def reset(self):
        self.ball_rect = pygame.Rect(width/2, 233, 20, 30)
        self.xmove = random.randint (-7, 7)
        if self.xmove == 0:
            self.xmove = 1
        self.ymove = math.sqrt(50-(self.xmove**2))


class Paddle:
    def __init__(self, xPos):
        self.rectangle = pygame.Rect(xPos, 233, 20, 100)
        self.rectangle.center = (xPos, height/2)
        self.points = 0
    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), self.rectangle)
    def collide(self, outsideRectangle):
        return self.rectangle.colliderect(outsideRectangle)
    def move(self, yIncrement):
        self.rectangle.left
        if self.rectangle.left < 0:
            self.rectangle.left = 0
        if self.rectangle.right > width:
            self.rectangle.right = width
        if self.rectangle.top < 0:
            self.rectangle.top = 0 
        if self.rectangle.bottom > height:
            self.rectangle.bottom = height
        self.rectangle = self.rectangle.move(0, yIncrement)
    def move_absolute(self, mousey):
        self.rectangle.centery = mousey
        if self.rectangle.top < 0:
            self.rectangle.top = 0 
        if self.rectangle.bottom > height:
            self.rectangle.bottom = height



    def update(self, ball: Ball):
        r = self.rectangle
        
        if ball.ball_rect.clipline(*r.bottomleft, *r.bottomright):
            ball.ball_rect.top = r.bottom
            ball.ymove *= -1
        if ball.ball_rect.clipline(*r.topleft, *r.topright):
            ball.ball_rect.bottom = r.top
            ball.ymove *= -1
        if ball.ball_rect.clipline(*r.bottomleft, *r.topleft):
            ball.ball_rect.right = r.left            
            ball.xmove *= -1
        if ball.ball_rect.clipline(*r.bottomright, *r.topright):
            ball.ball_rect.left = r.right
            ball.xmove *= -1


paddle1 = Paddle(30)
paddle2 = Paddle(width - 30)
move_speed = 10
ball = Ball()

WHITE = 255, 255, 255
def draw_score(paddle: Paddle, topleft: tuple):
    font = pygame.font.SysFont("Comic Sans MS", 40)
    textobj = font.render(str(paddle.points), 1, WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = topleft
    screen.blit(textobj, textrect)

mousey = 0
mousex = 0
ball_color = (255, 255, 255)
while True:
    for event in pygame.event.get():  # event loop needs to be here
      if event.type == pygame.QUIT:
          pygame.quit()
          break
    ## input
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.move(-move_speed)
    if keys[pygame.K_s]:
        paddle1.move(move_speed)
    if keys[pygame.K_SPACE]:
        R = random.randint (0, 255)
        G = random.randint (0, 255)
        B = random.randint (0, 255)
        ball_color = (R, G, B)
    # if keys[pygame.K_UP]:
    #     paddle2.move(-move_speed)
    # if keys[pygame.K_DOWN]:
    #     paddle2.move(move_speed)
    # pygame.mouse.get_pos() => [x, y]
    mousex, mousey = pygame.mouse.get_pos()
    
    # update 
    paddle2.move_absolute(mousey)

    ball.move()
    if ball.ball_rect.right >= width:
        paddle1.points += 1
        ball.reset()
    if ball.ball_rect.left <= 0:
        paddle2.points += 1
        ball.reset()
    if ball.ball_rect.center[1] >= height or ball.ball_rect.center[1] <= 0:
        ball.ymove *= -1
    paddle1.update(ball)
    paddle2.update(ball)
    ## draw
    screen.fill((100, 0, 0))
    pygame.draw.rect(screen, ball_color, ball.ball_rect)
    paddle1.draw()
    draw_score(paddle1, (200, 100))
    paddle2.draw()
    draw_score(paddle2, (300, 100))
    
    
    pygame.display.update()
    
    clock.tick(50)
    



# while True: 
#     x = input("Say byw:\n")
#     print("Byw")
#     if x == "byw":
#         break
# print("Hellow")
