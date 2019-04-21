# def factorial(n):
#     if n >= 1:
#         result = n * factorial(n-1)
      
#         return result
    
#     else:
        
#         return 1
  


# def fib(n):
#     if n >= 3:
#         result = fib(n-1) + fib(n-2)
#         print(fib(n-1),fib(n-2))
#         return result
    
#     else:
        
#         return 1


# print(fib(7))





# def fib(n):
#     a,b = 1,1
#     for i in range(n-1):
#         a,b = b, a + b
#     return a

# print(fib(7))



num_list = [1,2,3,4,5,6,7,8,9,]

str_list='actually,am coming,home'

def reverse_num(num):
    return "=".join(num.split(","))


# print(reverse_num(str_list))




num = [1,2,3,4,5]

map_func = list(map(lambda x: x+20,filter(lambda x: x%2==0,num)))


# def yld(i):
    
#     if i > 10:
#         print("Sorry that number is too large")
#     else:
#         while i < 10:
#             yield i
#             i += 1

# for i in yld(5):
#     print(i) 


# def ryield():
#     for i in range(40):
#         if i%15 == 0:
#             yield i

# print(list(ryield())) 

# word_set = set([1,2,2,3,3,4,5,6,7,8,8,9])

# print(word_set)

# from itertools import permutations

# print(list(permutations(("A","B","C"))))


# print(map_func)




class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == 'pineapple':
            raise ValueError("No pineapples!")
        else:
            return True
ingredients = ["cheese","onions","spam","pineapple"]

if any(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)

    # print(bool(pizza))


# multi-docker-redis.4oqni4.ng.0001.use2.cache.amazonaws.com
# multi-docker.c6avycbo4tgl.us-east-2.rds.amazonaws.com



