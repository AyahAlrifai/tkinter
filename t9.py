import time
import pygame

List=["سبحان الله","الحمد لله","لا اله الا الله","الله اكبر","لا حول ولا قوة الا بالله","اشهد ان لا اله الا الله واشهد ان محمد رسول","سبحان الله وبحمده سبحان الله العظيم"]

def write_text(win,text,color,location,size):
    z=pygame.font.Font('freesansbold.ttf',size)
    w=z.render(text,True,color)
    win.blit(w,location)
    

    

pygame.init()
win = pygame.display.set_mode((300,40)) 
pygame.display.set_caption("AZKAR")
run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        for l in List:
            write_text(win,l,(250,120,200),(100,20),20)
            pygame.display.update()
            time.sleep(3)
            win.fill((0,0,0))
pygame.quit()


