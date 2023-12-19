import pygame
import pymunk
import pymunk.pygame_util
import random
import math

pygame.init()

WIDTH, HEIGHT = 1000,800
window = pygame.display.set_mode((WIDTH, HEIGHT))


def draw (space, window, draw_options):
    window.fill("white")
    space.debug_draw(draw_options)
    pygame.display.update()


def create_swinging_ball(space):
    rotation_center_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_center_body.position = (300, 300)

    body = pymunk.Body()
    body.position = (300, 300)
    line = pymunk.Segment(body, (0, 0), (200, 0), 5)
    circle = pymunk.Circle(body, 40, (200, 0))
    line.friction = 1
    circle.friction = 1
    line.mass = 8
    circle.mass = 30
    circle.elasticity = 0.95
    rotation_center_joint = pymunk.PinJoint(body, rotation_center_body, (0, 0), (0, 0))
    space.add(circle, line, body, rotation_center_joint)


def run(window, width, height):
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1 / fps

    space = pymunk.Space()
    space.gravity = (0, 1044)
    space.damping = 0.981
    create_swinging_ball(space)

    draw_options = pymunk.pygame_util.DrawOptions(window)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(space, window, draw_options)
        space.step(dt)
        clock.tick(fps)

    pygame.quit()


if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)