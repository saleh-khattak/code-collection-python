import random
def scoreGame():
    print("Your playing high score game....")
    score=random.randint(1,62)
    print(f"Your scire is {score}")
    with open("high_score.txt","r") as f:
        highScore=f.read()
        if(highScore!=""):
            highScore=int(highScore)
        else:
            highScore=0
    with open("high_score.txt","w") as f:
        if(score>highScore):
            with open("high_score.txt","w") as f:
                f.write(str(score))
    return score

scoreGame()

