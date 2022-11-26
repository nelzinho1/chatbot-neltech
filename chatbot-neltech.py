import os


def processar_resposta(resposta, nome):
  if resposta == '1':
    print(
      f'{os.linesep}{nome}, Acredito que sim meu amigo, liga ja aqui nos temos os melhores preços (98) 999720433.{os.linesep}'
    )
  elif resposta == '2':
    print(
      f'{os.linesep}{nome} , Aqui na Neltech temos os melhores preços venha conferir{os.linesep}'
    )
  elif resposta == '3':
    print(
      f'{os.linesep}{nome}, obrigado o proprietario Emanuel da Neltech manda outro abraço para você. Tenha um bom dia.{os.linesep}'
    )
  elif resposta == '4':
    print(
      f'{os.linesep}{nome} você pode estudar através de vídeos gratúitos no YouTube, livros e sites de programação, porém se buscar um lugar com suporte 1 a 1, estrutura sequencial, projetos novos todos os meses dos ano e um curso que vai te ensinar toda a base e habilidades mais lucrativas que precisa para criar aplicações em python e estar pronto para o mercado, recomendo o cursodepython.net.{os.linesep}'
    )
  else:
    print('Digite apenas 1, 2, 3 ou 4')


def start():

  print('Olá! Bem-vindo a Neltech.com')

  nome = input('Digite seu nome: ')

  email = input('Digite seu e-mail: ')
  while True:

    resposta = input(
      f'O que gostaria de saber hoje?{os.linesep}[1] -  Vale a pena contratar a Neltech manutenções?{os.linesep}[2] - Quais os valores das manutenções? {os.linesep}[3] - Mande um abraço para a Neltech manutenções?{os.linesep}[4] - Onde me recomenda estudar Python para conseguir um emprego hoje?{os.linesep}'
    )

    processar_resposta(resposta, nome)


if __name__ == '__main__':
  start()