from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from pathlib import Path
import pypdfium2 as pdfium

root=Path(__file__).resolve().parent.parent
pdfmetrics.registerFont(TTFont('Editorial','C:/Windows/Fonts/georgia.ttf'))
pdfmetrics.registerFont(TTFont('EditorialItalic','C:/Windows/Fonts/georgiai.ttf'))
pdfmetrics.registerFont(TTFont('Body','C:/Windows/Fonts/arial.ttf'))
path=root/'public/shruti-media-kit.pdf'
c=canvas.Canvas(str(path),pagesize=(595,842))
c.setTitle('SHRUTI - The Creator Edit | Media Kit')
c.setAuthor('Shruti')
cream='#FAF7F2';ink='#241B1B';rose='#AE596B';muted='#746A66'
def text(x,y,s,font='Body',size=10,color=ink):
 c.setFillColor(HexColor(color));c.setFont(font,size);c.drawString(x,y,s)
def background():
 c.setFillColor(HexColor(cream));c.rect(0,0,595,842,fill=1,stroke=0)
def line(y):
 c.setStrokeColor(HexColor('#DCD4CE'));c.line(40,y,555,y)
def photo(name,x,y,w,h):
 from PIL import Image,ImageOps
 im=ImageOps.fit(Image.open(root/f'public/images/{name}.webp'),(int(w*2),int(h*2)))
 c.drawImage(ImageReader(im),x,y,w,h)
background()
text(40,803,'THE CREATOR EDIT / MEDIA KIT',size=8)
text(514,803,'2026',size=8)
line(787)
text(36,697,'SHRUTI.',font='Editorial',size=81)
text(42,671,'Your brand, through my lens.',font='EditorialItalic',size=21,color=rose)
photo('hero',40,310,290,335)
photo('evening',348,434,207,211)
text(348,402,'BEAUTY. STYLE.',size=10)
text(348,384,'LIFESTYLE. STORIES.',size=10)
text(348,345,'10K+',font='Editorial',size=35)
text(348,326,'Instagram followers',size=9,color=muted)
text(40,277,'Hi, I\'m Shruti.',font='Editorial',size=25)
for y,s in [(252,'A beauty, fashion and lifestyle content creator with a love for authentic,'),(236,'visually engaging stories. From outfit inspiration to everyday discoveries,'),(220,'I create relatable content that brings brands closer to their audience.')]:text(40,y,s,size=10,color=muted)
line(197)
text(40,171,'REELS REACHING',size=8)
text(40,145,'Millions of views',font='Editorial',size=22)
text(324,171,'COLLABORATION EXPERIENCE',size=8)
text(324,145,'Paid & barter',font='Editorial',size=22)
text(40,84,'Let\'s create something beautiful.',font='EditorialItalic',size=21,color=rose)
text(40,56,'INSTAGRAM: @_.shru_.ti19',size=10)
c.linkURL('https://www.instagram.com/_.shru_.ti19/',(40,49,245,70),relative=0)
text(530,40,'01',size=8)
c.showPage();background()
text(40,803,'SHRUTI / COLLABORATION NOTES',size=8);line(787)
text(40,739,'Good brands.',font='Editorial',size=39)
text(40,692,'Even better stories.',font='EditorialItalic',size=39,color=rose)
formats=[('01  Paid partnerships','Sponsored reels, product features and brand campaigns.'),('02  Barter collaborations','Product-for-content partnerships. Deliverables agreed together.'),('03  PR & gifting','Unboxings and first impressions. Coverage agreed in advance.'),('04  Creative content','Discuss UGC concepts, availability, deliverables and usage rights.')]
for i,(title,body) in enumerate(formats):
 y=640-i*65
 text(40,y,title,font='Editorial',size=19);text(40,y-22,body,size=10,color=muted);line(y-38)
text(40,352,'A GLIMPSE INTO MY WORLD',size=8)
for i,name in enumerate(['heritage','evening','off-duty']):photo(name,40+i*175,153,165,177)
text(40,130,'PERSONAL STYLE',size=7);text(215,130,'FASHION MOMENTS',size=7);text(390,130,'EVERYDAY STORIES',size=7)
text(40,91,'Have a brief? Let\'s talk on Instagram.',font='EditorialItalic',size=20,color=rose)
text(40,65,'@_.shru_.ti19  /  Custom proposals discussed directly.',size=10)
c.linkURL('https://www.instagram.com/_.shru_.ti19/',(40,54,340,80),relative=0)
text(40,32,'Metrics supplied by creator. No engagement or campaign results implied.',size=7,color=muted)
text(530,32,'02',size=8)
c.save()
doc=pdfium.PdfDocument(str(path))
for i,page in enumerate(doc):page.render(scale=1.3).to_pil().save(root/f'artifacts/media-kit-{i+1}.png')
print(f'Created {len(doc)} pages: {path}')
