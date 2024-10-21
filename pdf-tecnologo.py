from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Tabela de Preços - Tecnólogos', 0, 1, 'C')
        self.ln(10)

    def tabela_tecnologos(self):
        # Cabeçalho da Tabela para Tecnólogos
        self.set_font('Arial', 'B', 10)
        self.cell(10, 10, 'Nº', 1, 0, 'C')
        self.cell(100, 10, 'Tecnólogos', 1, 0, 'C')
        self.cell(40, 10, 'Valor com Desconto', 1, 0, 'C')
        self.cell(40, 10, 'Valor Integral', 1, 0, 'C')
        self.cell(60, 10, 'Quantidade de Mensalidades', 1, 0, 'C')
        self.cell(40, 10, 'Duração', 1, 1, 'C')  # Quebra a linha

        # Dados dos cursos de tecnólogos
        self.set_font('Arial', '', 12)
        dados_tecnologos = [
            # Adicionando os cursos de tecnólogos
            ['01', 'Análise e Desenvolvimento de Sistemas', 'R$ 149,90', 'R$ 199,90', '31 Mensalidades', '2,6 Anos'],
            ['02', 'Arquitetura de Dados', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['03', 'Automação Industrial', 'R$ 149,90', 'R$ 199,90', '37 Mensalidades', '3 Anos'],
            ['04', 'Big Data e Business Intelligence', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['05', 'Big Data e Inteligência Artificial', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['06', 'Cibersegurança', 'R$ 149,90', 'R$ 199,90', '31 Mensalidades', '2,6 Anos'],
            ['07', 'Ciência de Dados', 'R$ 149,90', 'R$ 199,90', '31 Mensalidades', '2,6 Anos'],
            ['08', 'Coaching Digital', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['09', 'Coaching e Mentoring', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['10', 'Comércio Exterior', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['11', 'Computação em Nuvem', 'R$ 149,90', 'R$ 199,90', '31 Mensalidades', '2,6 Anos'],
            ['12', 'Desenvolvimento de Aplicativos para Dispositivos Móveis', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['13', 'Desenvolvimento Mobile', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['14', 'Design de Interiores', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['15', 'Design Gráfico', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['16', 'Empreendedorismo Digital', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['17', 'Fotografia', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['18', 'Game Design', 'R$ 149,90', 'R$ 199,90', '31 Mensalidades', '2,6 Anos'],
            ['19', 'Gestão Ambiental', 'R$ 209,90', 'R$ 229,90', '25 Mensalidades', '2 Anos'],
            ['20', 'Gestão Comercial', 'R$ 209,90', 'R$ 229,90', '25 Mensalidades', '2 Anos'],
            ['21', 'Gestão da Produção Industrial', 'R$ 149,90', 'R$ 199,90', '37 Mensalidades', '3 Anos'],
            ['22', 'Gestão da Tecnologia da Informação', 'R$ 149,90', 'R$ 199,90', '31 Mensalidades', '2,6 Anos'],
            ['23', 'Gestão de Call Center', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['24', 'Gestão de Marketing em Mídias Digitais', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['25', 'Gestão de Negócios Digitais e Ecommerce', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['26', 'Gestão de Qualidade', 'R$ 209,90', 'R$ 229,90', '25 Mensalidades', '2 Anos'],
            ['27', 'Gestão de Recursos Humanos', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['28', 'Gestão de Serviços Jurídicos e Notariais', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['29', 'Gestão de Turismo', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['30', 'Gestão Desportiva e de Lazer', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['31', 'Gestão Financeira', 'R$ 209,90', 'R$ 229,90', '25 Mensalidades', '2 Anos'],
            ['32', 'Gestão Hospitalar', 'R$ 209,90', 'R$ 229,90', '37 Mensalidades', '3 Anos'],
            ['33', 'Gestão Pública', 'R$ 209,90', 'R$ 229,90', '25 Mensalidades', '2 Anos'],
            ['34', 'Inteligência Artificial Aplicada', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['35', 'Inteligência de Mercado e Análise de Dados', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['36', 'Internet das Coisas e Computação em Nuvem', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['37', 'Jogos Digitais', 'R$ 149,90', 'R$ 199,90', '31 Mensalidades', '2,6 Anos'],
            ['38', 'Logística', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['39', 'Marketing', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['40', 'Processos Gerenciais', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['41', 'Secretariado', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['42', 'Segurança do Trabalho', 'R$ 209,90', 'R$ 229,90', '37 Mensalidades', '3 Anos'],
            ['43', 'Segurança Pública', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
            ['44', 'Varejo Digital', 'R$ 149,90', 'R$ 199,90', '25 Mensalidades', '2 Anos'],
        ]

        for linha in dados_tecnologos:
            self.cell(10, 10, linha[0], 1, 0, 'C')  # Número
            self.cell(100, 10, linha[1], 1, 0, 'L')  # Nome do curso
            self.cell(40, 10, linha[2], 1, 0, 'C')  # Valor com desconto
            self.cell(40, 10, linha[3], 1, 0, 'C')  # Valor integral
            self.cell(60, 10, linha[4], 1, 0, 'C')  # Quantidade de mensalidades
            self.cell(40, 10, linha[5], 1, 1, 'C')  # Duração do curso

# Criando o PDF
pdf = PDF('L', 'mm', 'A4')
pdf.add_page()
pdf.tabela_tecnologos()
pdf.output('tabela_precos_tecnologo.pdf')

