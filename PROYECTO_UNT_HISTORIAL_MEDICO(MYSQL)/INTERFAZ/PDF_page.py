from fpdf import FPDF
import datetime

class PDF(FPDF):

    def header(self):
        self.image('./ICONOS/logo.png',
                x = 10, y = 10, w = 30, h = 30)

        self.set_font('Arial', '', 15)

        self.set_text_color(r=96,g=181,b=218) 
        self.set_font_size(45)
        self.set_font('Arial', 'B')
        
        self.cell(w = 0, h = 20, txt = 'Historial Medico', border = 0, ln=1,
                align = 'C', fill = 0)

        self.set_font_size(10)
        self.set_text_color(r=0,g=0,b=0)
        self.set_font('Arial', 'I')
        
        self.cell(w = 0, h = 10, txt = 'Generado el '+ str(datetime.date.today()), border = 0, ln=2,
                align = 'C', fill = 0)

        self.ln(5)

    def footer(self):
        
        self.set_y(-20)

        self.set_font('Arial', 'I', 12)

        self.cell(w = 0, h = 10, txt =  'Pagina ' + str(self.page_no()) + '/{nb}',
                 border = 0,
                align = 'C', fill = 0)   

