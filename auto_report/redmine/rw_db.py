from pprint import pprint
from redmine.redmine_worker import RedmineWorker

rw = RedmineWorker()




def get_all_users():
    employers = rw.get_all_users()
    employers_list = []
    for user in employers:
        user_name = f"{user.firstname} {user.lastname}"
        redmine_id = user.id
        redmine_url = user.url
        employer = {
            "user_name": user_name,
            "redmine_id": redmine_id,
            "redmine_url": redmine_url,
        }
        employers_list.append(employer)
    return employers_list
        
        
def get_all_projcts():
    projects = rw.get_all_projects()
    projects_list = []
    for project in projects:
        projects_list.append(
            {
                "project_name": project.name,
                "redmine_id": project.id,
                "redmine_url": project.url,
            }
        )
    return projects_list


get_all_projcts()

# [('issues', None),
#  ('issues_assigned', None),
#  ('issues_authored', None),
#  ('time_entries', None),
#  ('memberships', None),
#  ('groups', None),
#  ('id', 1),
#  ('login', 'admin'),
#  ('admin', True),
#  ('firstname', 'Давид'),
#  ('lastname', 'Юсупов'),
#  ('mail', 'dyusupov@icdc.ru'),
#  ('created_on', '2017-01-17T09:20:05Z'),
#  ('updated_on', '2022-07-12T13:31:11Z'),
#  ('last_login_on', '2022-06-24T05:23:20Z'),
#  ('passwd_changed_on', '2018-01-10T14:47:38Z'),
#  ('twofa_scheme', None),
#  ('internal_id', 1),
#  ('manager', <redminelib.managers.UserManager object for User resource>),
#  ('url', 'http://172.16.1.154/redmine/users/1')]