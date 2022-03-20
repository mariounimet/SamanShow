from functions import *
from events_manage import events_manage
def main():

    #obtener data proveniente de API
    data = init_data()

    events_manage(data['events'])

main()