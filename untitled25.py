import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#과목별 평균 구하기
x = pd.read_csv('score.csv', header=None).values
arr_x=x[1:,1:]
arr_x1=arr_x.astype('float')
subject_mean = arr_x1.mean(axis=0)
subject_mean_str = subject_mean.astype("str")
header = x[0,1:]+"subj.mean"

#두 1차원 텐서를 수직방향으로 합침
subject_mean_complete=np.vstack((header,subject_mean_str))
print(subject_mean_complete)

# 과목별 평균 그림 그리기
X=subject_mean_complete[0,:]
Y=subject_mean_complete[1,:]
plt.title("Subject Mean_2270005_KwonJiHyean")
bar=plt.bar(X, Y.astype('float'), color = 'blue')
plt.ylim(0,100)
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1f' % height, ha='center', va='bottom', size = 12)
plt.show()

#학생별 평균 구하기
student_mean = arr_x1.mean(axis=1)
student_mean_str=student_mean.astype("str")
header = x[1:,0]+" stu. mean"
student_mean_complete= np.vstack((header,student_mean_str)) 
print(student_mean_complete)
X=student_mean_complete[0,:]
Y=student_mean_complete[1,:]
plt.title("Student Mean_2270005_KJH")
bar=plt.bar(X, Y.astype('float'), color='red')
plt.ylim(0,100)
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1f' % height, ha='center', va='bottom', size = 12)    
plt.show   

 