import random
import math


calci_use_again='yes'


def logo():
    print("========***WELCOME  TO  SCIENTIFIC  CALCULATION  APP***========")
    for i in range(8):
        for j in range(i+2):
            print(" " ,end = " ")
        for j in range(1,7-i):
            print('!', end= " ")
        for j in range(5-i,0,-1):
            print(random.randint(0,9),end = " ")
        for j in range(3-i,0,-1):
            print('%',end = " ")
        print(' ')

def header(i):
        print(' ')
        option=('Percentage','Factorial','LCM(Least Common Multiple)','HCF(Highest Common Factor)',
                'Square root', 'Log','exp(x)','x^y', 'Cos(x)+sin(x)')
        print("===========Calculate ",option[i],"===========")

def number():
    num= int(input("Enter a number:"))
    return num
def percentage(num,value):
    percent_output= float(num)*(value/100)
    print(value," % of ",num," = ",percent_output)
def factorial(num):
     factorial=1
     if num < 0:
        print("sorry, factorial does not exist for negative numbers")
     elif num == 0:
          print("The factorial of 0 is 1 ")
     else:
        for i in range(1,num+1):
                factorial = factorial*i
        print(str(num)+chr(33),"=",factorial)
def LCM(num1,num2):
        if num1 > num2:
           greater = num1
        else:
           greater = num2
        while(True):
           if((greater % num1 == 0) and ( greater % num2 == 0)):
                 lcm_output = greater
                 break
           greater = greater + 1
        print("LCM of",num1,"and",num2,"=",lcm_output)
def HCF (num1, num2):
       if (num1>num2):
            smaller = num2
       else:
            smaller= num1
       i = 1
       while (i<=smaller):
           if(num1%i==0 and num2%i ==0):
              hcf_output = i
           i= i+1
       print(" HCF of", num1,"and",num2,"+",hcf_output)
def square_root(num):
      sqrt_output=math.sqrt(num)
      print("The square root of",num," = ",sqrt_output)
def log(num):
      log_output=math.log10(num)
      print("The log of",num," = ",log_output)
def exp(num):
      exp_output=math.exp(num)
      print("The exp(%d)" %num, " = ", exp_output)
def power(num, power_val): 
      power_output=math.pow(num,power_val)
      print(" The ",power_val," raised to the power of", num, " = ", power_output)
def cossin(num1, num2): 
      cossin_output=math.cos(num1)+math.sin(num2)
      print("The cos ({0])+sin({1})".format(num1,num2)," = ",cossin_output)

logo()



while calci_use_again in ('Yes','Y','Y','Yes'):
    print(" Calculator options: %, Factorial, LCM , HCF ,Square root, log, exp(x),x^y,cos(x)+sin(x)")
    calculate=input("select calcuator options:")

    count_more_numbers='yes'
    while count_more_numbers in ('yes','y','yes'):

        if calculate == " % ":
                     header(0)
                     num=number()
                     value=int(input("Enter % value:"))
                     percentage(num,value)
                     count_more_numbers = input("Do you want to calculate more numbers? ")
        elif calculate == "Factorial":
              header(1)
              num=number(num)
              factorials(num)
              count_more_numbers = input("Do you want to calculate more numbers?)")
        elif calculate == "LCM":
              header(2)
              num1=number()
              num2=int(input("Enter an another number:"))
              LCM(num1,num2)
              count_more_numbers = input("Do you want to calculate more numbers?")
        elif calculate == "HCF":
              header(3)
              num1=number()
              num2=int(input("Enter an another number:"))
              HCF(num1,num2)
              count_more_numbers = input("Do you want to calculate more numbers?")
        elif calculate == "Square root":
              header(4)
              num=number()
              square_root(num)
              count_more_numbers = input("Do you want to calculate more numbers?")
        elif calculate == "Log":
              header(5)
              num=number()
              log(num)
              count_more_numbers = input("Do you want to calculate more numbers?")
        elif calculate == "exp(x)":
              header(6)
              num=number()
              exp(num)
              count_more_numbers = input("Do you want to calculate more numbers?")
        elif calculate == "x^y":
              header(7)
              num=number()
              power_val=int(input("Enter power value:"))
              power(num,power_val)
              count_more_numbers = input("Do you want to calculate more numbers?")
        elif calculate == "cos(x)+sin(x)":
              header(8)
              num1=number()
              num2=int(input("Enter a number:"))
              cossin(num1,num2)
              count_more_numbers = input("Do you want to calculate more numbers?")
        else :
              print("Sorry enter option is not available in calculator.")
              count_more_numbers = 'n'

              print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
              print(' ')
              calci_use_again= input("Do you want to use calculator for other options?")
