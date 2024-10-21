from abc import ABC, abstractmethod
import itertools
import random
from time import sleep

class Player:
    def __init__(self, balance=0):
        self.balance = balance

class CassaNiquel:

    def __init__(self, level=1, balance=0):
        self.SIMBOLOS = {
            'GRAPES': 'U+1F347',       # UVA
            'ORANGE': 'U+1F34A',       # LARANJA
            'BANANA': 'U+1F34C',       # BANANA
            'STRAWBERRY': 'U+1F353',   # MORANGO
            'WATERMELON': 'U+1F349'     # MELANCIA
        }
        self.level = level
        self.permutations = self._gen_permutations()
        self.balance = balance

    def _gen_permutations(self):
        permutations = list(itertools.product(self.SIMBOLOS.keys(), repeat=3))
        
        for _ in range(self.level):
            for symbol in self.SIMBOLOS.keys():
                permutations.append((symbol, symbol, symbol))
        return permutations

    def _get_final_result(self):
        result = random.choice(self.permutations)
        
        if len(set(result)) == 3 and random.randint(0, 5) >= 2:
            result = list(result)
            result[1] = result[0]

        return tuple(result)

    def _display(self, amount_bet, result, time=0.3):
        seconds = 2
        for _ in range(0, int(seconds / time)):
            print(self._emojize(random.choice(self.permutations)))
            sleep(time)
            
         
        print(self._emojize(result))

        if self._check_result_user(result):
            print(f"Você venceu e recebeu: {amount_bet * 3}")
        else:
            print('Tente novamente')

    def _emojize(self, emojis):
        return "".join(chr(int(self.SIMBOLOS[code][2:], 16)) for code in emojis)

    def _check_result_user(self, result):
        return all(x == result[0] for x in result)

    def _update_balance(self, amount_bet, result, player: Player):
        if self._check_result_user(result):
            self.balance -= amount_bet  # Aumenta o saldo da máquina
            player.balance += (amount_bet * 3)  # 3x a aposta
        else:
            self.balance += amount_bet  # Aumenta o saldo da 
            player.balance -= amount_bet  # Diminui o saldo 

    def play(self, amount_bet, player: Player):
        if amount_bet > player.balance:
            print("Saldo insuficiente para jogar.")
            return
        
        result = self._get_final_result()
        self._display(amount_bet, result)
        self._update_balance(amount_bet, result, player)


maquinal = CassaNiquel(level=2)
player1 = Player(balance=50)  # Define um saldo inicial para o jogador

# Realiza 5 jogadas
for _ in range(5):
    maquinal.play(10, player1)

# Exibe o saldo da máquina e do jogador
print(f"Saldo da máquina: {maquinal.balance}")
print(f"Saldo do jogador: {player1.balance}")

