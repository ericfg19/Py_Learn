
#library
import random
from random import randint
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.styles import Style
import time

style = Style.from_dict({
    'aaa': '#ff0066',
    'bbb': '#44ff00 italic',
})
##

maos = ["PEDRA", "PAPEL", "TESOURA"]

cpu = randint(0, 2)
print_formatted_text(HTML("<bbb> JOGUE JOKENPO COM O ALGORITMO EM PYTHON \n</bbb>"))
print("      ESCOLHA SUA OPÇÃO: \n")
print("[0] PEDRA  ** [1] PAPEL ** [2] TESOURA")

##Escolha da Jogada
player = int(input("Escolha o número que será a sua jogada: "))
while player > 2 :
    player = int(input("Escolha o número que será a sua jogada(de 0 a 2): "))
print("*" * 15)
print("JO... (ง '̀-'́) ")
time.sleep(1)
print('...KEN...')
time.sleep(2)
print(" (っ•́｡•́) ...PO!")
time.sleep(1)
print("*" * 15)
print("\n")
print(f"O Computador jogou {maos[cpu]}.")
print(f"Você jogou {maos[player]}.")

print("*" * 15)
##
if cpu == 0 :
    if player == 0 :
        print("EMPATOU! (╯°□°)︵  ︵ (°□° ╯)")
    elif player == 1 :
        print("VOCÊ VENCEU! ♪♪ ヽ(ˇ∀ˇ )ゞ")
    elif player == 2 :
        print("VOCÊ PERDEU! ヽ༼ ಠ益ಠ ༽ﾉ")
    else:
        print("Esta jogada não existe! - Número inválido.")

elif cpu == 1 :
    if player == 0 :
        print("VOCÊ PERDEU! ヽ༼ ಠ益ಠ ༽ﾉ")
    elif player == 1 :
        print("EMPATOU! (╯°□°)︵  ︵ (°□° ╯)")
    elif player == 2 :
        print("VOCÊ VENCEU! ♪♪ ヽ(ˇ∀ˇ )ゞ")
    else:
        print("Esta jogada não existe! - Número inválido.")
        
elif cpu == 2 :
    if player == 0 :
        print("VOCÊ VENCEU! ♪♪ ヽ(ˇ∀ˇ )ゞ")
    elif player == 1 :
        print("VOCÊ PERDEU! ヽ༼ ಠ益ಠ ༽ﾉ")
    elif player == 2 :
        print("EMPATOU! (╯°□°)︵  ︵ (°□° ╯)")
    else:
        print("Esta jogada não existe! - Número inválido.")
##
time.sleep(2)
print("\n")
print("Fim de jogo!")
time.sleep(5)


