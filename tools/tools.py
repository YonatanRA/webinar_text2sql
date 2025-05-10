import logging as log

class Logger:
    def __init__(self, name: str) -> None:
        """
        Crea logger para feedback.
        :param name: String. Nombre del logger.
        """
        self.logger = log.getLogger(name)
        self.logger.setLevel(log.DEBUG)

        # crea console para debuggear
        ch = log.StreamHandler()
        ch.setLevel(log.DEBUG)

        # crea formatter
        formatter = log.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # añade formatter a la consola
        ch.setFormatter(formatter)

        # añade consola al logger
        self.logger.addHandler(ch)