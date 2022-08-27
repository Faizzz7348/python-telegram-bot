import asyncio
import telegram

async def main():
    bot = telegram.Bot("1868356667:AAFUzjidDK4RLlVaCEm6C969jZbj9R3tR68")
    async with bot:
        print((await bot.get_updates())[0])

if __name__ == '__main__':
    asyncio.run(main())