def fibSeries(n):
    fArr = [0, 1]   
    next = 1        
    for i in range(2, n):
        next = next + fArr[i - 2]  
        fArr.append(next)           
    return fArr                    
n = 10
result = fibSeries(n)
print(result)