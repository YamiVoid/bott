import random
import asyncio
from highrise import BaseBot, Position, AnchorPosition
from highrise.models import SessionMetadata, User, CurrencyItem, Item
from highrise.__main__ import main, BotDefinition
from typing import Union


class Bot(BaseBot):
  greetings = [
      "أهلاً وسهلاً في الروم {username} 😎🔥 نورتنا!",
      "يا هلا فيك يا {username} 🌟، الله يحييك!",
      "مرحباً {username} 😍، اللمعة هنا أكثر بوجودك!",
      "أهلاً بقدومك {username} 👐🏼، المكان صار أروع الآن!",
      "واو! {username} دخل الروم 🚀💥، النور نورك!",
      "مرحبا {username} 🌟، هلأ نورنا بوجودك في الروم!",
      "سلامات {username} 🖐🏼، نورت الروم فيك!",
  ]

  dance_mapping = {
      "1": "emote-tired",
      "2": "emoji-thumbsup",
      "3": "emoji-angry",
      "4": "dance-macarena",
      "5": "emote-hello",
      "6": "dance-weird",
      "7": "emote-superpose",
      "8": "idle-hero",
      "9": "emote-wings",
      "10": "emote-laughing",
      "11": "emote-kiss",
      "12": "emote-wave",
      "13": "emote-hearteyes",
      "14": "emote-theatrical",
      "15": "emote-teleporting",
      "16": "emote-slap",
      "17": "emote-ropepull",
      "18": "emote-think",
      "19": "emote-hot",
      "20": "dance-shoppingcart",
      "21": "emote-greedy",
      "22": "emote-frustrated",
      "23": "emote-float",
      "24": "emote-baseball",
      "25": "emote-yes",
      "26": "idle-floorsleeping",
      "27": "idle-enthusiastic",
      "28": "emote-confused",
      "29": "emoji-celebrate",
      "30": "emote-no",
      "31": "emote-swordfight",
      "32": "emote-shy",
      "33": "dance-tiktok2",
      "34": "emote-model",
      "35": "emote-charging",
      "36": "emote-snake",
      "37": "dance-russian",
      "38": "emote-sad",
      "39": "emoji-cursing",
      "40": "emoji-flex",
      "41": "emoji-gagging",
      "42": "dance-tiktok8",
      "43": "dance-blackpink",
      "44": "dance-pennywise",
      "45": "emote-bow",
      "46": "emote-curtsy",
      "47": "emote-snowball",
      "48": "emote-snowangel",
      "49": "emote-telekinesis",
      "50": "emote-maniac",
      "51": "emote-energyball",
      "52": "emote-frog",
      "53": "emote-cute",
      "54": "dance-tiktok9",
      "55": "dance-tiktok10",
      "56": "emote-pose7",
      "57": "emote-pose8",
      "58": "idle-dance-casual",
      "59": "emote-pose1",
      "60": "emote-pose3",
      "61": "emote-pose5",
      "62": "emote-cutey",
      "63": "emote-relaxing",
      "64": "emote-model",
      "65": "emote-curtsy",
      "66": "emote-frog",
      "67": "dance-macarena",
      "68": "emote-kiss",
      "69": "emote-sad",
      "70": "emote-laughing",
      "71": "emote-hello",
      "72": "emote-outfit",
      "73": "emoji-thumbsup",
      "74": "emote-pose12",
      "75": "emote-shy",
      "76": "dance-tiktok5",
      "77": "emote-fading",
      "78": "emote-dinner",
      "79": "emote-opera",
      "80": "dance-hiphop",
      "81": "emoji-angry",
      "82": "dance-tiktok15",
      "83": "dance-tiktok6",
      "84": "emote-breakscreen",
      "85": "emote-juggling",
      "86": "emote-thief",
      "87": "emote-shocked",
      "88": "emote-flirt",
      "89": "emote-outfit2",
      "90": "emote-fireworks",
      "91": "emote-musclepose",
      "92": "dance-tiktok7",
      "93": "emote-dropped",
      "94": "emote-oops",
      "95": "emote-wavey",
      "96": "emote-cold",
      "97": "emote-twitched",
      "98": "emote-surf",
      "99": "emote-pose11",
      "100": "dance-tiktok16",
      "101": "dance-shuffle",
      "102": "dance-tiktok3",
      "103": "dance-tiktok1",
      "104": "emote-cartwheel",
      "105": "emote-electrified",
      "106": "emote-dramatic",
      "107": "emote-purr",
      "108": "emote-armcannon",
      "109": "emote-fruity",
      "110": "dance-cheerleader",
      "111": "emote-magnetic",
      "112": "emote-trampoline",
      "113": "emote-shrink",
      "114": "emote-puppet",
      "115": "emote-pushups",
      "116": "dance-duckwalk",
      "117": "dance-voguehands",
      "118": "emote-giveup",
      "119": "emote-pray",
      "120": "emote-collapse",
      "121": "emote-panic",
      "122": "emote-boo",
      "123": "emote-elbowbump",
      "124": "emote-hugyourself",
      "125": "emote-jetpack",
      "126": "emote-judochop",
      "127": "emote-levelup",
      "128": "dance-nightfever",
      "129": "emote-peace",
      "130": "emote-peekaboo",
      "131": "dance-proposing",
      "132": "emote-rainbow",
      "133": "emote-ropepull",
      "134": "emote-sumofight",
      "135": "emote-superpunch",
      "136": "emote-relaxing",
      "137": "emote-ponder",
      "138": "dance-gangnamstyle",
      "139": "dance-wiggle",
      "140": "dance-feelthebeat",
      "141": "emote-happy",
      "142": "emote-hug",
      "143": "emote-slap",
      "144": "emote-exasperated",
      "145": "dance-tapedance",
      "146": "emote-thumbsuck",
      "147": "emote-heartfingers",
      "148": "dance-aerobics",
      "149": "emote-heartshape",
      "150": "emote-hearteyes",
      "151": "emote-think",
      "152": "emote-stunned",
      "153": "emote-embarrassed",
      "154": "emote-blastoff"
  }

  async def repeat_message(self, text: str, interval: int):
    try:
      while True:
        await self.highrise.chat(text)
        await asyncio.sleep(interval)
    except asyncio.CancelledError:
      pass

  moderators = {
      "Sh0RT",
      "Darwin699",
      "lokmane",
      "YamiVoid",
      "Tissa_NG",
      "its__me17",
      "sarah_vxs21",
      "islammami",
      "R0__YA",
      "khalil111111",
  }

  # Positions
  vip_position = Position(5, 20, 2, "FrontRight")
  second_position = Position(1, 12, 8, "FrontRight")
  third_position = Position(10, 0, 7, "FrontRight")
  bot_position = Position(10, 1, 1, "FrontRight")

  users_in_room = {}
  following_user = None
  follow_mode = False
  dance_tasks = {}
  bot_dance_task = None

  async def on_start(self, session_metadata: SessionMetadata) -> None:
    print("✅ Bot started")
    self.bot_user_id = session_metadata.user_id
    await self.highrise.teleport(self.bot_user_id, self.bot_position)
    self.bot_dance_task = asyncio.create_task(self.continuous_dancing())

  async def continuous_dancing(self):
    while True:
      try:
        random_dance = random.choice(list(self.dance_mapping.values()))
        await self.highrise.send_emote(random_dance, self.bot_user_id)
        await asyncio.sleep(5)
      except Exception as e:
        print(f"Error in continuous_dancing: {e}")
        await asyncio.sleep(1)

  async def on_user_join(self, user: User,
                         position: Union[Position, AnchorPosition]) -> None:
    self.users_in_room[user.username] = user.id
    greeting = random.choice(self.greetings).format(username=user.username)
    await self.highrise.chat(greeting)

  async def on_user_leave(self, user: User) -> None:
    self.users_in_room.pop(user.username, None)
    if user.username == self.following_user:
      self.follow_mode = False
      self.following_user = None
    if user.username in self.dance_tasks:
      self.dance_tasks[user.username].cancel()
      del self.dance_tasks[user.username]

  async def on_tip(self, sender: User, receiver: User,
                   tip: CurrencyItem | Item) -> None:
    if isinstance(tip, CurrencyItem):
      await self.highrise.chat(
          f"شكراً لك {sender.username} على التبرع ـ {tip.amount} 💛")

  async def on_chat(self, user: User, message: str) -> None:
    print(f"{user.username}: {message}")

    if message.lower().startswith("duel @"):
      try:
        parts = message.split()
        if len(parts) == 3:
          target = parts[1][1:]  # Remove @
          dance_num = parts[2]

          if target in self.users_in_room:
            if dance_num in self.dance_mapping:
              dance = self.dance_mapping[dance_num]
              await asyncio.gather(
                  self.highrise.send_emote(dance, user.id),
                  self.highrise.send_emote(dance, self.users_in_room[target]))
              await self.highrise.chat(
                  f"🎵 {user.username} و {target} يرقصان معاً! 🎵")
            else:
              await self.highrise.chat(
                  f"❌ رقم رقص غير صحيح. جرب 1-{len(self.dance_mapping)}")
          else:
            await self.highrise.chat(f"❌ {target} غير موجود بالغرفة")
        else:
          await self.highrise.chat("❌ استخدم: dancewith @username رقم_الرقص")
      except Exception as e:
        print(f"Dance error: {e}")
        await self.highrise.chat("❌ حدث خطأ في الرقص")

    elif message.lower().startswith("dance @"):
      try:
        parts = message.split()
        if len(parts) == 3:
          target_username = parts[1][1:]  # Remove @
          dance_num = parts[2]

          if target_username in self.moderators:
            if dance_num in self.dance_mapping:
              await self.highrise.send_emote(
                  self.dance_mapping[dance_num],
                  self.users_in_room[target_username])
            else:
              await self.highrise.chat(
                  f"رقص غير صحيح. الأرقام المتاحة: {', '.join(self.dance_mapping.keys())}"
              )
          else:
            await self.highrise.chat(f"{target_username} غير موجود في الغرفة")
        else:
          await self.highrise.chat("استخدم: dual @username رقم_الرقص")
      except Exception as e:
        print(f"Dual command error: {e}")
        await self.highrise.chat("حدث خطأ في الأمر")

    elif message.lower().startswith(
        "dall ") and user.username in self.moderators:
      try:
        dance_num = message.split()[1]
        if dance_num in self.dance_mapping:
          emote = self.dance_mapping[dance_num]
          room_users = await self.highrise.get_room_users()
          for member, _ in room_users.content:
            try:
              await self.highrise.send_emote(emote, member.id)
            except Exception as e:
              print(f"Couldn't make {member.username} dance: {e}")
        else:
          await self.highrise.chat(
              f"رقص غير صحيح. استخدم رقم من 1 إلى {len(self.dance_mapping)}")
      except Exception as e:
        print(f"Dance all error: {e}")
        await self.highrise.chat("❌ استخدم: dall رقم_الرقص")

    elif message.startswith("say "):
      try:
        if user.username not in self.moderators:
          await self.highrise.chat("❌ هذا الأمر مخصص فقط للمشرفين.")
          return
        msg_body = message[5:].strip()
        if msg_body.endswith("s"):
          parts = msg_body.rsplit(" ", 1)
          if len(parts) == 2:
            say_text = parts[0]
            interval = int(parts[1][:-1])
            if hasattr(self, "say_task") and self.say_task:
              self.say_task.cancel()
            self.say_task = asyncio.create_task(
                self.repeat_message(say_text, interval))
            await self.highrise.chat(
                f"🔁 Repeating every {interval} seconds: {say_text}")
          else:
            await self.highrise.chat("❌ Please format like: !say your text 5s")
        else:
          await self.highrise.chat("❌ End with a time like 5s (for seconds).")
      except Exception as e:
        await self.highrise.chat(
            "❌ Error in !say format. Use: !say your message 5s")
        print("Error in !say command:", e)

    elif message.strip() == "shutup":
      if user.username not in self.moderators:
        await self.highrise.chat("❌ هذا الأمر مخصص فقط للمشرفين.")
        return
      if hasattr(self, "say_task") and self.say_task:
        self.say_task.cancel()
        self.say_task = None
        await self.highrise.chat(" Stopped repeating message.")

    elif message.strip() == "vip" and user.username in self.moderators:
      await self.highrise.teleport(user.id, self.vip_position)
      await self.highrise.chat(f"{user.username} تم نقلك إلى VIP 🚀")

    elif message.strip() == "up":
      await self.highrise.teleport(user.id, self.second_position)
      await self.highrise.chat(f"{user.username} تم نقلك إلى المكان الثاني 🚀")

    elif message.strip() == "down":
      await self.highrise.teleport(user.id, self.third_position)
      await self.highrise.chat(f"{user.username} تم نقلك إلى المكان الثالث 🚀")

    elif message.startswith("vip @") and user.username in self.moderators:
      target_username = message.split("vip @")[1].strip()
      if target_username in self.users_in_room:
        await self.highrise.teleport(self.users_in_room[target_username],
                                     self.vip_position)
        await self.highrise.chat(f"{target_username} تم نقله إلى VIP 🚀")
      else:
        await self.highrise.chat(f"{target_username} غير موجود في الروم.")

    elif message.strip() == "sleep" and user.username in self.moderators:
      room_users = await self.highrise.get_room_users()
      for member, _ in room_users.content:
        try:
          await self.highrise.send_emote("idle-floorsleeping", member.id)
        except Exception as e:
          print(f"❌ Couldn't make {member.username} sleep: {e}")

    elif message.strip() in self.dance_mapping:
      emote = self.dance_mapping[message.strip()]
      if user.username in self.dance_tasks:
        self.dance_tasks[user.username].cancel()
      task = asyncio.create_task(self.loop_dance(user, emote))
      self.dance_tasks[user.username] = task

    elif message.strip() in ["توقف رقص", "stopd"]:
      if user.username in self.dance_tasks:
        self.dance_tasks[user.username].cancel()
        del self.dance_tasks[user.username]
        await self.highrise.chat(f"{user.username} تم إيقاف الرقص.")
      else:
        await self.highrise.chat(f"{user.username} أنت لا ترقص حالياً.")

    elif message.startswith("mute @") and user.username in self.moderators:
      try:
        parts = message.split()
        target_username = parts[1][1:]
        duration = int(parts[2]) * 60 if len(parts) > 2 else 60 * 60
        duration = min(duration, 1440 * 60)
        room_users = await self.highrise.get_room_users()
        for u, _ in room_users.content:
          if u.username == target_username:
            await self.highrise.moderate_room(u.id,
                                              "mute",
                                              action_length=duration)
            await self.highrise.chat(
                f"{target_username} تم كتمه لمدة {duration // 60} دقيقة 🔇")
            break
        else:
          await self.highrise.chat(f"{target_username} غير موجود في الروم.")
      except Exception as e:
        print(f"Mute Error: {e}")
        await self.highrise.chat("حدث خطأ أثناء تنفيذ أمر الكتم.")

    elif message.startswith("summon @") and user.username in self.moderators:
      try:
        target_username = message.split("summon @")[1].strip()
        room_users = await self.highrise.get_room_users()

        summoner_pos = None
        target_user_id = None

        for room_user, pos in room_users.content:
          if room_user.username == user.username:
            summoner_pos = pos
          if room_user.username == target_username:
            target_user_id = room_user.id

        if not summoner_pos:
          await self.highrise.chat("Couldn't determine your position!")
          return

        if not target_user_id:
          await self.highrise.chat(f"{target_username} is not in the room!")
          return

        await self.highrise.teleport(target_user_id, summoner_pos)
        await self.highrise.chat(
            f"✨ {target_username} has been summoned to your location!")

      except Exception as e:
        print(f"Summon error: {e}")
        await self.highrise.chat("Failed to summon user. Please try again.")

    elif message.startswith("tp @") and user.username in self.moderators:
      try:
        target_username = message.split("tp @")[1].strip()
        room_users = await self.highrise.get_room_users()

        target_pos = None
        sender_id = user.id

        for room_user, pos in room_users.content:
          if room_user.username.lower() == target_username.lower():
            target_pos = pos
            break

        if not target_pos:
          await self.highrise.chat(f"{target_username} is not in the room!")
          return

        if isinstance(target_pos, Position):
          sender_facing = "FrontRight"
          for u, pos in room_users.content:
            if u.id == sender_id and hasattr(pos, 'facing'):
              sender_facing = pos.facing
              break

          new_pos = Position(x=target_pos.x,
                             y=target_pos.y,
                             z=target_pos.z,
                             facing=sender_facing)

          await self.highrise.teleport(sender_id, new_pos)
          await self.highrise.chat(
              f"✨ {user.username} teleported to {target_username}!")

      except Exception as e:
        print(f"Teleport error: {e}")
        await self.highrise.chat(f"Failed to teleport: {str(e)}")

    elif message.startswith("ban @") and user.username in self.moderators:
      try:
        parts = message.split()
        target_username = parts[1][1:]
        duration = int(parts[2]) * 60 if len(parts) > 2 else 60 * 60
        duration = min(duration, 1440 * 60)
        room_users = await self.highrise.get_room_users()
        for u, _ in room_users.content:
          if u.username == target_username:
            await self.highrise.moderate_room(u.id,
                                              "ban",
                                              action_length=duration)
            await self.highrise.chat(
                f"{target_username} تم حظره لمدة {duration // 60} دقيقة 🚫")
            break
        else:
          await self.highrise.chat(f"{target_username} غير موجود في الروم.")
      except Exception as e:
        print(f"Ban Error: {e}")
        await self.highrise.chat("حدث خطأ أثناء تنفيذ أمر الحظر.")

  async def loop_dance(self, user: User, emote: str) -> None:
    while user.username in self.dance_tasks:
      try:
        await self.highrise.send_emote(emote, user.id)
        await asyncio.sleep(5)
      except Exception as e:
        print(f"Loop dance error for {user.username}: {e}")
        break


ROOM_ID = "65d9b911dbf45887f1ddc811"
BOT_TOKEN = "5c2951838dc9d877fd9db6d2d0a1328e92820eb47520e156dc7cdc53be4f3d87"

if __name__ == "__main__":
  asyncio.run(main([BotDefinition(Bot(), ROOM_ID, BOT_TOKEN)]))
