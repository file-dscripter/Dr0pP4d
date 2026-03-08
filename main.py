import pygame
import random

"""CONSTANTS"""
# window
WIDTH = 600
HEIGHT = 400
FPS = 60
WINDOW_COLOUR = (0,0,0)
TITLE = "Pygame Assessment"

# player
PLAYER_STEP_SIZE = 5
PLAYER_COLOUR = (255,255,255)
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 20
PLAYER_STARTING_X_POSITION = WIDTH/2
PLAYER_STARTING_Y_POSITION = 320

# ball
BALL_STARTING_Y_POSITION = 0
BALL_COLOUR = (255,0,0)
BALL_RADIUS = 10
BALL_FALL_SPEED = 3

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
window.fill(WINDOW_COLOUR)
clock = pygame.time.Clock()
pygame.display.flip()

"""SUBPROGRAMS"""
"""
Procedure:
    checkBallTouchingPlayer
parameters:
    none
purpose:
    checks if the ball's position is making contact or inside the player's hitbox.
produces:
    True, False - boolean values
preconditions:
    none
postconditions:
    if (ball.x <= (player.x+PLAYER_WIDTH)) and (ball.x >= (player.x-PLAYER_WIDTH + 30)) and (ball.y <= (player.y+PLAYER_HEIGHT / 2)) and (ball.y >= (player.y-PLAYER_HEIGHT / 2))
        return true
    elseif
        return false
"""
def checkBallTouchingPlayer():
    if (ball.get_x_position() <= (player.get_x_position()+PLAYER_WIDTH)) and (ball.get_x_position() >= (player.get_x_position()-PLAYER_WIDTH+30)) and (ball.get_y_position() <= (player.get_y_position()+PLAYER_HEIGHT/2)) and (ball.get_y_position() >= (player.get_y_position()-PLAYER_HEIGHT/2)):
        return True # ball is making contact/inside the player's hitbox
    else:
        return False

"""CLASSES"""
# player class
class Player():
    """
    Procedure:
        __init__
    parameters:
        self - class attributes,
        p_xPosition - integer, 
        p_yPosition - integer, 
        p_colour - tuple, 
        p_width - integer, 
        p_height - integer, 
        p_stepSize - integer
    purpose:
        initialise all attributes in the player class
    produces:
        none
    preconditions:
        none
    postconditions:
        xpos = p_xPosition-30
        ypos = p_yPosition
        colour = p_colour
        width = p_width
        height = p_height
        step = p_stepSize

        rect = Rect(xpos, ypos, width, height)
    """
    def __init__(self, p_xPosition, p_yPosition, p_colour, p_width, p_height, p_stepSize):
        self.__xpos = p_xPosition-30
        self.__ypos = p_yPosition
        self.__colour = p_colour
        self.__width = p_width
        self.__height = p_height
        self.__step = p_stepSize

        self.__rect = pygame.Rect(self.__xpos, self.__ypos, self.__width, self.__height)

    """
    Procedure:
        draw
    parameters:
        self - class attributes, 
        p_screen - surface
    purpose:
        display a rect of the player on the screen
    produces:
        none
    preconditions:
        none
    postconditions:
        new.rect(p_screen, colour, get_rect())
    """
    def draw(self, p_screen):
        pygame.draw.rect(
            surface=p_screen,
            color=self.__colour,
            rect=self.get_rect()
        )

    """
    Procedure:
        move_left
    parameters:
        self - class attributes
    purpose:
        checks if the player is within the border so that they can move left, before updating the x position to move left.
    produces:
        none
    preconditions:
        none
    postconditions:
        if rect.x <= 0 or get get_x_position() - step <= 0
            set_x_position(0)
        elseif
            set_x_position(get_x_position() - step)
        set_rect()
    """
    def move_left(self):
        if self.__rect.x <= 0 or self.get_x_position() - self.__step <= 0:
            self.set_x_position(0)
        else:
            self.set_x_position(self.get_x_position() - self.__step)
        self.set_rect()

    """
    Procedure:
        move_right
    parameters:
        self - class attributes
    purpose:
        checks if the player is within the border so that they can move right, before updating the x position to move right.
    produces:
        none
    preconditions:
        none
    postconditions:
        if rect.x >= (WIDTH-PLAYER_WIDTH) or (get_x_position() - step > (WIDTH-PLAYER_WIDTH))
            set_x_position(WIDTH-PLAYER_WIDTH)
        elseif
            set_x_position(get_x_position() + step)
        set_rect()
    """
    def move_right(self):
        if (self.__rect.x >= (WIDTH-PLAYER_WIDTH)) or (self.get_x_position() - self.__step >= (WIDTH-PLAYER_WIDTH)):
            self.set_x_position(WIDTH-PLAYER_WIDTH)
        else:
            self.set_x_position(self.get_x_position() + self.__step)
        self.set_rect()

    # getter and setter methods
    """
    Procedure:
        get_rect
    parameters:
        self - class attributes
    purpose:
        return rect value of the player class
    produces:
        self.__rect, a rect
    preconditions:
        none
    postconditions:
        return rect
    """
    def get_rect(self):
        return self.__rect
    
    """
    Procedure:
        get_x_position
    parameters:
        self - class attributes
    purpose:
        return the value of the currect x-coordinate of the player's rectangle
    produces:
        self.__xpos, a class attribute
    preconditions:
        none
    postconditions:
        return xpos
    """
    def get_x_position(self):
        return self.__xpos
    
    """
    Procedure:
        get_y_position
    parameters:
        self - class attributes
    purpose:
        return the current y-coordinate of the player's rect
    produces:
        self.__ypos, a class attribute
    preconditions:
        none
    postconditions:
        return ypos
    """
    def get_y_position(self):
        return self.__ypos
    
    """
    Procedure:
        set_x_position
    parameters:
        self - class attributes,
        newPosition - integer
    purpose:
        update the player's rect x position using the integer passed into the class method
    produces:
        none
    preconditions:
        newPosition <= WIDTH and newPosition >= 0
    postconditions:
        xpos = newPosition
    """
    def set_x_position(self, newPosition):
        self.__xpos = newPosition

    """
    Procedure:
        set_rect
    parameters:
        self - class attributes
    purpose:
        update the players's rect.
    produces:
        none
    preconditions:
        none
    postconditions:
        rect = Rect(xpos, ypos, width, height)
    """
    def set_rect(self):
        self.__rect = pygame.Rect(self.__xpos, self.__ypos, self.__width, self.__height)

# ball class
class Ball():
    """
    Procedure:
        __init__
    parameters:
        self - class attributes,
        p_xPosition - integer,
        p_yPosition - integer,
        p_colour - tuple,
        p_radius - integer,
        p_fallSpeed - integer
    purpose:
        initialise all attributes in the ball class.
    produces:
        none
    preconditions:
        none
    postconditions:
        xpos = p_xPosition
        ypos = p_yPosition
        colour = p_colour
        radius = p_radius
        fallspeed = p_fallSpeed
    """
    def __init__(self, p_xPosition, p_yPosition, p_colour, p_radius, p_fallSpeed):
        self.__xpos = p_xPosition
        self.__ypos = p_yPosition
        self.__colour = p_colour
        self.__radius = p_radius
        self.__fallspeed = p_fallSpeed

    """
    Procedure:
        fall
    parameters:
        self - class attributes
    purpose:
        move the ball downwards towards the player every frame
    produces:
        none
    preconditions:
        none
    postconditions:
        set_y_position(get_y_position() + fallspeed)
    """
    def fall(self):
        self.set_y_position(self.get_y_position() + self.__fallspeed)

    """
    Procedure:
        reset
    parameters:
        self - class attributes
    purpose:
        move the ball to the top of the screen and to a random x-position
    produces:
        none
    preconditions:
        ball.x <= 20 and ball.x >= WIDTH-20 and ball.y = 0
    postconditions:
        set_y_position(0)
        set_x_position(random(20, WIDTH-20))
    """
    def reset(self):
        # set height here manually - hard coded = more secure
        self.set_y_position(0)
        self.set_x_position(random.randint(20, WIDTH-20))

    """
    Procedure:
        draw
    parameters:
        self - class attributes,
        p_screen - surface
    purpose:    
        display a circle representing the ball on the window
    produces:
        none
    preconditions:
        none
    postconditions:
        circle(p_screen, colour, (xpos, ypos), radius)
    """
    def draw(self, p_screen):
        pygame.draw.circle(
            surface=p_screen,
            color=self.__colour,
            center=(self.__xpos,self.__ypos),
            radius=self.__radius
        )

    """
    Procedure:
        checkBallTouchingBoundary
    parameters:
        self - class attributes
    purpose:
        return a boolean value telling if the ball has touched the bottom border of the window.
    produces:
        True, False - boolean values
    preconditions:
        ball.y >= HEIGHT
    postconditions:
        if get_y_position() >= HEIGHT
            return true
        elseif
            return false
    """
    def checkBallTouchingBoundary(self):
        # hitbox touching window edge - lose a point?
        if self.get_y_position() >= HEIGHT: 
            return True # touching boundary
        else:
            return False

    # getter and setter methods
    """
    Procedure:
        get_x_position
    parameters:
        self - class attributes
    purpose:
        return the x-coordinate of the ball's hitbox
    produces:
        self.__xpos - integer
    preconditions:
        none
    postconditions:
        return xpos
    """
    def get_x_position(self):
        return self.__xpos

    """
    Procedure:
        get_y_position
    parameters:
        self - class attributes
    purpose:
        return the y-coordinate of the ball's hitbox
    produces:
        self.__ypos - integer
    preconditions:
        none
    postconditions:
        return ypos
    """
    def get_y_position(self):
        return self.__ypos
    
    """
    Procedure:
        set_x_position
    parameters:
        self - class attributes,
        newPosition - integer
    purpose:
        update the ball's x position with the new position passed in
    produces:
        none
    preconditions:
        newPosition <= WIDTH and newPosition >= 0
    postconditions:
        xpos = newPosition
    """
    def set_x_position(self, newPosition):
        self.__xpos = newPosition

    """
    Procedure:
        set_y_position
    parameters:
        self - class attributes,
        newPosition - integer,
    purpose:
        update the ball's y position with the new position passed in
    produces:
        none
    preconditions:
        newPosition <= HEIGHT and newPosition >= 0
    postconditions:
        ypos = newPosition
    """
    def set_y_position(self, newPosition):
        self.__ypos = newPosition

"""SPRITE INSTANTIATION"""
# player sprite
player = Player(
    p_xPosition=PLAYER_STARTING_X_POSITION, 
    p_yPosition=PLAYER_STARTING_Y_POSITION, 
    p_colour=PLAYER_COLOUR, 
    p_width=PLAYER_WIDTH, 
    p_height=PLAYER_HEIGHT, 
    p_stepSize=PLAYER_STEP_SIZE
)

# ball sprite
ball = Ball(
    p_xPosition=random.randint(20, WIDTH-20), 
    p_yPosition=BALL_STARTING_Y_POSITION,
    p_colour=BALL_COLOUR,
    p_radius=BALL_RADIUS,
    p_fallSpeed=BALL_FALL_SPEED
)

"""MAIN PROGRAM LOOP"""
running = True
while running:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False

    window.fill(WINDOW_COLOUR)

    ball.fall()

    ball.draw(window)
    player.draw(window)

    keyPresses = pygame.key.get_pressed()

    if keyPresses[pygame.K_LEFT]:
        player.move_left()
    if keyPresses[pygame.K_RIGHT]:
        player.move_right()

    """COLLISIONS"""
    # hitbox overlaps with player's - add point?
    if checkBallTouchingPlayer():
        ball.reset()

    if ball.checkBallTouchingBoundary():
        ball.reset()
    
    pygame.display.update()
    pygame.display.flip()
    
    clock.tick(FPS)



