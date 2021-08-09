from tkinter import *
from tkinter import ttk
import requests
#-------- FUNCOES -------#

def consulta():
    nomedoPokemon = escolhaPokemon.get()
    opcao = caixaopcoes.get()

    api = f"https://pokeapi.co/api/v2/pokemon/{nomedoPokemon}"
    res = requests.get(api)
    requisicao = res.json()

    if opcao == opcoes[0]:
        habilidades(requisicao, nomedoPokemon)
    elif opcao == opcoes[1]:
        tipo(requisicao, nomedoPokemon)
    elif opcao == opcoes[2]:
        golpes(requisicao, nomedoPokemon)
    elif opcao == opcoes[3]:
        estatisticas(requisicao, nomedoPokemon)

def habilidades(pokemon, nomedoPokemon):
    tituloHabilidades = Label(janela, text="Habilidades:  ", bg="red")
    tituloHabilidades.grid()
    for i in pokemon ["abilities"]:
        habilidadesList = Label(janela, text=i["ability"]["name"], bg="white")
        habilidadesList.grid()

def tipo(pokemon, nomedoPokemon):
    tituloTipo = Label(janela, text="Tipo:  ", bg="red")
    tituloTipo.grid()
    for i in pokemon ["types"]:
        tipoList = Label(janela, text=i["type"]["name"], bg="white")
        tipoList.grid()

def golpes(pokemon, nomedoPokemon):
    tituloGolpes = Label(janela, text="Golpes:    ", bg="red")
    tituloGolpes.grid()
    for i in pokemon ["moves"]:
        golpesList = Label(janela, text=i["move"]["name"], bg="white")
        golpesList.grid()

def estatisticas(pokemon, nomedoPokemon):
    tituloStats = Label(janela, text="Estatísticas:  ", bg="red")
    tituloStats.grid()
    for i in pokemon ['stats']:
        #print(i['stat']['name'], i['base_stat'])
        estatisticasnomeList = Label(janela, text= i['stat']['name'], bg="white")
        estatisticasList = Label(janela, text=i['base_stat'], bg="white")
        estatisticasnomeList.grid(), estatisticasList.grid()

# ------- LAYOUT ------- #
janela =Tk()
janela.title("POKEDEX PYTHON")
altura = 850
largura = 500
janela.resizable(True, True)
janela.configure(bg='white')
alturatela = janela.winfo_screenheight()
larguratela = janela.winfo_screenwidth()
posx = larguratela/2 - largura/2
posy = alturatela/2  - altura/2
janela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
janela.columnconfigure(0,weight=1)

img = PhotoImage(file="Imagem/download.png")
label_imagem = Label(janela,image=img, bg='white')

texto_bemvindo = Label(janela, text="BEM VINDO/A A POKEDEX DO PYTHON \n ", bg="white")
texto_escolha = Label(janela, text="QUAL POKEMON VOCÊ GOSTARIA DE CONSULTAR ?", bg="white")

escolhaPokemon = StringVar
escolhaPokemon = Entry(janela, width=50, textvariable = escolhaPokemon)

espaco = Label(janela, text=" ",  bg='white')

texto_escolha2 = Label(janela, text="O QUE VOCÊ GOSTARIA DE CONSULTAR ?", bg="white")

opcoes = ["Habilidades ", "Tipo do Pokemon ", "Golpe do Pokemon", "Estatísticas"]
caixaopcoes = ttk.Combobox(janela, value=opcoes)

espaco2 = Label(janela, text=" ",  bg='white')

consultarPokemon = Button(janela, text="CONSULTAR",  bg='white', command=consulta)

label_imagem.grid()
texto_bemvindo.grid()
texto_escolha.grid()
escolhaPokemon.grid()
espaco.grid()
texto_escolha2.grid()
caixaopcoes.grid()
espaco2.grid()
consultarPokemon.grid()

janela.mainloop()






