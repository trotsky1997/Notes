import translators as ts
import json
from functools import lru_cache
import random
import time
from retry import retry
q_text = '季姬寂，集鸡，鸡即棘鸡。棘鸡饥叽，季姬及箕稷济鸡。'
q_html = '''<!DOCTYPE html><html><head><title>《季姬击鸡记》</title></head><body><p>还有另一篇文章《施氏食狮史》。</p></body></html>'''


@lru_cache(65535)
def do_trans(txt,translator):
    return ts.translate_text(txt,translator=translator,to_language='zh')

@retry(delay=1, jitter=1, max_delay=5)
@lru_cache(65535)
def trans(txt):
    translator = random.choice(['bing','google','baidu','youdao',])
    ret = ''
    for i in range(0,len(txt),998):
        # time.sleep(random.random())
        ret += do_trans(txt[i:i+998],translator=translator)
    return ret
### usage
# _ = ts.preaccelerate_and_speedtest()  # Optional. Caching sessions in advance, which can help improve access speed.

# print(ts.translators_pool)
# print(ts.translate_text(q_text,to_language='zh'))
with open('./general_dpo_data_cn.jsonl',mode='r',encoding='utf-8') as f0:
    f0_len = len(f0.readlines())


with open('./general_dpo_data_cn.jsonl',mode='a',encoding='utf-8') as f0:
    with open('./general_dpo_data.jsonl','r',encoding='utf8') as f:
        for i,line in enumerate(f):
            if i < f0_len:
                continue
            print(i)
            # print(ts.translate_text(line,to_language='zh'))
            data = json.loads(line)
            data['instruction'] = trans(data['instruction'])
            good,bad = data['output']
            good = trans(good)
            bad = trans(bad)
            data['output'] = [good,bad]
            historys = []
            for h in data['history']:
                h0 = trans(h[0])
                h1 = trans(h[1])
                historys.append([h0,h1])
            data['history'] = historys
            f0.write(json.dumps(data,ensure_ascii=False)+'\n')