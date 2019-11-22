import sys, pygame, random
from threading import Thread

max_frame_ticker = 100
frame_ticker = max_frame_ticker

pygame.font.init()

sw = 600
sh = 600
fullscreen = False
caption = "snake"

if not fullscreen:
    screen = pygame.display.set_mode((sw, sh))
else:
    screen = pygame.display.set_mode((sw, sh), pygame.FULLSCREEN)
pygame.display.set_caption(caption)

def generate_colission_box(objx, objy, objh, objw):
    a = (objx, objy)
    b = (objx + objw, objy)
    c = (objx + objw, objy - objh)
    d = (objx, objy - objh)
    return([a, b, c, d])

def check_colission(cb1, cb2):
    a1 = cb1[0]
    a2 = cb2[0]
    b1 = cb1[1]
    b2 = cb2[1]
    c1 = cb1[2]
    c2 = cb2[2]
    d1 = cb1[3]
    d2 = cb2[3]
    if a1[0] <= a2[0] or a2[0] >= a1[0]:
        if b1[0] >= b2[0] or b2[0] <= b1[0]:
            if c1[1] <= c2[1] or c2[1] >= c1[1]:
                if d1[1] >= d2[1] or d2[1] <= d1[1]:
                    return(True)
                else:
                    return(False)
            else:
                return(False)
        else:
            return(False)
    else:
        return(False)

class snake_head:
    w = 20
    h = 20
    start = (20, 80)
    length = 1
    color = (255,255,0)
    pos = start
    cube = (0, 0)
    snake = [(1, 4), (1, 5)]

class snake_dot:
    w = 20
    h = 20
    color = (0,0,0)

def snakeonpos(pos):
    for i in snake_head.snake:
        if pos == i:
            return(True)
        else:
            return(False)

def snakeheadonpos(pos):
    head = snake_head.snake[0]
    if pos == head:
        return(True)
    else:
        return(False)

def touchessnakebody(pos):
    for i in snake_head.snake:
        if snake_head.snake.index(i) == 0:
            pass
        else:
            if pos == i:
                return(True)
            else:
                return(False)

# MAIN GAMELOOP
gameClock = pygame.time.Clock()
direction = "up"
appleCollected = False

newApple = (random.randint(2, 27), random.randint(2, 27))
if not snakeonpos(newApple):
    applePos = newApple
else:
    while True:
        newApple = (random.randint(2, 27), random.randint(2, 27))
        if not snakeonpos(newApple):
            applePos = newApple
            break
        else:
            pass


while True:
    if frame_ticker == max_frame_ticker:
        isMaxTicker = True
        frame_ticker = 0
        pygame.display.update()
    else:
    	isMaxTicker = False
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit(print("Quitting..."))
    screen.fill((255,255,255))
    pygame.draw.rect(screen, snake_head.color, (snake_head.pos[0], snake_head.pos[1], 20, 20))
    for n in range(0, snake_head.length):
        pygame.draw.rect(screen, snake_dot.color, (snake_head.snake[n + 1][0] * 20, snake_head.snake[n + 1][1] * 20, 20, 20))
    pygame.draw.rect(screen, (255,0,0), (applePos[0] * 20, applePos[1] * 20, 20, 20))
    if snake_head.snake[0] == applePos:
        appleCollected = True
        snake_head.snake.append((-100, -100))
        snake_head.length += 1
    for i in snake_head.snake:
        head = snake_head.snake[0]        
        up = (head[0], head[1] - 1)
        down = (head[0], head[1] + 1)
        left = (head[0] - 1, head[1])
        right = (head[0] + 1, head[1])
        if direction == "up" and i == up:
            sys.exit(print("Game Over"))
        elif direction == "down" and i == down:
            sys.exit(print("Game Over"))
        elif direction == "left" and i == left:
            sys.exit(print("Game Over"))
        elif direction == "right" and i == right:
            sys.exit(print("Game Over"))
        else:
            pass
    keys = pygame.key.get_pressed()
    for key in keys:
    	if keys[pygame.K_UP]:
    		direction = "up"
    	elif keys[pygame.K_DOWN]:
    		direction = "down"
    	elif keys[pygame.K_LEFT]:
    		direction = "left"
    	elif keys[pygame.K_RIGHT]:
    		direction = "right"
    	else:
    		pass
    
    if isMaxTicker:
        if direction == "up":
            previous_dot = None
            for i in snake_head.snake:
                if snake_head.snake.index(i) == 0:
                    previous_dot = i
                    snake_head.snake[0] = i[0], i[1] - 1
                else:
                   mem = previous_dot
                   previous_dot = i
                   snake_head.snake[snake_head.snake.index(i)] = mem
        elif direction == "down":
            previous_dot = None
            for i in snake_head.snake:
                if snake_head.snake.index(i) == 0:
                    previous_dot = i
                    snake_head.snake[0] = i[0], i[1] + 1
                else:
                    mem = previous_dot
                    previous_dot = i
                    snake_head.snake[snake_head.snake.index(i)] = mem
        elif direction == "right":
            previous_dot = None
            for i in snake_head.snake:
                if snake_head.snake.index(i) == 0:
                    previous_dot = i
                    snake_head.snake[0] = i[0] + 1, i[1]
                else:
                    mem = previous_dot
                    previous_dot = i
                    snake_head.snake[snake_head.snake.index(i)] = mem
        elif direction == "left":
            previous_dot = None
            for i in snake_head.snake:
                if snake_head.snake.index(i) == 0:
                    previous_dot = i
                    snake_head.snake[0] = i[0] - 1, i[1]
                else:
                    mem = previous_dot
                    previous_dot = i
                    snake_head.snake[snake_head.snake.index(i)] = mem
    if appleCollected == True:
        appleCollected = False
        newApple = (random.randint(2, 27), random.randint(2, 27))
        if not snakeonpos(newApple):
            applePos = newApple
        else:
            while True:
                newApple = (random.randint(2, 27), random.randint(2, 27))
                if not snakeonpos(newApple):
                    applePos = newApple
                    break
                else:
                    pass

    if snake_head.snake[0][0] == 30:
        snake_head.snake[0] = (1, snake_head.snake[0][1])
    if snake_head.snake[0][0] == 0:
        snake_head.snake[0] = (29, snake_head.snake[0][1])
    if snake_head.snake[0][1] == 30:
        snake_head.snake[0] = (snake_head.snake[0][0], 1)
    if snake_head.snake[0][1] == 0:
        snake_head.snake[0] = (snake_head.snake[0][0], 29)
        
    snake_head.pos = (snake_head.snake[0][0] * 20, snake_head.snake[0][1] * 20)
    frame_ticker += 1
    
    
    
