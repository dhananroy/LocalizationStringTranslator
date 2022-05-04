from googletrans import Translator
from bs4 import BeautifulSoup

values_list = ['values', 'values-ro', 'values-te', 'values-ru', 'values-tl', 'values-oc', 'values-it', 'values-ca',
               'values-cs', 'values-ia', 'values-in', 'values-ja', 'values-el', 'values-lv', 'values-da', 'values-mr',
               'values-gu', 'values-he', 'values-ms', 'values-hy', 'values-be', 'values-sc', 'values-pl', 'values-vi',
               'values-sq', 'values-sv', 'values-sl', 'values-sk', 'values-ur', 'values-sw', 'values-tr', 'values-ta',
               'values-th', 'values-fa', 'values-lt', 'values-or', 'values-eu', 'values-jv', 'values-la', 'values-iw',
               'values-fi', 'values-eo', 'values-fr', 'values-es', 'values-et', 'values-hr', 'values-hu', 'values-nl',
               'values-bg', 'values-ks', 'values-bn', 'values-ne', 'values-af', 'values-hi', 'values-de', 'values-az',
               'values-ko', 'values-ml', 'values-ku', 'values-mk', 'values-bs', 'values-ar', 'values-gl', 'values-pt',
               'values-uk', 'values-sr', 'values-pa', 'values-si', 'values-so']
input_text = input("Enter Text: ")
input_var = input("Enter String Var Name: ")
res = input("Enter res Path: ")
final_list = []


def get_translator(q, cinto):
    translator = Translator()
    text = translator.translate(str(q), src='en', dest=str(cinto))
    return text.text


for val in values_list:
    try:
        slist = val.split("-")
        if len(slist) > 1:
            print("Translating in: ", slist[-1])
            fianl_text = get_translator(input_text, slist[-1])
        else:
            fianl_text = input_text
        final_list.append([val, fianl_text])
    except:
        continue

for dt in final_list:
    print("Writing Data -- {}".format(dt))
    dir_name = '{}/{}/strings.xml'.format(res, dt[0])
    values = '<string name="{}">{}</string>\n\n'.format(input_var, dt[1])
    with open(dir_name, 'r') as f:
        data = f.read()
    data = BeautifulSoup(data.replace("</resources>", values), "xml")
    fw = open(dir_name, "w")
    fw.write(str(data))
    fw.close()
