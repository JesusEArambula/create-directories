import docx

def replace_text(filename, output_filename, replacements):
    # Open docx file
    doc = docx.Document(filename)

    # Loop throuh each paragraph in the docx file
    for p in doc.paragraphs:
        for key in replacements:
        # If the key appears in the text, replace it with the value
            if key in p.text:
                # Replacing text at the paragraph level often loses formatting
                p.text = p.text.replace(key, replacements[key])
                print(f"Replaced '{key}' with '{replacements[key]}'")
    
    # You also need to check tables, headers, and footers separately
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    for key in replacements:
                        if key in p.text:
                            p.text = p.text.replace(key, replacements[key])
                            print(f"Replaced '{key}' with '{replacements[key]}'")

    doc.save(output_filename)
    print(f"Document saved as {output_filename} using python-docx-replace.")

replace_text("(#20 SPANISH) Mon, Wed March 2026 Workshop 360 Valencia/Class Documents/Cohort #20 Enrollment Form.docx", "(#20 SPANISH) Mon, Wed March 2026 Workshop 360 Valencia/Class Documents/Cohort #20 Enrollment Form.docx", {"{Day1}": "Lunes", "{Day2}": "Miercoles"})


my_dict = {1: "Mon Wed", 2: "Tue Thu"}

print(my_dict[1].split()[0])
