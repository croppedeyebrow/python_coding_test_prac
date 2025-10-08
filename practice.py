# 01. Print 명령어  Hello World로 시작하기.

# print("Hello World")

#print("Hello" + " " + "World")

# print({'name': 'John', 'age': 30, 'city': 'New York'})

#print([1,2,3,4,5])

#print((1,2,3,4,5))

# print(44)
# print(3.14)
# print(True)

# 02. Input 명령어에 대해 알아보기.

#print(input("What is your nickname?"))

#print("My nickname is" + " "+ input("What is your nickname?"))

#print(len(input("What is your nickname?")))


# 03. variable(변수)에 대해서 알아보기.

# name = input("What is your nickname?")
# print("My nickname is" + " "+ name)
#input으로 만든 값을 name이라는 '변수'에 할당을 하고, print문으로 출력.

# 변수명은 항상 의미있는 이름으로.
# name = "data_forge"
# print(name)

#int + int = int
# print(1 + 2)
# #str + str = str
# print("1" + "2")





# 04. Primitive data type(원시 자료형)에 대해 알아보기.

# # Integers(정수형)
# progile_number = 7216
# print(progile_number)


# # Floats(실수형으로 변환)
# score = float(60)
# print(score)

# # Booleans(불리언형, 참/거짓)
# is_student = True
# print(is_student)


# # Strings(문자열형)
# dba_name = "data_forge" #따옴표 2개로 표시.
# db_name = 'andamiro' #따옴표 1개로 표시.
# schema_detatil ="""this shcema is about
# data_forge"""  #여러줄 문자열은 큰따옴표 3개로 표시.

# print(dba_name)
# print(db_name)
# print(schema_detatil)


# # string indexing(문자열 인덱싱)
# name = "data_forge"
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# print(name[6])
# print(name[7])
# print(name[8])
# print(name[9])

# # check object type (객체 타입 확인)
# print(type(name))


# 05. Type error(타입 오류)에 대해 알아보기.

# str + int = error
# print("Hello" + 1 + "World")


# convert type (타입 변환) int to str
# print(type(1))
# print(type(str(1)))

# print("Hello" + str(1) + "World")

# 06.Mathmatical opertaion(수학 연산자)에 대해서 알아보기

# print(1 + 2)
# print(1 - 2)
# print(1 * 2)

# # /의 리턴값은 float = /(나누기 연산자)
# print(1 / 2)
# print(1/1)

# # floor division(몫) = //(몫 연산자)
# print(3//2)
# print(7//3)

# # Exponentiation(제곱) = **(제곱 연산자)
# print(2**3)
# print(3**3)

# # modulo(나머지) = %(나머지 연산자)
# print(60 % 13)
# print(52 % 8)

# PEMDAS(수학 연산자 우선순위)
# Parentheses(괄호)
# Exponents(제곱)
# Multiplication(곱셈)
# Division(나눗셈)
# Addition(덧셈)
# Subtraction(뺄셈)
# And Left To Right(왼쪽에서 오른쪽으로 계산)


# sum = 8
# sum += 1  #sum = sum + 1
# print(sum)


#07. f-string(문자열 포맷팅)에 대해 알아보기.

# name = "data_forge"
# age = 30
# print("Hello, %s" %name) #%s는 문자열 포맷팅
# print("Hello, %s, you are %s years old" %(name, age)) #%s는 문자열 포맷팅, ()안에 변수를 넣어준다.
# print("--------------------------------")
# #문제는 변수를 하나씩 넣어줘야 하는 번거로움.

# # 번거로움을 피하기 위해 {}안에 인덱스를 넣어서 하는 방법이 2.6부터 고안됨.

# print("Hello, {0}, i am {1} years old".format(name, age)) #{}안에 인덱스를 넣어서 하는 방법.

# print("--------------------------------")
# # 딕셔너리를 사용하는 방법 
# person = {"name": "data_forge", "age": 30}
# print("Hello, {name}, i am {age} years old".format(name=person["name"], age=person["age"])) #format_map를 사용하여 딕셔너리를 풀어서 하는 방법.
# print("Hello, {name}, i am {age} years old".format(**person)) #**를 사용하여 딕셔너리를 풀어서 하는 방법.

# # 딕셔너리는 키-값 쌍으로 이루어져 있기 때문에, 키를 사용하여 값을 가져올 수 있다.

# print("--------------------------------")

# #f-string 방법

# #""앞에 f를 붙여서 사용하는 방법. 중괄호를 넣고 변수 이름을 넣으면 자동으로 할당

# print(f"Hello, {name}, i am {age} years old") #f-string 방법.


# 08. Conditional statement(조건문)에 대해 알아보기.

# condition(조건절) : if, else
# if 10 > 20:
#     print("10 is greater than 20")
# else:
#     print("10 is less than 20")
    
# print("--------------------------------")  

# # condition(조건절) : if, elif, else
# if 20 > 20:
#     print("10 is greater than 20")
# elif 20 == 20:
#     print("10 is equal to 20")
# else:
#     print("10 is less than 20")

# print("--------------------------------")

# my_stock = 100000

# if my_stock == 0:
#     print(f"My stock, {my_stock} is equal to 0")
# elif my_stock == 100:
#     print(f"My stock, {my_stock} is equal to 100")
# elif my_stock == 1000:
#     print(f"My stock, {my_stock} is equal to 1000")
# elif my_stock == 10000:
#     print(f"My stock, {my_stock} is equal to 10000")
# else:
#     print(f"My stock, {my_stock} is equal to 100000")




# print("--------------------------------")   
 
# # input에 int값을 받는 condition 조건절
# if int(input("How tall, are you in cm?")) > 180:
#     print("You are over 180cm")
# else:
#     print("You are under 180cm")
    
    
# 09. 복합 조건절(Multiple if Conditional Expression)에 대해서.    

# my_stock = 100

# if my_stock > 0:
#     print(f"My stock, {my_stock} is greater than 0")
# if my_stock > 100:
#     print(f"My stock, {my_stock} is greater than 100")
# if my_stock > 1000:
#     print(f"My stock, {my_stock} is greater than 1000")
# if my_stock > 10000:
#     print(f"My stock, {my_stock} is greater than 10000")
# else:
#     print(f"My stock, {my_stock} is equal to 0")


# 10. Logical operator(논리 연산자)에 대해 알아보기.