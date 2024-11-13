
# ZADANIE REKRUTACYJNE OXIDO

Witam bardzo serdecznie w repozytorium z moim rozwiązaniem :)

W kodzie została uwzględniona również część przeznaczona "dla chętnych", dlatego w folderze output istnieje rozwiązanie dla części pierwszej jak i tej drugiej.

W repozytorium są trzy główne katalogi:
- src 
- output 
- data

### src - katalog zawierający główny kod 
### data - katalog z danymi wejściowymi oraz szablonem
### output - katalog na dane wyjściowe
## Installation

W celu wypróbowania programu sciągamy repo używając git clone

```bash
  git clone https://github.com/fabilier228/zadanie-rekrutacyjne-oxido
  cd zadanie-rekrutacyjne-oxido
  pip install -r requirements.txt
```

Aby program działał na stronie [openAI](https://platform.openai.com/docs/overview) zakładamy konto i generujemy key API, a następnie wklejamy w src/article_processor.py,
w miejscu do tego przeznaczonym.

Program uruchamiamy:

```bash
  py src/main.py
```    
## Dokumentacja

[openai-python](https://github.com/openai/openai-python)

