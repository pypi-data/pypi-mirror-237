from protectremote.main import RuleService
from python_settings import settings 
from protectremote.file import write_to_protectremote_file


def update_request_data():
    try:
        service = RuleService()
        data = service.post_rules()
        if data is not None:
            write_to_protectremote_file(data)
            print(f'Data updated.. {data}')
        else:
            print("apiden gelen data none")
    except Exception as e:
        print("data couldnt updated", e)
    