import clique as clique
import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')


janela = customtkinter.CTk()
janela.geometry('500x300')

texto = customtkinter.CTkLabel(janela, text='Bem-Vindo ao Adivinhador')
texto.pack(padx=10, pady=10)

jogar = customtkinter.CTkEntry(janela, placeholder_text='Digite seu nome')
jogar.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text='JOGAR', command=clique)
botao.pack(pady=10, padx=10)



janela.mainloop()

from random import randint
from time import sleep
c = randint( 0, 6)
print('Pensei no numero {}.'.format(c)) #Faz o computador 'pensar'
print('-=-' * 12)
print(' Vou pensa em um numero entre 0 e 6.')
print('-=-' * 12 )
j = int(input('Em que numero pensei ?'))# jogador tenta adivinha
print('Carregando...')
sleep(2)
if j == c:
    print('Parabens você ganhou !')
else:
    print('Ganhei ! Eu pensei no numero {} e nao no {}'.format(c,j))


