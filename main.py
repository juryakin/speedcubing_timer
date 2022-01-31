import time
import pygame
import keyboard
import scrambles_generator
import avg_counter
pygame.init()
pygame.font.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('JU_timer')
run = True
act_timer = False
clock = pygame.time.Clock()
font = pygame.font.Font('etna.otf', 30)
font1 = pygame.font.Font('etna.otf', 22 )
time_text_color = (0, 0, 0)
seconds = 0
minutes = 0
hours = 0
finished = True
is_pressed = False
line = pygame.Surface((500, 5))
line_color = (0, 0, 0)
inf = ''

scramble = ''.join(scrambles_generator.generate_scramble())
while run:
    scramble_text = font1.render(''.join(scramble), True, (0, 0, 0))
    avg5_text = font.render('avg5 - '+str(avg_counter.avg5('solves_list.txt')), True, (0, 0, 0))
    if hours == 0 and minutes > 0:
        inf = str(minutes) + ' : ' + str(seconds)
    elif hours == 0 and minutes == 0 and seconds > 0:
        inf = str(seconds)
    elif seconds == 0:
        inf = ''
    else:
        str(hours) + ' : ' + str(minutes) + ' : ' + str(seconds)
    time_text = font.render(inf, True, time_text_color)
    if seconds >= 60:
        seconds = 0
        minutes += 1
    if minutes >= 60:
        minutes = 0
        hours += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and finished:
                is_pressed = True
            elif event.key == pygame.K_SPACE and not finished:
                scramble = ''.join(scrambles_generator.generate_scramble())
                finished = True
                solves_list = open('solves_list.txt', 'a')
                solves_list.write(inf+'\n')
                solves_list.close()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and finished and is_pressed:
                seconds = 0
                now = time.time()
                finished = False
                is_pressed = False
    if keyboard.is_pressed('space') and finished and is_pressed:
        line_color = (0, 255, 0)
    else:
        line_color = (0, 0, 0)
    if not finished:
        inf = seconds
        seconds = round(time.time() - now, 3)
        time.sleep(0.01)
    window.fill((255, 255, 255))
    line.fill(line_color)
    window.blit(time_text, (200, 100))
    window.blit(scramble_text, (5, 50))
    window.blit(avg5_text, (20, 270))
    window.blit(line, (0, 130))
    pygame.display.flip()
    clock.tick(600)
quit()
