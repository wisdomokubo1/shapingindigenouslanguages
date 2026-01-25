import vertexai
from vertexai.language_models import TextGenerationModel

vertexai.init(project="woven-spring-403010", location="us-central1")
parameters = {
    "candidate_count": 1,
    "max_output_tokens": 1024,
    "temperature": 0.2,
    "top_p": 0.8,
    "top_k": 40
}
model = TextGenerationModel.from_pretrained("text-bison")
response = model.predict(
    """a: \"a\".
ability: \"nwe kpenem\".
able: \"nwe kpenem\".
above: \"ofun fieknen\".
abroad: \"ekein bekein\".
accept: \"meme yaw\".
accident: \"ohom\".
accompany: \"due\".
according to: \"ubo okunu\".
accurate: \"uwunenen\".
action: \"ukpene, akpene\".
add: \"yon inum\".
admire: \"o diomoswon\".
admit: \"o memen\".
adult: \"odegnein\".
advice: \"tweyam usow\".
advise: \"tweyam usow\".
afford: \"wen dem\".
afraid: \"egugu\".
after: \"ohovi\".
afternoon: \"odisan\".
age: \"nwa akpe\".
agree: \"memen, o memen\".
ahead: \"ta madu\".
air: \"oferu\".
aircraft: \"ukor ekun\".
airline: ukor ekun\".
alcohol: \"udi nu mibom owei\".
alive: \"o swei\".
all: \"ikikre\".
all right: \"isom\".
alright: \"isom\".
allow: \"vekeke\".
alone: \"oyi kpein\".
always: \"oho vroho\".
ambition: \"ema vor kpenem inum\".
ancient: \"Ina terrbo\".
and: \"nu\".
anger: \"ulom\".
angry: \"ulom\".
animal: \"enam\".
announce: \"duko yem\".
announcement: \"duko yem\".
annoy: \"ulom\".
annoyed: \"o lom\".
another: \"ovivi\".
answer: \"may may\".
appear: \"yenem iwiyn\".
appearance: yenem iwiyn\".
argument: \"nunakne\".
arise: \"bedene\".
army: \"eni savaknem\".
ashamed: \"uwa\".
ask: \"bine, binen\".
asleep: \"mesi, umesi\".
b: \"b\".
baby: \"omo, omofain\".
bad: \"o dierr\".
bag: \"ebre\".
banana: \"obibi\".
bank: \"ekokom ikpoki\".
basket: \"atuwo\".
bath: \"amin duvam\".
bathroom: \"esi duvam amin\".
battle: \"ukorn\".
beauty: \"usom\".
because: \"utom okunu\".
bed: \"eknesi\".
bedroom: \"ebo\".
beg: \"bine\".
begin: \"kel\".
bird: \"efen\".
birthday: \"tenu ebien\".
bite: \"gbom\".
black: \"obibi, bia, biya\".
blood: \"izala\".
blue: \"bulobulo\".
boat: \"ukor amin\".
body: \"nwo\".
boil: \"twain, twine\".
bone: \"ubwo\".
book: \"ubi\".
books: \"abi\".
born: \"biye\".
borrow: \"bine, binen\".
bottle: \"ololo\".
bowl: \"pani\".
box: \"igbe\".
boy: \"omo omosi\".
boyfriend: \"uga\".
break: \"kei, keyi\".
breast: \"iviyow, iviyoun\".
breath: \"uvowa\".
breathe: \"vowu\".
bright: \"bara\".
bring: \"veyi\".
brother: \"oto me omosi\".
build: \"bo\".
c: \"c\".
can: \"ololo\".
car: \"ukor\".
chair: \"agada, osusuwa\".
cheap: \"otul eki\".
check: \"gen, gehn\".
chemistry: \"kemistri\".
chicken: \"ohorhor\".
chief: \"odede\".
child: \"omo\".
church: \"sosi\".
cigarette: \"siga\".
circle: \"okuro\".
climb: \"cin\".
clock: \"onwanyam oho\".
cloth: \"osoma\".
clothes: \"isoma\".
clothing: \"osoma\".
come: \"yi\".
cook: \"derr\".
count: \"nwain\".
cover: \"pu\".
covered: \"epun\".
cream: \"alo, aloe\".
create: \"dum\".
cup: \"ego amin, ego udi\".
cut: \"gbogbo, lav\".
d: \"d\".
dad: \"osu nomo\".
dance: \"ukpa\".
dancing: \"ukpa\".
dark: \"ibiv\".
date: \"tre\".
daughter: \"omo ovitam\".
day: \"tre\".
dead: \"owute\".
death: \"uwu\".
die: \"wu\".
disease: \"ikpom\".
dish: \"idiom\".
divide: \"kese\".
division: \"kesnete\".
divorced: \"o sikin\".
do: \"kpene\".
door: \"eguw\".
draw: \"gor\".
dream: \"umesne\".
drink: \"udi or nyonw\".
drive: \"yayn\".
dust: \"ovluvul\".
e: \"e\".
ear: \"usow, asow\".
eat: \"di\".
eight: \"inuman, anin\".
eighteen: \"egbein nu inuman\".
eleven: \"egbein nu ovu\".
evening: \"obite\".
everyday: \"trevru tre\".
eye: \"ikmadul\".
f: \"f\".
face: \"adu\".
faith: \"umeme\".
fall: \"dein\".
family: \"ufain, atu\".
far: \"odesin\".
farm: \"kpev\".
fast: \"yasbo\".
fat: \"ubuw, uboow\".
fear: \"egugu\".
female: \"oftam\".
fifteen\' \"egbein nu isuwon\".
fifth: \"onu isuwon\".
fight: \"korn, ukorn\".
fire: \"itain\".
fish: \"esen\".
five: \"isuwon\".
flame: \"itain\".
flash: \"barr\".
fly: \"vev\".
follow: \"duw\".
food: \"idiom\".
forty: \"uva\".
four: \"ini\".
fourteen: \"egbein nu ini\".
fourth: \"onu ini\".
friend: \"over\".
front: \"adu\".
fuel: \"abirr\".
g: \"g\".
girlfriend: \"uga\".
give: \"kiye\".
go: \"ta\".
God: \"Osuo, Oswo\".
good: \"ivi\".
good afternoon: \"odisante\".
good evening: \"obiite\".
good morning: \"owiite\".
goodnight: \"ude emon\".
grandfather: \"osu nomo gina\".
grandmother: \"onuma gina\".
grass: \"itutwain, itutwayn\".
great: \"gina, okor\".
green: \"ungiyo\".
greet: \"kotun, ikota\".
ground: \"utor\".
guest: \"okikiya\".
guitar: \"gita\".
gun: \"alagba\".
guy: \"omoelem\".
h: \"h\".
hair: \"itu\".
hand: \"ubo\".
hard: \"okar\".
have: \"yan\".
head: \"utom\".
hear: \"swene\".
heart: \"ivom\".
heaven: \"oblele\".
heavy: \"mor koya\".
help: \"yonk mubo, yonk ubo\".
her: \"oyi\".
here: \"bana\".
hers: \"onoun\".
high: \"mekun ekun\".
his: \"onoun\".
hold: \"bol\".
hole: \"otoklo\".
home: \"uvay\".
hospital: \"uvay ukokurom\".
hot: \"motwa, mortwa\".
house: \"uvay\".
i: \"i\".
if: \"kam\".
illness: \"ikpom\".
iron: \"ekulele\".
j: \"j\".
job: \"ukpene\".
joy: \"ivom dioma\".
jump: \"sol, sorl\".
k: \"k\".
key: \"sambi\".
kick: \"sa, sar\".
kid: \"omo gberr\".
kill: \"gbiyie\".
kind (caring): \"mor yonk ubo ewei\".
kind (type): \"ude\".
king: \"onu oyan ekein\".
knife: \"elege\".
knock: \"gbolo\".
know: \"deri, derin\".
knowledge: \"inum deriam\".
l: \"l\".
lady: \"omatam\".
land: \"uto, utor\".
language: \"udem ekein\".
laptop: \"komputa\".
large: \"okor, orkor\".
last long: \"yaw oho\".
later: \"oho vi\".
laugh: \"gbeyi\".
laughter: \"agbeyi\".
lazy: \"egbe\".
leaf: \"abi tain, abi tayn\".
lean: \"olamlam\".
learn: \"makne\".
leave: \"yokro\" 
leg: \"avi\".
lend: \"wule\".
lie down: \"blolo, blorlor\".
lie: \"bwo, ibwo\".
life: \"aswei\".
light: \"efufu\".
light (not heavy): \"or koy\".
like: \"blamasen\".
like (similar): \"bokom\".
listen: \"kpakne\".
little: \"omo gberin, imi gberin\".
live: \"yin\".
look: \"gen\".
lost: \"ovaite\".
m: \"m\".
me: \"ume, meh\".
mercy: \"migriri genam\".
midnight: \"ihel asu\".
mind: \"ivom\".
money: \"okpoki, ikpoki\".
morning: \"awiye\".
music: \"ivi\".
n: \"n\".
name: \"ini\".
near: \"kpeki\".
night: \"asu\".
no: \"ihiyn\".
now: \"muna\".
o: \"o\".
offspring: \"ifain\".
on: \"mure\".
on top: \"mekun\".
open: \"venye\".
p: \"p\".
papa: \"osu nomo\".
people: \"ewey, ewei\".
place (location): \"esi, banu\".
please: \"soso\".
praise: \"siv\".
prayer: \"ikpe kpena\".
put: \"nyon\".
q: \"q\".
queen: \"oftam onu oyan ekein\".
r: \"r\".
reach: \"tul\".
read: \"go ubi\".
rest: \"opoki\".
rice: \"arusin\".
road: \"uswei\".
s: \"s\".
sacrifice: \"egba\".
save: \"odarem\".
see: \"mon\".
seen: \"monte\".
show me: \"kakme\".
sickness: \"ikpom\".
sing: \"kpor\".
skin: \"nwo\".
sky: \"oblele\".
sleep: \"umesi\".
something: \"inum\".
soul: \"ema\".
stomach: \"ifain\".
strength: \"ukarr\".
t: \"t\".
talk: \"duko, kwe, ekwe\".
these: \"ina\".
thing: \"inum\".
things: \"irar, ararar\".
this: \"ona\".
thought: \"ivom\".
tie: \"kpo\".
time: \"oho\".
today: \"inina\".
treasures: \"Ingo, ingor\".
u: \"u\".
under: \"utor\".
us: \"eni, neni\".
v: \"v\".
w: \"w\".
wait: \"kpene\".
wake up: \"lomine\".
wall: \"ukpa vai\".
wind: \"oferu\".
x: \"x\".
y: \"y\".
you: \"nwo, uwo\".
yours: \"onuwo\".
z: \"z\".
zoo: \"banu ta genam inam\".

input: what is the word: ability
output: Just say: \"nwe kpenem\".

input: what is the word: above
output: Just say: \"ofun fieknen\".

input: What is the word:  abroad
output: Just say: \"ekein bekein\".

input: what is the word: soul
output:
""",
    **parameters
)
print(f"Response from Model: {response.text}")