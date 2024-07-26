"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/134387126


题目描述
小明来到某学校当老师，需要将学生按考试总分或单科分数进行排名，你能帮帮他吗？

输入描述
第 1 行输入两个整数，学生人数 n 和科目数量 m。
    0 < n < 100
    0 < m < 10
第 2 行输入 m 个科目名称，彼此之间用空格隔开。
    科目名称只由英文字母构成，单个长度不超过10个字符。
    科目的出现顺序和后续输入的学生成绩一一对应。
    不会出现重复的科目名称。
第 3 行开始的 n 行，每行包含一个学生的姓名和该生 m 个科目的成绩（空格隔开）
    学生不会重名。
    学生姓名只由英文字母构成，长度不超过10个字符。
    成绩是0~100的整数，依次对应第2行种输入的科目。
第n+2行，输入用作排名的科目名称。若科目不存在，则按总分进行排序。

输出描述
输出一行，按成绩排序后的学生名字，空格隔开。成绩相同的按照学生姓名字典顺序排序。

用例1
输入
3 2
yuwen shuxue
fangfang 95 90
xiaohua 88 95
minmin 100 82
shuxue
输出
xiaohua fangfang minmin
说明
按shuxue成绩排名，依次是xiaohua、fangfang、minmin
"""

# 输入
# 学生人数 n 和科目数量 m
n, m = map(int, input().split())
# m 个科目名称, 写成科目：索引的字典形式
subject_to_idx = {subject:i for i, subject in input().split()}
# n 行，每行包含一个学生的姓名和该生 m 个科目的成绩
student_dict = {}  # key是学生姓名，val是对应科目成绩 + 总成绩 列表
for i in range(n):
    stu = input().split()
    name = stu[0]
    scores = list(map(int, stu[1:]))
    student_dict[name] = scores + [sum(scores)]
# 排名科目
rank_subject = input()

# 输出：按排名科目成绩降序，成绩相同按照姓名字典序升序，若排名科目不存在就按照总分
# todo 查找排名科目在科目字典中的索引，如果key不存在，指定默认值为最后一个索引（学生总分）
rank_idx = subject_to_idx.get(rank_subject, -1)

# 第n+2行，输入用作排名的科目名称。若科目不存在，则按总分进行排序
# 成绩相同的按照学生姓名字典顺序排序。
sorted_names = sorted(student_dict.items(),
                      key=lambda x: (-x[1][rank_idx], x[0]))
print(' '.join(map(lambda x: x[0], sorted_names)))
