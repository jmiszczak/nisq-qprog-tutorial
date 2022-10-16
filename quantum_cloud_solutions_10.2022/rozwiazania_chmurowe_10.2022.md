# Rozwiązania chmurowe dla obliczeń kwantowych
## Stan na październik 2022

### Streszczenie

Raport przedstawia zestawienie systemów udostępniających możliwość
wykonywania obliczeń kwantowych z poziomu chmury obliczeniowej.
Uwzględnione są rozwiązania poszczególnych firmy produkujących komputery
kwantowe jak rozwiązania dostawców usług obliczeniowych.

### Amazon Braket

Amazon Braket to w pełni zarządzana usługa obliczeń kwantowych, która ma
pomóc w przyspieszeniu badań naukowych i rozwoju oprogramowania dla
obliczeń kwantowych. Usługa pozwala na zapoznanie się z możliwościami
programowania komputerów kwantowych i zbadać potencjalne zastosowania.
Amazon Braket zapewnia środowisko programistyczne, który można uruchomić
lokalnie na laptopie lub w pełni zarządzanym środowisku notebooków w
chmurze obliczeniowej.

![Koncepcja funkcjonowania dostępu do maszyn kwantwoych w serwisie Amazon Braket](amazon-braket-diagram.png)

W chwili obecnej Amazon Braket udostępnia urządzenia firm D-Wave, ION Q, Oxford Quantum Circuit, Rigetti oraz Xanadu. Każde z tych urządzeń jest zbudowane w opariu o innny zestaw technologi i możliwości programowania.

![Urządzenia kwantowe dostępne poprzed interfejs AWS. Stan na październik 2022](amazon-braket-10.0222.png)

### Google Cloud Platfrom

Google Cloud oferuje dostęp do komputera firmy IonQ w ramach usłudi zarządzanej.
Udsotępniana maszyna pozwala na wykonywania obliczeń z pamięcią kwantową 11
kubitów.

![Informacje o usłudzie dostępu do komputera IonQ z poziomu Google Cloud
console](google-cloud-ionq-10.2022.png)

Usługi zarządzane są w pełni hostowane, zarządzane i obsługiwane przez
usługodawców. Aby korzystać z usługi konieczna jest rejstracja się u
usługodawcy. Natomiast firma Google zajmuje się rozliczeniami kosztów
korzystania ze sprzętu.

Usługa ta jest dostępna poprzez wybranie jej z usług Google Cloud Marketplace. 

### Xanadu Cloud

Firma Xanadu udostępniła swój komputer w czerwcu 2022.  Udostępniony komputer to
Borealis, programowalny fotoniczny komputer kwantowy z 216 qubitami w stanie
ściśniętym. MAszyn ta zostałą wykorzystana do uzyskania  czyli który przewyższa
najlepsze klasyczne superkomputery w konkretnym zadaniu, dostępny dla ludzi
wszędzie poprzez Xanadu Cloud i Amazon Braket.

![Interfejs użytkownika udostępniany w Xandau Cloud](xanadu-cloud-interface.png)

Xanadau Cloud dostarcza interfejsu opratego o Jupyter Lab. Firma dostarcza
również zestawy przykładów oraz tutoriali pozwalających na zaznajomienie się z
proramowaniem w bibliotece PennyLane.

### IBM Qunatum

IBM Quantum Composer i IBM Quantum Lab tworzą platformę internetową
umożliwiającą publiczny i premium dostęp do opartych na chmurze usług obliczeń
kwantowych świadczonych przez IBM Quantum. Obejmuje to dostęp do zestawu
prototypowych procesorów kwantowych IBM, zestawu samouczków dotyczących obliczeń
kwantowych oraz dostęp do interaktywnego podręcznika.

![Przykład wykorzystania narzędzia Composer w systemie IBM Quantum](ibm-q-composer.png)

IBM Quantum pozwala również na zarządzania zasobami komputerowymi przypisanymi
do danego konta. W tej chili w podstawowoje wersji dostępnych jest sześć
komputerów o maksymalnej pamięci 7 qubitów. IBM udostępnia równiez spejalizowane
symulatory pozwalające na testowanie kodu kwantowego w różnych scenariuszach. 

![Zarządzanie zasobami komputerowymi w paneu IBM Quantum](ibm-q-resources.png)

### D-Wave Systems

Oprogramowanie Ocean to pakiet narzędzi, które D-Wave Systems udostępnia na
repozytorium D-Wave GitHub do rozwiązywania trudnych problemów z wykorzystaniem
komputerów kwantowych.

Dostęp do wyżażacza D-Wave systems jest możliwy poprzez interfejst Leap.
Interfejs ten zapewnie kontrolę na wykorzystaniem zasobó obliczniowych.
Dostarcza również środowiska progrmistycznego bazującego na VS Code oraz
zintegrowanego z GitHub i GitPod.

![Widok zarządzania wykorzystaniem czasu obliczeniowego w systemie D-Wave Leap.](d-wave-leap-dashboard.png)

### IONQ

Firma IonQ, opróc dostępu poprzez Google Cloiud Platfrom, udostępnia również
narzędzie do kontrolowania kolejki wykonania peocesów na maszynie waktowej.


Dodatkowo, możliwe jest uruchamianie zadań na komputerze IonQ z poziomu
biblioteki Qiskit.

### AQT

Firma AQT udostępnia w tej chili symulator pułpki jonowej. Obecnie dostępne są
idealne i zaszumione symulatory do uruchamiania obwodów kwantowych. Trwają prace
nad udostępnieniem sprzętu kwantowego.

![Zarządzanie subskrypcją z poziomu interfejsu firmy AQT](aqt-subscriptions.png)


#### Źródła

1. https://www.aboutamazon.com/news/aws/aws-launches-new-quantum-computing-center, October 28, 2021
1. https://aws.amazon.com/braket/
1. https://cloud.google.com/blog/products/compute/ionq-quantum-computer-available-through-google-cloud, June 18, 2021
1. https://cloud.xanadu.ai/
1. https://www.xanadu.ai/press/xanadu-launches-first-public-cloud-deployed-computer-with-quantum-computational-advantage, June 1, 2022
1. L.S. Madse, et al., Quantum computational advantage with a programmable photonic processor, Nature, 606, pages 75–81 (2022), https://doi.org/10.1038/s41586-022-04725-x
1. https://pennylane.ai/
1. https://cloud.dwavesys.com/leap/
1. https://www.gitpod.io/
1. https://www.ibm.com/quantum
1. https://quantum-computing.ibm.com
1. https://cloud.ionq.com
1. https://gateway-portal.aqt.eu/
