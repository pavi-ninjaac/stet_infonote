from image_processing import img_prosessing
import cv2
from PIL import Image
import requests
from io import BytesIO
class fetch_mangidb_data():
    def fetch_data():
        from pymongo import MongoClient

        client= MongoClient('mongodb+srv://web-client:yjpMsZ7WgH2eueA@default.droi9.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority')

        #db=client.get_database('stet')
        #records=db.applications
        #record=list(records.find())
        record=[{ 'name': 'Krishna Moorthy', 'fatherName': 'Athinarayanan', 'motherName': 'Mariammal', 'sex': 'Male', 'nationality': 'Indian', 'mobileNumber': 9677068234.0, 'email': 'akrishnamoorthy007@gmail.com', 'permanentAddress': 'this is an address', 'aadhaarNo': 5432198765012.0, 'voterId': 'KR89TQ672', 'motherTongue': 'Tamil', 'identificationMarks': 'Mole in back', 'maxQualification': 'B.E CSE', 'SSLC': {'institute': 'SRMHSS', 'percentage': 96, }, 'HSC': {'institute': 'SRMHSS', 'percentage': 94, }, 'college': {'degree': 'B.E', 'department': 'CSE', 'institute': 'UCE, Trichy', 'university': 'Anna University', 'percentage': 76,}, 'documents': {'aadhaar': 'https://i.postimg.cc/3Rpm45wz/in-gov-uidai-ADHAR-2549ca8f1a4fdfde9c2126572edad6e0.png', 'voter': 'voter', 'SSLC': 'SSLC', 'HSC': 'https://i.postimg.cc/rFqxmH2Y/in-nic-tn-dgecert-HSCER-1710243086.png', 'deg': 'degree', 'photo': 'photo', 'signature': 'sign', 'pan': 'https://i.postimg.cc/vHyLnBfh/in-gov-pan-PANCR-GJEPD1150-D.png'},  '__v': 0}]
        feature_name=['name','fatherName','motherName','sex','nationality','mobileNumber','email','permanentAddress','aadhaarNo', 'voterId','motherTongue','identificationMarks','HSC', 'college',]
        #print(record)
        #__________________________---collect required data
        #_________________________colect the documents
        documents=record[0]['documents']
        #print(documents)
        pan_card=documents['pan']
        pan_text=img_prosessing.img_text_pan(pan_card)
        #print(pan_text)
        aadhar_card='https://i.postimg.cc/1XwrWSKw/aadhar.png'
        aadhar_text=img_prosessing.img_to_text_aadhar(aadhar_card)
        #print(aadhar_text)
        twelth_mark=documents['HSC']
        twelth_mark_text=img_prosessing.img_to_text_tweth_mark(twelth_mark)
        #print(twelth_mark_text)
        document_dict={'pan_card':pan_text,'aadhar_card':aadhar_text,'tweth_markSheet':twelth_mark_text}
        return document_dict,record
        #print("the number of documnets precent in collections {}".format( records.count_documents({})))
        #print(record[0]['SSLC']['institute'])
#document_dict,records_dict=fetch_mangidb_data.fetch_data()
#print(document_dict,records_dict)

    def insert_mangodb(name,mailid,valid=True,reg_no=[22202001]):
        from pymongo import MongoClient
        client = MongoClient(
            'mongodb+srv://web-client:yjpMsZ7WgH2eueA@default.droi9.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority')
        db=client.get_database('stet')
        records=db.valid
        print(records.count_documents({}))
        reg_no=reg_no[0]

        new_record={
            'valid':valid,
            'Reg_no':reg_no,
            'mailid':mailid,
            'name':name,
        }
        records.insert_one(new_record)
        print(records.count_documents({}))
        return reg_no

#print(fetch_mangidb_data.insert_mangodb('pavi','pavi@gmail.com'))
