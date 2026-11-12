import os
import sys,asyncio,json
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for f in sys.argv[1:]:
            fp=os.path.abspath(os.path.join('out',f))
            for w,h in [(1280,900),(390,844)]:
                pg=await b.new_page(viewport={'width':w,'height':h}); errs=[]
                pg.on('console',lambda m:errs.append(m.text) if m.type=='error' else None); pg.on('pageerror',lambda e:errs.append(str(e)))
                await pg.route('**/*',lambda r:r.continue_() if r.request.url.startswith('file:') else r.abort())
                await pg.goto('file://'+fp); await pg.wait_for_timeout(900)
                ov=await pg.evaluate("()=>{var d=document.documentElement,o=[];document.querySelectorAll('body *').forEach(e=>{var r=e.getBoundingClientRect();if(r.right>d.clientWidth+2&&r.width>0&&!e.closest('.links,.tw,pre,.cwrap,.eq'))o.push(e.tagName+'.'+e.className);});return [d.scrollWidth-d.clientWidth,o.slice(0,5)]}")
                noimg=await pg.evaluate("()=>[...document.querySelectorAll('img[data-who]')].filter(i=>!i.getAttribute('src')).length")
                errs=[e for e in errs if 'net::' not in e and 'ERR_FAILED' not in e]
                print(f,w,'넘침',ov,'빈그림',noimg,'오류',errs)
                if w==1280:
                    t=await pg.evaluate("()=>JSON.stringify(PAGE._T||{},(k,v)=>typeof v==='number'?+v.toFixed(3):v)"); print(' T',t[:900])
                    if await pg.locator('#duel .reveal').count():
                        await pg.click('#duel .reveal'); await pg.wait_for_timeout(int(sys.argv[0]=='x' or 0)+ (9000 if 'SLOW' in f else 900))
                        try: await pg.wait_for_selector('#duel.open',timeout=20000)
                        except Exception as e: print(' duel timeout')
                        print(' 대결:',(await pg.inner_text('#duel .result')).replace('\n',' ')[:330]); print(' 주석:',(await pg.inner_text('#duelNote')).replace('\n',' ')[:300])
                    for sel in ['#k1','#k2','#sumTb','#ins1','#ins2']:
                        if await pg.locator(sel).count(): print(' ',sel,(await pg.inner_text(sel)).replace('\n',' | ')[:420])
                    await pg.screenshot(path='/tmp/full_%s.png'%f[:3],full_page=True)
                await pg.close()
        await b.close()
asyncio.run(main())
