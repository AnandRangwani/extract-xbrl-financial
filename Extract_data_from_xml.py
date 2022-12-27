import scipy.stats as stats
import xml.etree.ElementTree as ET
import datetime as dt
import pandas as pd
import re

file_path = ("E:\python_project\schemas\AdaniPorts1_INDAS_828228_5538_01112022194338_WEB.xml")
tree = ET.parse(file_path)
root = tree.getroot()

for x in root:
    #print(x.tag)
    x.tag = re.sub("{http://www.bseindia.com/xbrl/fin/2019-09-30/in-bse-fin}","",str(x.tag))

    tags = [x.tag]
    data = [x.text]
    #print(tags)
    #print(data)
    df = pd.DataFrame()
    df = df.reindex(columns = tags)
    df2 =  pd.DataFrame(data)
    df4 = pd.concat([df,df2], ignore_index=False)
    print(df4)

    #df.to_excel("output1.xlsx")
    
    



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
