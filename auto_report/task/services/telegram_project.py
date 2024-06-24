from task.models import Project

def create_new_project(project_name:str):
    return Project.objects.create(
        project_name=project_name
    )
    
def get_all_projects():
    return Project.objects.all()

def get_project_by_name(project_name: str):
    return Project.objects.filter(project_name=project_name)
    