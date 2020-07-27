import cv2
import pytesseract
import pdf2image as pdf
from PIL import Image
import requests
from io import BytesIO

from pdf2image.exceptions import (
PDFInfoNotInstalledError,
PDFPageCountError,
PDFSyntaxError
)

pytesseract.pytesseract.tesseract_cmd = 'E:\\tesseract\\installed_file\\tesseract.exe'

class img_prosessing():
    #convert pdf to images_____________________________________________--__________________--
    def pdf_img(file_path,img_name):
        file_path = file_path

        images = pdf.convert_from_path(file_path, 500,
                                       poppler_path=r'E:\poppler\poppler-0.68.0_x86 (1)\poppler-0.68.0\bin')

        image_count=0
        image_path_list=[]
        for image in images:
            image_name = img_name + str(image_count) + ".jpeg"
            image.save(image_name, 'JPEG')
            image_pa='C:/Users/ninjaac/PycharmProjects/Image_to_text/venv/'
            image_path=image_pa+image_name
            image_path_list.append(image_path)
        return image_path_list
    def find_template(image_paths,template_path):
        image = cv2.imread(image_paths, 0)

        template=cv2.imread(template_path,0)

        w, h = template.shape[::-1]

        method='cv2.TM_CCOEFF_NORMED'
        method = eval(method)

        # Apply template Matching
        res = cv2.matchTemplate(image, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        #defien the top left for method
        top_left =max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        print(top_left,bottom_right)
        #rectangle(image,start_point,end_point,color,thickness)
        cv2.rectangle(image, top_left, bottom_right, (255,0,0), 2)
        #image resize to fix the screen
        res_s=cv2.resize(res,(600,600))
        cv2.imshow('image result',res_s)
        image_s=cv2.resize(image,(600,600))
        cv2.imshow('image',image_s)
        cv2.waitKey()


    def img_text_pan(img_path):
        #pyteseract location defenotion
        pytesseract.pytesseract.tesseract_cmd = 'E:\\tesseract\\installed_file\\tesseract.exe'
        response=requests.get(img_path)
        img = Image.open(BytesIO(response.content))
        text = pytesseract.image_to_string(img)
        text_count = 1
        text_file = "text" + str(text_count) + ".txt"
        with open(text_file, 'w+') as f:
            f.writelines(text)
            text_count += 1
        file=open(text_file,'r')
        line_count_list=[9,10,11,12,]
        dic=dict()
        for line_count,line in enumerate(file):
            if line_count in line_count_list:
                a=line.split()
                dic[a[0]]=a[1:]
        return dic
    def img_to_text_aadhar(image_path):
        response=requests.get(image_path)
        img = Image.open(BytesIO(response.content))
        text = pytesseract.image_to_string(img)
        print(text)
        text_count = 1
        text_file = "text" + str(text_count) + ".txt"
        with open(text_file, 'w+') as f:
            f.writelines(text)
            text_count += 1
        file=open(text_file,'r')
        line_count_list=[9,]
        dic=dict()
        for line_count,line in enumerate(file):
            if line_count in line_count_list:
                a=line.split()
                dic['aadhar_no']=a
        return dic
    def text_number(list):
        zum_dict = {'ZERO': 0, '(ONE': 1, 'TWO': 2, 'THREE': 3, 'FOUR': 4, 'FIVE': 5, 'SIX': 6, 'SEVEN': 7, 'EIGHT': 8,
                    'NINE': 9}
        mark = ''
        for n in list:
            for text, value in zip(zum_dict, zum_dict.values()):
                if n == text:
                    mark += str(value)
        return (int(mark) / 1200) * 100
    def img_to_text_tweth_mark(image_path):
        response=requests.get(image_path)
        img = Image.open(BytesIO(response.content))
        text = pytesseract.image_to_string(img)
        text_count = 1
        text_file = "text" + str(text_count) + ".txt"
        with open(text_file, 'w+') as f:
            f.writelines(text)
            text_count += 1
        file=open(text_file,'r')
        line_count_list=[15,49,53,55]
        dic=dict()
        for line_count,line in enumerate(file):
            #print(line_count,line)
            if line_count==15:
                a=line.split()
                b=a[-3::-1]
                dic['name']=b[::-1]
                dic['dateOfExam']=a[-2:]
            if line_count==49:
                a=line.split()

                percentage=img_prosessing.text_number(a[6:])
                dic['percentage'] = percentage
            if(line_count==53):
                a = line.split()
                dic['regno']=a[0]
                dic['medium']=a[1]
            if(line_count==55):
                dic['school_name']=line
        return dic

image_path= 'https://i.postimg.cc/1XwrWSKw/aadhar.png'
print(img_prosessing.img_to_text_aadhar(image_path))
