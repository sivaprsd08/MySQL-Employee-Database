Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> age-list = [24, 25, 26, 27, 28]
SyntaxError: cannot assign to operator
>>> age_list = [24,25,26,27,28]
>>> age_list
[24, 25, 26, 27, 28]
>>> name_list = [siva,krishna,hari,prasad]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    name_list = [siva,krishna,hari,prasad]
NameError: name 'siva' is not defined
>>> name_list = ["siva", "krishna", "hari"]
>>> name_list
['siva', 'krishna', 'hari']
>>> name_list.append("Yazhini")
>>> name_list
['siva', 'krishna', 'hari', 'Yazhini']
>>> age_list.insert(2, 30)
>>> age_list
[24, 25, 30, 26, 27, 28]
>>> name_list.remove("Yazhini")
>>> name_list
['siva', 'krishna', 'hari']
>>> age_list.pop()
28
>>> age_list
[24, 25, 30, 26, 27]
>>> age_list.extend([29, 30, 26])
>>> age_list
[24, 25, 30, 26, 27, 29, 30, 26]
>>> age_list.sort(reverse=True)
>>> age_list
[30, 30, 29, 27, 26, 26, 25, 24]
>>> max(age_list)
30
>>> min(age_list)
24
>>> sum(age_list)
217
>>> name_list[0]
'siva'
>>> name_list[-1]
'hari'
>>> name_list[2:4]
['hari']
>>> name_list[::-1]
['hari', 'krishna', 'siva']
>>> student_marks = {"hari":80, "krishna":90, "siva":95}
>>> student_marks
{'hari': 80, 'krishna': 90, 'siva': 95}
>>> student_marks["siva"]
95
>>> student_marks["Janani"] = 92
>>> student_marks
{'hari': 80, 'krishna': 90, 'siva': 95, 'Janani': 92}
>>> student_marks["hari"] = 85
>>> student_marks
{'hari': 85, 'krishna': 90, 'siva': 95, 'Janani': 92}
>>> student_marks.key()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    student_marks.key()
AttributeError: 'dict' object has no attribute 'key'
>>> student_marks.keys()
dict_keys(['hari', 'krishna', 'siva', 'Janani'])
>>> student_marks.values()
dict_values([85, 90, 95, 92])
>>> student_marks.items()
dict_items([('hari', 85), ('krishna', 90), ('siva', 95), ('Janani', 92)])
>>> my_set = { 'a', 'e', 'i', 'o', 'u', 'a','i'}
>>> my_set
{'o', 'e', 'u', 'i', 'a'}
>>> my_set[4] = 's'
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    my_set[4] = 's'
TypeError: 'set' object does not support item assignment
>>> my_set.add('s')
>>> my_set
{'o', 'e', 'u', 'i', 's', 'a'}
>>> set1 = {1,3,5,7,9}
>>> set2 = {2,3,5,8,10}
>>> set1
{1, 3, 5, 7, 9}
>>> set2
{2, 3, 5, 8, 10}
>>> set1.union(set2)
{1, 2, 3, 5, 7, 8, 9, 10}
>>> set1.interaction(set2)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    set1.interaction(set2)
AttributeError: 'set' object has no attribute 'interaction'
>>> set1.intersection(set2)
{3, 5}
>>> 