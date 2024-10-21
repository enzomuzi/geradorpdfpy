from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 10)
        self.cell(0, 10, 'Tabela de Preços - Bacharelados', 0, 1, 'C')
        self.ln(5)

    def tabela_precos(self):
        # Cabeçalho da Tabela
        self.set_font('Arial', 'B', 8)  # Fonte menor para o cabeçalho
        self.cell(15, 8, 'Nº', 1, 0, 'C')
        self.cell(70, 8, 'Bacharelados', 1, 0, 'C')
        self.cell(35, 8, 'Valor com Desconto', 1, 0, 'C')
        self.cell(35, 8, 'Valor Integral', 1, 0, 'C')
        self.cell(50, 8, 'Quantidade de Mensalidades', 1, 0, 'C')
        self.cell(30, 8, 'Duração do Curso', 1, 1, 'C')

        # Dados da Tabela
        self.set_font('Arial', '', 8)  # Fonte menor para os dados
        dados = [
            ['01', 'Administração', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['02', 'Arquitetura e Urbanismo', 'R$ 329,90', 'R$ 369,00', '61 Mensalidades', '5 Anos'],
            ['03', 'Biblioteconomia', 'R$ 119,90', 'R$ 179,90', '37 Mensalidades', '3 Anos'],
            ['04', 'Biomedicina', 'R$ 369,90', 'R$ 399,90', '49 Mensalidades', '4 Anos'],
            ['05', 'Ciências Contábeis', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['06', 'Ciências Econômicas', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['07', 'Ciências Políticas', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['08', 'Comunicação Social - Publicidade e Propaganda', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['09', 'Educação Física', 'R$ 339,90', 'R$ 359,90', '49 Mensalidades', '4 Anos'],
            ['10', 'Engenharia Ambiental', 'R$ 279,90', 'R$ 319,90', '61 Mensalidades', '5 Anos'],
            ['11', 'Engenharia Civil', 'R$ 279,90', 'R$ 319,90', '61 Mensalidades', '5 Anos'],
            ['12', 'Engenharia de Controle e Automação', 'R$ 279,90', 'R$ 319,90', '61 Mensalidades', '5 Anos'],
            ['13', 'Engenharia de Produção', 'R$ 279,90', 'R$ 319,90', '61 Mensalidades', '5 Anos'],
            ['14', 'Engenharia Industrial Mecânica', 'R$ 279,90', 'R$ 319,90', '61 Mensalidades', '5 Anos'],
            ['15', 'Engenharia Elétrica', 'R$ 279,90', 'R$ 319,90', '61 Mensalidades', '5 Anos'],
            ['16', 'Farmácia', 'R$ 369,90', 'R$ 399,90', '61 Mensalidades', '5 Anos'],
            ['17', 'Fisioterapia', 'R$ 369,90', 'R$ 399,90', '61 Mensalidades', '5 Anos'],
            ['18', 'Nutrição', 'R$ 369,90', 'R$ 399,90', '49 Mensalidades', '4 Anos'],
            ['19', 'Relações Internacionais', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['20', 'Serviço Social', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['21', 'Sistemas de Informação', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['22', 'Teologia', 'R$ 119,90', 'R$ 179,90', '49 Mensalidades', '4 Anos'],
            ['23', 'Terapia Ocupacional', 'R$ 169,90', 'R$ 199,90', '49 Mensalidades', '4 Anos'],
        ]

        for linha in dados:
            self.cell(15, 8, linha[0], 1, 0, 'C')  # Número
            self.cell(70, 8, linha[1], 1, 0, 'L')  # Bacharelados
            self.cell(35, 8, linha[2], 1, 0, 'C')  # Valor com Desconto
            self.cell(35, 8, linha[3], 1, 0, 'C')  # Valor Integral
            self.cell(50, 8, linha[4], 1, 0, 'C')  # Quantidade de Mensalidades
            self.cell(30, 8, linha[5], 1, 1, 'C')  # Duração do Curso

# Criação do PDF
pdf = PDF(orientation='L')  # 'L' para orientação paisagem
pdf.add_page()
pdf.set_margins(10, 10, 10)  # Margens esquerda, superior e direita

# Tabela de Preços
pdf.tabela_precos()

# Geração do arquivo PDF
pdf.output('tabela_precos_bacharelados_2.pdf')
