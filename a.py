tab = [['0' for x in range(8)] for i in range(8) ]

def show(tab_):
  for row in tab_:
    print(row)

def zatruj_kurwe(tab,posx, posy):
  
#lewo gora
  t_x, t_y = posx, posy
  while t_x >= 0 and t_y >= 0:
    tab[t_x][t_y] = "X"
    t_x -= 1
    t_y -= 1

#prawo gora
  t_x, t_y = posx, posy
  while t_x >= 0 and t_y <= len(tab)-1:
    tab[t_x][t_y] = "X"
    t_x -= 1
    t_y += 1

#prawo dol
  t_x, t_y = posx, posy
  while t_x <= len(tab)-1 and t_y <= len(tab)-1:
    tab[t_x][t_y] = "X"
    t_x += 1
    t_y += 1

#lewo dol
  t_x, t_y = posx, posy
  while t_x <= len(tab)-1 and t_y >= 0:
    tab[t_x][t_y] = "X"
    t_x += 1
    t_y -= 1

zatruj_kurwe(tab, 4, 3)

show(tab