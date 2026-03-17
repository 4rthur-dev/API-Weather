import requests
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QMessageBox, QFrame
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp, Qt

#Chave API
key = "c25e540d267a62ee02839cc1303db0a5"

#Função do clima
def weather():
	cidade =  boxPesq.text().strip()

	#URL da API
	url = "https://api.openweathermap.org/data/2.5/weather"         

	#Parametros da API
	params = {"q": cidade,             
			"appid": key,  
			"units": "metric",             
			"lang": "pt_br"}
	        
	try:            
		resposta = requests.get(url, params=params)      
		dados = resposta.json()   

		if resposta.status_code == 200: 

			temperatura_atual = dados ['main']['temp']
			temperatura_min = dados ['main']['temp_min']
			temperatura_max = dados ['main']['temp_max']
			descricao = dados ['weather'][0]['description']
			umidade = dados ['main']['humidity']
			vento = dados ['wind']['speed']

			#Resultado das informações do clima
			atual.setText("   {:.0f}°C".format(temperatura_atual))
			atual.move(190, 250)
			min.setText("{:.0f}°C".format(temperatura_min))
			max.setText("{:.0f}°C".format(temperatura_max))
			descri.setText("{}".format(descricao))
			umi.setText("{}% 💧".format(umidade))
			txtwind.setText("{} m/s".format(vento))


		else:
			QMessageBox.critical(tela, "Atenção", "Digite o nome de uma cidade!")
			boxPesq.clear()		
			  
	except Exception as e:
		QMessageBox.critical(tela, "Erro", "Erro ao obter o clima: {}".format(e))


#Limpa o texto preenchido
def limpaCampos():

	#Erro se não estiver nada dentro do campo
	if boxPesq.text() == '':
		QMessageBox.critical(tela, "Atenção", "Nenhum texto inserido a ser limpo")
	#Limpa o campo
	else:
		boxPesq.clear()
		atual.setText("  --°C")
		temp_min.setText("Mínima:")
		temp_max.setText("Máxima:")
		max.setText("  --°C")
		min.setText("  --°C")
		umi.setText("  --% 💧")
		descri.setText("...")
		txtwind.setText("--m/s      ")
		boxPesq.setFocus()

#------------------------------------------------------------------------------------------------


#=====================================================================
#                          FRONT-END 
#=====================================================================

#Criando aplicação
app =QApplication(sys.argv)

#Janela principal
tela = QWidget()
tela.setObjectName('tela')
tela.setWindowTitle('⛅')
tela.setGeometry(700, 300, 550, 500)

#Personalizando a tela (QSS)
tela.setStyleSheet("""

#tela {
	background-color:  #F0FFFF;
	border: 1px solid 	#B0E0E6;
	padding: 14px;
	border-radius: 12px;
    }				   
				   

#previsao {
    color: 	#1E90FF;
    font-size: 26px;
    font-weight: bold;
    }

#Pesquisar {
	border-radius: 10px;
	padding: 10px;
	border: 2px solid black;
	}
				   
#Buscar {
	border-radius: 10px;
	padding: 12px;
	background-color:		#1E90FF;
	color: white;	   
	}
				   
#Buscar:hover {
	border: 2px solid 		#1E90FF;
	background-color: white;
	color: black;			   
   }
				   
#Limpar {
	border-radius: 10px;
	padding: 12px;
		   
	}
				   
#Limpar:hover {

	background-color: 	#E6E6FA;			   
	}
				   
#Temp {
	font-size: 14px;
	font-weight: bold;			   
    }
				   
#card {
	background-color: transparent;
	border: 2px solid #E2E8F0;
	border-radius: 16px;	   
	}
"""
)
#--------------------------------------------------------------------------

# ---- Label ----
txt = QLabel('Previsão do Tempo 🌤', tela)
txt.setObjectName('previsao')
txt.move(140, 20)

#Temperatura atual
temp = QLabel('Temperatura: ', tela)
temp.setObjectName('Temp')
temp.move(200, 200)
temp.setStyleSheet("font-size: 14px; font-weight: bold; color: #64748B;")
temp.setAlignment(Qt.AlignCenter)

atual = QLabel("     --°C", tela)
atual.move(180, 250)
atual.setStyleSheet("font-size: 30px; font-weight: bold; color: #1E90FF; ")
atual.setAlignment(Qt.AlignCenter)

#Temperatura minima
temp_min = QLabel('Mínima: ' ,tela)
temp_min.move(60, 330)
temp_min.setStyleSheet("font-size: 12px; font-weight: bold;")
min = QLabel("  --°C", tela)
min.setStyleSheet("font-size: 18px; font-weight: bold;")
min.move(60, 350)

#Temperatura maxima
temp_max = QLabel('Máxima:', tela)
temp_max.move(180, 330)
temp_max.setStyleSheet("font-size: 12px; font-weight: bold;")
max = QLabel("  --°C", tela)
max.setStyleSheet("font-size: 18px; font-weight: bold;")
max.move(180, 350)

#Descrição
description = QLabel('Descrição Climatica:', tela)
description.move(60, 410)
description.setStyleSheet("font-size: 12px; font-weight: bold;")
descri = QLabel("                                                ", tela)
descri.setStyleSheet("font-size: 18px; font-weight: bold;")
descri.move(60, 430)

#Umidade
umid = QLabel('Umidade:', tela)
umid.move(290, 330)
umid.setStyleSheet("font-size: 12px; font-weight: bold;")
umi = QLabel("  --% 💧", tela)
umi.setStyleSheet("font-size: 18px; font-weight: bold;")
umi.move(290, 350)

#Vento
wind = QLabel('Vento:', tela)
wind.move(410, 330)
wind.setStyleSheet("font-size: 12px; font-weight:bold;")
txtwind = QLabel("--m/s      ", tela)
txtwind.setStyleSheet("font-size: 18px; font-weight: bold;")
txtwind.move(410,350 )

# --- ELEMENTOS DE BUSCA ---
boxPesq = QLineEdit(tela)
boxPesq.setObjectName('Pesquisar')
boxPesq.move(50, 80)
boxPesq.setFixedWidth(390)
boxPesq.setPlaceholderText('🔎 Buscar cidade')
reg_ex = QRegExp("[^0-9]*")
validator = QRegExpValidator(reg_ex)
boxPesq.setValidator(validator) #impede de digitar numeros

#QFrame 
card = QFrame(tela)
card.setObjectName("card")
card.setGeometry(30, 190, 490, 300)


#-------------------------------------------------------------------------
#Criando botao
#Buscar
btnBusc = QPushButton("Ver Clima", tela)
btnBusc.setObjectName('Buscar')
btnBusc.move(240, 125)
btnBusc.setFixedWidth(200)

#Limpar
btnLimpar = QPushButton("Limpar", tela)
btnLimpar.setObjectName('Limpar')
btnLimpar.move(50, 125)
btnLimpar.setFixedWidth(140)

#Conectando o botao a função (buscar)
btnBusc.clicked.connect(weather)

#Conectando o botao a função (limpar)
btnLimpar.clicked.connect(limpaCampos)

#Exixibindo a janela
tela.show()

#Loop infinito
sys.exit(app.exec_())