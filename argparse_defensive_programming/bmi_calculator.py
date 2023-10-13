# this gets user height and weight and computes the BMI

def main():
    height:float = float(input("Enter height: "))
    weight:float = float(input("Enter weight: "))
    print(f"your BMI is {BMI(0,2)}")

def BMI(height:float, weight:float) -> float:    
    return height**2 / weight

if __name__ == '__main__':
    main()