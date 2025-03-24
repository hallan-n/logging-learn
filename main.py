from logging import Filter, basicConfig, Formatter
from logging import DEBUG
from logging import debug, info, error, warning, critical
from logging import FileHandler, StreamHandler


class Filtro(Filter):
    def filter(self, record):
        if record.msg.lower().startswith("senha"):
            return False
        return True


format_handler = Formatter("%(asctime)s:%(levelname)s:%(message)s:%(name)s")
file_handler = FileHandler("logs.txt", "a", encoding="utf-8")
file_handler.setLevel(DEBUG)
file_handler.setFormatter(format_handler)
file_handler.addFilter(Filtro())


stream_handler = StreamHandler()
stream_handler.setLevel(DEBUG)
stream_handler.setFormatter(format_handler)
stream_handler.addFilter(Filtro())

basicConfig(level=DEBUG, handlers=[file_handler, stream_handler])

debug("Entrei aqui")
info("Pessoa X logou")
error("Erro na solicitação")
warning("Algo deu errado")
critical("Aplicação parou")
critical("Senha 123")
