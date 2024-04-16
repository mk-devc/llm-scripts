import PyPDF2

def count_tokens(filepath):
  """
  This function takes the filepath of a PDF document and returns the number of tokens (words) in the text.

  Args:
      filepath: A string representing the filepath of the PDF document.

  Returns:
      An integer representing the number of tokens (words) found in the text of the PDF document.
  """
  # Open the PDF document using PyPDF2
  with open(filepath, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Iterate through all pages in the PDF
    num_tokens = 0
    for page_num in range(len(pdf_reader.pages)):
      page = pdf_reader.pages[page_num]

      # Extract text from the page
      page_text = page.extract_text()

      # Split the page text into tokens (words) using whitespace as delimiter
      tokens = page_text.split()
      num_tokens += len(tokens)

  return num_tokens

# Example usage
filepath = "/home/asrix01/Downloads/2311.11045.pdf"  # Replace with the path to your PDF file
number_of_tokens = count_tokens(filepath)

print(f"The PDF document '{filepath}' contains {number_of_tokens} tokens (words).")
