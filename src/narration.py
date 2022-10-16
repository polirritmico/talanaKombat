#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class Narration():
    def __init__(self, player, on_left_side: bool=False):
        self.name = player.name
        self.on_left = on_left_side


    @staticmethod
    def greetings(p1, p2):
        print("\n--- TALANA KOMBAT ------------------------------------------" \
                "-----")
        print("Bienvenido a la pelea entre:")
        print("{} vs {}".format(p1.name, p2.name))
        print("--------------------------------------------------------------" \
                "---")
        print("Ronda final... ¡¡A pelear!!")


    def take_damage(self, damage):
        if random.randrange(1, 100) > 34:
            return
        messages = [
                "¡Esperen! {} recibe el impacto de lleno"
                .format(self.name),
                "¡OH NO! {} queda sorprendido y recibe todo el impacto"
                .format(self.name),
                ]
        print(random.choice(messages))


    def attack(self, combo, target_player, extra_move_keys):
        target = target_player.name
        damage = combo.power
        attack = combo.name
        if attack[-1] == "a":
            attack = "a " + attack
        else:
            attack = " " + attack

        message_before = "{} ".format(self.name)
        if extra_move_keys != "":
            match extra_move_keys[-1]:
                case "W":
                    message_before += "salta y "
                case "S":
                    message_before += "se agacha y "
                case "D":
                    if self.on_left:
                        message_before += "se adelanta y "
                    else:
                        message_before += "retrocede y "
                case "A":
                    if self.on_left:
                        message_before += "retrocede y "
                    else:
                        message_before += "avanza y "
        message_mid = [
                "lanza un{}".format(attack),
                "connecta un{}".format(attack),
                "encaja un{}".format(attack),
                ]
        message_after_mid = [
                ", impacto directo sobre {}".format(target),
                " con mucha potencia sobre {}".format(target),
                ]
        message_end = [
                ". Causándole {} puntos de doloroso daño."
                .format(damage),
                ". Esos {} de daño deben doler bastante."
                .format(damage),
                ", quien al parecer soporta bien esos {} de daño."
                .format(damage)
                ]
        full_message = message_before
        full_message += random.choice(message_mid)
        full_message += random.choice(message_after_mid)
        full_message += random.choice(message_end)
        print(full_message)


    def move_only(self, rival):
        messages = [
                "{} se pasea por el lugar esperando el momento de atacar"
                .format(self.name),
                "{} se mueve esperando una abertura en la defensa de {}"
                .format(self.name, rival.name),
                "{} cambia de posición en la arena"
                .format(self.name),
                ]
        print(random.choice(messages))


    def nothing(self):
        messages = [
                "{} se queda mirando el horizonte"
                .format(self.name),
                "¡{} parece confundido y no hace nada!"
                .format(self.name),
                "¡{} se queda petrificado en medio del combate!"
                .format(self.name),
                ]
        print(random.choice(messages))

    
    def falls_unconscious(self):
        messages = [
                "¡Ese golpe ha sido durísimo! ¡{} cae inconsciente!"
                .format(self.name),
                "¡{} se desploma sobre el suelo!".
                format(self.name),
                "¡Y cae! ¡Y {} cae inconsciente! ¡Todo el público enloquece!"
                .format(self.name),
                ]
        print(random.choice(messages))


    def end_combat(self, rival: str, hp: int):
        messages = [
                "\nY ese ha sido el final de este emocionante combate.",
                "\nY así termina otra emocinante batalla en TalanaKombat.",
                "\nFinaliza entonces el combate.",
                "\nBueno, otro excelente combate que llega a su fin."
                ]
        print(random.choice(messages))
        print("La victoria se la lleva {}\n¡Hasta pronto!".format(self.name))
        print("\n--- RESULTADO: ---------------------------------------------" \
                "-----")
        print("{} vs {}\nGanador: {} con {} puntos de energía restantes"
              .format(self.name, rival, self.name.upper(), hp))
        print("--------------------------------------------------------------" \
                "---")


