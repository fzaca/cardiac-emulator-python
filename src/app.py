''' Cardiac App '''

# modules
from cardiac import Cardiac
from flet import (
    flet,
    app,
    Page, 
    Container, 
    Row, 
    Column, 
    TextField,
    UserControl    
)

# Main Class
class CardiacApp(UserControl):

    # Main container
    def main_container(self):
        self.main = Container(
            width=1000,
            height=700,
            bgcolor='black',
            padding=8
        )

        # Main row
        self.main_row = Row()

        # Right and left containers
        self.left_container = Container(
            height=self.main.height,
            expand=3,
            bgcolor='blue',
        )

        self.right_container = Container(
            height=self.main.height,
            expand=1,
            bgcolor='red',
        )

        # Right and left containers display
        self.left_col = Column(spacing=0)
        self.right_col = Column(spacing=0)

        # Memory Container
        self.memory_container = Container(
            width=self.left_container.width,
            expand=2,
            bgcolor='green',
        )

        # Controls Container
        self.controls_container = Container(
            width=self.left_container.width,
            expand=3,
            bgcolor='white',
        )

        #
        self.left_col.controls.append(self.memory_container) # or use extend
        self.left_col.controls.append(self.controls_container) 

        self.left_container.content = self.left_col
         
        #
        self.main_row.controls.append(self.left_container) # or use extend
        self.main_row.controls.append(self.right_container)

        # 
        self.main.content = self.main_row 

        return self.main

    def build(self):
        return Column(
            controls=[
                self.main_container(),
            ]
        )

def main(page: Page):
    page.title = "Cardiac"
    page.window_width = 1000
    page.window_height = 700
    page.padding = 0

    app = CardiacApp()
    page.add(app)

    page.update()

flet.app(target=main)