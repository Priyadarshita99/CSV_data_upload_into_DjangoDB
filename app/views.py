from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
import csv

def insert_bank(request):
    with open('C:\\Users\\Priyadarshita Rout\\Desktop\\Django Project\\Priya\\Scripts\\Project42\\app\\bank.csv','r') as FO:
        IOD=csv.reader(FO)
        for i in IOD:
            bn=i[0].strip()
            BO=Bank(bank_name=bn)
            BO.save()
    return HttpResponse('Bank data has inserted successfully')
        
def insert_branch(request):
    with open('C:\\Users\\Priyadarshita Rout\\Desktop\Django Project\\Priya\\Scripts\\Project42\\app\\branch1.csv','r') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for i in IOD:
            bn=i[0]
            BO=Bank.objects.filter(bank_name=bn)
            if BO:
                ifs=i[1]
                branc=i[2]
                addr=i[3]
                cont=i[4]
                cit=i[5]
                dis=i[6]
                st=i[7]
                BRO=Branch(bank_name=BO[0],ifsc=ifs,branch=branc,address=addr,contact=cont,city=cit,district=dis,state=st)
                BRO.save()
    return HttpResponse('Branch data has inserted successfully')
