import document, openpyxl

def replace_text_in_docx(filename, output_filename, replacements):
    # Open docx file
    doc = document.Document(filename)

    # Loop throuh each paragraph in the docx file
    for p in doc.paragraphs:
        for run in p.runs:
            for key in replacements:
            # If the key appears in the text, replace it with the value
                if key in run.text:
                    print(f"Replacing '{run.text}' ...")
                    # Replacing text at the paragraph level often loses formatting
                    run.text = run.text.replace(key, replacements[key])
                    print(f"Replaced '{key}' with '{replacements[key]}'")
    
    # You also need to check tables, headers, and footers separately
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    for run in p.runs:
                        for key in replacements:
                            if key in run.text:
                                run.text = run.text.replace(key, replacements[key])
                                print(f"Replaced '{key}' with '{replacements[key]}'")

    doc.save(output_filename)
    print(f"Document saved as {output_filename} using python-docx-replace.")



# Replace words in xlsx files
def replace_text_in_excel(source_file, target_file, replacements):
    """
    Opens an Excel file, finds and replaces text, and saves it to a new file.
    
    Args:
        source_file (str): The path to the original .xlsx file.
        target_file (str): The path where the modified .xlsx file will be saved.
        find_string (str): The text to search for.
        replace_string (str): The text to replace with.
    """
    # Load the workbook
    try:
        wb = openpyxl.load_workbook(source_file)
    except FileNotFoundError:
        print(f"Error: {source_file} not found.")
        return

    # Iterate through all sheets
    for sheet in wb.worksheets:
        print(f"Processing worksheet: {sheet}")
        for row in sheet.iter_rows():
            for cell in row:
                if cell.value and isinstance(cell.value, str):
                    # Perform all replacements on the cell value
                    for old_text, new_text in replacements.items():
                        if old_text in cell.value:
                            cell.value = cell.value.replace(old_text, new_text)
                            print(f"Replaced '{old_text}' with '{new_text}' in cell {cell.coordinate} (value: {cell.value})")
                        if old_text in sheet.title:
                            new_name = sheet.title.replace(old_text, new_text)
                            sheet.title = new_name
                            print(sheet.title)

    # Save the modified file
    wb.save(target_file)
    print(f"\nReplacement complete. File saved as {target_file}")


