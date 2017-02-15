# -*- coding: utf-8 -*-
from alchemyapi import AlchemyAPI
import xlsxwriter #엑셀로 output하기 위해 xlsxwriter 모듈을 설치하세요
import time #엑셀 이름을 현재 시간으로 저장하기 위해 사용한 모듈입니다


alchemyapi = AlchemyAPI()

print('###AlchemyAPI###')
print('##사용법##')
print('텍스트 분석 종료 : Q')
print('종료시 엑셀 파일이 생성됩니다')
print('##시작##')

while True:
    input_maxC = input('최대 검색 컨셉수를 정수로 입력하세요 : ')
    if input_maxC.isdigit(): #최대 컨셉 수를 숫자로만 받을 것입니다
        break

input_url = ''
title_num = 0 #분석 텍스트 갯수

title = [] #제목

now = time.localtime()
s = "%02d%02d%02d"%(now.tm_hour, now.tm_min, now.tm_sec) #현재시간으로 제목을 만듭니다.
workbook = xlsxwriter.Workbook('{}.xlsx'.format(s)) #엑셀 시트를 생성합니다
worksheet = workbook.add_worksheet()


while input_url != 'Q': #Q를 누르면 종료
    row_num = 0

    print('기사들을 세미콜론(;)으로 구분해서 입력해주세요.')
    input_url = input('분석할 기사 주소들을 입력(종료는 Q) > ')

    if input_url != 'Q':
        input_url = input_url.split(";") #기사주소들을 세미콜론을 기준으로 나누었음, 아무것도 넣지 않으면 스페이스를 기준으로 나눠집니다.
        url_num = 1
        for myurl in input_url:
            concept_list=[]
            keyword_list=[]

            #alchemyapi에서 url로 콜 한 뒤 결과를 받아옵니다.
            response = alchemyapi.concepts('url', myurl,options={'maxRetrieve': input_maxC})

            worksheet.write(row_num,0,'concept')
            worksheet.write(row_num + 1,0,'keyword')

            if response['status'] == 'OK':
                i = 0
                print('##Concepts##') #컨셉
                for concept in response['concepts']:
                    print('text: ', concept['text'])
                    #print('relevance : ', concept['relevance']) #relevance도 받아올 수 있습니다.
                    print('')

                    concept_list.append(concept['text']) #엑셀에 입력할 변수에 문자열을 추가합니다
                    i += 1

            else:
                print('Error in concept tagging call: ', response['statusInfo'])
                print('다시 시도 하거나 다른 주소를 입력하세요.')

            response2 = alchemyapi.keywords('url', myurl, options={'maxRetrieve': input_maxC})
            if response2['status'] == 'OK':
                print('## Keywords ##')
                i = 0

                for keyword in response2['keywords']:
                    print('text: ', keyword['text'])
                    #print('relevance: ', keyword['relevance'])
                    print('')

                    keyword_list.append(keyword['text'])
                    i +=1

            else:
                print('Error in keywords call: ', response2['statusInfo'])
                print('다시 시도 하거나 다른 주소를 입력하세요.')

            #출력된 결과들을 엑셀에 씁니다
            worksheet.write_row(row_num,1,concept_list)
            worksheet.write_row(row_num+1,1,keyword_list)
            row_num += 2
            url_num +=1
            title_num += 1

    else:
        print('엑셀 파일을 생성하고 프로그램을 종료합니다.')
        workbook.close()
