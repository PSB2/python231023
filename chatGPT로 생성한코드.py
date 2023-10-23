# List의 장점: 순서가 있고 수정이 가능함
my_list = [1, 2, 3]
my_list.append(4)  # 수정 가능
print("List:", my_list)

# List의 단점: 검색 및 삭제에 비효율적일 수 있음
# 검색: O(n), 삭제: O(n)

# Tuple의 장점: 순서가 있고 수정이 불가능함
my_tuple = (1, 2, 3, 3)
print("Tuple:", my_tuple)

# Tuple의 단점: 수정 및 삭제가 불가능함
# 검색: O(n) - List와 동일

# Set의 장점: 중복된 요소를 허용하지 않고 빠른 검색 가능
my_set = {1, 2, 3, 3}
my_set.add(4)
print("Set:", my_set)

# Set의 단점: 순서가 없어 인덱스로 접근 불가능함

# Dict의 장점: 키-값 쌍을 저장하여 빠른 검색 가능
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict['d'] = 4
print("Dictionary:", my_dict)

# Dict의 단점: 순서가 없어 인덱스로 직접 접근 불가능함


