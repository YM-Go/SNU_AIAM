# -*- coding: utf-8 -*-
from alchemyapi import AlchemyAPI
import xlsxwriter
import time


alchemyapi = AlchemyAPI()

print('###AlchemyAPI###')
print('##사용법##')
print('텍스트 분석 종료 : Q')
print('종료시 엑셀 파일이 생성됩니다')
print('##시작##')

while True: #최대 컨셉수를 숫자로만 받자..!!
    input_maxC = input('최대 검색 컨셉수를 정수로 입력하세요 : ')
    if input_maxC.isdigit():
        break

input_url = ''
row_num = 1
title_num = 0 #분석 텍스트 갯수

concept_list=[]
concept_rel=[]
keyword_list=[]
keyword_rel=[]
title = [] #제목


while input_url != 'Q': #Q를 누르면 종료


    #print('{}번째 분석입니다.'.format(title_num+1))
    print('기사들을 세미콜론(;)으로 구분해서 입력해주세요.')
    input_url = input('분석할 기사 주소들을 입력하세요 > ')
    input_url = input_url.split(";") #기사주소들을 세미콜론을 기준으로 나누었음
    if input_url != 'Q':
        response = alchemyapi.concepts('url', input_url,options={'maxRetrieve': input_maxC})

        if response['status'] == 'OK':
            print('##Concepts##') #컨셉
            col_num = 2
            conc_num = 0
            concept_temp = []
            con_rel_temp=[]
            for concept in response['concepts']:
                print('text: ', concept['text'])
                print('relevance : ', concept['relevance'])
                print('')
                concept_temp.append(concept['text'])
                con_rel_temp.append(concept['relevance'])
                """
                concept_list[title_num][conc_num] = concept['text']
                relevance_list[title_num][conc_num]=concept['relevance']
                conc_num += 1
                """


        else:
            print('Error in concept tagging call: ', response['statusInfo'])
            print('다시 시도 하거나 다른 주소를 입력하세요.')

        response2 = alchemyapi.keywords('url', input_url, options={'maxRetrieve': input_maxC})
        if response2['status'] == 'OK':
            print('## Keywords ##')
            keyword_temp = []
            key_rel_temp=[]
            #rel_temp=[]
            for keyword in response2['keywords']:
                print('text: ', keyword['text'])
                print('relevance: ', keyword['relevance'])
                print('')
                keyword_temp.append(keyword['text'])
                key_rel_temp.append(keyword['relevance'])
        else:
            print('Error in keywords call: ', response2['statusInfo'])
            print('다시 시도 하거나 다른 주소를 입력하세요.')

        if 'y' == input('이 결과를 저장하시겠습니까?(y/n)'):
            title_input = input('제목을 입력하세요 : ')
            concept_list.append(concept_temp)
            concept_rel.append(con_rel_temp)
            keyword_list.append(keyword_temp)
            keyword_rel.append(key_rel_temp)

            concept_list[title_num].insert(0,title_num+1)
            concept_list[title_num].insert(1,title_input)

            row_num += 4
            title_num += 1
        else :
            print('저장하지 않습니다')
            continue

    else:
        x = 4
        now = time.localtime()
        s = "%02d%02d%02d"%(now.tm_hour, now.tm_min, now.tm_sec)
        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook('{}.xlsx'.format(s))
        worksheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True,'fg_color': 'yellow'})
        worksheet.merge_range('A1:A4', 'No.', cell_format)
        worksheet.merge_range('B1:B4', 'title', cell_format)
        for i in range(int(input_maxC)):
            col_form = 2
            worksheet.write(0,col_form + i,'concept',cell_format)
            worksheet.write(1,col_form + i,'relevance',cell_format)
            worksheet.write(2,col_form + i,'keyword', cell_format)
            worksheet.write(3,col_form + i,'relevance', cell_format)

        for i in range(title_num):
            worksheet.write_row(i+x,0,concept_list[i])
            worksheet.write_row(i+x+1,2,concept_rel[i])
            worksheet.write_row(i+x+2,2,keyword_list[i])
            worksheet.write_row(i+x+3,2,keyword_rel[i])
            x += 4
        print('엑셀 파일을 생성하고 프로그램을 종료합니다.')
        workbook.close()
