import pandas as pd 

duong_dan = r'C:\Users\Vo Phu Toan\Contacts\Desktop\New folder\danhsach1.xls' #Đường dẫn mở file

vi_tri_luu = r'C:\Users\Vo Phu Toan\Contacts\Desktop\New folder\danhsach1_edit.xls' #Đường dẫn lưu file

file_mau = pd.read_excel(duong_dan,sheet_name = 0)

file_mau['Tình trạng'] =''#Thêm 1 cột mới có tên là "Tình trạng"

file_mau.loc[2,'Tình trạng'] = 'Còn hàng' #Thay giá trị tại vị trí hàng 3, cột "tình trạng" thành "còn hàng"

file_mau.head()

file_mau.to_excel(vi_tri_luu) #Lưu file lại theo đường dẫn




