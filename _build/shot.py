import os
import sys,asyncio
from playwright.async_api import async_playwright
async def main():
    f,sel,click=sys.argv[1],sys.argv[2],(sys.argv[3] if len(sys.argv)>3 else None)
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':1100,'height':900})
        await pg.route('**/*',lambda r:r.continue_() if r.request.url.startswith('file:') else r.abort())
        await pg.goto('file://'+os.path.abspath(os.path.join('out',f))); await pg.wait_for_timeout(700)
        await pg.add_style_tag(content='nav.top,#study{display:none!important}')
        if click:
            for c in click.split(','): await pg.click(c); await pg.wait_for_timeout(3500)
        await pg.locator(sel).scroll_into_view_if_needed(); await pg.wait_for_timeout(500)
        await pg.locator(sel).screenshot(path='/tmp/shot.png'); await b.close()
asyncio.run(main())
