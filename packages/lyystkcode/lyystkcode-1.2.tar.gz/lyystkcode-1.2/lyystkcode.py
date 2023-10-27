import re


def 提取网址(full_text, debug=False):
    pattern = re.compile(r'http[s]?://[\w-]+(?:\.[\w-]+)+[\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-]')

    #pattern = re.compile(r'http://[^s]*\.pdf')
    result = re.findall(pattern, full_text)
    url = result[0]

    # 去除前后的标点符号
    url = url.strip('\'"<>')
    if debug: print("提取网址结果=" + result[0])
    return result[0]

if __name__ == '__main__':
    t = '"http://43.132.151.196:9993/down.php/f846e67d6ef725ec2a087405abde6b62.pdf"'

    print(提取网址(t))




