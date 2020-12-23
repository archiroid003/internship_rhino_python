# coding: utf-8
import rhinoscriptsyntax as rs


print(circle_packs)
circle_num = len(circle_packs)
print(circle_num)



for i in range(circle_num):
    my_circle = circle_packs[i]
    
    for j in range(circle_num):
        you_circle = circle_packs[j]
        
        
        if my_circle == you_circle:
            continue
        
        my_circle.Moveobj(you_circle)

#--- 出力
ids = []
for i in range(circle_num):
    circle_pack = circle_packs[i]
    id = circle_pack.circle_obj
    ids.append(id)

out_circles = ids
