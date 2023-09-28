 Projekto idėja kilo, kadangi turiu asmeninę prekybos strategiją FOREX finansų rinkoje,
 kurią norėčiau išbandyti su "backtesting" ir pažiūrėti, kokią metinę grąžą galėčiau gauti, 
 jei ją automatizuociau naudojant Python. Pradėjęs daryti projektą supratau, kad dėl laiko 
 trūkumo reikia sutrumpinti visą projektą. Palikau tik kelis strategijos pradinius komponentus, 
 kuriuos panaudojau. 
 
 1. COT duomenis rinkos krypties nustatymui. Remdamasis jais, nustaciau jog prekybos algoritmas tik pirks norimą instrumentą, siuo atveju EURJPY
  jokių pardavimų neatliksime.
 2. Panaudojau industrijoje plačiai naudojamą indikatorių "pivot points". Jo formulę, kaip jis apskaičiuojamas, paliksiu apraše apačioje."



 
 Terminologija:

Long (ilgasis pozicijos uždarymas): Tai reiškia pirkti finansinį instrumentą su tikimybe, kad jo vertė augs ateityje. Kada jūs einate "long", 
tai reiškia, kad jūs perkate instrumentą.

Short (trumpasis pozicijos uždarymas): Tai reiškia parduoti finansinį instrumentą, kurio neturite, su tikimybe, kad jo vertė kris ateityje. 
Vėliau jums reikės nusipirkti tą pačią prekę už mažesnę kainą, kad uždarytumėte poziciją. Tai leidžia uždirbti pelną iš krentančių kainų.


Pivot Point (PP)  Tai techninės analizės indikatorius, naudojamas nustatyti potencialias paramos (S) ir pasipriešinimo (R) zonas. 
Jis skaičiuojamas pagal šią formulę:
   PP = Vakarinė kaina + Aukščiausia kaina + Žemiausia kaina ir / dalinam visa suma is 3 
  Kur:
  - **Vakarinė kaina** yra ankstesnės prekybos dienos uždarymo kaina.
  - **Aukščiausia kaina** yra ankstesnės prekybos dienos didžiausia kaina.
  - **Žemiausia kaina** yra ankstesnės prekybos dienos mažiausia kaina. (Musu pavizdyja naudojame savaitinius duomenys tai yra nuo pirmadienio iki penktadienio)  

  Iš šio pivot point galima skaičiuoti pasipriešinimo ir paramos lygius:
  - **R1 Pasipriešinimo lygis 1: [ R1 = (2 \times PP) - Žemiausia kaina ]
  - **R2 Pasipriešinimo lygis 2:[ R2 = PP + (Aukščiausia kaina - Žemiausia kaina) ]
  - **S1 Paramos lygis 1:[ S1 = (2 \times PP) - Aukščiausia kaina ]
  - **S2 Paramos lygis 2:[ S2 = PP - (Aukščiausia kaina - Žemiausia kaina) ]

---

Leverage (Svertas):** Tai finansinis įrankis, kuris leidžia investuotojui padidinti savo pozicijos dydį naudojant mažiau nuosavų lėšų nei būtina. 
Leverage veikia kaip skolinimasis, kai investuotojas įneša tam tikrą sumą (vadinamąją pradinę maržą) ir gali prekiauti didesne vertės pozicija. 
Pavyzdžiui, 1:10 svertu, su 1000 USD sąskaitoje galima prekiauti pozicija verta 10,000 USD.

Aš naudoju 1:10 svertą su 1000 USD sąskaitoje,(Strategy-1,pynb) nes tai leidžia man padidinti potencialų pelną, neperkraunant sąskaitos ir išlaikant saugų maržos 
rezervą. Tačiau reikėtų nepamiršti, kad svertas didina tiek potencialų pelną, tiek ir potencialius nuostolius.




