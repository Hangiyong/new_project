# list append insert
# index, value(element) -> item
# append : 추가
# isnert : 삽입

user1 = ["Spencer", '200']
user2 = ["Mussg", "50"]

user1.append(100)
print(user1)

user2.insert(0, "Name")
print(user2)

new_list = [1, 2, [3, 4, 5]]

print(new_list[2][2])



# 리스트 참조(ref)와 복사(copy)
score_A = [80, 70, 60, 50, 40]
score_B = score_A.copy()
score_B[0] = 100

print(score_A)
print(score_B)

# id()
print(id(score_A))