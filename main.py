from blackbox import get_data
from date_parser import parse_date
from webhook import sendWebhook
import datetime


enlisted_id = []


def begin():
    global enlisted_id
    try:
        data = get_data()
        for objct in data: 
            try:
                #print(objct['Project'] , objct['Price'] , objct['Sale Date'],objct['Website'] , objct['Discord'],objct['TwitterId'] ,sep=' ')
                #print(objct['date'])
                Sale_date = 'None'
                Presale_date = 'None'
                try:
                    Sale_date = str(parse_date(objct['Sale Date']))
                except:
                    a = 1
                try:
                    Presale_date = str(parse_date(objct['Presale Date']))
                except:
                    b =1 
                current_date = str((datetime.datetime.utcnow() - datetime.timedelta(hours = 5)).date())
               # print(current_date,Sale_date,Presale_date)
                if current_date == Presale_date:
                    if (objct , 'Presale') in enlisted_id:
                        continue
                    enlisted_id.append((objct,'Presale'))
                    print(objct['Project'])
                    try:
                        Project , Price , Website , Discord , Twitter = parse_data(objct)
                        sendWebhook(Project , Price , Website , Discord , Twitter,'Presale')
                    except:
                        print("Error in sending webhook")
                if current_date == Sale_date:
                    if (objct , 'Sale') in enlisted_id:
                        continue
                    enlisted_id.append((objct,'Sale'))
                    print(objct['Project'])
                    #print(objct['Project'] , objct['Price'],objct['Website'] ,objct['Discord'],objct['TwitterId'])
                    try:
                        Project , Price , Website , Discord , Twitter = parse_data(objct)
                        sendWebhook(Project , Price , Website , Discord , Twitter,'Sale')
                    except:
                        print("Error in sending webhook")
                #print(date)
            except:
                print("error caught",objct['id'])
                continue
    except:
        print("Error in fetching rarity data ")


def parse_data(objct):
    Project = 'None'
    Price = 'Free'
    Website = 'None'
    Discord = 'None'
    Twitter = 'None'
    try:
        Project = objct['Project']
    except:
        a = 1
    try:
        Price = objct['Price']
    except:
        a = 1
    try:
        Website = objct['Website']
    except:
        a = 1
    try:
        Discord = objct['Discord']
    except:
        a = 1
    try:
        Twitter = objct['TwitterId']
    except:
        a = 1
    return Project , Price , Website , Discord , Twitter


    

