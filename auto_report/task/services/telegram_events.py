from task.models import Events

def create_telegram_event(
    task_info: str, start_time: str,
    end_time: str, ready_status: str,
    comments: str = None
    ):
    
    event = Events(
        task_info=task_info,
        start_time=start_time,
        end_time=end_time,
        ready_status=ready_status,
        comments=comments
    )
    event.save()
    return event

def get_all_events():
    return Events.objects.all( )

def get_event_by_name(event_name: str):
    return Events.objects.filter(project_name=event_name).first()

def filter_events_by_ready_status():
    # может быть имеет смысл добавить фильтрацию событий
    pass

def update_comment(event_name: str, comment: str):
    event = get_event_by_name(project_name=event_name)
    event.comments = comment
    event.save()
    