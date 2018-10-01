import xlrd, xlwt

rbook = xlrd.open_workbook('demo.xlsx')
rsheet = rbook.sheet_by_index(0)

k = rsheet.ncols
rsheet.put_cell(0, k, xlrd.XL_CELL_TEXT, '总分', None)

for i in range(1, rsheet.nrows):
    t = sum(rsheet.row_values(i, 1))
    rsheet.put_cell(i, k, xlrd.XL_CELL_NUMBER, t, None)


wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)

for i in range(rsheet.nrows):
    for j in range(rsheet.ncols):
        wsheet.write(i, j, rsheet.cell_value(i, j))

wbook.save('out.xlsx')
