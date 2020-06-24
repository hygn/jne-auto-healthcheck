import pycurl
import sys
from io import BytesIO
from urllib.parse import urlencode
buffer = BytesIO()
school = sys.argv[1]
name = sys.argv[2]
birth = sys.argv[3]
def curl(url, postfields, cookie, posten, cookien, os, browser):
    curl = pycurl.Curl()
    curl.setopt(curl.URL, url)
    if posten:
        curl.setopt(curl.POSTFIELDS, urlencode(postfields))
    else:
        pass
    if cookien:
        curl.setopt(pycurl.COOKIE, cookie)
    else:
        pass
    if os == "windows":
        if browser == "chrome":
            curl.setopt(pycurl.USERAGENT,
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36")
        if browser== "firefox":
            curl.setopt(pycurl.USERAGENT,
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0")
    if os == "linux":
        if browser == "chrome":
            curl.setopt(pycurl.USERAGENT,
                   "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36")
        if browser== "firefox":
            curl.setopt(pycurl.USERAGENT,
                    "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0")
    curl.setopt(pycurl.WRITEDATA, buffer)
    curl.setopt(pycurl.SSL_VERIFYPEER, 0)
    curl.setopt(pycurl.SSL_VERIFYHOST, 0)
    curl.perform()
    curl.close()
    dat = buffer.getvalue().decode('UTF-8')
    return dat
schcode = curl("https://eduro.jne.go.kr/stv_cvd_co00_004.do",{'schulNm' : school}, '', True, False, 'windows', 'chrome').split('"data":{"crtfcScCode":"","schulCode":"')[1].split('","')[0]
postfields = {
    'qstnCrtfcNoEncpt' : '', 
    'rtnRsltCode' : '',     
    'schulCode' : schcode,
    'schulNm' : school,
    'pName' : name,
    'frnoRidno' :  birth,
    'aditCrtfcNo' : ''}
encpt = curl("https://eduro.jne.go.kr/stv_cvd_co00_012.do",postfields, '', True, False, 'windows', 'chrome').split('"method":"selectUsrByStdntInfo","qstnCrtfcNo":"","qstnCrtfcNoEncpt":"')[1].split('","')[0]
postfields = {
    'rtnRsltCode': 'SUCCESS',     
    'qstnCrtfcNoEncpt': encpt,
    'schulNm': '',
    'stdntName': '',    
    'rspns01': '1',
    'rspns02': '1',
    'rspns07': '0',
    'rspns08': '0',
    'rspns09': '0',}
curl("https://eduro.jne.go.kr/stv_cvd_co01_000.do",postfields, '', True, False, 'windows', 'chrome')
postfields = {
    'rtnRsltCode': 'SUCCESS',     
    'qstnCrtfcNoEncpt': encpt,
    'schulNm': school,
    'stdntName': name,    
    'rspns01': '1',
    'rspns02': '1',
    'rspns07': '0',
    'rspns08': '0',
    'rspns09': '0',}
out = curl("https://eduro.jne.go.kr/stv_cvd_co02_000.do",postfields, '', True, False, 'windows', 'chrome').split('<p class="point2" style="text-indent:0px;" role="contentinfo">')[1].split('.')[0].strip()
if out == '코로나19 예방을 위한 자가진단 설문결과 의심 증상에 해당되는 항목이 없어 등교가 가능함을 안내드립니다':
    comp = True
else:
    comp = False
print(school + ',' + schcode + ',' + name + ',' + birth + ',' + encpt + ',' + str(comp))