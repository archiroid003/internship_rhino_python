# coding: utf-8
import rhinoscriptsyntax as rs
import random

#クラス定義
class CirclePack():
    def __init__(self, _name, _circle_obj): #イニシャライズ関数の引数を何にすれば良いのか？
        self.name=_name
        self.circle_obj=_circle_obj
    
    def getDistance(self, y_c_i):
        m_p = rs.CircleCenterPoint(self.circle_obj)
        y_p = rs.CircleCenterPoint(y_c_i.circle_obj)
        dis = rs.Distance(m_p,y_p)
        return dis
        
    def getStatus(self, y_c_i):
        #TODO:getDistanse関数を使う
        if rs.IsCircle(self.circle_obj) and rs.IsCircle(y_c_i.circle_obj):
            radius_1 = rs.CircleRadius(self.circle_obj)
            radius_2 = rs.CircleRadius(y_c_i.circle_obj)
        
        m_p = rs.CircleCenterPoint(self.circle_obj)
        y_p = rs.CircleCenterPoint(y_c_i.circle_obj)
        dis_1_2=rs.Distance(m_p,y_p)

        if(dis_1_2 == radius_1 + radius_2):
            status = 0
        if(radius_1 + radius_2 < dis_1_2):
            status = 1
        if(dis_1_2 < radius_1 + radius_2):
            status = 2
        return status 
        
    def Moveobj(self,y_c_i):
        m_p=rs.CircleCenterPoint(self.circle_obj)
        y_p=rs.CircleCenterPoint(y_c_i.circle_obj)

        vector_m_y=rs.VectorCreate(y_p,m_p)
        vector_y_m=rs.VectorCreate(m_p,y_p)
        unit_vec_m_y=rs.VectorUnitize(vector_m_y)
        unit_vec_y_m=rs.VectorUnitize(vector_y_m)
        
        radius_1 = rs.CircleRadius(self.circle_obj)
        radius_2 = rs.CircleRadius(y_c_i.circle_obj)
        
        dis_1_2=rs.Distance(m_p,y_p)
        dis=dis_1_2 - (radius_1 + radius_2)
        move_dis=(dis/2) /10
        move_vec_m_y=rs.VectorScale(unit_vec_m_y,move_dis)
        move_vec_y_m=rs.VectorScale(unit_vec_y_m,move_dis)
        
#        status = self.getStatus(y_c_i)
#        
#        if(status == 1):
#            rs.MoveObject(self.circle_obj,move_vec_m_y)
#            rs.MoveObject(y_c_i.circle_obj,move_vec_y_m)
#    
#        if(status == 2):
#            rs.MoveObject(self.circle_obj,move_vec_y_m)
#            rs.MoveObject(y_c_i.circle_obj,move_vec_m_y)
        
        rs.MoveObject(self.circle_obj,move_vec_m_y)
        rs.MoveObject(y_c_i.circle_obj,move_vec_y_m)


#id_1=rs.AddCircle((0,0,0),40)
#id_2=rs.AddCircle((100,100,0),50)
#id_3=rs.AddCircle((-100,200),60)
#id_4=rs.AddCircle((0,100,0),30)

#- TODO:GHコンポーネントの入力変数に変更
circle_num =5

#--- 円作成
ids = []
for i in range(circle_num):
    circle_x = random.randint(0, 1000)
    circle_y = random.randint(0, 1000)
    circle_r = random.randint(20, 100)
    circle_id = rs.AddCircle((circle_x, circle_y,0), circle_r)
    ids.append(circle_id)

#--- インスタンス化
circle_packs = []
for i in range(circle_num):
    id = ids[i]
    circle_pack = CirclePack(str(i), rs.coercecurve(id))
    circle_packs.append(circle_pack)

#--- 出力
ids = []
for i in range(circle_num):
    circle_pack = circle_packs[i]
    id = circle_pack.circle_obj
    ids.append(id)

#↓メソッドの試しにこっちのコンポーネントにも

#for i in range(circle_num):
#    my_circle = circle_packs[i]
#    
#    for j in range(circle_num):
#        you_circle = circle_packs[j]
#        
#        
#        if my_circle == you_circle:
#            continue
#        move = my_circle.Moveobj(you_circle)
##        print(move)



out_circles = ids
out_circle_packs = circle_packs
