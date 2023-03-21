
import io
from PyPDF2 import PdfReader, PdfWriter
import streamlit as st

def extract_text_from_pdf(file):
    if file is not None and file.size > 0:
        pdf_reader = PdfReader(io.BytesIO(file.read()))
        num_pages = len(pdf_reader.pages)
        text = ''
        for page in range(num_pages):
            page_obj = pdf_reader.pages[page]
            text += page_obj.extract_text()
        return text
    else:
        return ''

def main():
    # Prompt user to upload up to 10 PDF files
    st.write("For uploading Real Text PDFs only")
    st.write(" ")
    st.write("For scanned images PDFs, need to convert PDF to Image & Image to text first to be readable PDFs")
    st.write("Upload up to 3 Real texts PDF files to combine:")
    
    files = []
    for i in range(3):
        file = st.file_uploader(f"PDF file {i+1}", type="pdf", key=f"pdf_upload{i}")
        if file:
            files.append(file)
    
    if not files:
        st.warning("Please upload one or more PDF files to continue.")
    else:
        texts = []
        for file in files:
            text = extract_text_from_pdf(file)
            if text:
                texts.append(text)

        combined_text = '\n\n'.join(texts)

        st.write("Combined text:")
        st.write(combined_text)

        output_bytes = io.BytesIO()
        writer = PdfWriter()
        for file in files:
            if file is not None and file.size > 0:
                reader = PdfReader(io.BytesIO(file.read()))
                for page in reader.pages:
                    writer.add_page(page)
        writer.write(output_bytes)
        output_bytes.seek(0)
        
        st.download_button(
            label="Download combined PDF",
            data=output_bytes,
            file_name="combined.pdf",
            mime="application/pdf"
        )

if __name__ == "__main__":
    main()
