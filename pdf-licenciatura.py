from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 10)
        self.cell(0, 10, 'Tabela de Preços', 0, 1, 'C')
        self.ln(5)  # Reduzi o espaço após o cabeçalho

    def tabela_precos(self):
        # Cabeçalho da Tabela
        self.set_font('Arial', 'B', 9)  # Fonte menor para o cabeçalho
        self.cell(50, 8, 'Licenciaturas', 1, 0, 'C')
        self.cell(40, 8, 'Valor com Desconto', 1, 0, 'C')
        self.cell(40, 8, 'Valor Integral', 1, 0, 'C')
        self.cell(60, 8, 'Quantidade de Mensalidades', 1, 0, 'C')
        self.cell(30, 8, 'Duração', 1, 1, 'C')

        # Dados da Tabela
        self.set_font('Arial', '', 8)  # Fonte menor para os dados
        dados = [
            ['Artes Visuais', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['Biologia', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['Educação Especial', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['Educação Física', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['Filosofia', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['Física', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['Geografia', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['História', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['Letras - Português', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['Letras - Português/Inglês', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['Letras - Português/Espanhol', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['Matemática', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['Música', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['Pedagogia', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['Química', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['Sociologia', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
        ]

        for linha in dados:
            self.cell(50, 8, linha[0], 1, 0, 'L')
            self.cell(40, 8, linha[1], 1, 0, 'C')
            self.cell(40, 8, linha[2], 1, 0, 'C')
            self.cell(60, 8, linha[3], 1, 0, 'C')
            self.cell(30, 8, linha[4], 1, 1, 'C')

# Criação do PDF
pdf = PDF(orientation='L')  # 'L' para orientação paisagem
pdf.add_page()
pdf.set_margins(10, 10, 10)  # Margens esquerda, superior e direita

# Tabela de Preços
pdf.tabela_precos()

# Geração do arquivo PDF
pdf.output('tabela_precos_licenciatura.pdf')
