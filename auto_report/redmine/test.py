from redminelib import Redmine


REDMINE_CONNECTION = {
    "url":"http://172.16.1.154/redmine/",
    "version" : "4.2.0",
    "username" : "it_galimov",
    "password" : "mansur22042"
}

# 16376 номер задачи
# 49 id разработчика (Максим)
# 162 id проекта 

redmine = Redmine(**REDMINE_CONNECTION)


def get_all_users():
    # выводит просто объект
   return redmine.users.all()
    
    
def get_all_projects():
    # выводит просто объект
   return redmine.project.all()
    

def get_all_task():
    # выдает весь список задач а потом ошибку redminelib.exceptions.ForbiddenError: Requested resource is forbidden
    # мейби впихнуть сюда try except
    for project in redmine.project.all():
        for task in project.issues:
            return task
        
        
def get_project_tasks(project_id):
    # выводит тоже только 1 объект 
    for project_task in redmine.issue.filter(projet_id=project_id):
        return project_task
    
    
def get_user_tasks(user_id):
    # задачу выдает но вызывается по окончанию та же ошибка что и в get_all_task
    # поэтому может быть имеет смысл использовать yield
    for user_task in redmine.user.get(user_id).issues:
        yield user_task
    

def get_task_by_id(task_id):
    # отрабатывает нормально
    for project in redmine.project.all():
            for task in project.issues.filter(id=task_id):
                return task


for project in redmine.project.all():
    for item in project.issues:
        print(item)
#print(get_project_tasks(162))
#project = redmine.project.get(163)
#print(project.wiki_pages)


#print(list(user))
# ['created_on', 'description', 'enabled_modules', 'files', 
# 'id', 'identifier', 'inherit_members', 'internal_id', 
# 'is_public', 'issue_categories', 'issue_custom_fields', 
# 'issues', 'manager', 'memberships', 'name', 'news', 'status', 
# 'time_entries', 'time_entry_activities', 'trackers', 
# 'updated_on', 'url', 'versions', 'wiki_pages']

# выходит вот такой список. я не совсем понимаю что это за значения? ключи? если да то как мне обратиться к ним
# пытаюсь достать задачи которые находятся внутри проектов как будто
# возможно нужно искать в enabled_modules но я не знаю как туда залезть  

