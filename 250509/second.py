# 딕셔너리 dict()
# key:value
# my_dict = {"me": "길도"}
# my_dict2 = dict()
# my_dict2_1 = dict([("one", "하나"), ("two", "둘")])
# print(my_dict2_1)
# print(my_dict)

# # 데이터 추가
# dict4 = dict()
# dict4["max"] = "노잼"
# dict5 = dict()
# dict5["1"] = [1,2,"3",4]
# print(dict4)
# print(dict5)

"""
dict() 를통해 빈 딕셔너리를 만든 후

데이터 삽입을 하여 키가 4개 , 각각의 밸류에는 다른 타입의 데이터를 넣어서

그 딕셔너리를 출력
"""
# a = dict()
# a["이름"] = "홍길동"
# a["나이"] = 90 , (100)
# a["취미"] = ["잠자기", ("푹자기"), ["계속자기"]]
# a["진짜? 가짜?"] = True
# print(a)

# 데이터 읽기
# person = {"name": "licat", "age": 25, "height": 165.5}
# print(f"이름은: {person['name']}입니다.")
# print(f"나이는: {person['age']}입니다.")
# # print(f"생년월일은: {person['good']}입니다.") -> KeyError: 'good'
# # 데이터 수정
# person["age"] = 30  # age 키를 통해 value 값을 30으로 변경
# print(person)
# person["name"] = "BJH"
# person["weight"] = 1
# print(person)

# # 데이터 삭제
# del person["height"]
# print(person)

# person["age"] = None  # 키를 남기고 값을 없애고 싶을 때
# print(person)
# a = {"good": ["a", "b", "c"]}
# a["good"].remove("c")
# print(a)  # {'good': ['a', 'b']}

# b = {"good1": {"good2": [1, 2, 3, [1, 2, 3]]}}
# #'good1': {'good2': [1, 2, 3, [1, 2, 3,4]]}}
# b["good1"]["good2"][3].append(4)
# print(b)

person = {"name": "licat", "age": 25, "city": "seoul"}
# get(키, 키가 없을 경우 valuy)
# city = person.get("city","없는뎅")
# print(city)
# city2 = person.get("city2","없는뎅")
# print(city2)

# 키만 가져온다.
person_keys = person.keys() # 키 값들만 추출
print(person_keys) # dict_keys(['name', 'age', 'city'])
a = list(person_keys) # 형변환
print(a)

# Value만 추출
person_values = person.values() # Value 값들만 추출
print(person_values) # dict_values(['licat', 25, 'seoul'])
b = list(person_values)
print(b)

# 전체를 추출
person_items = person.items()
print(person_items) # dict_items([('name', 'licat'), ('age', 25), ('city', 'seoul')])
c = list(person_items) #[('name', 'licat'), ('age', 25), ('city', 'seoul')]
print(c)

# del person['age'] 권장x
a = person.pop("age") # age라는 키에 있는 값을 a에 저장
print(a)
print(person)