
import random
import logging
#logging.basicConfig(level=logging.INFO)

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4


# deal: Crea un arreglo hand y la llena de manera random
# elimina los números dados de la mano global "deck" y
# si la carta tiene un valor de 11,12, 13, 14 le asigna 
# una letra.

def deal():
  global deck
  deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
  hand = []
  for i in range(2):
    random.shuffle(deck)
    card = deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
  return hand

def deal_Card():
  global deck
  deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
  hand = []
  for i in range(1):
    random.shuffle(deck)
    card = deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
  return hand

# select_hand: Método para seleccionar una nueva mano
def select_hand(hand, new_hand):
  selected_hand = hand
  trigger = True
  action = 0;
 
  while trigger == True:
    action = input("Ahora tienes dos manos, elige cuál deseas escoger para seguir jugando:\n  1.Mano principal -> " + str(hand) + "\n  2.Mano nueva -> " + str(new_hand)+"\n").lower()
    assert action in ["1", "2"]

    if action == "1":
      print("Haz seleccionado la mano 1")
      trigger = False
    elif action == "2":
      print("Haz seleccionado la mano 2")
      selected_hand = new_hand
      trigger = False
    else:
      print("Haz seleccionado una mano inválida, prueba otra vez")
  return select_hand

# split: Si el jugador tiene dos carstas iguales, las divide en dos mazos distintos 
# y otorga una nueva carata a cada uno.
def split(hand):
  nueva = deal()
  hand =[4,4]
  aux_card = ''
  counter=0
  selected_hand = hand;
  split = False

  for card in hand:
    if (card == aux_card):
      print(str(card) + " y " + str(aux_card) +" son iguales. Puedes dividir")
      split = True
      hand.pop(counter)
      nueva.pop()
      nueva.append(card)
      # Da nuevas caratas, una a cada mano
      hand.append(deal_Card())
      nueva.append(deal_Card())

    aux_card = card
    counter = counter +1
  if split == True:
    selected_hand = select_hand(hand, nueva)
  return select_hand

def total(hand, return_usable_ace=False):
  total = 0
  aces = 0
  used_aces = 0
  for card in hand:
    if card == "J" or card == "Q" or card == "K":
      total += 10
    elif card == "A":
      total += 1
      aces += 1
    else:
      total += card
  if total < 11 and aces > 0:
    total += 10
    used_aces += 1
  if return_usable_ace:
    return (total, used_aces)
  else:
    return total


def hit(hand):
  card = deck.pop()
  if card == 11:card = "J"
  if card == 12:card = "Q"
  if card == 13:card = "K"
  if card == 14:card = "A"
  hand.append(card)
  return hand


def print_results(dealer_hand, player_hand):
  logging.info("El dealer tiene un" + str(dealer_hand) + " para un total de " + str(total(dealer_hand)))
  logging.info("Tu tienes " + str(player_hand) + " para un total de  " + str(total(player_hand)))


def score(dealer_hand, player_hand):
  print_results(dealer_hand, player_hand)
  if total(player_hand) == 21:
    logging.info("¡Felicitaciones, ganaste! ¡Tienes un Blackjack!\n")
    return 1.0
  elif total(dealer_hand) == 21:
    logging.info("Perdiste. El dealer gana con un Blackjack.\n")
    return -1.0
  elif total(player_hand) > 21:
    logging.info("Lo siento, te pasaste de 21 y perdiste\n")
    return -1.0
  elif total(dealer_hand) > 21:
    logging.info("El dealer se pasó de 21. ¡Ganaste!\n")
    return 1.0
  elif total(player_hand) < total(dealer_hand):
    logging.info("Lo siento! Tu puntuación es menos que la del dealer, perdiste.\n")
    return -1.0
  elif total(player_hand) > total(dealer_hand):
    logging.info("Felicitaciones! Ganaste!, tu puntuación es más grande que la del dealer\n" )
    return 1.0
  else:
    logging.info("Un empate")
    return 0.0

def game(get_player_action):

  # store list of data that
  player_data_lst = []
  logging.info("Bienvenido a Blackjack!\n")
  
  dealer_hand = deal() #Da carats aleatorias al jugador
  player_hand = deal()
  choice = 0
  reward = -2.0
  while choice != "q":
    logging.info("El dealer muestra " + str(dealer_hand[0]))
    logging.info("Tu tienes " + str(player_hand) + " para un total de " + str(total(player_hand)))
    # si alguno de los jugadores llega a 21 automáticamente se queda ahí con stand.
    if total(player_hand) >= 21 or total(dealer_hand) >= 21: 
      choice = "s"
    else:
      action_state = get_player_action(player_hand, dealer_hand[0])
      choice = action_state[0]
      player_data_lst.append(action_state)
    if choice == "h":
      hit(player_hand)
    elif choice == "s":
      while total(dealer_hand) < 17:
        hit(dealer_hand)
      reward = score(dealer_hand, player_hand)
      choice = "q"
    elif choice == "sp":
      print("Ha seleccionado dividir")
      split(player_hand)
    	# player_hand = split(player_hand)
    	
    	
  final_state = (player_hand, dealer_hand)
  return (reward, player_data_lst, final_state)


def interactive_action(player_hand, dealer_hand):
 
  action = input("Quieres [H]it(Pedir carta), [S]tand(Plantarte),[Sp]Split(Separar), o [Q]uit(Salir): ").lower()
  assert action in ["s", "h","sp", "q"]
  return (action, ())


if __name__ == "__main__":
  logging.getLogger().setLevel(logging.INFO)
  print("Juguemos 21!")
  # Puntuación, listado de jugadas ,estado final
  (reward, player_data_lst, final_state) = game(interactive_action)
  # print(f"reward: {reward}")
  # print(f"Listado de jugadas: {player_data_lst}")
  print(f"Mano final: {final_state}")

