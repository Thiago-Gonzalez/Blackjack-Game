#Blackjack Game in Python
#Author: Thiago González
#Git: github.com/Thiago-Gonzalez

from ASCII import cards_ascii
from game_rules import rules
from art import logo
from cards_values import cv
import random
import os

def deal_card():
  '''Returns a random card from the deck.'''
  deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(deck)
  return card

def card_suit(card_value):
  '''Returns a random card suit according to its value.'''
  suit = random.choice(cv[card_value])
  return suit

def calculate_score(cards_list):
  '''Returns the score of a list of cards according to its values.'''
  if sum(cards_list) == 21 and len(cards_list) == 2:
    return 0
  
  if 11 in cards_list and sum(cards_list) > 21:
    cards_list.remove(11)
    cards_list.append(1)
  return sum(cards_list)

def compare(player_score, dealer_score):
  if player_score > 21 and dealer_score > 21:
    return "You lose, both exceeded the limit of 21 😤"
  elif player_score == dealer_score:
    return "It's a draw 🙃"
  elif dealer_score == 0:
    return "You lose, dealer has a Blackjack 😱"
  elif player_score == 0:
    return "You win with a Blackjack 😎"
  elif player_score > 21:
    return "You lose, exceeded the limit of 21 😭"
  elif dealer_score > 21:
    return "You win, dealer exceeded the limit of 21 😁"
  elif player_score > dealer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def start_game():
  print(logo)

  player_cards = []
  player_cards_display = []
  dealer_cards = []
  dealer_cards_display = []

  game_over = False

  for add_cards in range(2):
    player_cards.append(deal_card())
    player_cards_display.append(random.choice(cv[player_cards[-1]]))
    dealer_cards.append(deal_card())
    dealer_cards_display.append(random.choice(cv[dealer_cards[-1]]))
  
  while not game_over:

    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)

    print("Your cards: ")
    for card in player_cards_display:
      print(card)
    input("Press enter. ")
    os.system('clear') or None
    print("Dealer cards: ")
    print(f"{dealer_cards_display[0]}{cards_ascii[52]}")
    input("Press enter. ")
    os.system('clear') or None
    print(f"Your score: {sum(player_cards)}\tDealer's first card score: {dealer_cards[0]}")

    if player_score == 0 or dealer_score == 0 or player_score > 21:
      game_over = True
    else:
      print("Choose an option: \n\t1.Hit\n\t2.Stand")
      game_option = input("Type '1' to get another card or '2' to pass: ")
      if game_option == "1":
          player_cards.append(deal_card())
          player_cards_display.append(random.choice(cv[player_cards[-1]]))
          os.system('clear') or None
      else:
        input("Press enter.")
        os.system('clear') or None
        game_over = True
      
  while dealer_score != 0 and dealer_score < 17 and len(dealer_cards) <= 5:
    dealer_cards.append(deal_card())
    dealer_cards_display.append(random.choice(cv[dealer_cards[-1]]))
    dealer_score = calculate_score(dealer_cards)
  
  print("Your final cards: ")
  for card in player_cards_display:
    print(card)
  input("Press enter.")
  os.system('clear') or None
  print("Dealer's final cards: ")
  for card in dealer_cards_display:
    print(card)
  input("Press enter.")
  os.system('clear') or None
  print(f"Your final score: {sum(player_cards)}\tDealer's final score: {sum(dealer_cards)}")
  print(compare(player_score, dealer_score))


read_rules = input("Do you want to briefly read the Blackjack game rules before starting?\nType 'yes' or 'no': ")
if read_rules == "yes":
  print(f"Blackjack rules: \nCards: {rules['Cards']}\nGame: {rules['Game']}")
while input("Start a game of Blackjack?\nType 'yes' or 'no': ") == 'yes':
  os.system('clear') or None
  start_game()