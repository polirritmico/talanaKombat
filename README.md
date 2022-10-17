Talana Kombat JRPG
==================

## Descripción

Juego donde 2 personajes se enfrentan. Cada personaje tiene 2 golpes especiales
que se ejecutan con una combinación de movimientos + 1 botón de golpe.


### Controles

| Tecla | Función     |
|-------|-------------|
| `W`   | Arriba ↑    |
| `S`   | Abajo ↓     |
| `A`   | Izquierda ← |
| `D`   | Derecha →   |
| `P`   | Puño        |
| `K`   | Patada      |


### Golpes de personajes

**Tonyn Stallone**

| Combination | Power | Name          |
|-------------|-------|---------------|
| `DSD` + `P` | 3     | Taladoken     |
| `SD` + `K`  | 2     | Remeyuken     |
| `P` o `K`   | 1     | Puño o Patada |

**Arnaldor Shuatseneguer**

| Combination | Power | Name          |
|-------------|-------|---------------|
| `SA` + `K`  | 3     | Remuyuken     |
| `ASA` + `P` | 2     | Taladoken     |
| `P` o `K`   | 1     | Puño o Patada |

-------------------------------------------------------------------------------

## Instrucciones

> Desarrollar una solución que relata la pelea e informe el resultado final

### Especificaciones

- [x] Comienza atacando el jugador que envió una combinación menor de botones
  (movimiento más botones). En caso de empate:
    - [x] Parte el con menos movimientos
    - [x] El con menos golpes
    - [x] Inicia J1
- [x] Toda la secuencia de un jugador viene completa en un json
- [x] Cada personaje tiene 6 puntos de energía
- [x] Un personaje muere cuando su energía es 0 y termina la pelea
      inmediatamente
- [x] Tony, el player 1, siempre ataca hacia la derecha (no cambia de lado)
- [x] Arnaldor, el player 2, siempre ataca hacia la izquierda (no cambia de
      lado)
- [x] Los personajes atacan 1 a la vez estilo JRPG por turnos hasta que uno es
      derrotado.
- [x] Los golpes no pueden ser bloqueados, siempre son efectivos
- [x] Los datos llegan como un json con botones de movimiento y golpe que se
      correlacionan para cada jugada
- [x] Los movimientos pueden ser un string de largo máx 5 (puede ser vacío)
- [x] Los golpes pueden ser un solo botón máx (puede ser vacío)
- [x] Se asume que el botón de golpe es justo después de la secuencia de
      movimiento. Por ejemplo, `AADSD` + `P` es un _Taladoken_ (antes se movió
      a la izquierda 2 veces). `DSDAA` + `P` son movimientos más puño.

### Ejemplos

Por ejemplo, teniendo el siguiente json de pelea:

```json
{"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},"player2":
{"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}}
```
- _Tonyn avanza y da una patada_
- _Arnaldor conecta un Remuyuken_
- _Tonyn usa un Taladoken_
- _Arnaldor se mueve_
- _Tonyn le da un puñetazo al pobre Arnaldor_
- _Arnaldor conecta un Remuyuken_
- _Arnardold Gana la pelea y aun le queda 1 de energía_

### Inputs

```json
{"player1":{"movimientos":[“SDD”, “DSD”, “SA”, “DSD”] ,"golpes":[“K”, “P”, “K”, “P”]}, "player2":
{"movimientos":[“DSD”, “WSAW”, “ASA”, “”, “ASA”, “SA”],"golpes":[“P”, “K”, “K”, “K”, “P”, “k”]}}
```
> GANA TONYN

```json
{"player1":{"movimientos":[“DSD”, “S”] ,"golpes":[ “P”, “”]},
"player2":{"movimientos":[“”, “ASA”, “DA”, “AAA”, “”, “SA”],"golpes":[“P”, “”, “P”, “K”, “K”, “K”]}}
```
> Gana Arnaldor

-------------------------------------------------------------------------------

## Preguntas generales

1. Supongamos que en un repositorio GIT hiciste un commit y olvidaste un
   archivo. Explica cómo se soluciona si hiciste push, y cómo si aún no
   hiciste. De ser posible que quede solo un commit con los cambios.
2. Si has trabajado con control de versiones ¿Cuáles han sido los flujos con
   los que has trabajado?
3. ¿Cuál ha sido la situación más compleja que has tenido con esto?
4. ¿Qué experiencia has tenido con los microservicios?
5. ¿Cuál es tu servicio favorito de GCP o AWS? ¿Por qué?

