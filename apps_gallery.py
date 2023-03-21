
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Apps Gallery", page_icon=":guardsman:", layout="wide")
st.title("Apps Gallery")
st.write("Here are some of the apps:")
st.write("Code links:")
st.write('https://github.com/ProjectGroupInfo/apps_gallery/blob/main/README.md/')

col1, col2, col3, col4, col5 = st.columns(5)

# URLs of the images in the GitHub repository
img1_url = "https://github.com/ProjectGroupInfo/apps_gallery/blob/main/img/img1.jpg?raw=true"
img2_url = "https://github.com/ProjectGroupInfo/apps_gallery/blob/main/img/img2.jpg?raw=true"
img3_url = "https://github.com/ProjectGroupInfo/apps_gallery/blob/main/img/img3.jpg?raw=true"
img4_url = "https://github.com/ProjectGroupInfo/apps_gallery/blob/main/img/img4.jpg?raw=true"
img5_url = "https://github.com/ProjectGroupInfo/apps_gallery/blob/main/img/img5.jpg?raw=true"

# Display the images and create clickable links
with col1:
    st.markdown(f'[![PDF to Image converter]({img1_url})](https://projectgroupinfo-apps-gallery-pdf-to-imgpdf2img-swzak6.streamlit.app/)')
    st.write("PDF to Image converter")
    st.markdown('[Go to App →](https://projectgroupinfo-apps-gallery-pdf-to-imgpdf2img-swzak6.streamlit.app/)')
    st.markdown('[View source code →](https://github.com/ProjectGroupInfo/apps_gallery/tree/main/pdf_to_img)')
    
with col2:
    st.markdown(f'[![Image to Text converter]({img2_url})](https://projectgroupinfo-apps-gallery-image-to-textimg2text-x340a3.streamlit.app/)')
    st.write("Image to text converter")
    st.markdown('[Go to App →](https://projectgroupinfo-apps-gallery-image-to-textimg2text-x340a3.streamlit.app/)')
    st.markdown('[View source code →](https://github.com/ProjectGroupInfo/apps_gallery/tree/main/image_to_text)')

with col3:    
    st.markdown(f'[![PDF Summarizer]({img3_url})](https://projectgroupinfo-apps-gallery-pdf-summarypdf-summary-btwsj3.streamlit.app/)')
    st.write("PDF Summarizer")
    st.markdown('[Go to App →](https://projectgroupinfo-apps-gallery-pdf-summarypdf-summary-btwsj3.streamlit.app/)')
    st.markdown('[View source code →](https://github.com/ProjectGroupInfo/apps_gallery/tree/main/pdf_summary)')    
    
with col4:    
    st.markdown(f'[![Question Answering App]({img4_url})](https://projectgroupinfo-apps-gallery-qnaqa-gpt-urpko3.streamlit.app/)')
    st.write("Question Answering App")
    st.markdown('[Go to App →](https://projectgroupinfo-apps-gallery-qnaqa-gpt-urpko3.streamlit.app/)')
    st.markdown('[View source code →](https://github.com/ProjectGroupInfo/apps_gallery/tree/main/QnA)')            

with col5:
    st.markdown(f'[![PDF Combiners]({img5_url})](https://projectgroupinfo-apps-gallery-combine-pdfscombine-pdf-7fou56.streamlit.app/)')
    st.write("PDF combiners")
    st.markdown('[Go to App →](https://projectgroupinfo-apps-gallery-combine-pdfscombine-pdf-7fou56.streamlit.app/)')
    st.markdown('[View source code →](https://github.com/ProjectGroupInfo/apps_gallery/tree/main/combine_pdfs)')
    
#FOR FUTURE APPS       
col6, col7, col8, col9, col10 = st.columns(5)

# URLs of the images in the GitHub repository
img6_url = "https://github.com/ProjectGroupInfo/apps_gallery/blob/main/img/img6.jpg?raw=true"
img7_url = "https://github.com/ProjectGroupInfo/apps_gallery/blob/main/img/img7.jpg?raw=true"
img8_url = "https://github.com/ProjectGroupInfo/apps_gallery/blob/main/img/img8.jpg?raw=true"
img9_url = "https://github.com/ProjectGroupInfo/apps_gallery/blob/main/img/img9.jpg?raw=true"
img10_url = "https://github.com/ProjectGroupInfo/apps_gallery/blob/main/img/img10.jpg?raw=true"

# Display the images and create clickable links
with col6:
    st.write("Speech to text converter")
    
with col7:
    st.write("Extract Data from PDF")

with col8:    
    st.write("Settlement Predictor App")
    
with col9:    
    st.write("Future App")

with col10:
    st.write("Other App")
