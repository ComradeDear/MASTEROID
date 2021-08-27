from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("")
print("""Welcome To MASTEROID string session generator""")
print("""Kindly Enter Your Details To Continue ! """)

API_KEY = input("API_KEY: ")
API_HASH = input("API_HASH: ")

while True:
 try:
  with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
   print(
       "String Sent To Your Saved Message, Store It To A Safe Place!! "
   )
   print("")
   session = client.session.save()
   client.send_message(
       "me",
       f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it)👇 \n\n {session} \n\n"
   )

   print(
       "Thanks for Choosing MASTEROID... Have A Good Time...."
   )
 except:
  print("")
  print(
      "Wrong phone number \n make sure its with correct country code. Example : +91 123456789 ! Kindly Retry"
  )
  print("")
  continue
 break
