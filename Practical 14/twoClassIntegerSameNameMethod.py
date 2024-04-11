class PrintData:
  def print_data(self, n, c):
    print(f"{n} {c}")

  def print_data(self, c, n):
    print(f"{c} {n}")


obj = PrintData()

obj.print_data(5, 'A') 
obj.print_data('B', 3)  
