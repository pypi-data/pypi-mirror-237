
import re
from datetime import datetime
import pandas as pd

def format_ocr_text(text):
    symbols = ['1、', '2、', '3、', '4、', '5、', '6、', '7、', '8、', '9、', '10、', '11、', '12、', '一、', '二、', '三、']
    pattern = '|'.join(re.escape(symbol) for symbol in symbols)
    paragraphs = re.split('(' + pattern + ')', text)
    formatted_text = ''
    indent = False
    for i, paragraph in enumerate(paragraphs):
        if paragraph.strip() != '':
            formatted_paragraph = paragraph.strip()
            if formatted_paragraph.startswith(('一、', '二、', '三、')):
                if formatted_text and formatted_text[-1] != '\n':
                    formatted_text += '\n'
                formatted_text += formatted_paragraph + '\n'
                indent = False
            elif formatted_paragraph.startswith(('1、', '2、', '3、', '4、', '5、', '6、', '7、', '8、', '9、', '10、', '11、', '12、')):
                if formatted_text and formatted_text[-1] != '\n':
                    formatted_text += '\n'
                formatted_text += '  ' + formatted_paragraph + '\n'
                indent = True
            else:
                if not indent:
                    formatted_paragraph = '  ' + formatted_paragraph
                    indent = True
                formatted_text += formatted_paragraph + '\n'
    return formatted_text


def 提取url(full_text, debug=False):
    pattern = re.compile(r'http[s]?://[\w-]+(?:\.[\w-]+)+[\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-]')

    #pattern = re.compile(r'http://[^s]*\.pdf')
    result = re.findall(pattern, full_text)
    url = result[0]

    # 去除前后的标点符号
    url = url.strip('\'"<>')
    if debug: print("提取url结果=" + result[0])
    return result[0]


def extract_info_from_df(df):
    today_date = datetime.now().strftime("%Y-%m-%d")
    msg_dic = {}
    dict_list = []
    for index, row in df.iterrows():
        row_dict = {}
        for column in df.columns:
            row_dict[column] = row[column]
            row_dict['time'] = pd.to_datetime(row['time'], unit='ms').strftime('%Y-%m-%d %H:%M:%S').replace(today_date + " ", "")  #如果是今天就不需要显示日期，所以把年，同后面的空格替换成短时间。
        dict_list.append(row_dict)
    return dict_list

if __name__ == '__main__':
    # exit()
    log("testest")
