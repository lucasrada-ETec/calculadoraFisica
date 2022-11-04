import math
import matplotlib.pyplot as plt
import numpy as np
case = int(input("(1) Aceleración\n(2) Velocidad\n"))
array = [[],[]]
def prom(y): plt.axhline(y=np.nanmean(y), color='red', linestyle='--', linewidth=3)
def scat(a): plt.scatter(range(len(a)), a)
if case == 2:
    t = float(input("Tiempo: "))
    a = float(input("Aceleración: "))
    vi = float(input("Velocidad inicial: "))
    x = np.linspace(0, t)
    y = vi * x + (a * (x ** 2)) / 2
    vf = (a * t) + vi
    if a < 0: vf = 0
    print("La velocidad final es {} m/s".format(vf))
    plt.xlabel("Metros")
    plt.ylabel("Segundos")
    plt.grid()
    plt.tight_layout()
    plt.plot(x, y, marker = ".")
if case == 1:
    while case == 1:
        m = float(input("Ingrese la masa del cuerpo (Kilogramos) "))
        f = float(input("Ingrese la fuerza aplicada al cuerpo (Newton) "))
        h = float(input("Ingrese la altura del objeto (Metros) "))
        g = 9.8
        inc = int(input("¿Cuantos grados(°) esta inclinado el plano? "))
        while inc > 90 or inc < 0:
            print("No es posible, ingrese otro valor ")
            inc = int(input("¿Cuantos grados(°) esta inclinado el plano? "))
        px = m * g * math.sin(inc * math.pi / 180)
        py = m * g * math.cos(inc * math.pi / 180)
        fx = f - px
        if input("¿Hay friccion? (s/n) ").lower() == "s":
            material = input("¿Que materiales componen a los cuerpos?\na. Madera sobre madera\nb. Acero sobre hielo\nc. Teflón sobre teflón\nd. Caucho sobre cemento seco\ne. Vidrio sobre vidrio\nf. Esquí sobre nieve\ng. Madera sobre cuero\nh. Aluminio sobre acero\ni. Articulaciones humanas\nj. Personalizado\n")
            if material == "a": ue = 0.5; ud = 0.3
            elif material == "b": ue = 0.03; ud = 0.02
            elif material == "c": ue = 0.04; ud = 0.04
            elif material == "d": ue = 1; ud = 0.8
            elif material == "e": ue = 0.9; ud = 0.4
            elif material == "f": ue = 0.1; ud = 0.05
            elif material == "g": ue = 0.5; ud = 0.4
            elif material == "h": ue = 0.61; ud = 0.47
            elif material == "i": ue = 0.02; ud = 0.003
            elif material == "j":
                ue = float(input("Coeficiente de friccion estatico: "))
                ud = float(input("Coeficiente de friccion dinamico: "))
            ffe = ue * py
            ffd = ud * py
            fuerzaNeta = fx - ffd
            if ffe > abs(fx):
                print("Fuerza Aplicada:", f, "Newton\nFuerza de Friccion Estatica:", ffe, "Newton\nEste objeto no se mueve porque la friccion entre los cuerpos es muy grande")
                a = 0
                exit()
            else: a = fuerzaNeta / m
            print("El objeto tiene una aceleración de", a, "m/s² (Positivo: -> Negativo: <-)")
        else:
            a = fx / m
            print("h ", h, "a ", a)
            print("El objeto tiene una aceleración de {} m/s² (Positivo: -> Negativo: <-)".format(a))
            if a == 0:
                print("Este objeto no se mueve")
        if h > 0 and a != 0 and a == abs(a):
            t = math.sqrt((2 * h) / a)
            array[1].append(t)
            print("El tiempo que tarda en llegar al piso es de {} segundos".format(t))
        if input("¿Desea evaluar otro caso? (s/n) ") == "s": case = 1
        else: case = 0
        array[0].append(a)
    arrayOrder = array[0][:]
    array[0].sort(reverse = True)
    print("Valores de aceleración de mayor a menor")
    for i in range(len(array[0])): print("Objeto ", arrayOrder.index(array[0][i]) + 1, ":", array[0][i], "m/s²")
    angle = np.deg2rad(inc)
    vertices = np.array([[-np.cos(angle), 0, 0, -np.cos(angle)], [0, 0, np.sin(angle), 0],])
    plt.axis("off")
    plt.axis('equal')
    plt.figure(1)
    plt.plot(*vertices)
    plt.figure(2)
    plt.grid()
    plt.autoscale
    scat(array[0])
    prom([array[0]])
    plt.figure()
    scat([array[1]])
    prom([array[1]])
plt.show()