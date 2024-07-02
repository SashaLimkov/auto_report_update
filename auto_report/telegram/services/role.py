from telegram.models import Role


def get_all_roles():
    return Role.objects.all()

def get_role_by_name(name: str) -> Role:
    return Role.objects.filter(name=name).first()