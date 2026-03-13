class Stock:
  def __init__(self, name:str, quantity:float):
    self.name = name
    self.quantity = quantity

  def currentPrice(self):
    return 1
  
  def totalValue(self):
    return self.currentPrice() * self.quantity
  
class Portfolio:
  def __init__(self, idOwner:int, stocks:list[Stock], allocation:dict[str, float]):
    self.idOwner = idOwner         
    self.stocks = stocks            
    self.allocation = allocation    
  
  def totalValue(self):
    total = 0
    for stock in self.stocks:
      total = total + stock.totalValue()
    return total 

  def rebalance(self):    #se asume que la aplicacion permite vender porcentajes de una accion 
    movimientos = {}
    total = self.totalValue()
    if total == 0:
      print('realiza tus primeras compras antes de rebalancear')
      return
    for stock in self.stocks: #se recorren solo las stocks por que al cambiar la distribucion se agregan stocks con cantidad 0 
      expectedValue = 0
      if stock.name in self.allocation:
        expectedValue = total * self.allocation[stock.name]
      actualValue = stock.quantity * stock.currentPrice()
      movimientos[stock.name] = (expectedValue - actualValue) / stock.currentPrice()
    
    for key in movimientos.keys():
      if movimientos[key] < 0:
        print(f'Vender {abs(movimientos[key])} acciones de {key}')
      if movimientos[key] > 0:
        print(f'Comprar {movimientos[key]} acciones de {key}')
    return movimientos
  
  def isValidName(name:str): # revisa si el nombre es valido
    return True
  
  def setAllocation(self, allocation): # se asumio que se ocupa esta funcion despues de crear un portfolio vacio
    sum = 0
    for key in allocation.keys():
      if not self.isValidName(key):
        print(f"no es una accion valida {key}") #o dependeiendo si se necesitara raise ValueError(f"nombre de accion no valido {key}")
        return 
      if allocation[key] < 0 :
        print("no se permiten distribuciones menor a 0") #o dependeiendo si se necesitara raise ValueError("valores negativos de distribucion no permitido")
        return 
      sum = sum + allocation[key]

    if abs(sum) - 1.0 > 1e-7:
      print("suma incorrecta") #o dependeiendo si se necesitara raise ValueError("la distribucion tiene que sumar 100")
      return 
      
    for key in allocation.keys():
      if not key in self.stocks:
        self.stocks[key] = Stock(key, 0)
  


