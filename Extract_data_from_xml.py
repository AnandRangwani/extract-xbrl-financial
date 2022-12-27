import scipy.stats as stats
import xml.etree.ElementTree as ET
import datetime as dt
import pandas as pd
import re

file_path = ("D:\Learning\extract-xbrl-financial\AmbujaCement_INDAS_790050_4966_22102022125650_WEB.xml")
tree = ET.parse(file_path)
root = tree.getroot()

for x in root:
    
    x.tag = re.sub("{http://www.bseindia.com/xbrl/fin/2020-03-31/in-bse-fin}","",str(x.tag))
    cols = x.tag
    data = x.text
    
    print(cols)
    print(data)
    # col = x.tag
    # print(col)
    
   
    # datas = x.text
    # print(data)
    
    

    



    #     newx = x.replace("{http://www.bseindia.com/xbrl/fin/2019-09-30/in-bse-fin}","")
    # except AttributeError:
    #     pass
    #     print(newx)

# replace_bse_text = ("{http://www.bseindia.com/xbrl/fin/2019-09-30/in-bse-fin}","")

# for old, replace in replace_bse_text:
#     newx = re.sub(old, replace, root.findall(), flags=re.IGNORECASE)
#     print(newx)
    

# # # for x in root.findall("{http://www.bseindia.com/xbrl/fin/2019-09-30/in-bse-fin}"):
# # #     print(x.tag)
