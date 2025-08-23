import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai import BrowserConfig, CrawlerRunConfig

async def simple_crawler():
    brower_config = BrowserConfig(verbose=True)
    crawler_config = CrawlerRunConfig(
        exclude_external_links=True,
        process_iframes=True,
        remove_overlay_elements=True
    )

    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun("https://crawl4ai.com")
        if result.success:
            for i in result.media["images"]:
                print(f"image source: {i['src']}")

asyncio.run(simple_crawler())