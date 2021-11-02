import garage_users
import data.mongo_setup as mongo_setup


def main():
    mongo_setup.global_init()

    try:
        while True:
            garage_users.run()
    except KeyboardInterrupt:
        return


if __name__ == '__main__':
    main()
