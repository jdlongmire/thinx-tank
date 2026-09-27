"""Render the article's simple typographic hero at 1200x630."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

root=Path(__file__).resolve().parent.parent
out=root/'static/img/posts/human-curated-ai-enabled-enterprise-architecture'
out.mkdir(parents=True,exist_ok=True)
im=Image.new('RGB',(1200,630),'#05283f');d=ImageDraw.Draw(im)
regular='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def line(x,y,text,size,color='#f2f8fc',strong=False):
    d.text((x,y),text,font=ImageFont.truetype(bold if strong else regular,size),fill=color)
line(64,42,'THINX-TANK',36,'#78d6ff',True)
line(64,150,'Human judgment.',76,strong=True)
line(64,254,'AI-enabled',76,strong=True)
line(64,352,'architecture.',76,strong=True)
d.line((64,476,1136,476),fill='#78d6ff',width=4)
line(64,511,'Curated knowledge. Accountable decisions.',42)
im.save(out/'hero.png')
