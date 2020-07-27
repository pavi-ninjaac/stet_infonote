
from fpdf import FPDF

class mail():
    def generate_hall(reg_no):
        exam_center='Sikkim Govertmetn College-Tadong'
        land_mark='Tadong'
        maplink=''
        return exam_center,land_mark,maplink
    def generate_mail(doc_name,reg_no):
        exam_center,land_mark,maplink=mail.generate_hall(reg_no)
        name = doc_name
        reg_no = 1234455
        datetime = '10-08-2020'
        exam_center = exam_center
        land_mark = land_mark
        maplink = maplink
        msg_header = f"""ADMIT CARD
        STATE TEACHERS ELIGIBILITY TEST - 2020 EXAMINATION
        Selection Committee Directrate of Education, Sikkim
        E-CALL FOT THE STET EXAMINATION - 2020
        """
        msg_body = [["Name of the candidate", name],
                    ['Register Number', reg_no],
                    ["Exam Date/Reporting Time", datetime],
                    ["Exam Center", exam_center],
                    ["Land Mark ", land_mark],
                    ["Google Map link:", maplink]]

        msg_footer = f"""

        TO BE FILLED ON EXAMINATION

        Candidate's sign                                                                               Invigilator's sign

        """
        pdf = FPDF('P', 'mm',(250,240))
        pdf.add_page()
        pdf.rect(x=5,y=5,w=(pdf.w)-10,h=(pdf.h)-10)
        pdf.rect(x=6, y=6, w=(pdf.w) - 12, h=(pdf.h) - 12)
        pdf.set_font('Times', size=12)
        epw = pdf.w - 2 * pdf.l_margin
        col_width = epw / 2
        th = (pdf.font_size) + 5
        pdf.image('sikkim_logo_2.jpg',w=40,h=30)
        for line in msg_header.split('\n'):
            pdf.cell(200, 10, txt=line, ln=1, align='C')
        for row in msg_body:
            for col in row:
                pdf.cell(col_width, th, str(col), border=1) \

            pdf.ln(th)
        for line in msg_footer.split('\n'):
            pdf.cell(200, 10, txt=line, ln=1, align='C')

        file_name='admit_card_'+str(doc_name)+'.pdf'
        pdf.output(file_name)
        return file_name


    
