import time
import string as st

class FirstChar:
  def __init__(self):
    self.__setVogais = set("aeiouAEIOU")
    self.string = ""
    self.tempoTotal = ""
  
  def __ehVogal(self, char) -> bool:
    return (char in self.__setVogais)

  def compute(self, string) -> float:
    startTime = time.process_time()
    self.string = string
    vogal = ''

    if string != "":
      ultimo = string[0]
      antePenultimo = string[0]
      caracteresPossiveis = {}

      for atual in self.string.strip():
        if atual in caracteresPossiveis:
          caracteresPossiveis.pop(atual)
        elif self.__ehVogal(atual) and not self.__ehVogal(ultimo) and self.__ehVogal(antePenultimo):
          caracteresPossiveis[atual] = 1
        antePenultimo = ultimo
        ultimo = atual
    
      if len(caracteresPossiveis) != 0:
        vogal = list(caracteresPossiveis.keys())[0]

    endTime = time.process_time()
    self.tempoTotal = f"{((endTime - startTime)*1000):.4f}"
    return vogal
