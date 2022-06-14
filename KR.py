def fact(x):
  if x == 1:
        return 1
  else:
        return x * fact(x - 1)
    
def filter_even(li):
  return list(filter(lambda elem: elem % 2 == 0, li))

def square(li):
  return list(map(lambda x: x * x, li))

def bin_search(li, element):
    start = 0
    end = len(li)
    mid = 0
    while start <= end:
        mid = (start + end) // 2
        if element == li[mid]:
            return mid
        
        if element < li[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1
  
def is_palindrome(string):
    redundant_symbols = '.,!?:;()[]\{\}\'\"/\\- '
    for symbol in string:
        if symbol in redundant_symbols:
            string = string.replace(symbol, '')

    string = string.lower()
    length = len(string)
    mid = length // 2
    for i in range(mid):
        if string[i] != string[length - 1 - i]:
            print('NO')
            return

    print('YES')
    return
  
def calculate(path2file):
    input = open(path2file, 'r')
    output = open('output.txt', 'w')
    string = ''
    for line in input:
        words = line.split()
        if words[0] == '+': result = int(words[1]) + int(words[2])
        elif words[0] == '-': result = int(words[1]) - int(words[2])
        elif words[0] == '*': result = int(words[1]) * int(words[2])
        elif words[0] == '//': result = int(words[1]) // int(words[2])
        elif words[0] == '%': result = int(words[1]) % int(words[2])
        elif words[0] == '**': result = int(words[1]) ** int(words[2])
        string += str(result) + ','
    
    string = string[:-1]
    return string
  
def substring_slice(path2file_1,path2file_2):
    file1 = open(path2file_1, 'r')
    file2 = open(path2file_2, 'r')
    str = ''
    for line in file1:
        indexes = (file2.readline()).split()
        str += line[int(indexes[0]):int(indexes[1]) + 1] + ' '

    str = str[:-1]
    return str

def decode_ch(sting_of_elements):
    periodic_table = json.load(open('periodic_table.json', encoding='utf-8'))
    str = ''
    length = len(sting_of_elements)
    for i in range(length):
        if sting_of_elements[i].islower():
            continue
        if i + 1 < length:
            if sting_of_elements[i + 1].islower():
                str += periodic_table[sting_of_elements[i:i + 2]]

            else:
                str += periodic_table[sting_of_elements[i]]
        else:
            str += periodic_table[sting_of_elements[i]]

    return str

  
class Student:
    def __init__(self, name, surname, grades = [3, 4, 5]):
        self.name = name
        self.surname = surname
        self.fullname = name + ' ' + surname
        self.grades = grades
    
    def greeting(self):
        print('Hello, I am Student!')

    def mean_grade(self):
        return sum(self.grades) / len(self.grades)

    def is_otlichnik(self):
        if self.mean_grade >= 4.5:
            return 'YES'
        else:
            return 'NO'

    def __add__(self, obj):
        return self.name + ' is friends with ' + obj.name

    def __str__(self):
        return self.fullname

class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
