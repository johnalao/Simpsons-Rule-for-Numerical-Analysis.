def f(t,v):
  m = 0.034
  g = -9.81
  r = 0.35
  c1 = 0.00031
  c2 = 0.85
  if v == 0:
    return g
  else:
    return(m*g-(c1*r*abs(v)+c2*r*r*v*v)*v/abs(v))/m

deltat = 0.1
t = 0
v = 0
vlist = [(t,v)]
for i in range(20):
  k1 = f(t,v)
  k2 = f(t + deltat/2, v +k1*deltat/2)
  k3 = f(t + deltat/2, v +k2*deltat/2)
  k4 = f(t + deltat, v +k3*deltat)
  v = v + (k1 + 2*k2 + 2*k3 +k4)/6 *deltat
  t = t + deltat
  vlist.append((t,v))


deltat = deltat * 2
i = 0 
t = 0
y = 3
for i in range(10):
  k1 = vlist[2*i][1] 
  k2 = vlist[2*i+1][1]
  k3 = vlist[2*i+1][1]
  k4 = vlist[2*i+2][1]
  y = y+(k1+2*k2+ 2*k3 +k4)/6*deltat
  t = t + deltat
  print(t,y)