from templates.taskmanagerscrap.shopifyclient import Client
from templates.lib.data import asdict
from rich import print


def main():
    shopy: Client = Client()
    response = shopy.get_data()
    pedal = shopy.parse_data(response)
    print(asdict(pedal))

if __name__ == '__main__':
    main()