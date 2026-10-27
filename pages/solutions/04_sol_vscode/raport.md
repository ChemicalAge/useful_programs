# Rzut ukośny — od paraboli do ruchu z oporem powietrza

*Raport obliczeniowy o ruchu ciała wyrzuconego pod kątem do poziomu.*

**Temat:** tor, czas lotu i zasięg rzutu ukośnego.

**Metoda:** rozwiązanie analityczne dla ruchu bez oporu oraz całkowanie numeryczne modelu z oporem kwadratowym.

**Charakter danych:** przykład modelowy; wartości nie pochodzą z pomiaru laboratoryjnego.

Rzut ukośny można rozłożyć na dwa prostsze ruchy: poziomy, w którym ciało bez oporu porusza się ze stałą prędkością, oraz pionowy, w którym działa przyspieszenie grawitacyjne. Po uwzględnieniu oporu powietrza składowe przestają być niezależne — siła oporu zależy od całej prędkości i zmienia się wraz z ruchem.

## Spis treści

1. [Cel i założenia modelu](#1-cel-i-założenia-modelu)
2. [Rzut bez oporu powietrza](#2-rzut-bez-oporu-powietrza)
3. [Rzut z oporem powietrza](#3-rzut-z-oporem-powietrza)
4. [Przykład liczbowy i porównanie](#4-przykład-liczbowy-i-porównanie)
5. [Kod do odtworzenia obliczeń](#5-kod-do-odtworzenia-obliczeń)
6. [Jak wykonać doświadczenie](#6-jak-wykonać-doświadczenie)
7. [Wnioski](#7-wnioski)
8. [Dalsza lektura](#8-dalsza-lektura)

---

## 1. Cel i założenia modelu

Celem raportu jest opisanie położenia i prędkości ciała wyrzuconego z prędkością początkową $v_0$ pod kątem $\theta$ do poziomu. Porównujemy model idealny z modelem, w którym powietrze stawia opór.

### 1.1. Założenia

- Układ współrzędnych jest nieruchomy względem podłoża; oś $x$ jest pozioma, a oś $y$ skierowana pionowo w górę.
- Przyspieszenie grawitacyjne ma stałą wartość $g=9{,}81\,\mathrm{m/s^2}$ i jest skierowane w dół.
- W modelu idealnym pomijamy opór powietrza oraz rozmiar i obrót ciała.
- W modelu z oporem powietrza powietrze jest nieruchome, a współczynnik oporu i gęstość powietrza są stałe.
- Lądowanie następuje na wysokości startu, chyba że podano inaczej.

Wektor położenia zapisujemy jako $\mathbf{r}=(x,y)$, a wektor prędkości jako $\mathbf{v}=(v_x,v_y)$. Kąt $\theta$ mierzymy od dodatniego kierunku osi poziomej.

### 1.2. Symbole i jednostki

| Symbol | Znaczenie | Jednostka SI |
| :--- | :--- | :---: |
| $x$, $y$ | współrzędne położenia | $\mathrm{m}$ |
| $v_x$, $v_y$, $v$ | składowe prędkości i szybkość | $\mathrm{m/s}$ |
| $a_x$, $a_y$ | składowe przyspieszenia | $\mathrm{m/s^2}$ |
| $v_0$, $\theta$ | prędkość początkowa i kąt wyrzutu | $\mathrm{m/s}$, $\mathrm{rad}$ lub $\mathrm{^\circ}$ |
| $g$ | przyspieszenie grawitacyjne | $\mathrm{m/s^2}$ |
| $t$, $T$ | czas i czas lotu | $\mathrm{s}$ |
| $R$, $H$ | zasięg poziomy i maksymalna wysokość | $\mathrm{m}$ |
| $m$ | masa ciała | $\mathrm{kg}$ |
| $\rho$ | gęstość powietrza | $\mathrm{kg/m^3}$ |
| $C_D$ | bezwymiarowy współczynnik oporu | bez jednostki |
| $A$ | pole powierzchni czołowej | $\mathrm{m^2}$ |

---

## 2. Rzut bez oporu powietrza

### 2.1. Składowe prędkości początkowej

Prędkość początkową rozkładamy na składowe:

$$
v_{0x}=v_0\cos\theta,
\qquad
v_{0y}=v_0\sin\theta.
$$

Bez oporu poziome przyspieszenie jest równe zeru, a pionowe wynosi $-g$:

$$
a_x=0,
\qquad
a_y=-g.
$$

Dla chwili początkowej $t=0$ i położenia $(x_0,y_0)$ równania ruchu są następujące:

$$
x(t)=x_0+v_0\cos\theta\,t,
$$

$$
y(t)=y_0+v_0\sin\theta\,t-\frac{1}{2}gt^2.
$$

Prędkość zmienia się według zależności:

$$
v_x(t)=v_0\cos\theta,
\qquad
v_y(t)=v_0\sin\theta-gt.
$$

W najwyższym punkcie toru $v_y=0$. Nie oznacza to, że całkowita prędkość jest tam równa zeru — składowa pozioma nadal wynosi $v_0\cos\theta$.

### 2.2. Kształt toru

Eliminujemy czas z równań położenia, korzystając z $t=(x-x_0)/(v_0\cos\theta)$. Dla $\cos\theta\ne0$ otrzymujemy:

$$
y(x)=y_0+(x-x_0)\tan\theta
-\frac{g(x-x_0)^2}{2v_0^2\cos^2\theta}.
$$

Jest to parabola. Jej kształt wynika z połączenia stałej prędkości poziomej i stałego przyspieszenia pionowego. Dla rzutu pionowego, gdy $\cos\theta=0$, ciało nie przemieszcza się poziomo i powyższa postać $y(x)$ nie ma zastosowania.

### 2.3. Czas lotu, wysokość maksymalna i zasięg

Dla startu i lądowania na tej samej wysokości ($y_0=0$) z równania $y(T)=0$ wynika niezerowy czas lotu:

$$
T=\frac{2v_0\sin\theta}{g}.
$$

W najwyższym punkcie $v_y=0$, więc czas wznoszenia i maksymalna wysokość względem miejsca wyrzutu wynoszą:

$$
t_H=\frac{v_0\sin\theta}{g},
\qquad
H=\frac{v_0^2\sin^2\theta}{2g}.
$$

Zasięg poziomy to $R=x(T)-x_0$:

$$
R=\frac{v_0^2\sin(2\theta)}{g}.
$$

Przy ustalonym $v_0$ i równych wysokościach startu oraz lądowania model idealny przewiduje największy zasięg dla $\theta=45^\circ$. Kąty $\theta$ i $90^\circ-\theta$ dają taki sam zasięg, lecz inną wysokość maksymalną i czas lotu. Wniosek o kącie $45^\circ$ zależy od tych założeń — nie jest uniwersalny, gdy start i lądowanie są na różnych wysokościach albo działa opór.

**Kontrola jednostek:** $v_0^2/g$ ma jednostkę $\mathrm{m}$, a $v_0/g$ — $\mathrm{s}$.

---

## 3. Rzut z oporem powietrza

### 3.1. Kierunek i model siły oporu

Siła oporu działa przeciwnie do prędkości względem powietrza. W typowym zakresie prędkości dla ciał poruszających się w powietrzu często stosuje się model kwadratowy:

$$
\mathbf{F}_{\mathrm{op}}
=-\frac{1}{2}\rho C_D A\,|\mathbf{v}|\,\mathbf{v}.
$$

Znak minus wskazuje przeciwny zwrot. Ponieważ $|\mathbf{v}|=\sqrt{v_x^2+v_y^2}$, składowe siły zależą jednocześnie od $v_x$ i $v_y$. Równania Newtona przyjmują postać:

$$
\dot{x}=v_x,
\qquad
\dot{y}=v_y,
$$

$$
\dot{v}_x=-c|\mathbf{v}|v_x,
\qquad
\dot{v}_y=-g-c|\mathbf{v}|v_y,
\qquad
c=\frac{\rho C_D A}{2m}.
$$

Współczynnik $c$ ma jednostkę $\mathrm{m^{-1}}$. Dla prędkości względem poruszającego się powietrza należy w równaniu oporu zastąpić $\mathbf{v}$ prędkością względną $\mathbf{v}-\mathbf{u}_{\mathrm{pow}}$.

Przy małych prędkościach lub w innym zakresie przepływu spotyka się również model liniowy $\mathbf{F}_{\mathrm{op}}=-b\mathbf{v}$, gdzie $b$ jest współczynnikiem proporcjonalności. Wybór między modelem liniowym a kwadratowym zależy od warunków przepływu i geometrii ciała; w przykładzie liczbowym używamy modelu kwadratowego.

### 3.2. Co zmienia opór?

- Składowa pozioma prędkości maleje, więc zasięg jest mniejszy niż w modelu idealnym przy tych samych warunkach początkowych.
- Tor nie jest parabolą: przyspieszenie zależy od aktualnej prędkości.
- Wznoszenie i opadanie nie są symetryczne. Po przejściu przez wierzchołek ruchu ciało na ogół nie wraca po tej samej krzywej.
- Kąt dający największy zasięg zależy od masy, kształtu, rozmiaru, gęstości powietrza, prędkości początkowej i wysokości lądowania. Zwykle nie wynosi dokładnie $45^\circ$.
- Energia mechaniczna maleje, ponieważ opór rozprasza ją w postaci energii wewnętrznej powietrza i ciała.

Dla modelu kwadratowego nie ma na ogół prostych wzorów analitycznych na cały tor i zasięg. Równania ruchu rozwiązuje się numerycznie, na przykład metodą Rungego–Kutty.

### 3.3. Energia i prędkość graniczna

Moc siły oporu jest ujemna:

$$
\frac{d}{dt}\left(\frac{1}{2}mv^2+mgy\right)
=\mathbf{F}_{\mathrm{op}}\cdot\mathbf{v}
=-\frac{1}{2}\rho C_D A\,v^3\le0.
$$

Dla pionowego spadania w modelu kwadratowym prędkość graniczną można oszacować, zrównując ciężar i wartość siły oporu:

$$
v_{\mathrm{gr}}=
\sqrt{\frac{2mg}{\rho C_D A}}.
$$

Jest to wynik dla spadania pionowego w dół, przy stałych parametrach oporu. Nie oznacza, że w rzucie ukośnym wektor prędkości od razu przyjmuje tę wartość.

---

## 4. Przykład liczbowy i porównanie

Przyjmijmy prędkość początkową $v_0=20{,}0\,\mathrm{m/s}$ i kąt $\theta=45^\circ$. Dla porównania z oporem wybieramy modelową piłkę o masie $m=0{,}145\,\mathrm{kg}$, polu czołowym $A=0{,}0042\,\mathrm{m^2}$ i współczynniku $C_D=0{,}47$. Przyjmujemy $\rho=1{,}225\,\mathrm{kg/m^3}$ oraz start i lądowanie na tym samym poziomie.

### 4.1. Wyniki modelu idealnego

$$
T=\frac{2(20{,}0)\sin45^\circ}{9{,}81}
\approx2{,}88\,\mathrm{s},
$$

$$
H=\frac{(20{,}0)^2\sin^245^\circ}{2(9{,}81)}
\approx10{,}2\,\mathrm{m},
$$

$$
R=\frac{(20{,}0)^2\sin90^\circ}{9{,}81}
\approx40{,}8\,\mathrm{m}.
$$

### 4.2. Wyniki z oporem kwadratowym

Dla podanych parametrów:

$$
c=\frac{(1{,}225)(0{,}47)(0{,}0042)}{2(0{,}145)}
\approx0{,}00834\,\mathrm{m^{-1}}.
$$

Całkowanie równań ruchu daje w przybliżeniu:

| Wielkość | Bez oporu | Z oporem kwadratowym |
| :--- | ---: | ---: |
| Czas lotu | $2{,}88\,\mathrm{s}$ | $2{,}70\,\mathrm{s}$ |
| Maksymalna wysokość nad miejscem startu | $10{,}2\,\mathrm{m}$ | $8{,}98\,\mathrm{m}$ |
| Zasięg | $40{,}8\,\mathrm{m}$ | $32{,}5\,\mathrm{m}$ |
| Położenie wierzchołka w poziomie | $20{,}4\,\mathrm{m}$ | $17{,}0\,\mathrm{m}$ |

Wartości dla oporu są przybliżone i zależą od przyjętych parametrów oraz modelu. W tym przykładzie opór skraca zasięg o około $20\%$ względem wartości idealnej. Wyniki nie opisują każdej piłki ani warunków pogodowych — zmiana masy, powierzchni czołowej, współczynnika oporu lub wiatru zmieni rezultat.

---

## 5. Kod do odtworzenia obliczeń

Poniższy skrypt w Pythonie oblicza analityczny zasięg bez oporu, numerycznie rozwiązuje równania dla oporu kwadratowego i rysuje porównanie torów. Wymaga pakietów `numpy`, `scipy` oraz `matplotlib`.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

g = 9.81
v0 = 20.0
theta = np.deg2rad(45.0)
x0, y0 = 0.0, 0.0

m = 0.145
rho = 1.225
Cd = 0.47
A = 0.0042
c = rho * Cd * A / (2 * m)

vx0 = v0 * np.cos(theta)
vy0 = v0 * np.sin(theta)
T_ideal = 2 * vy0 / g
t_ideal = np.linspace(0, T_ideal, 500)
x_ideal = x0 + vx0 * t_ideal
y_ideal = y0 + vy0 * t_ideal - 0.5 * g * t_ideal**2

def rownania(t, stan):
    x, y, vx, vy = stan
    speed = np.hypot(vx, vy)
    return [vx, vy, -c * speed * vx, -g - c * speed * vy]

def ladowanie(t, stan):
    return stan[1]

ladowanie.terminal = True
ladowanie.direction = -1

wynik = solve_ivp(
    rownania,
    (0.0, 10.0),
    [x0, y0, vx0, vy0],
    events=ladowanie,
    dense_output=True,
    max_step=0.01,
    rtol=1e-9,
    atol=1e-11,
)
if not wynik.success:
    raise RuntimeError(wynik.message)
if len(wynik.t_events[0]) == 0:
    raise RuntimeError("Nie wykryto chwili lądowania.")

T_drag = wynik.t_events[0][0]
t_drag = np.linspace(0.0, T_drag, 500)
x_drag, y_drag = wynik.sol(t_drag)[:2]
t_apex = wynik.t[np.argmax(wynik.y[1])]
height_drag = np.max(wynik.y[1])
range_drag = wynik.y_events[0][0][0] - x0

print(f"Zasięg bez oporu: {x_ideal[-1] - x0:.2f} m")
print(f"Zasięg z oporem:  {range_drag:.2f} m")
print(f"Czas lotu z oporem: {T_drag:.3f} s")
print(f"Czas do wierzchołka z oporem: {t_apex:.3f} s")
print(f"Maksymalna wysokość z oporem: {height_drag:.2f} m")

plt.plot(x_ideal, y_ideal, label="Bez oporu")
plt.plot(x_drag, y_drag, label="Opór kwadratowy")
plt.xlabel("Położenie poziome x [m]")
plt.ylabel("Wysokość y [m]")
plt.title("Rzut ukośny: porównanie modeli")
plt.grid(alpha=0.25)
plt.legend()
plt.tight_layout()
plt.show()
```

W powyższym kodzie `solve_ivp` całkuje układ czterech równań pierwszego rzędu. Zdarzenie `ladowanie` kończy obliczenia przy pierwszym przejściu przez poziom $y=0$ w dół. Tolerancje solvera ograniczają błąd numeryczny, ale nie usuwają niepewności fizycznych założeń, takich jak przybliżona wartość $C_D$.

---

## 6. Jak wykonać doświadczenie

### 6.1. Procedura pomiarowa

1. Wybierz niewielki, niezbyt lekki obiekt i ustal miejsce wyrzutu oraz poziom lądowania.
2. Zmierz lub oszacuj masę obiektu. Zapisz jego kształt i wymiary, ponieważ wpływają na opór.
3. Zmierz prędkość początkową i kąt wyrzutu, najlepiej na podstawie nagrania z boku z widoczną skalą.
4. Nagraj cały lot w nieruchomym układzie kamery, prostopadle do płaszczyzny ruchu.
5. Wyznacz położenia obiektu w kolejnych klatkach i porównaj je z modelem idealnym oraz numerycznym modelem oporu.
6. Powtórz pomiar kilka razy i podaj rozrzut wyników zamiast opierać wniosek na jednym rzucie.

Nie należy wykonywać doświadczenia w pobliżu ludzi, okien ani ruchu drogowego. Bezpieczeństwo i stabilny, niezakłócony kadr są ważniejsze niż zwiększanie prędkości wyrzutu.

### 6.2. Ograniczenia pomiaru i modelu

- Niepewność kąta i prędkości początkowej wpływa na przewidywany zasięg.
- Perspektywa kamery i jej ruch mogą powodować błędne odczyty położenia.
- Opór zależy od kształtu, orientacji, obrotu i prędkości; stałe $C_D$ jest przybliżeniem.
- Podmuchy wiatru zmieniają prędkość ciała względem powietrza.
- Przy obiektach wirujących mogą pojawić się dodatkowe siły aerodynamiczne, których ten model nie uwzględnia.
- Jeśli różnica między pomiarem a obliczeniem jest większa niż niepewność, należy najpierw sprawdzić warunki początkowe i założenia, a nie dopasowywać wynik przez przypadkową zmianę parametrów.

---

## 7. Wnioski

1. Bez oporu powietrza składowe ruchu poziomego i pionowego można analizować niezależnie, a tor jest parabolą.
2. Przy równych wysokościach startu i lądowania czas lotu, wysokość maksymalną i zasięg wyznaczają proste wzory. W modelu idealnym największy zasięg występuje dla kąta $45^\circ$.
3. Opór powietrza zmniejsza prędkość, zasięg i zwykle wysokość maksymalną. Ponieważ siła zależy od wektora prędkości, tor przestaje być parabolą.
4. Dla oporu kwadratowego ruch oblicza się numerycznie. Wynik należy interpretować razem z przyjętymi parametrami i ograniczeniami modelu.
5. W przykładzie modelowym zasięg zmniejszył się z około $40{,}8\,\mathrm{m}$ do $32{,}5\,\mathrm{m}$, ale tych liczb nie należy traktować jako uniwersalnych.

---

## 8. Dalsza lektura

- [OpenStax: Projectile Motion](https://openstax.org/books/university-physics-volume-1/pages/4-3-projectile-motion) — rozkład ruchu na składowe i równania rzutu bez oporu.
- [NASA Glenn: The Drag Equation](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/drag-equation/) — równanie oporu aerodynamicznego i znaczenie jego parametrów.
- [SciPy: `solve_ivp`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html) — dokumentacja numerycznego rozwiązywania zagadnień początkowych.