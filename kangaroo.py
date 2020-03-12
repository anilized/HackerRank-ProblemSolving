# 1st => if position and speed is same then true
# 2nd => if (x1>=x2 and v1>=v2) or (x1<=x2 and v1<=v2) => FALSE
# 3rd => if opposite of 2nd then take absolute values if mod == 0 then return TRUE

def kangaroo(x1, v1, x2, v2):
    if x1==x2 and v1==v2:
        return "YES"
    elif (x1>=x2 and v1>=v2) or (x1<=x2 and v1<=v2):
        return "NO"
    else:
        z=abs(x2-x1)
        x=abs(v2-v1)
        if z%x==0:
            return "YES"
        else:
            return "NO"
