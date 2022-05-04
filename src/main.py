import logging

from bot import start_bot


def run():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG
    )
    start_bot()


if __name__ == '__main__':
    run()
