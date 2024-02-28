import aiosqlite


class Database:
    """База данных"""
    def __init__(self, path: str):
        self.path = path
        self.db = None

    async def __aenter__(self):
        self.db = await aiosqlite.connect(self.path)
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.db.close()

    async def get_version(self):
        """Получить версию базы данных"""
        query = "SELECT sqlite_version();"
        async with self.db.execute(query) as cursor:
            version = await cursor.fetchone()
            return version
