from protectremote.main import RuleService
from python_settings import settings 


def update_request_data():
    try:
        service = RuleService()
        data = service.post_rules()
        if settings.RULES_DATA != data:
            settings.RULES_DATA = data
            print(f'Data updated... from {settings.RULES_DATA} to {data}')
        print("Cachdeki data ile apiden gelen data aynı, bu yüzden güncellenmedi.")
    except Exception as e:
        print("data couldnt updated", e)
    