from task.models import TaskData
from task.services.telegram_project import get_project_by_name

def create_telegram_task(
    initiator: str,  status: str, ready: str, 
    time_manage: float, work_manage: float,
    task_type: str, description: str = None,
    project_name: str = get_project_by_name()
    ):
    
    task = TaskData(
        project_name=project_name,
        initiator=initiator,
        status=status,
        description=description,
        ready=ready,
        time_manage=time_manage,
        work_manage=work_manage,
        task_type=task_type 
        # почему то вызывается ошибка с этим полем
    )
    task.save()
    return task


def get_task_by_name(project_name: str):
    return TaskData.objects.filter(project_name=project_name).first()

def update_task_status(status: str, project_name: str):
    task = get_task_by_name(project_name=project_name)
    task.status = status
    task.save()

def delete_task(project_name: str):
    TaskData.objects.delete(project_name)    

def edit_description(description: str, project_name: str):
    task = get_task_by_name(project_name=project_name)
    task.description = description
    task.save()
    
def get_time_manage():
    pass

def get_work_manage():
    pass

def filter_tasks_by_time():
    pass