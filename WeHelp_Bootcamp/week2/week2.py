# ============== task 1 =============
print("====== task 1 ======")
from typing import Dict

def find_and_print(messages: Dict):
    key_words = {
        '18 years old', 'college student', 'legal age in Taiwan', 'vote'
      }  # -> array

    for name, msg in messages.items():  # -> object
        for kw in key_words:  # -> for
            if kw in msg:  # msg.include(kw)
                print(name)  # console.log(name)


find_and_print({
    "Bob": "My name is Bob. I'm 18 years old.",
    "Mary": "Hello, glad to meet you.",
    "Copper": "I'm a college student. Nice to meet you.",
    "Leslie": "I am of legal age in Taiwan.",     
    "Vivian": "I will vote for Donald Trump next week",
    "Jenny": "Good morning."
 })

# =============== task 2 ================
print("====== task 2 ======")

def calculate_sum_of_bonus(data):
    performance_multiplier = {
        'above average': 3,
        'average': 2,         
        'below average': 1,
     }
    role_multiplier = {
        'Engineer': 3,
        'CEO': 1,
        'Sales': 2,
     }
    
    bonus = 0 

    for info in data['employees']:
         

        if isinstance(info['salary'], str) and info['salary'].endswith('USD'):
             # 把文字去除, 然後轉成整數
             salary = int(info['salary'][:-3])*30

        elif isinstance(info['salary'], str):
             salary = int(info['salary'].replace(',', ''))

        elif isinstance(info['salary'], int):
             salary = info['salary']
        
        if salary >= 60000 :
            salary_multiplier =1
        elif 40000 < salary < 60000 :
            salary_multiplier =2
        else:
            salary_multiplier =3

        bonus += (round( (salary_multiplier + performance_multiplier[info['performance']] + role_multiplier[info['role']]) / 18 *10000))

    print(bonus)
    

calculate_sum_of_bonus({
     "employees": [
         {
             "name": "John",
             "salary": "1000USD",
             "performance": "above average",
             "role": "Engineer"
         },
         {
             "name": "Bob",
             "salary": 60000,
             "performance": "average",
             "role": "CEO"
         },
         {
             "name": "Jenny",
             "salary": "50,000",
             "performance": "below average",
             "role": "Sales"
         }
     ]
 })

# =============== task 3 ================
print("====== task 3 ======")  

def func(*data):
    d = {}

    for name in data:
         #中間名如果不在d 裡面
         if name[1] not in d:
             d[name[1]] = [name]
         else:
             d[name[1]].append(name) 
         

    ans=[]
    for name in d:
        if len(d[name])==1:
            ans= d[name]
                     

    if len(ans)!=1:
        print("沒有")
    else:
        print(ans[0])

# 用for迴圈掃過整個d
# 如果 長度 == 1, 印出名字
# 如果沒有, 印沒有

func("彭⼤牆", "王明雅", "吳明")  # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有

# =============== task 4 ================
print("====== task 4 ======")

def get_number(index):
    
    def recu(index):
        if index == 0:
            return 0 
        
        if index % 2 == 0:
            return recu(index - 1) -1
        
        else:
            return recu(index - 1) +4
    print(recu(index))

get_number(1)  # print 4
get_number(5)  # print 10
get_number(10)  # print 15

# =============== task 5 ================
print("====== task 5 ======")

def find_index_of_car(seats, status, number):
    diff = float('inf')
    ans = -1
    for i in range(len(seats)):
        if seats[i] >= number and status[i] == 1:
            if seats[i] - number < diff:
                diff = seats[i] - number
                ans = i
    print(ans)


find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2)  # print 4
find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4)  # print -1
find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4)  # print 2