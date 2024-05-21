#Button Class to be called, whenever we use buttons, mainly in Main menu and every option
class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color): #initializes class by setting up objects of the class
		self.image = image #variable for the "image" object
		self.x_pos = pos[0] #variable for pos 0
		self.y_pos = pos[1] #variable for pos 1
		self.font = font #font variable of the button
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input #variable for text
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None: #if there is no object image
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos)) #gets position of the image rectangle
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos)) #gets the position of text on a rectangle

	def update(self, screen): #updates the button what it looks like
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position): #checks to see if you click on the button
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position): #checks for when to switch color of text
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)