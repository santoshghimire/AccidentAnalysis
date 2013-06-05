import lxml.html
from lxml import etree     
from cStringIO import StringIO
import urllib
import os

def map_number(given_string):
    new_date =""
    preeti = "!@#$%^&*()M"
    num = "1234567890:"
    for s in given_string:
        new_char = s
        try:
            pos = preeti.index(s)
            new_char = num[pos]
        except:
            pass
        new_date+= new_char
    return new_date


APP_ROOT = os.path.realpath('.')
def accident_records():
    print "reached"
    all_accidents =[]
    for file_name in range(29):
        file_name = APP_ROOT+"/accidentApp"+"/try/"+str(file_name)+".html"
        print file_name
        try:
            html = urllib.urlopen(file_name)
        except:
            continue
        html = html.read()
        i =1

        while True:
            if i ==1:
                my_iter = 1
                my_iter2 = 3
            else:
                my_iter = 0
                my_iter2 = 0
            root1 = lxml.html.fromstring(html)
            try:
                main_content = root1.cssselect('div#pf'+str(i))
                i += 1

            except:
                break
            print main_content
            if main_content == []:
                break


            node = main_content[0]
            try:
                content_date = node.cssselect('div.x4')[my_iter:]
                content_time = node.cssselect('div.x4 div.t')[my_iter:]
                content_location = node.cssselect('div.x4 div.t')[my_iter:]
                
                death_1 = node.cssselect('div.x12')[my_iter2:]
                death_2 = node.cssselect('div.x1d')[my_iter:]
                death_3 = node.cssselect('div.x1e')[my_iter:]
                death_4 = node.cssselect('div.x1f')[my_iter:]    

                injury_1 = node.cssselect('div.x13')[my_iter2:]
                injury_2 = node.cssselect('div.x20')[my_iter:]
                injury_3 = node.cssselect('div.x21')[my_iter:]
                injury_4 = node.cssselect('div.x22')[my_iter:]

                injury2_1 = node.cssselect('div.x14')[my_iter2:]
                injury2_2 = node.cssselect('div.x23')[my_iter:]
                injury2_3 = node.cssselect('div.x24')[my_iter:]
                injury2_4 = node.cssselect('div.x25')[my_iter:]
                
                vehicle_1 = node.cssselect('div.x15')
                vehicle_2 = node.cssselect('div.x26')
                vehicle_3 = node.cssselect('div.x27')
                vehicle_4 = node.cssselect('div.x28')
                vehicle_5 = node.cssselect('div.x29')
                vehicle_6 = node.cssselect('div.x2a')
                vehicle_7 = node.cssselect('div.x2b')
                vehicle_8 = node.cssselect('div.x2c')
                
                vehicle_damaged = node.cssselect('div.x18')[1:]
                rows = zip(content_date, content_time, content_location,
                        death_1, death_2, death_3, death_4,
                        injury_1, injury_2, injury_3, injury_4,
                        injury2_1, injury2_2, injury2_3, injury2_4,
                        vehicle_1, vehicle_2, vehicle_3, vehicle_4, vehicle_5,
                        vehicle_6, vehicle_7, vehicle_8, vehicle_damaged)
                
            except:
                pass

            for item in rows:
                try:
                    print "------------------------------"
                    accident = {}
                    my_date =  map_number(item[0].cssselect("div.t")[0].text_content().split()[0])
                    print my_date
                    accident["year"] = my_date.split(".")[0]
                    accident["month"] = my_date.split(".")[1]
                    accident["day"] = my_date.split(".")[2]
                    

                    time =  map_number(item[0].cssselect("div.t")[1].text_content().split()[0])
                    accident ["hour"] = time.split(":")[0]
                    accident["minute"] = time.split(":")[1]

                    accident["location"] =  item[0].cssselect("div.t")[2].text_content().strip()
                    death = 0
                    for each_death in item[3:7]:
                        death+= int(each_death.text_content().strip() or 0)
                    
                    injury = 0
                    for each_injury in item[7:15]:
                        injury+= int(each_injury.text_content().strip() or 0)
                    accident["death"] = death
                    accident ["injury"] = injury
                    accident ["vehicle_damaged"] = int(item[-1].text_content().strip() or 0)
                    
                    all_accidents.append(accident)
                    #print all_accidents
                except:
                    pass
    print all_accidents
    return all_accidents