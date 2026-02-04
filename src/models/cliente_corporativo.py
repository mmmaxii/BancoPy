from .cliente import Cliente

class ClienteCorporativo(Cliente):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
