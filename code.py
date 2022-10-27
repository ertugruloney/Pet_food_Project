#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 00:37:38 2022

@author: ertugruloney
"""
from gurobipy import GRB
import gurobipy as gp
import pandas as pd
import numpy as np

product=2
m=gp.Model("project")

bagdemands=[[0,0,0,0,15185,0,0,0,0,0,0,0],
            [0,14489,0,0,0,21733,0,0,0,0,0,21733]]

weeks=12
mininventory=[[0,0,0,0,2278,0,0,0,0,0,0,0],
              [0,2173,0,0,0,3260,0,0,0,0,0,0]]


maxsuppinventor=[[15185,15185,15815,15185,15185,0,1265,2531,3796,5062,6327,7593],
                 [36222,36222,21733,21733,21733,43467,26563,31393,36222,41052,45881,50711]]
maxWareinve=[51407,	51407,	36919	,36919,	36919,	43467,	27828	,33923,	40019	,46114	,52209	,58304]
Moq=15000;

Costs=[[1,0.85,0.76,0.72,0.61,0.57,0.56],
       [1,0.85,0.76,0.72,0.61,0.57,0.56]]
orderamountsqty=[15000,30000,40000,60000,100000,200000,300000]

orderamounts=m.addVars(product,weeks,name="orderamounts",lb=0,vtype="I")
InventorySupp=m.addVars(product,weeks,name="Inventory at supplier",lb=0,vtype="I")
InventoryWare=m.addVars(product,weeks,name="Inventory in warehouse",lb=0,vtype="I")
ShipmentFWare=m.addVars(product,weeks,name="Shipments from supplier to WH",lb=0,vtype="I")
y=m.addVars(product,weeks,len(orderamountsqty),name='y',vtype="B")#if j. week for i. product is sold at k. price: 1
z=m.addVars(product,weeks,name='z', vtype='B')
#demandconstrait for first Week

constraint1= m.addConstrs(bagdemands[i][0]<=ShipmentFWare[i,0] for i in  range(product));
#demandconstrait for oher Week
constraint2= m.addConstrs(bagdemands[i][j]<=ShipmentFWare[i,j]+ InventoryWare[i,j-1] for j in range(1,weeks) for i in  range(product));
#moq const
constraint3= m.addConstrs(orderamounts[i,j]>=Moq*z[i,j] for j in range(weeks) for i in  range(product))
constraint32= m.addConstrs(orderamounts[i,j]<=15000000000*z[i,j] for j in range(weeks) for i in  range(product))
#Inventory at supplier const
constraint4= m.addConstrs(orderamounts[i,j]-ShipmentFWare[i,j]==InventorySupp[i,j] for j in range(weeks) for i in  range(product));

#max Inventory at supplier const
constrain5= m.addConstrs(InventorySupp[i,j]<=maxsuppinventor[i][j] for j in range(weeks) for i in  range(product));

#warehouse constrait

constrain6= m.addConstrs(ShipmentFWare[i,j]-bagdemands[i][j]+InventoryWare[i,j-1]==InventoryWare[i,j] for j in range(1,weeks) for i in  range(product))
constrain6_2= m.addConstrs(ShipmentFWare[i,0]-bagdemands[i][0]==InventoryWare[i,0]  for i in  range(product))
#min warehouse constrait
constrain7= m.addConstrs(InventoryWare[i,j]>=mininventory[i][j]for j in range(weeks) for i in  range(product))


#max warehouse constrait
constrain8= m.addConstrs(gp.quicksum(InventoryWare[i,j] for i in  range(product))<=maxWareinve[j] for j in range(weeks) )
# y total constarit
constrain9= m.addConstrs(gp.quicksum(y[i,j,k] for k in range(len(orderamountsqty)))<=1 for i in  range(product) for j in range(weeks) )
#y cost constarit
constrain10=m.addConstrs(orderamounts[i,j]<=gp.quicksum(orderamountsqty[k]*y[i,j,k] for k in range(len(orderamountsqty))) for i in  range(product) for j in range(weeks) )


m.setObjective(gp.quicksum(Costs[i][k]*orderamounts[i,j]*y[i,j,k] for k in range(len(orderamountsqty)) for i in  range(product) for j in range(weeks)),GRB.MINIMIZE)

m.write("project.lp")
m.optimize()


for v in m.getVars():
    print('%s %g' %(v.VarName,v.X))
    