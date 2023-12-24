import numpy as np
data = np.loadtxt('sales.tsv',delimeter="\t",dtype = float)
branch = data[:,0]

sales = data[:,1:]
sum_perbranch = np.sum(sales, axis = 1) #sum for horizontal line
for i in range(data.shape[0]): #data.shape[0] = the number of rows of 'data'
    print("Branch%d --> %.2f"%(data[i,0],sum_perbranch[i]))

products = ["A","B","C"]
sum_perproduct = np.sum(sales, axis = 0) #sum for vertical line
for i in range(sales.shape[1]): #data.shape[1] = the number of colums of 'data'
    print("Product%s --> %.2f"%(products[i],sum_perproduct[i]))
    
    
#Find the branch number with the highest sale amount
sort_sumperbranch = sorted(sum_perbranch)
print("The highest sale amount = %.2f"%(sort_sumperbranch[-1]))

argsort_sumperbranch = np.argsort(sum_perbranch) #To get index of sum per branch, which is index of branch
print("The branch with the hisghest sale amount = %d"%data[argsort_sumperbranch[-1],0])