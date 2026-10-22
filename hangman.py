import pygame
import random
import json
pygame.init()
screen = pygame.display.set_mode((900, 900))
font = pygame.font.SysFont("Arial", 50)


with open ("Files/words.json") as file:
    realwords=json.load(file)

def guesses(letter,guess):
    text = font.render(letter, True, (0, 0, 0))
    screen.blit(text, (100+35*guess,700 ))
    pygame.display.update()

def guessing(letter):
    global guess
    check=False
    runs=0
    while True:
        runs+=1
        for i in range(len(letters)):
            print(i,letter)
            if letters[i]==letter:
                drawletter(letters[i],position[i])
                position.pop(position.index(position[letters.index(letters[i])]))
                letters.pop(letters.index(letters[i]))
                check=True
                break
        if runs>=len(letters):
            break
    if check==False:
        guess+=1
        guesses(letter, guess)
        hangman()
    
def drawword(word):
    global font
    
    for i in range(len(word)):
        pygame.draw.line(screen, (0, 0, 0), (100+50*i, 100), (130+50*i, 100), 5)
        letters.append((word[i]))
        position.append((100+50*i, 25))
    
def drawletter(letter, pos):
    global font
    
    text = font.render(letter, True, (0, 0, 0))
    screen.blit(text, pos)
    pygame.display.update()

def lose():
    screen.fill((255,255,255))
    text = font.render("You lose! The word was: "+word, True, (0, 0, 0))
    screen.blit(text, (200, 200))

def hangman():
    global guess
    hangman=["base","pole","beam","rope","head","body","left arm","right arm","left leg","right leg"]
    if len(hangman)<guess+1:
        
        lose()
        for i in range(guess):
            draw(hangman[i])
        pygame.display.update()
        pygame.time.delay(5000)
        main()
    else: 
        for i in range(guess):
            draw(hangman[i])
        pygame.display.update()

def draw(part):
    if part == "base":
        pygame.draw.line(screen, (0, 0, 0), (50, 650), (150, 650), 5)
    elif part == "pole":
        pygame.draw.line(screen, (0, 0, 0), (100, 650), (100, 350), 5)
    elif part == "beam":
        pygame.draw.line(screen, (0, 0, 0), (100, 350), (200, 350), 5)
    elif part == "rope":
        pygame.draw.line(screen, (0, 0, 0), (200, 350), (200, 400), 5)
    elif part == "head":
        pygame.draw.circle(screen, (0, 0, 0), (200, 425), 25, 5)
    elif part == "body":
        pygame.draw.line(screen, (0, 0, 0), (200, 450), (200, 600), 5)
    elif part == "left arm":
        pygame.draw.line(screen, (0, 0, 0), (200, 500), (150, 525), 5)
    elif part == "right arm":
        pygame.draw.line(screen, (0, 0, 0), (200, 500), (250, 525), 5)
    elif part == "left leg":
        pygame.draw.line(screen, (0, 0, 0), (200, 600), (150, 640), 7)
    elif part == "right leg":
        pygame.draw.line(screen, (0, 0, 0), (200, 600), (250, 640), 7)
    


def main():
    global word,guess,letters,position, game
    guess=0
    word=random.choice(realwords)
    letters=[]
    position=[]
    screen.fill((255,255,255))
    drawword(word)
    pygame.display.update()
    run=True
    while run==True:
        event = pygame.event.wait()
        while event.type != pygame.KEYDOWN:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run=False
                    game=False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        guessing("a")
                    elif event.key == pygame.K_b:
                        guessing("b")
                    elif event.key == pygame.K_c:
                        guessing("c")
                    elif event.key == pygame.K_d:
                        guessing("d")
                    elif event.key == pygame.K_e:
                        guessing("e")
                    elif event.key == pygame.K_f:
                        guessing("f")
                    elif event.key == pygame.K_g:
                        guessing("g")
                    elif event.key == pygame.K_h:
                        guessing("h")
                    elif event.key == pygame.K_i:
                        guessing("i")
                    elif event.key == pygame.K_j:
                        guessing("j")
                    elif event.key == pygame.K_k:
                        guessing("k")
                    elif event.key == pygame.K_l:
                        guessing("l")
                    elif event.key == pygame.K_m:
                        guessing("m")
                    elif event.key == pygame.K_n:
                        guessing("n")
                    elif event.key == pygame.K_o:
                        guessing("o")
                    elif event.key == pygame.K_p:
                        guessing("p")
                    elif event.key == pygame.K_q:
                        guessing("q")
                    elif event.key == pygame.K_r:
                        guessing("r")
                    elif event.key == pygame.K_s:
                        guessing("s")
                    elif event.key == pygame.K_t:
                        guessing("t")
                    elif event.key == pygame.K_u:
                        guessing("u")
                    elif event.key == pygame.K_v:
                        guessing("v")
                    elif event.key == pygame.K_w:
                        guessing("w")
                    elif event.key == pygame.K_x:
                        guessing("x")
                    elif event.key == pygame.K_y:
                        guessing("y")
                    elif event.key == pygame.K_z:
                        guessing("z")
                    else:
                        run=False
                        game=False
                    break
        
        pygame.display.update()
        if len(letters)==0:
            text = font.render("You win!", True, (0, 0, 0))
            screen.blit(text, (350, 400))
            pygame.display.update()
            pygame.time.delay(5000)
            run=False
game=True
while game==True:
    main()
        
            