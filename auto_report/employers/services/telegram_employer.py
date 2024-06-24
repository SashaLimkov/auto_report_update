from employers.models import Employer


def create_telegram_employer(
    user_name: str, start_time: str,
    end_time: str, employer_status: str,
    tg_urls: str
    ):
    employer = Employer(
        user_name=user_name,
        start_time=start_time,
        end_time=end_time,
        employer_status=employer_status,
        tg_urls=tg_urls
    )
    employer.save()
    
    return employer


def get_all_employers():
    return Employer.objects.all()


def filter_employers_by_status():
    employers = get_all_employers()
    for employer in employers:
        pass
    pass
 
