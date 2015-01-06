'''
Created on 30-Dec-2014

@author: naveen
'''
import xlsxwriter
import xlwt
from xlwt import Style
from selenium.webdriver.support.color import Color
# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('/home/naveen/Desktop/output/demo.xlsx')
worksheet1 = workbook.add_worksheet('Config')
worksheet2 = workbook.add_worksheet('Sheet1')

print(Color.from_string('#00ff33').rgba)
print(Color.from_string('rgb(1, 255, 3)').hex)
print(Color.from_string('blue').rgba)

# Widen the first column to make the text clearer.
worksheet2.set_column('A:A',  10)
worksheet2.set_column('B:B', 6)
worksheet2.set_column('C:C', 7)
worksheet2.set_column('D:D', 20)
worksheet2.set_column('H:H', 20)
worksheet2.set_column('K:K', 10)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})
format = workbook.add_format()  # @ReservedAssignment

format.set_font_color('red')
format.set_bold()
format.set_italic()
worksheet1.write(3, 3, 'wheelbarrow', format)

worksheet2.conditional_format('A1:D12', {'type': '2_color_scale'})

# Write some simple text.
worksheet1.write('A1', 'S.No')
worksheet1.write('B1', 'Target')
worksheet1.write('C1', 'BrowStackUrl')
worksheet1.set_column('C:C', 15)
worksheet1.write('D1', 'Operating System')
worksheet1.write('E1', 'Device/Brow')
worksheet1.write('F1', 'Version')
worksheet1.write('G1', 'App/Url')
worksheet1.write('H1', 'Width')
worksheet1.write('I1', 'Height')
worksheet1.write('J1', 'Test')
worksheet1.write('K1', 'SheetName')
worksheet1.write('L1', 'Result')
worksheet1.write('M1', 'Report')

worksheet2.write('D6', 'hhalldl')
worksheet2.write('A1', 'Action No')
worksheet2.write('B1', 'Run on')
worksheet2.write('C1', 'Window')
worksheet2.write('D1', 'Description')
worksheet2.write('E1', 'Dependency')
worksheet2.write('F1', 'Scenario')
worksheet2.write('G1', 'Sub-Scenario')
worksheet2.write('H1', 'Locator')
worksheet2.write('I1', 'Action')
worksheet2.write('J1', 'Values')
worksheet2.write('K1', 'Expected Url')
worksheet2.write('L1', 'Expected Contents')
worksheet2.write('M1', 'Actual Contents')
worksheet2.write('N1', 'Expected X axis')
worksheet2.write('O1', 'Expected Y Axis')
worksheet2.write('P1', 'Actual X axis')
worksheet2.write('Q1', 'Actual Y Axis')
worksheet2.write('Q1', 'Actual Y Axis')
worksheet2.write('R1', 'Test?')
worksheet2.write('S1', 'Result')
worksheet2.write('T1', 'Report')
worksheet2.write('U1', 'Timetaken')
worksheet2.write('V1', 'Screenshot')

#Autofilter
worksheet1.autofilter('A1:J1')

# Text with formatting.
worksheet2.write('A2', 'World', bold)

# Write some numbers, with row/column notation.
worksheet2.write(2, 0, 123)
worksheet2.write(4, 3, 767573)
worksheet2.write(0,23, 'Sambo')
worksheet2.write(3, 0, 123.456)

# Insert an image.
worksheet1.insert_image('B5', '/home/naveen/Documents/excels/logoputtogether.png')

workbook.close()