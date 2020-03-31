def addPoint(curve,pointp,pointq):
    #curve are curve parameters, point 1 is in the form [x1,y1], point 2 is in the form [x2,y2]
    diff1=mod_sub(pointp[0],pointq[0],curve[0]) #x1-x2
    diff2=mod_sub(pointp[1],pointq[1],curve[0]) #y1-y2
    diff1=mod_inverse(diff1,curve[0]) #(x1-x2)^-1
    grad=mod_mul(diff2,diff1,curve[0]) #(y1-y2) x (x1-x2)^-1
    x3=mod_exp(grad,2,curve[0]) #l^2
    x3=mod_sub(x3,pointp[0],curve[0]) #l^2-x1
    x3=mod_sub(x3,pointq[0],curve[0]) #l^2-x1-x2
    y3=mod_sub(pointp[0],x3,curve[0]) 
    y3=mod_mul(grad,y3,curve[0])
    y3=mod_sub(y3,pointp[1],curve[0])
    return [x3,y3]
    
def doublePoint(curve,pointp):
    mul1=mod_mul(3,mod_exp(pointp[0],2,curve[0]),curve[0])
    add1=mod_add(mul1,curve[2],curve[0])
    mult2=mod_mul(2,pointp[1],curve[0])
    mult2=mod_inverse(mult2,curve[0])
    grad=mod_mul(mult2,add1,curve[0])
    x3=mod_exp(grad,2,curve[0]) #l^2
    x3=mod_sub(x3,pointp[0],curve[0]) #l^2-x1
    x3=mod_sub(x3,pointp[0],curve[0]) #l^2-x1-x2
    y3=mod_sub(pointp[0],x3,curve[0]) 
    y3=mod_mul(grad,y3,curve[0])
    y3=mod_sub(y3,pointp[1],curve[0])
    return [x3,y3]
#Curve point multiplication using Montgomery Ladder

def mulPoint(curve,point,factor):
    factor=bin(factor)[2:]
    point0=float('inf')
    point1=point
    for i in range(len(factor)):
        if int(factor[i])==1:
            if point0 == float('inf'):
                point0,point1=point1,doublePoint(curve,point1)
            else:
                point0,point1=addPoint(curve,point1,point0),doublePoint(curve,point1)
        else:
            if point0==float('inf'):
                point0,point1=point0,addPoint(curve,point1,point0)
            else:
                point0,point1=doublePoint(curve,point0),addPoint(curve,point1,point0)
    return point0
