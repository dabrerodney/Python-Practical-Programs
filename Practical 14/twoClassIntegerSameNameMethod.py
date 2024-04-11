class Printer:
    def print_item(self, integer):
        print("Integer:", integer)
    
    def print_item(self, character):
        print("Character:", character)

# Example usage:
printer = Printer()
printer.print_item(5)       # Calls the first method
printer.print_item('A')     # Calls the second method
