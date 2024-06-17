# -=encoding=utf-8=-
import json

from re import template
from datasets import load_dataset
import json
from markdownify import markdownify
import mdformat

import re

import random
from tqdm import tqdm
from functools import lru_cache


def replace_image_tags_with_alt_text(md_text):
    # 图片标签的正则表达式
    img_pattern = r'!\[([^\]]*)\]\(([^\)]*)\)'
    
    # 使用alt_text替换
    new_md_text = re.sub(img_pattern, r'\1', md_text)
    
    return new_md_text

def replace_link_tags_with_alt_text(md_text):
    # 链接标签的正则表达式
    link_pattern = r'\[([^\]]*)\]\(([^\)]*)\)'
    
    # 使用alt_text替换
    new_md_text = re.sub(link_pattern, r'\1', md_text)
    
    return new_md_text



import re
from pylatexenc.latex2text import LatexNodes2Text

def replace_math_codes_with_text(md_text):
    # 多行数学公式标签的正则表达式
    multiline_math_pattern = r'\$\$(.*?)\$\$'
    
    # 使用LaTeX公式的普通文本替换
    new_md_text = re.sub(multiline_math_pattern, lambda m: "\n$$\n"+LatexNodes2Text().latex_to_text(m.group(1)) +"\n$$\n", md_text, flags=re.DOTALL)
    
    return new_md_text

def replace_multiline_math_tags_with_text(md_text):
    # 多行数学公式标签的正则表达式
    multiline_math_pattern = r'\$\$(.*?)\$\$'
    
    # 使用LaTeX公式的普通文本替换
    new_md_text = re.sub(multiline_math_pattern, lambda m: "\n$$\n"+LatexNodes2Text(math_mode='text').latex_to_text(m.group(1)) +"\n$$\n", md_text, flags=re.DOTALL)
    
    return new_md_text

import re
from pylatexenc.latex2text import LatexNodes2Text

def replace_math_tags_with_text(md_text):
    # 数学公式标签的正则表达式
    math_pattern = r'\$(.*?)\$'
    
    # 使用LaTeX公式的普通文本替换
    new_md_text = re.sub(math_pattern, lambda m: "$"+LatexNodes2Text(math_mode='text').latex_to_text(m.group(1)) +"$", md_text)
    
    return new_md_text

import re

def remove_http_links(text):
    # HTTP链接的正则表达式
    http_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    
    # 使用空字符串替换所有HTTP链接
    cleaned_text = re.sub(http_pattern, '', text)
    
    return cleaned_text

# def clean(match):
#     # 在这里添加你的清洗逻辑
#     smiles_string = match.group(0)
#     if '.' in smiles_string:
#         return smiles_string
#     else:
#         cleaned_smiles = f'\n```smiles\n{smiles_string}\n```\n'
#         return cleaned_smiles

# def replace_smiles_with_cleaned(text):
#     # SMILES字符串的正则表达式
#     smiles_pattern = r'[A-Za-z0-9@+\-\[\]\(\)=%#:.]*'

#     # 使用re.sub()替换所有的SMILES字符串
#     cleaned_text = re.sub(smiles_pattern, clean, text)

#     return cleaned_text

def md(txt):
    txt = remove_http_links(txt)
    # txt = replace_multiline_math_tags_with_text(txt)
    # txt = replace_math_tags_with_text(txt)
    txt = LatexNodes2Text(math_mode='with-delimiters').latex_to_text(txt)
    txt = txt.replace('\\[','[').replace('\\]',']').replace('\\_','_')

    txt = markdownify(txt)
    # txt = mdformat.text(txt)
    
    txt = replace_image_tags_with_alt_text(txt)
    txt = replace_link_tags_with_alt_text(txt)
    txt = replace_link_tags_with_alt_text(txt)
    txt = mdformat.text(txt)
    txt = txt.replace('lt;','<').replace('gt;','>').replace('amp;','&').replace('quot;','"').replace('apos;',"'").replace('nbsp;',' ').replace('ldquo;','“').replace('rdquo;','”').replace('lsquo;','‘').replace('rsquo;','’').replace('mdash;','—').replace('ndash;','–').replace('times;','×').replace('divide;','÷').replace('leq;','≤').replace('geq;','≥').replace('neq;','≠').replace('infty;','∞').replace('alpha;','α').replace('beta;','β').replace('gamma;','γ').replace('delta;','δ').replace('epsilon;','ε').replace('zeta;','ζ').replace('eta;','η').replace('theta;','θ').replace('iota;','ι').replace('kappa;','κ').replace('lambda;','λ').replace('mu;','μ').replace('nu;','ν').replace('xi;','ξ').replace('omicron;','ο').replace('pi;','π').replace('rho;','ρ').replace('sigma;','σ').replace('tau;','τ').replace('upsilon;','υ').replace('phi;','φ').replace('chi;','χ').replace('psi;','ψ').replace('omega;','ω').replace('Alpha;','Α').replace('Beta;','Β').replace('Gamma;','Γ').replace('Delta;','Δ').replace('Epsilon;','Ε').replace('Zeta;','Ζ').replace('Eta;','Η').replace('Theta;','Θ').replace('Iota;','Ι').replace('Kappa;','Κ').replace('Lambda;','Λ').replace('Mu;','Μ').replace('Nu;','Ν').replace('Xi;','Ξ').replace('Omicron;','Ο').replace('Pi;','Π').replace('Rho;','Ρ').replace('Sigma;','Σ').replace('Tau;','Τ').replace('Upsilon;','Υ').replace('Phi;','Φ').replace('Chi;','Χ').replace('Psi;','Ψ').replace('Omega;','Ω').replace('forall;','∀').replace('part;','∂').replace('exist;','∃').replace('empty;','∅').replace('nabla;','∇').replace('isin;','∈').replace('notin;','∉').replace('ni;','∋').replace('prod;','∏').replace('sum;','∑').replace('minus;','−').replace('lowast;','∗').replace('radic;','√').replace('prop;','∝').replace('infin;','∞').replace('ang;','∠').replace('and;','∧').replace('or;','∨').replace('cap;','∩').replace('cup;','∪').replace('int;','∫').replace('there4;','∴').replace('sim;','∼').replace('cong;','≅').replace('asymp;','≈').replace('ne;','≠').replace('equiv;','≡').replace('le;','≤').replace('ge;','≥').replace('sub;','⊂').replace('sup;','⊃').replace('nsub;','⊄').replace('sube;','⊆').replace('supe;','⊇').replace('oplus;','⊕').replace('otimes;','⊗').replace('perp;','⊥').replace('sdot;','⋅').replace('lceil;','⌈').replace('rceil;','⌉').replace('lfloor;','⌊').replace('rfloor;','⌋').replace('lang;','⟨').replace('rang;','⟩').replace('loz;','◊').replace('spades;','♠').replace('clubs;','♣').replace('hearts;','♥').replace('diams;','♦').replace('quot;','"').replace('amp;','&').replace('lt;','<').replace('gt;','>').replace('nbsp;',' ').replace('iexcl;','¡').replace('cent;','¢').replace('pound;','£').replace('curren;','¤')
    txt = txt.replace('yen;','¥').replace('brvbar;','¦').replace('sect;','§').replace('uml;','¨')
    # if 'smiles' in txt or 'SMILES' in txt:
    #     txt = replace_smiles_with_cleaned(txt)
    # txt = txt.split('References:')[0]
    txt = txt.replace('\\[','[').replace('\\]',']').replace('\\_','_')
    txt = txt.replace('enter image description here','')
    return txt


data = []
with open("./general_dpo_data_cn.jsonl", 'r',encoding='utf8') as f:
    with open("./cleaned_general_dpo_data_cn.jsonl", 'w+',encoding='utf8') as f0:
        for line in f:
            # if any([ i in line.lower() for i in ['编写','代码','翻译',"脚本",'编程','程序','print','if','IF','python']]):
            #     continue
            # else:
            data = json.loads(line)
            if data['instruction'] != '':
                data['instruction'] = md(data['instruction'])
            if data['input'] != '':
                data['input'] = md(data['input'])
            if data['output'] != []:
                data['output'] = [md(data['output'][0]),md(data['output'][1])]
            if data['history']:
                history = []
                for qa in data['history']:
                    history.append([md(qa[0]),md(qa[1])])
                data['history'] = history
            f0.write(json.dumps(data,ensure_ascii=False)+'\n')