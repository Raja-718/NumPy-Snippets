
import numpy as np 
   
# construct a NumPy array 
weight = np.array([50.7, 52.5, 50, 58, 55.63, 73.25, 49.5, 45]) 
   
# minimum and maximum  
print('Minimum and maximum weight of the students: ') 
print(np.amin(weight), np.amax(weight)) 
   
# percentile 
print('Weight below which 70 % student fall: ') 
print(np.percentile(weight, 70)) 
    
# mean  
print('Mean weight of the students: ') 
print(np.mean(weight)) 
   
# median  
print('Median weight of the students: ') 
print(np.median(weight)) 
   
# standard deviation  
print('Standard deviation of weight of the students: ') 
print(np.std(weight)) 
   
# variance  
print('Variance of weight of the students: ') 
print(np.var(weight)) 
   
# average  
print('Average weight of the students: ') 
print(np.average(weight))