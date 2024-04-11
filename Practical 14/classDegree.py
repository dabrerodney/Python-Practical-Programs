class Degree:
    def getDegree(self):
        print("I got a degree")

class Undergraduate(Degree):
    def getDegree(self):
        print("I am an Undergraduate")

class Postgraduate(Degree):
    def getDegree(self):
        print("I am a Postgraduate")

# Example usage:
degree = Degree()
degree.getDegree()

undergraduate = Undergraduate()
undergraduate.getDegree()

postgraduate = Postgraduate()
postgraduate.getDegree()
