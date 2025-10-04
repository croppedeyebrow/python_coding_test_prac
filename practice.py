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


sum = 8
sum += 1  #sum = sum + 1
print(sum)


