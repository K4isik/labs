 

import pygame

pygame.init()
W = 640
H = 630
sc = pygame.display.set_mode((W,H))
pygame.display.set_caption("Music")
h = pygame.image.load("C:/Users/user/Desktop/progging/python/pictures/0.png")
ha = pygame.image.load("C:/Users/user/Desktop/progging/python/pictures/1.png")
has = pygame.image.load("C:/Users/user/Desktop/progging/python/pictures/2.png")

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

music = ['Candy Shop - 50 Cent.mp3', 'Ed Sheeran — Perfect.mp3', 'Скриптонит - Животные.mp3']
for i in range(len(music)):
    k = i
    pygame.mixer.music.load(music[k])
    pygame.mixer.music.play(0)

def images():
    if k == 0:
        sc.blit(h, (0, 0))
    elif k == 1:
        sc.blit(ha, (0, 0))
    elif k == 2:
        sc.blit(has, (0, 0))

done = True
while done:
    images()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == SONG_END:
            print('The song ended!')
            k+=1
            if 0<=k and k<2:
                pygame.mixer.music.load(music[k])
                pygame.mixer.music.play(0)
            elif k>2:
                k = 0
                pygame.mixer.music.load(music[k])
                pygame.mixer.music.play(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == pygame.K_LEFT:
                k -=1
                if 0<=k and k<=2:
                    pygame.mixer.music.load(music[k])
                    pygame.mixer.music.play(0)
                elif k<0:
                    k = 2
                    pygame.mixer.music.load(music[k])
                    pygame.mixer.music.play(0)
            if event.key == pygame.K_UP or event.key == pygame.K_RIGHT:
                k+=1
                if 0<=k and k<=2:
                    pygame.mixer.music.load(music[k])
                    pygame.mixer.music.play(0)
                elif k>2:
                    k = 0
                    pygame.mixer.music.load(music[k])
                    pygame.mixer.music.play(0)
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            if event.key == pygame.K_RCTRL:
                pygame.mixer.music.unpause()

    pygame.display.update()