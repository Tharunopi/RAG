import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai import BrowserConfig, CrawlerRunConfig

async def simple_crawler():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun("https://crawl4ai.com")
        print(result.markdown.fit_markdown)

asyncio.run(simple_crawler())