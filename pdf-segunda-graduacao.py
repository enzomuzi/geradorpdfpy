from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Tabela de Preços - 2ª Graduação', 0, 1, 'C')
        self.ln(10)

    def tabela_graducao(self):
        # Cabeçalho da Tabela para 2ª Graduação
        self.set_font('Arial', 'B', 10)
        self.cell(10, 10, 'Nº', 1, 0, 'C')
        self.cell(100, 10, '2ª Graduação', 1, 0, 'C')
        self.cell(40, 10, 'Valor com Desconto', 1, 0, 'C')
        self.cell(40, 10, 'Valor Integral', 1, 0, 'C')
        self.cell(60, 10, 'Quantidade de Mensalidades', 1, 0, 'C')
        self.cell(40, 10, 'Duração', 1, 1, 'C')

        # Dados dos cursos de 2ª Graduação
        self.set_font('Arial', '', 12)
        dados_graducao = [
            ['01', 'CIÊNCIAS CONTÁBEIS', 'R$ 360,90', 'R$ 390,90', '13 Mensalidades', '12 a 18 Meses'],
        ]

        for linha in dados_graducao:
            self.cell(10, 10, linha[0], 1, 0, 'C')  # Número
            self.cell(100, 10, linha[1], 1, 0, 'L')  # Nome do curso
            self.cell(40, 10, linha[2], 1, 0, 'C')  # Valor com desconto
            self.cell(40, 10, linha[3], 1, 0, 'C')  # Valor integral
            self.cell(60, 10, linha[4], 1, 0, 'C')  # Quantidade de mensalidades
            self.cell(40, 10, linha[5], 1, 1, 'C')  # Duração do curso

# Criando o PDF
pdf = PDF('L', 'mm', 'A4')
pdf.add_page()
pdf.tabela_graducao()
pdf.output('tabela_preco_2a_graduacao.pdf')
