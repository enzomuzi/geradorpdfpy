from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Tabela de Preços - 2ª Licenciaturas', 0, 1, 'C')
        self.ln(10)

    def tabela_licenciaturas(self):
        # Cabeçalho da Tabela para 2ª Licenciaturas
        self.set_font('Arial', 'B', 10)
        self.cell(10, 10, 'Nº', 1, 0, 'C')
        self.cell(100, 10, '2ª Licenciaturas', 1, 0, 'C')
        self.cell(40, 10, 'Valor com Desconto', 1, 0, 'C')
        self.cell(40, 10, 'Valor Integral', 1, 0, 'C')
        self.cell(60, 10, 'Quantidade de Mensalidades', 1, 0, 'C')
        self.cell(40, 10, 'Duração', 1, 1, 'C')

        # Dados dos cursos de 2ª Licenciaturas
        self.set_font('Arial', '', 12)
        dados_licenciaturas = [
            ['01', 'Biologia', 'R$ 119,90', 'R$ 249,90', '19 Mensalidades', '6 a 18 Meses*'],
            ['02', 'Educação Especial', 'R$ 119,90', 'R$ 249,90', '19 Mensalidades', '6 a 18 Meses*'],
            ['03', 'Educação Física', 'R$ 119,90', 'R$ 249,90', '19 Mensalidades', '6 a 18 Meses*'],
            ['04', 'Filosofia', 'R$ 119,90', 'R$ 249,90', '19 Mensalidades', '6 a 18 Meses*'],
            ['05', 'Física', 'R$ 119,90', 'R$ 249,90', '19 Mensalidades', '6 a 18 Meses*'],
            ['06', 'Geografia', 'R$ 119,90', 'R$ 249,90', '19 Mensalidades', '6 a 18 Meses*'],
            ['07', 'História', 'R$ 119,90', 'R$ 249,90', '19 Mensalidades', '6 a 18 Meses*'],
            ['08', 'Matemática', 'R$ 119,90', 'R$ 249,90', '19 Mensalidades', '6 a 18 Meses*'],
            ['09', 'Química', 'R$ 119,90', 'R$ 249,90', '19 Mensalidades', '6 a 18 Meses*']
        ]

        for linha in dados_licenciaturas:
            self.cell(10, 10, linha[0], 1, 0, 'C')  # Número
            self.cell(100, 10, linha[1], 1, 0, 'L')  # Nome do curso
            self.cell(40, 10, linha[2], 1, 0, 'C')  # Valor com desconto
            self.cell(40, 10, linha[3], 1, 0, 'C')  # Valor integral
            self.cell(60, 10, linha[4], 1, 0, 'C')  # Quantidade de mensalidades
            self.cell(40, 10, linha[5], 1, 1, 'C')  # Duração do curso

# Criando o PDF
pdf = PDF('L', 'mm', 'A4')
pdf.add_page()
pdf.tabela_licenciaturas()
pdf.output('tabela_precos_2a_licenciatura.pdf')
