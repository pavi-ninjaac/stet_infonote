
num=['ZERO','NINE','SEVEN','EIGHT']
zum_dict={'ZERO':0,'(ONE':1,'TWO':2,'THREE':3,'FOUR':4,'FIVE':5,'SIX':6,'SEVEN':7,'EIGHT':8,'NINE':9}
mark=''
for n in num:
    for text,value in zip(zum_dict,zum_dict.values()):
        if n==text:
            mark+=str(value)
print((int(mark)/1200)*100)
from fpdf import FPDF
name='pavi'
reg_no=1234455
datetime='1343'
exam_center='madurai'
land_mark='madurai road'
maplink='fjskfnsjbfhdfbhdbfhdbfhdbfhdhgbd'
msg_header=f"""ADMIT CARD
STATE TEACHERS ELIGIBILITY TEST - 2020 EXAMINATION
Selection Committee Directrate of Education, Sikkim
E-CALL FOT THE STET EXAMINATION - 2020
"""
msg_body=[["Name of the candidate" ,name],
['Register Number',reg_no],
["Exam Date/Reporting Time" ,datetime],
["Exam Center",exam_center],
["Land Mark ",land_mark],
["Google Map link:",maplink]]

msg_footer=f"""


TO BE FILLED ON EXAMINATION

Candidate's sign                                                                               Invigilator's sign

"""
pdf=FPDF(orientation='P',unit='mm',format='A4')
pdf.add_page()
pdf.set_font('Times',size=12)
epw=pdf.w - 2*pdf.l_margin
col_width=epw/2
th=(pdf.font_size)+5

for line in msg_header.split('\n'):
    pdf.cell(200,10,txt=line,ln=1,align='C')
for row in msg_body:
    for col in row:

        pdf.cell(col_width,th,str(col),border=1)
    pdf.ln(th)
for line in msg_footer.split('\n'):
    pdf.cell(200, 10, txt=line, ln=1, align='C')
pdf.output('document_demo.pdf')