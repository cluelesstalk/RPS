import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Pygame‑CE Test")

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((30, 30, 30))  # dark gray background

        # Draw a simple moving circle
        t = pygame.time.get_ticks() / 500
        x = 320 + 100 * pygame.math.Vector2(1, 0).rotate(t * 60).x
        y = 240 + 100 * pygame.math.Vector2(1, 0).rotate(t * 60).y
        pygame.draw.circle(screen, (0, 200, 255), (int(x), int(y)), 30)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()