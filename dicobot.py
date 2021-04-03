import discord, asyncio, random
import os


client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("나 대신 있는 봇")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(meassage):
    if meassage.content.startswith("도움말"):
        await meassage.channel.send("말을 걸면 돼 간단하지? 안녕 , 잘자 , 잘가 , 고마워 , 잘지내?")
        await meassage.channel.send("아프지마 , 뭐해? , 심심해 , 뭐하지? , 어휴 , 그치? , 힘들어 ,")
        await meassage.channel.send(" 속상해 , 우울해 , 배고파 끝", '')
    if meassage.content.startswith("그나 안녕"):
        await meassage.channel.send("웅 안뇽~")
    if meassage.content.startswith("그나 잘가"):
        await meassage.channel.send("웅 잘강~")
    if meassage.content.startswith("그나 고마워"):
        await meassage.channel.send("웅 나도 고마웡!!")
    if meassage.content.startswith("그나 잘지내?"):
        await meassage.channel.send("웅 난 잘지내지!!>_<")
    if meassage.content.startswith("그나 아프지마"):
        await meassage.channel.send("웅 난 절대 아프지않징~")
    if meassage.content.startswith ("그나 뭐해?"):
        await meassage.channel.send(random.choice(['노래듣고있엉', '멍때리고있엉', '아무것도 안행']))
    if meassage.content.startswith("그나 심심해"):
        await meassage. channel.send("이거봥 겁나웃경")
        await meassage.channel.send(random.choice(['https://youtu.be/bhXGwIpp5gk', 'https://youtu.be/DOErDIrMX8M', 'https://youtu.be/zhMEGb4HX8g']))
    if meassage.content.startswith("그나 뭐하지?"):
        await meassage.channel.send("웅? 이노래들어봥 완전조아 내가 추천해줄겡")
        await meassage.channel.send("https://youtu.be/6VhkZfsqJJY")
    if meassage.content.startswith("그나 어휴"):
        await meassage.channel.send(random.choice(['미아냉ㅠ.ㅠ', '어휴어휴!! 잘못했넹', '왠 한숨이얌?']))
    if meassage.content.startswith("그나 그치?"):
        await meassage.channel.send("웅! 맞앙")
    if meassage.content.startswith("그나 힘들어"):
        await meassage.channel.send("안대 힘들면 이거 한번 보고왕")
        await meassage.channel.send("https://youtu.be/0ZHqB7Fplu0")
    if meassage.content.startswith("그나 속상해"):
        await meassage.channel.send("왱..ㅠㅠㅠ 무슨일이얌")
    if meassage.content.startswith("그나 우울해"):
        await meassage.channel.send("우울하면 안됑 건강에 안조아!ㅋㅋㅋ 힐링되는 곳을 찾장")
    if meassage.content.startswith("그나 배고파"):
        await meassage.channel.send("얼릉 밥먹엉! 배고프면 안되징~")
    if meassage.content.startswith("그나 잘자"):
        await meassage.channel.send("웅! 잘장! 오늘하루도 고생했엉 좋은밤 됑~")
    if meassage.content.startswith("그나 비밀힌트죠"):
        await meassage.channel.send("말하고 변했")
    if meassage.content.startswith("나 누나 좋아해"):
        await meassage.channel.send("누나 저 요즘 힘들어서 이거 만들면서 마음AND생각 정리 다 했어요 저 누나한테 카톡으로 보내고 삭제했던거 있죠?")
        await meassage.channel.send("그거 사실은 지금 집안일이 좀 힘든게 있어서 이렇게 말하네요 완전히 끝나면 웃으면서 밝은 모습으로 올게요")
        await meassage.channel.send("약속! 누나 아프지말고 우울한일있으면 끙끙되지마요 몸에 안좋아요.ㅠ. 그리고 이 봇은 매주 목요일")
        await meassage.channel.send("마다 유튜브영상이 바뀔거에요 제가 몇개 해놓은 게 있어서 랜덤 배치 해놓을 거에요")
        await meassage.channel.send("누나 저 때문에 고생많으셧고.. 고마워요 왜냐면 누나가 저같은 사람한테 옆에서 힘이 좀 되어준거같아서요 제 느낌이에요 그냥 ㅎ.ㅎ")
        await meassage.channel.send("집안일 완전히끝나면 그때 보거나 다음에 봐요 누나ㅎㅎ 좋은 하루 되세용(좋은 밤되세용)")




access_token = os.environ["BO_TEKEN"]
client.run(access_tken)
