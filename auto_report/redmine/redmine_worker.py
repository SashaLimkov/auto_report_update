from redminelib import Redmine
from redminelib.exceptions import ForbiddenError


class RedmineWorker: 
    
    def __init__(self):
        self.session = Redmine(**self.REDMINE_CONNECTION)
        
    
    def try_it(func):
        def wrapper(self, *args, **kwargs):
            while True:
                try:
                    return func(self, *args, **kwargs)
                except ForbiddenError:
                    self.__init__()
        return wrapper
    
    @try_it
    def get_all_users(self):
        return self.session.user.all()
    
    @try_it
    def get_all_projects(self):
        return self.session.project.all()
    
    @try_it
    def get_user_by_id(self,  user_id):
        return self.session.user.get(user_id)

    @try_it
    def get_project_by_id(self,  project_id):
        return self.session.project.get(project_id)
    
    @try_it
    def get_project_tasks(self,  project_id):
        return self.session.issue.filter(project_id=project_id)
    
    @try_it
    def get_project_issues(self,  project_id):
        return self.session.issue.filter(project_id=project_id)
    
    @try_it
    def get_user_issues(self, user_id):
        return self.session.issue.filter(assigned_to_id=user_id, status_id="*")
    
    
    @try_it
    def get_issue_by_id(self,  issue_id):
        return self.session.issue.get(issue_id)
   

   

    

# rw = RedmineWorker()
# all_users = rw.get_all_users()
# mansur = rw.get_user_by_id(user_id=60)
# all_projects  = rw.get_all_projects()
# project = all_projects[2]
# project_1 = rw.get_project_by_id(project_id=project.id)
# project_issues = rw.get_project_issues(project_id=project.id)
# all_user_issues  = rw.get_user_issues(user_id=49)
# for index, user_issue in enumerate(list(all_user_issues)):
#     print(index+1, user_issue.id, user_issue.status,  user_issue)
# # issue = rw.get_issue_by_id(issue_id=17775)
# print(list(user_issue))
# # print(issue, issue.status)
