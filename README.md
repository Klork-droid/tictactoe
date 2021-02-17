# Slapjack
> A game of one-player tic tac toe in your console.
![Menu](screenshots/menu.png)

### Game Rules
You must select one of the numbers in the table to put x
### Play the Game
![Gameplay](screenshots/gameplay.png)

##### Requirements
You must have 3.8+ to run the game.

##### Run the Game
Navigate to the directory in your console and then run:
```sh
$ python main.py -n "Кол-во строк" -k "Кол-во столбцов"
```
![Start](screenshots/start game.png)
Or
```sh
$ python main.py -l true
```
![Start](screenshots/load save.png)

##### Save the Game
Enter "save" when you are asked to enter x:
```sh
$ Куда поставить: X?
$ save
```
![Save](screenshots/save.png)
##### External Python Libraries Used
* `pickle`
* `argparse`
* `random`