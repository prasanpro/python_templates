import PyPDF2

def merge_pdfs(pdf1, pdf2, output):
    merger = PyPDF2.PdfMerger()
    
    # Add the first PDF
    merger.append(pdf1)
    
    # Add the second PDF
    merger.append(pdf2)
    
    # Write out the merged PDF
    with open(output, 'wb') as output_file:
        merger.write(output_file)
    
    print(f"Merged PDF saved as {output}")

# Example usage
merge_pdfs('C:/Users/prasa/Documents/', 'C:/Users/prasa/Documents/', 'merged_output.pdf')
