#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd #IMPORT THƯ VIỆN PANDAS

file_mau = pd.read_excel (r'x1') #ĐỌC FILE EXCEL CÓ ĐƯỜNG DẪN LÀ X1

print(file_mau) #IN RA MÀN HÌNH DỮ LIỆU CỦA FILE

file_mau.head() #IN RA MÀN HÌNH HÀNG ĐẦU TIÊN TRONG FILE

file_mau.shape #IN RA THÔNG TIN SỐ LƯỢNG HÀNG, CỘT CỦA BẢNG

gia = pd.DataFrame(df, columns= ['x2','x3']) #LẤY DỮ LIỆU TỪ CỘT CÓ TÊN X2, X3 VÀ IN RA MÀN HÌNH
print(gia) 

