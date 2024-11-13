#analiza 1 - ispisat će se 2 i 4

broj = 0
while broj < 5:
  broj +=2 
  print(broj)

#analiza 2 - prikazana petlja je beskonačna jer se neprestano događa ista
#akcija, dodaje se 1 i oduzima 1 i broj je uvijek manji od 

# broj = 0
# while broj < 5:
#   broj += 1
#   print(broj)
#   broj -= 1

#analiza 3 - uvjet broj += 2 stalno povećava broj za 2, te se broj nikad neće
#smanjiti na 0 i završiti petlju

broj = 10
while broj > 0:
  broj -= 1
  print(broj)
  if broj < 5:
    broj += 2