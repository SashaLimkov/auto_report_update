from employers.models import Employer


def create_telegram_employer(
    user_name=str,
    redmine_id=str,
    redmine_url=str,
    **args
    ):
    employer = Employer(
        user_name=user_name,
        redmine_id=redmine_id,
        redmine_url=redmine_url,
        **args,
    )
    employer.save()
    return employer




def get_all_employers():
    return Employer.objects.all()

def get_employer_by_id(redmine_id:str):
    return Employer.objects.filter(redmine_id=redmine_id).first()




def filter_employers_by_status():
    employers = get_all_employers()
    for employer in employers:
        pass
    pass
 
