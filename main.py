from jira.client import JIRA
import re

created_GTOPS=[]
description_GTOPS=[]
line_clear=[]
comment_created=[[]]
comment_body=[[]]
i = 0

login_name = 0
login_pass = 0

jira_options = {'server': 'https://sd.v-serv.ru/jira'} # эту строку оставлсять
jira = JIRA(options=jira_options, basic_auth=(login_name, login_pass)) # логин и пароль от аккуанта JIRA

#поиск тикетов по jql запросу
jql = 'project = GTOPS AND created >= 2024-01-01 AND issuetype = "ГТ ЗНИ" AND status in (Закрыт, Выполнен, "Подтвержден инициатором") ORDER BY key DESC, description ASC, status DESC'
#issues_list = str(jira.search_issues(jql, maxResults=1000))


'''# Кол-во заявок в запросе
issues = jira.search_issues(jql, maxResults=0) # поиск всех тикетов по условию jql
print('Total incidents found:', len(issues)) # подсчет кол-ва тикетов
amount_GTOPS = len(issues)

issues_list_gtops = re.findall(r'GTOPS-\d+', str(jira.search_issues(jql, maxResults=0))) # регулярное выражение для получение конструции: GTOPS-****
file_amount_GTOPS = open('file_amount_GTOPS.csv', 'w') # файл для записи номером тикетов
for result in issues_list_gtops:
    i += 1
    print(str(i) + ". " + result) # вывод номеров тикетов
    file_amount_GTOPS.write(result) # запись этих номер в файл
file_amount_GTOPS.close()
'''

#Код по обработке комментариев
GTOPS_file = 'file_amount_GTOPS.txt'
#file_comments_GTOPS = open('file_comments_GTOPS.txt', 'w')

with open(GTOPS_file, 'r') as file:
    for line in file:

        line_clear.append( line.strip()) # удаление лишних пробелом и энтеров из строки
        issue = jira.issue(line_clear[i]) # поиск тикета в Jira
        tmp = issue.fields.comment.comments # получение всех комментариев из тикета
        comm_count = len(tmp) # подсчет кол-во комментов в тикете
        """print('')
        print('$$$' + line_clear + '$$$') # вывод номер тикета"""

        created_GTOPS.append(issue.fields.created) # вывод даты и времени создания тикета
        #print(created_GTOPS)

        #print('Описание к тикету: ')
        custom_field_id = ('customfield_23609')  # id поле с видом услуги
        custom_field_value = issue.raw['fields'][custom_field_id]['value']
        #print(f"Услуга: {custom_field_value}")

        #print('')

        custom_field_id = ('customfield_23742')  # Номер обращения в Bi.Zone
        custom_field_value = issue.raw['fields'][custom_field_id]
        #print(f"Bi.Zone: {custom_field_value}")

        description_GTOPS.append(issue.fields.description) # вывод описания тикета
        #print(description_GTOPS)

        #Вывод всех комментов
        for j in range(comm_count):
            print(j)
            print(i)
            comment_created[i][j] = issue.fields.comment.comments[j].created # дата и время создания тикета
            #print(comment_created)
            comment_body[i][j] = issue.fields.comment.comments[j].body # тело комменатрия
            #print(comment_body)
           # file_comments_GTOPS.write(comment_created + '\n' + comment_body + '\n')
        #print('///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////' + '\n')
        i += 1

print(line_clear[5])