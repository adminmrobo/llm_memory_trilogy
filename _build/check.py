import sys,asyncio,json
from playwright.async_api import async_playwright
f=sys.argv[1]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for w,h in [(1280,900),(390,844)]:
            pg=await b.new_page(viewport={'width':w,'height':h}); errs=[]
            pg.on('console',lambda m:errs.append(m.text) if m.type=='error' else None); pg.on('pageerror',lambda e:errs.append(str(e)))
            await pg.route('**/*',lambda r:r.continue_() if r.request.url.startswith('file:') else r.abort())
            await pg.goto('file://'+f); await pg.wait_for_timeout(1200)
            ov=await pg.evaluate("()=>{var d=document.documentElement,o=[];document.querySelectorAll('body *').forEach(e=>{var r=e.getBoundingClientRect();if(r.right>d.clientWidth+2&&r.width>0&&!e.closest('.links,.tw,pre,.cwrap'))o.push(e.tagName+'.'+e.className+' '+Math.round(r.right));});return {sw:d.scrollWidth,cw:d.clientWidth,o:o.slice(0,8)}}")
            noimg=await pg.evaluate("()=>[...document.querySelectorAll('img[data-who]')].filter(i=>!i.getAttribute('src')).map(i=>i.dataset.who+'_'+i.dataset.mood)")
            print(w,'넘침',ov,'빈 그림',noimg,'오류',[e for e in errs if 'ERR_FAILED' not in e and 'net::' not in e])
            if w==1280:
                r=await pg.evaluate("()=>{var R=PAGE._R;return {v:[7,14,28,30,53,80,100].map(l=>[l,R[l].n,R[l].k,+R[l].tr.toFixed(3),+R[l].va.toFixed(3)]),best:PAGE._BEST,naive:PAGE._NAIVE,quiz:document.querySelectorAll('.quiz .qi').length,jt:document.querySelectorAll('.jt').length,k1:document.querySelector('#k1').innerText,k2:document.querySelector('#k2').innerText,sum:document.querySelector('#sumTb').innerText,kg:document.querySelector('#kgStats').innerText,ex:document.querySelector('#exKpi').innerText}}")
                print(json.dumps(r,ensure_ascii=False,indent=0))
                await pg.click('#b1E'); print(await pg.inner_text('#ins1'))
                await pg.fill('#r1L','30'); await pg.dispatch_event('#r1L','input'); print(await pg.inner_text('#ins1')); print(await pg.inner_text('#eq1'))
                await pg.fill('#r2L','100'); await pg.dispatch_event('#r2L','input'); print(await pg.inner_text('#ins2'))
                await pg.click('#duel .reveal'); await pg.wait_for_timeout(700)
                print(await pg.inner_text('#duel .result')); print(await pg.inner_text('#duelNote')); print(await pg.inner_text('#duel .ref'))
                await pg.click('#xBtn')
                for sel,name in [('#top','hero'),('#first','first'),('#lv1','lv1'),('#lv2','lv2'),('#vs','vs'),('#sum','sum'),('#kg','kg')]:
                    await pg.locator(sel).screenshot(path='/tmp/shot_%s.png'%name)
                await pg.locator('#cover').screenshot(path='/tmp/shot_cover.png')
            else:
                await pg.screenshot(path='/tmp/shot_m_top.png'); await pg.locator('#lv1 .twobox').screenshot(path='/tmp/shot_m_two.png')
        await b.close()
asyncio.run(main())
