Feature: Gender division 
As a usu�rio 
I want to poder escolher um g�nero de filme/s�rie 
So that eu consigo escolher qual irei assistir entre os filmes/s�ries desse g�nero 
Scenario: 
Escolher o g�nero a��o  
Given eu estou logado na como um "usu�rio comum" com login "cpv@email.com" senha "cainho123" e com o perfil "Caio" 
And eu estou na se��o "g�neros" 
And eu vejo os "g�neros": "a��o", "fic��o cient�fica", "com�dia", "romance" e "suspense" 
When eu escolho "g�nero" "a��o" 
Then eu estou na p�gina do g�nero "a��o" 
ECHO est� ativado.
Scenario: Assistir um filme/s�rie do g�nero a��o 
Given eu estou logado na como um "usu�rio comum" com login "cpv@email.com" senha "cainho123" e com o perfil "Caio" 
And existe um "filme" cadastrado com o nome "O resgate" e do g�nero "a��o" 
And existe um "s�rie" cadastrado com o nome "Narcos" e do g�nero "a��o" 
And eu estou na se��o "g�neros" 
When eu escolho a op��o "a��o" 
Then eu entro numa p�gina que cont�m o filme "O resgate" e a s�rie "Narcos" do g�nero "a��o" 
