from object import Document

# Open docx file
doc = Document("class documents/enrollment.docx")
tables = doc.tables

full_text = []
for paragraph in doc.paragraphs:
    full_text.append(paragraph.text)
    print(paragraph.text)

for table_index, table in enumerate(tables):
    print(f"Table {table_index + 1}:")
    for row_index, row in enumerate(table.rows):
        row_data = [cell.text for cell in row.cells]
        print(row_data)
