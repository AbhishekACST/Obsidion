import aiohttp

async def get(session, url):
    async with session.get(url) as resp:
        if resp.status == 200:
            data = await resp.json()
            return data
        else:
            return False


async def get_uuid(session, username):
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    async with session.get(url) as resp:
        if resp.status == 200:
            data = await resp.json()
            uuid = data["id"]
            return uuid
        else:
            return False