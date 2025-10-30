class DatabaseConnection():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            return cls._instance
        raise Exception("DatabaseConnection singleton already created")

    def __init__(self):
        pass

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
try:
    a = DatabaseConnection()
    b = DatabaseConnection()
except Exception as e:
    print(e)