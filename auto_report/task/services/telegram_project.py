from pprint import pprint
from task.models import Project, UniqueProject
from fuzzywuzzy import process
import csv
import xlsxwriter


def create_new_project(project_data:dict|list):
    if isinstance(project_data, list):
        for project in project_data:
           create_new_project(project)
    else:       
        return Project.objects.create(
            **project_data
        )
        
def get_all_projects():
    return Project.objects.all()

def get_project_by_name(project_name: str):
    return Project.objects.filter(project_name=project_name)
    
    
def create_unique_project(project_name: str):
    return UniqueProject.objects.create(name=project_name)

def filter_data(data:list, limit:int=98):
    return [obj[0] for obj in data if obj[1] >= limit]
def _get_projects_dict(projects_list:list)->dict:
    return {project["name"]:project["redmine_ids"] for project in projects_list}

def get_projects_dict():
    projects = get_all_projects()
    projects_list = [{"name":project.project_name.strip().rstrip(), "redmine_id":project.redmine_id} for project in projects]
    all_names = [project["name"] for project in projects_list]
    clear_names = list(set(all_names))
    new_projects_list = []
    for name in clear_names:
        redmine_ids = []
        for project in projects_list:
            if project["name"] == name:
                redmine_ids.append(project["redmine_id"])
        new_projects_list.append({"name":name, "redmine_ids":redmine_ids})
    projects_dict = _get_projects_dict(projects_list=new_projects_list)
    return projects_dict

def get_unique_projects_with_relations():
    projects_dict = get_projects_dict()
    project_names = list(projects_dict.keys())
    project_names.sort()
    result_list = []
    names_copy = project_names[::]
    while len(names_copy) > 0:
        name = names_copy[0]
        names_copy.remove(names_copy[0])
        nearest = process.extract(name, names_copy)
        filtered_nearest = filter_data(data=nearest)
        for nearest_name in filtered_nearest:
            names_copy.remove(nearest_name)
        if filtered_nearest:
            result_list.append({"name":name, "nearest":filtered_nearest})
    for project in result_list:
        nearest_name = project["nearest"]
        name = project["name"]
        for nearest in nearest_name:
            nearest_id = projects_dict[nearest]
            projects_dict[name] =  projects_dict[name] + nearest_id
            projects_dict.pop(nearest)
    return projects_dict
        

def create_unique_projects():
    projects_dict = get_unique_projects_with_relations()
    for project_name, redmine_ids in projects_dict.items():
        unique_project = create_unique_project(project_name=project_name)
        for redmine_id in redmine_ids:
            project = get_project_by_redmine_id(redmine_id=redmine_id)
            project.unique_project = unique_project
            project.save()
            
def get_project_by_redmine_id(redmine_id: str):
    return Project.objects.filter(redmine_id=redmine_id).first()
            
def get_project_by_name(project_name: str):
    return Project.objects.filter(project_name=project_name).first()

def writer():
    n = [
    '13 часов',
    '1C Аналит аптека',
    '1C Касса',
    '1С Бухгалтерия',
    '1С Бухгалтерия. Склад',
    '1С Медицина.Диетпитание',
    '1С Планирование',
    '1С Рарус Ресторан',
    '1С зарплата и кадры',
    'API',
    'HTTP - СУБД ',
    'Mzio Object',
    'R-Keeper',
    'Statistika (наука)',
    'АПО',
    'АС "Поликлиника"',
    'АС "Стационар"',
    'АС Кадры',
    'Администрирование',
    'Амбулаторный',
    'Амбулаторный проект',
    'Амбулаторный этап',
    'Амбулаторный/Стационарный',
    'Антикоугулянтный кабинет (А)',
    'Аптека',
    'БАРС. Бюджет Бухгалтерия ',
    'БАРС. Бюджет Кадры',
    'БД.Клинический фармаколог',
    'БД.Комитет качества',
    'БД.Эндокринолог',
    'База пациентов ',
    'Бизнес процессы ',
    'Внедренные разработки',
    'Внутренней работы отдела',
    'Гарант',
    'ДЦ ВМП МЗ РТ',
    'Диагностика',
    'Диспетчерская служба',
    'Диспетчерская служба АСУ',
    'Документооборот ',
    'Документы ПУ 5',
    'ЕГИС.Поликлиника (А)',
    'ЕГИС.Стационар (А)',
    'Ежеквартальный отчет в ПФР',
    'Интеграция Витакарт',
    'Интеграция ЕГИС',
    'Интеграция информационных систем (в рамках текущего состояния)',
    'Интеграция пищеблок в/б',
    'Инфраструктура КИС',
    'КАМ',
    'КИС Администрирование',
    'КИС Лотус',
    'КИС Стационар',
    'КИС.Диагностика',
    'КИС.Поликлиника',
    'КИС.Приемное отделение',
    'КИС.Радиология',
    'КИС.Статистика',
    'КИС.Учет посетителей',
    'КИС.ЦМП',
    'КИС.Экспертиза',
    'Кабинет динамического наблюдения',
    'Кадры',
    'Календарь назначение',
    'Клиника',
    'Коечный фонд',
    'Контроль исполнения решений',
    'Корпоративная почта',
    'Косвенные затраты',
    'ЛИС.КДЛ.Баклаборатория',
    'МКДЦ вер. 3',
    'МКДЦ версия 2',
    'МКДЦ с 2024г',
    'МКДЦ. Формирование ТЗ',
    'Маркировка Пищеблок',
    'Назначение ЛС и ИМН',
    'Налогоплательщик ЮЛ',
    'ОПК',
    'Онкорегистр (А)',
    'Отчеты',
    'Перечень льготных профессий',
    'Поликлиника',
    'Прачечная ',
    'Приемное отделение',
    'Проверка полисов пациента',
    'Проект "HIMMS и JCI"',
    'Проект "Дневник"',
    'Проект "Комитет Качества"',
    'Проект "Конструктор экранных форма «Designer»"',
    'Проект "Медицинская информационная система"',
    'Проект "Описание ИС"',
    'Проект "Перфузиолог"',
    'Проект "Реанимация"',
    'Проект "Умная палата пациента"',
    'Проект 99 приказ',
    'Проект «Ситуационная карта»',
    'Проект ТЭГ',
    'Проект аккредитация JCI',
    'Проекты МКДЦ',
    'Протоколы консультаций',
    'Процессинговый центр',
    'Прямые затраты',
    'Регистр ММСЦ (А)',
    'Регистр ОКС (А)',
    'Регистр ТПРИ (А)',
    'Регистры',
    'Создание сервиса гипер куб ',
    'Сотрудник',
    'Стационарный отчет',
    'Стационарный этап',
    'Требование',
    'УИС',
    'Удаленные задачи',
    'Удовлетворенность пациента',
    'Федеральный регистр медработников',
    'ЭСНТИ "Техэксперт"',
    'Экспертиза',
    'Электронный стетоскоп – распознание звуков ',
    'сервер PACS и задачи с вязанные с протоколом DICOM',
]
    workbook = xlsxwriter.Workbook('Выгрузка проектов.xlsx')
    worksheet = workbook.add_worksheet("My sheet")
    res = [["ИС", "Ссылка"]]
    for name in n:
        model = get_project_by_name(project_name=name)
        print(name, model)
        url = model.redmine_url
        res.append([name, url])
    names = ["ИС", "Ссылка"]
    row = 0
    col = 0
    for name, url in (res):
        worksheet.write(row, col, name)
        worksheet.write(row, col + 1, url)
        row += 1
        print(row)
    
    workbook.close()

def get_unique_projects_xlsx():
    workbook = xlsxwriter.Workbook('Выгрузка проектов2.xlsx')
    worksheet = workbook.add_worksheet("Проекты со ссылками на них")
    res = [["ИС", "Ссылка"]]
    unique_projects = UniqueProject.objects.all()
    for project in unique_projects:
        name = project.name
        urls = [p.redmine_url for p in project.porjects.all()]
        res.append([name, *urls])
    row = 0
    col = 0
    for data in res:
        worksheet.write(row, col, data[0])
        for i in range(1, len(data)):
            worksheet.write(row, col + i, data[i])
        row += 1
    
    workbook.close()
