from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class ImcApp(App):
  def build(self):
    self.window = GridLayout()
    self.window.cols = 1
    self.window.size_hint = (1, 0.9)
    self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}
    # image widget
    self.window.add_widget(Image(source="logo.png"))
            
    # label widget
    self.alt = Label(
      text= "SUA ALTURA EM METROS",
      font_size= 80,
      color= '#00FFCE'
      )
    self.window.add_widget(self.alt)
            
    # text input widget
    self.altura = TextInput(
      multiline= False,
      padding_y= (1,1),
      size_hint= (1, 0.2),
      input_type= 'number',
      input_filter= 'float'
      )
            
    self.window.add_widget(self.altura)
            
    self.pes = Label(
      text= "SEU PESO EM KG",
      font_size= 80,
      color= '#00FFCE'
      )
    self.window.add_widget(self.pes)
            
    self.peso = TextInput(
      multiline= False,
      padding_y= (1,1),
      size_hint= (0.1,0.2),
      input_type = 'number',
      input_filter= 'int'
      )
    self.window.add_widget(self.peso)
    
            
    # button widget
    self.button = Button(
      text= "CALCULAR IMC",
      size_hint= (1,0.3),
      bold= True,
      background_color ='#00FFCE'
      )
    self.button.bind(on_press=self.callback)
    self.window.add_widget(self.button)
            
    return self.window
            
  def callback(self, instance):
    p = int(self.peso.text)
    a = float(self.altura.text)
    imc = p / (a ** 2)
    rsp = ' '
    logo = "logo.png"
    if imc < 18.4:
        rsp = "MAGRO"
        logo = "magro.png"
    elif (imc >= 18.5) and (imc <= 24.9):
        rsp = "NORMAL"
        logo = "normal.png"
    elif (imc >= 25.0) and (imc <= 29.9):
        rsp = "SOBREPESO"
        logo = "sobrepeso.png"
    elif imc > 30.0:
        rsp = "OBESIDADE"
        logo = "obeso.png"
    elif imc > 40.0:
        rsp = "OBESIDADE GRAVE"
        logo = "grave.png"
    else:
        rsp = "SEM DEFINIÇÃO"
        logo = "logo.png"
    # change label text to "alt! and pes"
    self.alt.text = "CLASSIFICAÇÃO: " + rsp
    self.pes.text = "SEU IMC: " + "%1.5f" %(imc)
     # image widget
    self.window.add_widget(Image(source=logo))
            
# run IMCAPP App Calss
if __name__ == "__main__":
  ImcApp().run()
            
