# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
import sys


class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("Rock Paper Scissors Lizard Spock")

		# setting geometry
		self.setGeometry(200, 200, 640, 800)
		self.setStyleSheet(
			"border : 0px solid black; background : white;")

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

	# method for components
	def UiComponents(self):

		# counter variable
		self.counter = -1

		# choice variable
		self.choice = 0

		# creating head label
		head = QLabel("Rock Paper Scissors Lizard Spock", self)

		# setting geometry to the head
		head.setGeometry(40, 20, 560, 120)

		# font
		font = QFont('Calibri', 15)
		font.setBold(True)
		font.setItalic(False)
		font.setUnderline(False)

		# setting font to the head
		head.setFont(font)

		# setting alignment of the head
		head.setAlignment(Qt.AlignCenter)

		# setting color effect to the head
		color = QGraphicsColorizeEffect(self)
		color.setColor(Qt.black)
		head.setGraphicsEffect(color)

		# creating a vs label
		self.vs = QLabel("vs", self)

		# setting geometry
		self.vs.setGeometry(300, 160, 30, 50)

		# setting font
		font.setUnderline(False)
		font.setItalic(False)
		self.vs.setFont(font)

		# creating your choice label
		self.user = QLabel("", self)

		# setting geometry
		self.user.setGeometry(180, 150, 70, 70)
		self.user.setStyleSheet(
			"border : 2px solid black; background : white;")

		# setting alignment
		self.user.setAlignment(Qt.AlignCenter)

		# creating computer choice label
		self.computer = QLabel("", self)

		# setting geometry
		self.computer.setGeometry(360, 150, 70, 70)
		self.computer.setStyleSheet(
			"border : 2px solid black; background : white;")

		# setting alignment
		self.computer.setAlignment(Qt.AlignCenter)
		self.user.setStyleSheet("border-image : url(assets/profile.png);")
		self.computer.setStyleSheet("border-image : url(assets/bot.png);")

		# result label
		self.result = QLabel(self)

		# setting geometry to the result
		self.result.setGeometry(180, 295, 270, 50)

		# setting font
		self.result.setFont(QFont('Calibri', 14))

		# setting alignment
		self.result.setAlignment(Qt.AlignCenter)

		# setting border and color
		self.result.setStyleSheet(
			"border : 2px solid black; background : white;")

		# creating five push button
		# for rock paper scissors lizard and spock
		self.rock = QPushButton("Rock", self)
		self.rock.setGeometry(90, 390, 80, 80)
		self.rock.setStyleSheet("background-image : url(rock.png);")
		self.rock.setStyleSheet(
			"border : 1px solid black; background : white;")
	
		self.paper = QPushButton("Paper", self)
		self.paper.setGeometry(180, 390, 80, 80)
		self.paper.setStyleSheet(
			"border : 1px solid black; background : white;")
		
		self.scissors = QPushButton("Scissors", self)
		self.scissors.setGeometry(270, 390, 80, 80)
		self.scissors.setStyleSheet(
			"border : 1px solid black; background : white;")
	
		self.lizard = QPushButton("Lizard", self)
		self.lizard.setGeometry(360, 390, 80, 80)
		self.lizard.setStyleSheet(
			"border : 1px solid black; background : white;")
	
		self.spock = QPushButton("Spock", self)
		self.spock.setGeometry(450, 390, 80, 80)
		self.spock.setStyleSheet(
			"border : 1px solid black; background : white;")
		



		# adding actions to the buttons
		self.rock.clicked.connect(self.rock_action)
		self.paper.clicked.connect(self.paper_action)
		self.scissors.clicked.connect(self.scissors_action)
		self.lizard.clicked.connect(self.lizard_action)
		self.spock.clicked.connect(self.spock_action)
		

		# creating push button to reset all the game
		game_reset = QPushButton("Reset", self)

		# setting geometry
		game_reset.setGeometry(250, 500, 120, 50)

		game_reset.setFont(QFont('Calibri', 14))

		# setting color effect
		color = QGraphicsColorizeEffect(self)
		color.setColor(Qt.red)
		game_reset.setGraphicsEffect(color)

		# adding action to the reset button
		game_reset.clicked.connect(self.reset_action)

		# creating a timer object
		timer = QTimer(self)

		# adding action to the timer
		timer.timeout.connect(self.showTime)

		# starting the timer
		timer.start(1000)

	def showTime(self):

		# if counter value is - 1
		if self.counter == -1:
			pass

		# if counter is not - 1
		else:

			# setting counter value to the label
			self.computer.setText(str(self.counter))
			

			if self.counter == 0:
				self.user.setText("")
				self.comp_choice = random.randint(1, 5)

				# if computer choice is 1
				if self.comp_choice == 1:

					# setting rock image to the computer label
					self.computer.setStyleSheet(
						"border-image : url(assets/rock.png);")

				elif self.comp_choice == 2:
					# setting paper image to the computer label
					self.computer.setStyleSheet(
						"border-image : url(assets/paper.png);")
					
				elif self.comp_choice == 3:
					# setting scissors image to the computer label
					self.computer.setStyleSheet(
						"border-image : url(assets/scissors.png);")
					
				elif self.comp_choice == 4:
					# setting lizard image to the computer label
					self.computer.setStyleSheet(
						"border-image : url(assets/lizard.png);")

				elif self.comp_choice == 5:
					# setting spock image to the computer label
					self.computer.setStyleSheet(
						"border-image : url(assets/spock.png);")

				# checking who won the match
				self.who_won()

			# decrementing the counter value
			self.counter -= 1

	def rock_action(self):

		# making choice as 1
		self.choice = 1
		self.user.setText("")

		# setting rock image to the user label
		self.user.setStyleSheet("border-image : url(assets/rock.png);")

		# making counter value to 3
		self.counter = 3

		# disabling the push button
		self.rock.setDisabled(True)
		self.paper.setDisabled(True)
		self.scissors.setDisabled(True)
		self.lizard.setDisabled(True)
		self.spock.setDisabled(True)

	def paper_action(self):

		# making choice as 2
		self.choice = 2
		self.user.setText("")

		# setting rock image to the user label
		self.user.setStyleSheet("border-image : url(assets/paper.png);")

		# making counter value to 3
		self.counter = 3

		# disabling the push button
		self.rock.setDisabled(True)
		self.paper.setDisabled(True)
		self.scissors.setDisabled(True)
		self.lizard.setDisabled(True)
		self.spock.setDisabled(True)

	def scissors_action(self):

		# making choice as 3
		self.choice = 3
		self.user.setText("")

		# setting rock image to the user label
		self.user.setStyleSheet("border-image : url(assets/scissors.png);")

		# making counter value to 3
		self.counter = 3

		# disabling the push button
		self.rock.setDisabled(True)
		self.paper.setDisabled(True)
		self.scissors.setDisabled(True)
		self.lizard.setDisabled(True)
		self.spock.setDisabled(True)
	def lizard_action(self):

		# making choice as 4
		self.choice = 4
		self.user.setText("")

		# setting rock image to the user label
		self.user.setStyleSheet("border-image : url(assets/lizard.png);")

		# making counter value to 3
		self.counter = 3

		# disabling the push button
		self.rock.setDisabled(True)
		self.paper.setDisabled(True)
		self.scissors.setDisabled(True)
		self.lizard.setDisabled(True)
		self.spock.setDisabled(True)
	def spock_action(self):

		# making choice as 5
		self.choice = 5
		self.user.setText("")

		# setting rock image to the user label
		self.user.setStyleSheet("border-image : url(assets/spock.png);")

		# making counter value to 3
		self.counter = 3

		# disabling the push button
		self.rock.setDisabled(True)
		self.paper.setDisabled(True)
		self.scissors.setDisabled(True)
		self.lizard.setDisabled(True)
		self.spock.setDisabled(True)
	
		
    



	def reset_action(self):

		# making result label empty
		self.result.setText("")
		self.computer.setText("")

		# resting the counter value
		self.counter = -1

		# enabling the push buttons
		self.rock.setEnabled(True)
		self.paper.setEnabled(True)
		self.scissors.setEnabled(True)
		self.lizard.setEnabled(True)
		self.spock.setEnabled(True)

		# re-adding images to the user and computer label
		self.user.setStyleSheet("border-image : url(assets/profile.png);")
		self.computer.setStyleSheet("border-image : url(assets/bot.png);")

	def who_won(self):
		

		# if match is draw 
		rock,paper,scissors,lizard,spock="rock","paper","scissors","lizard","spock"
		choices={1:rock,2:paper,3:scissors,4:lizard,5:spock}
		self.computer.setText("")
		if self.choice == self.comp_choice:

			# setting text to the result label
			self.result.setText("Draw Match")

		else:
			# condition for winning
			# user choose rock
			if self.choice == 1:
				# computer choose paper and spock
				if self.comp_choice == 2 or self.comp_choice == 5:
					# setting text to the result
					self.result.setText("Computer Won")
				else:
					self.result.setText("You Won")

			# user chooses paper
			elif self.choice == 2:
				# computer choose scissors and lizard
				if self.comp_choice == 3 or self.comp_choice == 4:
					# setting text to the result
					self.result.setText("Computer Won")
				else:
					self.result.setText("You Won")

			# if user chooses scissor
			elif self.choice == 3:
				# computer choose rock amd spock
				if self.comp_choice == 1 or self.comp_choice == 5:
					# setting text to the result
					self.result.setText("Computer Won")
				else:
					self.result.setText("You Won")
			elif self.choice == 4:
				# computer choose rock and scissors
				if self.comp_choice == 1 or self.comp_choice == 3:
					# setting text to the result
					self.result.setText("Computer Won")
				else:
					self.result.setText("You Won")
			elif self.choice == 5:
				# computer choose rock and lizard
				if self.comp_choice == 2 or self.comp_choice == 4:
					# setting text to the result
					self.result.setText("Computer Won")
				else:
					self.result.setText("You Won")


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
