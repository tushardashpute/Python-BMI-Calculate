class BMI:
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def bmi(self):
        return(self.weight/(self.height*self.height))
    
    def print_score(self):
        print("{} your age is {} , BMI is {}".format(self.name,self.age,self.score))
    
def _get_user_info():
    while True:
        try:
            name=input("Enter the name: ")
            age=int(input("Enter the age: "))
            height=input("Enter the Height: ")
            weight=input("Enter the weight: ")
            
            if 18 < age < 60:
                return age
            else:
                raise ValueError("Invalid Age.")
        except ValueError:
            print('Invalid Age, age should be between 18 to 60.')
            continue
    return (name,age,height,weight)
            
def calculate_bmi():
    (name,age,height,weight) = _get_user_info()
    return BMI(name,age,height,weight)

if __name__ == '__main__':
    bmi = calculate_bmi()
    bmi.print_score()