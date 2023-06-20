def calc_pontos(proj):
  pts_total = 0
  pts = {'X':1, 'Z':2,'Y':3}
  
  with open(proj, 'r') as arquivo:
        linhas = arquivo.readlines()

        for linha in linhas:
            linha = linha.strip().split()

            hand = linha[0]
            myhand = linha[1]

            pts_turno = pts[myhand] + 3 if hand != myhand else 0

            pts_total += pts_turno

  return pts_total

arquivo = 'exemplo1.txt'
resultado = calc_pontos(arquivo)
print(f'Pontos ganhos em {arquivo}:')
print(resultado)

arquivo = 'exemplo2.txt'
resultado = calc_pontos(arquivo)
print(f'Pontos ganhos em {arquivo}:')
print(resultado)