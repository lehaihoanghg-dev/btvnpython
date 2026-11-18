def normalize_name(text):
    return " ".join(text.split())
def average_score(scores):
    if not scores : return None
    return sum(scores) / len(scores)
def count_passed(scores : list[float], threshold : float = 5 ) -> int:
    """dem so luong diem dat tu nguong tro len"""
    count = 0
    for i in scores:
        if i >= threshold:
            count += 1
    return count

def rank_students(score_by_name):
    kq = dict(sorted(score_by_name.items() , key = lambda item : (-item[1] , item[0])))
    return(kq)


print(normalize_name(" Nguyễn An "))
print(normalize_name("minh"))
print(normalize_name(" "))

ds1 = [8 , 4 , 9 , 5]
print("Danh sách 1:", ds1)
print("Trung bình:", average_score(ds1))
print("Số đạt (ngưỡng 5):", count_passed(ds1))
print("Số đạt (ngưỡng 8):", count_passed(ds1, 8))

ds2 = [5]
print("Danh sách 2:", ds2)
print("Trung bình:", average_score(ds2))
print("Số đạt (ngưỡng 5):", count_passed(ds2))
print("Số đạt (ngưỡng 8):", count_passed(ds2, 8))

ds3 = []
print("Danh sách 3:", ds3)
print("Trung bình:", average_score(ds3))
print("Số đạt (ngưỡng 5):", count_passed(ds3))
print("Số đạt (ngưỡng 8):", count_passed(ds3, 8))

score_by_name = {"Minh": 9, "Lan": 7, "An": 9, "Vy": 5}
print(rank_students(score_by_name))