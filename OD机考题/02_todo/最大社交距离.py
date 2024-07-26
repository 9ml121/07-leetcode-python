





import math
seatNum = 10
seatOrLeave = [1,1,1,1,-4,1]


used_idx = []
best_idx = -1
for item in seatOrLeave:
    print(used_idx)
    # 1.有人离开
    if item < 0:
        leave_idx = -item
        used_idx.remove(leave_idx)
        continue
    # 2.新进来一个人
    if len(used_idx) == seatNum:
        # 坐满了
        best_idx = -1
        continue
    
    if len(used_idx) == 0:
        best_idx = 0
        used_idx.append(0)
    elif len(used_idx) == 1:
        best_idx = seatNum-1
        used_idx.append(seatNum-1)
    else:
        # 101001
        max_dis = -1
        for i in range(1, len(used_idx)): # used_idx需要从小到大排序
            cur_dis = used_idx[i] - used_idx[i-1] - 1
            cur_dis = math.ceil(cur_dis/2)
            if cur_dis > max_dis: # 绝对大于
                max_dis = cur_dis
                best_idx = used_idx[i-1] + cur_dis 
        
        # 100010000
        if used_idx[-1] < seatNum-1:
            cur_dis =  seatNum-1 - used_idx[-1] - 1
            if cur_dis > max_dis: # 绝对大于
                best_idx = seatNum-1
        
        used_idx.append(best_idx)
        used_idx.sort()
    
print(best_idx)