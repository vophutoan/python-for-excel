import pandas as pd 

file_mau = pd.read_excel (r'C:\Users\Vo Phu Toan\Contacts\Desktop\New folder\danhsach1.xls') 

#file_mau.X1 #Lấy giá trị của cột X1, X1 không có khoảng cách
#file_mau['X2'] #Lấy giá trị của cột X2, X2 có khoảng cách

#file_mau.X1.sum() #Lấy Tổng của cột X1

#file_mau.X1.mean() #Trung bình cộng cột X1

#file_mau.X1.nunique() #Lấy số lượng của cột X1

#file_mau['X1'].value_counts() #Đếm số lượng các thành phần có trong cột X1
