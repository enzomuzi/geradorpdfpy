from fpdf import FPDF

# Criar o objeto PDF
pdf = FPDF(orientation='L', unit='mm', format='A4')
pdf.add_page()

# Definir fonte e título
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Programa Especial de Formação Docente', 0, 1, 'C')

# Adicionar cabeçalho da tabela
pdf.set_font('Arial', 'B', 10)
pdf.set_fill_color(200, 220, 255)
pdf.cell(10, 10, 'Nº', 1, 0, 'C', 1)
pdf.cell(60, 10, 'Programa', 1, 0, 'C', 1)
pdf.cell(40, 10, 'Valor com Desconto', 1, 0, 'C', 1)
pdf.cell(40, 10, 'Valor Integral', 1, 0, 'C', 1)
pdf.cell(50, 10, 'Quantidade de Mensalidades', 1, 0, 'C', 1)
pdf.cell(40, 10, 'Duração do Curso', 1, 1, 'C', 1)

# Adicionar dados das linhas
pdf.set_font('Arial', '', 10)
cursos = [
    (1, "Biologia", "R$ 199,90", "R$ 390,90", "13 Mensalidades", "6 a 18 meses*"),
    (2, "Educação Física", "R$ 199,90", "R$ 390,90", "13 Mensalidades", "6 a 18 meses*"),
    (3, "Filosofia", "R$ 199,90", "R$ 390,90", "13 Mensalidades", "6 a 18 meses*"),
    (4, "Física", "R$ 199,90", "R$ 390,90", "13 Mensalidades", "6 a 18 meses*"),
    (5, "Geografia", "R$ 199,90", "R$ 390,90", "13 Mensalidades", "6 a 18 meses*"),
    (6, "História", "R$ 199,90", "R$ 390,90", "13 Mensalidades", "6 a 18 meses*"),
    (7, "Matemática", "R$ 199,90", "R$ 390,90", "13 Mensalidades", "6 a 18 meses*"),
    (8, "Química", "R$ 199,90", "R$ 390,90", "13 Mensalidades", "6 a 18 meses*")
]

# Preencher a tabela com os dados dos cursos
for curso in cursos:
    pdf.cell(10, 10, str(curso[0]), 1, 0, 'C')
    pdf.cell(60, 10, curso[1], 1, 0, 'C')
    pdf.cell(40, 10, curso[2], 1, 0, 'C')
    pdf.cell(40, 10, curso[3], 1, 0, 'C')
    pdf.cell(50, 10, curso[4], 1, 0, 'C')
    pdf.cell(40, 10, curso[5], 1, 1, 'C')

# Salvar o PDF em um arquivo
pdf_file_path = 'Tabela_Programa_Especial_Formacao_Docente.pdf'
pdf.output(pdf_file_path)


