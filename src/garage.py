import garage_host
import garage_customer
import data.mongo_setup as mongo_setup


def main():
    mongo_setup.global_init()

    try:
        while True:
            if find_user_intent() == 'attend':
                garage_customer.run()
            else:
                garage_host.run()
    except KeyboardInterrupt:
        return


def find_user_intent():
    print("[c] Attend a garage sale")
    print("[h] Host a garage sale")
    print()
    choice = input("Are you a [c]ustomer or a [h]ost? ")
    if choice == 'h':
        return 'offer'
    return 'attend'


if __name__ == '__main__':
    main()
