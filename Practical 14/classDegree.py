class Degree:
  def getDegree(self):
    print("I got a degree")

class Undergraduate(Degree):
  def getDegree(self):
    super().getDegree()  # Call the parent class method first (optional in this case)
    print("I am an Undergraduate")

class Postgraduate(Degree):
  def getDegree(self):
    super().getDegree()  # Call the parent class method first (optional in this case)
    print("I am a Postgraduate")

# Create objects and call getDegree method
undergrad = Undergraduate()
undergrad.getDegree()

postgrad = Postgraduate()
postgrad.getDegree()

degree = Degree()
degree.getDegree()
