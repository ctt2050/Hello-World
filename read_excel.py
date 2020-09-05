import xlrd
#步骤：1、先获取表对象
#     2、再获取值


#变量名:数据类型 = 值 强调变量中所保存的值是str类型
file_name:str='MTT.xls'
#打开一个xls文件（注意后缀名必须是xls）得到指向这个文件的工作簿（workbook）对象
work_book = xlrd.open_workbook(file_name)

#获取工作簿下工作表名称的列表
names = work_book.sheet_names()
print(names)
#根据下标来获取指定的工作表，,下标从0开始
sheet = work_book.sheet_by_index(0)  #sheet对象
print(sheet.name)
# #根据工作表名称来获取自定的工作表
# sheet=work_book.sheet_by_name('Sheet1')
# print(sheet.name)
#
# #获取总行数，总列数, ncols代表列数,nrows代表行数
# print(sheet.ncols,sheet.nrows)
#
# #cell_type获取单元格中数据的类型，第一个参数代表行，第二个参数代表列,下标都是从0开始
# # 数据类型：0:empty(空)  1:string  2:number  3:boolean  4:error
# cell_type = sheet.cell_type(1,1)
#
# #cell_value获取单元格中数据的值，第一个参数代表行，第二个参数代表列,下标都是从0开始
# cell_value = sheet.cell_value(1,1)
# print(cell_type,cell_value)
#
# # 双层循环遍历表中内容
# for row in range(sheet.nrows):
#     for col in range(sheet.ncols):
#         print('{}行{}列:{}'.format(row+1, col+1, sheet.cell_value(row, col)))
#
# print('*'*20)
# #整行获取数据
# for row in range(sheet.nrows):
#     print(sheet.row_values(row))
#
# print('*'*20)
# #整列获取数据
# for col in range(sheet.ncols):
#     print(sheet.col_values(col))
#
# #获取指定行列的单元格对象
cell=sheet.cell(1,1)
print("cell.value:{}".format(cell.value))

