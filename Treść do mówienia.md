Model drapieżnik-łowca(model lotki-volterra) - jest to najprostszy model do opisywania interakcji dwóch organizmów które żyją w tym samym środowisku. Model został opracowany niezależnie przez Alfreda Lotke(matematyk z USA) w 1925 oraz przez Vito Volterre(włoski matematyk) w 1926 który zaproponował ten model wyjaśniający wahania wielkości populacji rekinów i ryb w morzu Adriatycjim. Inspirowali się czymś innym, lecz razem doszli do tych samych konkluzji. Medel ten może opisywać dowolne gatunkli które wchodzą ze sobą w interakcje, przykładami mogą być:
- wilki i zające
- rekiny i ryby
- mszyca i biedronki
- bakterie oraz ameby

Model zawiera dwie zmienne zależne, która każda jest funkcją czasu. Przez x(t) oznaczymy liczbę ofiar, a przez y(t) liczbę drapieżników w chwili t.
Przy braku drapieżników wysraczające zasoby pożywienia prowadziły by do wykładniczego wzrostu populacji ofiar:
$\frac{dx}{dt} = \alpha \times x$
gdzie $\alpha$ jest współczynnikiem który opisuje birth rate ofiar
Przy braku ofiar zakładamy że populacja drapieżników zmniejszałaby się w skutek śmiertelności proporcjonalnej do wielkości liczby drapieżników:
$\frac{dy}{dt} = -\gamma \times y$
gdzie $\gamma$ jest współczynnikiem opisującym death rate drapieżników.
Teraz do opisu interakcji pomiędzy tymi gatunkami musimy założyć że główną przyczyną śmierci ofiar jest bycie zjedzonym przez drapieżniki, a liczba urodzeń i zgonów jest zależna od liczby ofiar. Teraz możemy wyprowadzić układ dwóch równań różniczkowych:
$\frac{dx}{dt} = \alpha \times x - \beta \times xy$
$\frac{dy}{dt} = -\gamma \times y + \delta \times xy$

- x - liczba ofiar
- y - liczba drapieżników
- $\frac{dy}{dt} \frac{dy}{dt}$ - wzrost populacji
- t - czas
- $\alpha, \beta, \delta, \gamma$ - liczby większe od zera gdzie:
	- $\alpha$ - birth rate of prey
	- $\beta$ - death rate of prey due to predators
	- $\delta$ - natural death rate of predators
	- $\gamma$ - factor that describes how many eaten preys give birth to a new predator

Opisz ofiary:
- ofiara ma nielimitowany dostęp do jedzenia i rozmnaża się wykładniczo dopóki nie ma kontaktu z drpieżnikiem
- wzrost wykładniczy jest reprezentowany poprzez: $\alpha \times x$
- wskaźnik łowów jest proporcjonalny do częstości napotykania na siebie gatunki wyrażany poprzez: $\beta \times xy$
- $x$ i $y$ nie mogą być równe 0 ponieważ nie będzie wtedy występowało drapieżnictwo

***Podsumowując - tempo zmian populacji ofiar jest dane poprzez tempo wzrostu populacji minus tempo zjedzenia przez drapieżnika***

Opis drapieżnika:
-  tempo wzrostu populacji drapieżnika jest reprezentowane przez: $\delta \times xy$
-  ilość zjedzonych ofiar do rozwoju populacji opisuje $\gamma y$

Rozwiązaniem tego układu jest para funkcji, które opisują populację obu tych gatunków w funkcji czasu.
Podsumowując:
- populacja ofiary znajduje pożywienie cały czas
- pożywienie drapieżników zależy od wielkości populacji ofiar
- tepmpo zmiany populacji jest proporcjonalne do jej rozmiatu
- podczas całego procesu środowisko pozostaje nie zmienione
- drapieżnicy mają ograniczony apetyt, czyli ile ofiar mogą zjeść

Trajektoria fazowa przez punkt (1000,40) – punkt zielony. Jak można zauważyć nie ma wystarczająco dużo wilków aby utrzymać balans pomiędzy populacjami, dlatego rośnie populacja zajęcy. Rezultatem tego jest również wzrost populacji wilków. Kiedy jest ich na tyle dużo, że zające nie są w stanie ich uniknąć, ich populacja maleje (czerwony punkt to maximum jakie może osiągnąć populacja zajęcy , około 2800). To oznacza, że po pewnym czasie również populacja wilków zacznie się zmniejszać ( czarny punkt na wykresie, gdzie wilki = 140 a zające = 1000). Sprzyja to zającom więc ich populacja w końcu zacznie rosnąć (moment przełomowy – punkt pomarańczowy, wilki = 80, zające = 210). W konsekwencji liczność wilków zacznie rosnąć i kiedy wartości osiągną W = 40 i Z = 1000, to cykl powtórzy się na nowo.

![](/home/filip/PycharmProjects/rozniczkowe/321084715_3494783160794414_5211654160384390375_n.png)

![](/home/filip/PycharmProjects/rozniczkowe/320882178_2164821780369367_5264403790324036163_n.png)
