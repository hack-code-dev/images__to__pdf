from fpdf import FPDF
import os
from PIL import Image


extension=['jpg','png']
list_image_file=[]
def image_list_file():
    imagelist=os.listdir(".//bin//")
    for key in imagelist:
        if(key.endswith(tuple(extension))):
            list_image_file.append(key)
    return list_image_file

def create_images_pdf():
    margin=0
    watermark='@Author:Srinivas_chinthapalli'
    t=round(100/len(list_image_file))
    pdf=FPDF('P','mm','A4')
    
    for index,key in enumerate(list_image_file):
        cover=Image.open(".//bin//"+key)
        width,height=cover.size
        w=int(pdf.w)
        h=int(pdf.h)
        width, height = float(width * 0.264583), float(height * 0.264583)
        pdf.add_page()
        if(width>w):
            width=w-width/10
        if(height>h):
            height=h-height/10
        pdf.image(".//bin//"+key,(pdf.w-width)/2,(pdf.h-height)/2,width,height)
        
        pdf.set_font('Arial', 'B', 13)

        pdf.cell(0,0,watermark)
        if(t*(index+1)>100):
            print(end="\r%d%%"%(100))
        else:    
            print(end="\r%d%%"%(t*(index+1)))
        
    pdf.output('.//pdf//image_pdf.pdf','F')
    
    print("complete...")


def check_size():
    pass

image_list_file()
create_images_pdf()

from threading import Thread
if __name__ == '__main__':
    try:
        
      pass
    except :
        pass
