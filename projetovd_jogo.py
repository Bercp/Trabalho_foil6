#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vida OOP Game (console) — v2 (atividades atualizadas)
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional
import sys


class LifeStage:
    name: str = "LifeStage"
    age_range: Tuple[int, Optional[int]] = (0, None)  # (min, max)
    xp_goal: int = 3  # meta padrão de XP para subir de nível
    
    def activities(self) -> List[str]:
        return []
    
    def perform_activity(self, person: "Person", activity: str) -> str:
        raise NotImplementedError
    
    def in_range(self, age: int) -> bool:
        mn, mx = self.age_range
        return age >= mn and (mx is None or age <= mx)
    
    def next_stage_min_age(self) -> Optional[int]:
        return None


class Baby(LifeStage):
    name = "Bebê"
    age_range = (0, 5)
    xp_goal = 2
    
    def activities(self) -> List[str]:
        # Bebê:
        return ["Engatinhar", "Chorar", "Dormir"]
    
    def perform_activity(self, person: "Person", activity: str) -> str:
        if activity == "Engatinhar":
            person._skills["coordenação"] += 1
            person._energy -= 1
            person._xp += 1
            return "Você engatinhou! +1 coordenação, -1 energia, +1 XP."
        elif activity == "Chorar":
            person._skills["linguagem"] += 1
            person._energy -= 1
            person._xp += 1
            return "Você chorou (comunicação básica)! +1 linguagem, -1 energia, +1 XP."
        elif activity == "Dormir":
            person._energy = min(person._energy + 3, 10)
            return "Soneca boa! +3 energia."
        return "Atividade não reconhecida."


class Child(LifeStage):
    name = "Criança"
    age_range = (6, 12)
    xp_goal = 3
    
    def activities(self) -> List[str]:
        # Criança:
        return ["Brincar na rua", "Jogar Videogame", "Dormir"]
    
    def perform_activity(self, person: "Person", activity: str) -> str:
        if activity == "Brincar na rua":
            person._skills["coordenação"] += 1
            person._skills["saúde"] += 1
            person._energy -= 1
            person._xp += 1
            return "Você brincou na rua! +1 coordenação, +1 saúde, -1 energia, +1 XP."
        elif activity == "Jogar Videogame":
            person._skills["coordenação"] += 1
            person._skills["criatividade"] += 1
            person._energy -= 1
            person._xp += 1
            return "Jogou videogame! +1 coordenação, +1 criatividade, -1 energia, +1 XP."
        elif activity == "Dormir":
            person._energy = min(person._energy + 3, 10)
            return "Dormiu bem! +3 energia."
        return "Atividade não reconhecida."


class Teen(LifeStage):
    name = "Adolescente"
    age_range = (13, 17)
    xp_goal = 4
    
    def activities(self) -> List[str]:
        # Adolescente:
        return ["Estudar", "Jogar Futebol", "Jogar Videogame", "Dormir"]
    
    def perform_activity(self, person: "Person", activity: str) -> str:
        if activity == "Estudar":
            person._skills["conhecimento"] += 2
            person._energy -= 2
            person._xp += 1
            return "Estudou firme! +2 conhecimento, -2 energia, +1 XP."
        elif activity == "Jogar Futebol":
            person._skills["saúde"] += 2
            person._skills["coordenação"] += 1
            person._energy -= 2
            person._xp += 1
            return "Jogou futebol! +2 saúde, +1 coordenação, -2 energia, +1 XP."
        elif activity == "Jogar Tibia":
            person._skills["coordenação"] += 1
            person._skills["criatividade"] += 1
            person._energy -= 1
            person._xp += 1
            return "Jogou tibia! +1 coordenação, +1 criatividade, -1 energia, +1 XP."
        elif activity == "Dormir":
            person._energy = min(person._energy + 4, 10)
            return "Dormiu como um anjo! +4 energia."
        return "Atividade não reconhecida."


class Adult(LifeStage):
    name = "Adulto"
    age_range = (18, 59)
    xp_goal = 4
    
    def activities(self) -> List[str]:
        # Adulto:
        return ["Trabalhar", "Estudar", "Sair com os amigos", "Exercício físico", "Dormir"]
    
    def perform_activity(self, person: "Person", activity: str) -> str:
        if activity == "Trabalhar":
            person._skills["carreira"] += 2
            person._energy -= 2
            person._xp += 1
            return "Trabalhou! +2 carreira, -2 energia, +1 XP."
        elif activity == "Estudar":
            person._skills["conhecimento"] += 2
            person._energy -= 2
            person._xp += 1
            return "Estudou (engenharia nao é facil)! +2 conhecimento, -2 energia, +1 XP."
        elif activity == "Sair com os amigos":
            person._skills["bem-estar"] += 2
            person._skills["criatividade"] += 1
            person._energy -= 1
            person._xp += 1
            return "Saiu com os amigos! +2 bem-estar, +1 criatividade, -1 energia, +1 XP."
        elif activity == "Correr":
            person._skills["saúde"] += 2
            person._energy -= 1
            person._xp += 1
            return "Fez exercício! +2 saúde, -1 energia, +1 XP."
        elif activity == "Dormir":
            person._energy = min(person._energy + 4, 10)
            return "Sono reparador! +4 energia."
        return "Atividade não reconhecida."


class Veio(LifeStage):
    name = "Véio"
    age_range = (60, None)
    xp_goal = 3
    
    def activities(self) -> List[str]:
        # Véio: PREVISÃO DO FUTURO
        return ["Jogar Videogame", "Sair com os amigos", "Exercício físico", "Dormir"]
    
    def perform_activity(self, person: "Person", activity: str) -> str:
        if activity == "Jogar Videogame":
            person._skills["coordenação"] += 1
            person._skills["criatividade"] += 1
            person._energy -= 1
            person._xp += 1
            return "Jogou videogame! +1 coordenação, +1 criatividade, -1 energia, +1 XP."
        elif activity == "Sair com os amigos":
            person._skills["bem-estar"] += 2
            person._energy -= 1
            person._xp += 1
            return "Saiu com os amigos! +2 bem-estar, -1 energia, +1 XP."
        elif activity == "Exercício físico":
            person._skills["saúde"] += 2
            person._energy -= 1
            person._xp += 1
            return "Fez exercício! +2 saúde, -1 energia, +1 XP."
        elif activity == "Dormir":
            person._energy = min(person._energy + 4, 10)
            return "Tirou um cochilo ótimo! +4 energia."
        return "Atividade não reconhecida."


class StageFactory:
    stages: List[LifeStage] = [Baby(), Child(), Teen(), Adult(), Veio()]
    
    @classmethod
    def for_age(cls, age: int) -> LifeStage:
        for s in cls.stages:
            if s.in_range(age):
                return s
        return cls.stages[-1]
    
    @classmethod
    def next_stage_min_age(cls, age: int) -> Optional[int]:
        for i, s in enumerate(cls.stages):
            if s.in_range(age):
                if i + 1 < len(cls.stages):
                    nxt = cls.stages[i + 1]
                    return nxt.age_range[0]
                return None
        return None


@dataclass
class Person:
    name: str
    age: int = 0
    _energy: int = 10
    _xp: int = 0
    _skills: Dict[str, int] = field(default_factory=lambda: {
        "coordenação": 0, "linguagem": 0, "conhecimento": 0, "criatividade": 0,
        "saúde": 0, "carreira": 0, "bem-estar": 0, "propósito": 0
    })
    history: List[str] = field(default_factory=list)
    _destroyed: bool = False
    
    @property
    def energy(self) -> int:
        return self._energy
    
    @property
    def xp(self) -> int:
        return self._xp
    
    @property
    def skills(self) -> Dict[str, int]:
        return dict(self._skills)
    
    @property
    def stage(self) -> LifeStage:
        return StageFactory.for_age(self.age)
    
    def summary(self) -> str:
        key_skills = ", ".join([f"{k}: {v}" for k, v in self._skills.items() if v > 0]) or "nenhuma ainda"
        return (f"Nome: {self.name} | Idade: {self.age} ({self.stage.name}) | "
                f"Energia: {self._energy}/10 | XP: {self._xp}/{self.stage.xp_goal} | "
                f"Habilidades: {key_skills}")
    
    def perform(self, activity: str) -> str:
        if self._destroyed:
            return "Projeto de vida acabou. Jogo encerrado."
        if self._energy <= 0 and activity != "Dormir":
            return "Sem energia! Escolha 'Dormir' para se recuperar."
        msg = self.stage.perform_activity(self, activity)
        self.history.append(f"[{self.stage.name}] {activity}: {msg}")
        return msg
    
    def can_level_up(self) -> bool:
        return self._xp >= self.stage.xp_goal
    
    def level_up(self) -> str:
        if not self.can_level_up():
            return f"Você ainda não tem XP suficiente ({self._xp}/{self.stage.xp_goal})."
        next_min = StageFactory.next_stage_min_age(self.age)
        if next_min is None:
            self.age += 1
            self._xp = 0
            return f"Você ganhou experiência e envelheceu mais um ano como {self.stage.name}!"
        else:
            self.age = next_min
            self._xp = 0
            return f"Parabéns! Você avançou para o estágio '{self.stage.name}' (idade {self.age}+)."
    
    def destroy(self) -> str:
        self._destroyed = True
        return "Projeto de Vida concluido."



def ask_int(prompt: str, min_val: int, max_val: int) -> int:
    while True:
        raw = input(prompt).strip()
        if raw.isdigit():
            val = int(raw)
            if min_val <= val <= max_val:
                return val
        print(f"Por favor, digite um número entre {min_val} e {max_val}.")


def main() -> None:
    print("=== projeto de vida ===")
    print("a minha vida está funcionando? -> Sim")

    
    p = Person("Bernardo Couto Pereira", age=0)
    print("\n 19/09/1994 Nasceu um nova Pessoa ")
    print(p.summary())
    
    while True:
        stage = p.stage
        acts = stage.activities()
        options = acts + ["Subir de nível", "Ver resumo", "Sair"]
        
        print("\n--- Sua situação ---")
        print(p.summary())
        print("\nAtividades disponíveis nesta fase:", ", ".join(acts))
        print("Escolha uma opção:")
        for i, opt in enumerate(options, start=1):
            print(f"{i}) {opt}")
        
        choice = ask_int("> ", 1, len(options))
        selected = options[choice - 1]
        
        if selected == "Subir de nível":
            msg = p.level_up()
            print(msg)
        elif selected == "Ver resumo":
            print("\n==== HISTÓRICO ====")
            for h in p.history[-15:]:
                print("-", h)
            print("===================")
        elif selected == "Sair":
            print(p.destroy())
            print("\n=== RESUMO FINAL ===")
            print(p.summary())
            print("\nÚltimos eventos:")
            for h in p.history[-10:]:
                print("-", h)
            print("\nAté a próxima!")
            break
        else:
            msg = p.perform(selected)
            print(msg)
        
        p._energy = max(0, min(p._energy, 10))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário.")
        sys.exit(0)
