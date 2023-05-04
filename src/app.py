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
    UserControl,
    Text,    
    MainAxisAlignment,
    CrossAxisAlignment,
    ElevatedButton,
    border,
    colors,
    ListView,
    padding,
)

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = (1000, 500)

# Main Class
class CardiacApp(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.cardiac = Cardiac()

    # Main container
    def main_container(self):
        self.main = Container(
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            padding=8
        )

        # Main row
        self.main_row = Row()

        # Right and left containers
        self.left_container = Container(
            height=self.main.height,
            expand=3,
        )

        self.right_container = Container(
            height=self.main.height,
            expand=1,
            border_radius=20,
            border=border.all(1, colors.GREY_600)
        )

        # Right and left containers display
        self.left_col = Column(spacing=10)
        self.right_row = Row(spacing=0)

        # Memory Container
        self.memory_container = Container(
            width=self.left_container.width,
            expand=3,
            padding=10,
            border_radius=20,
            border=border.all(1, colors.GREY_600)
        )

        def generate_memory():
            ''' This function generates the memory grids returning a list of textboxs'''
            rows = []
            self.cells = []
            
            for i in range(10):
                columns = []
                for j in range(10):
                    t = TextField(
                        width=45, height=24, 
                        text_size=12, 
                        content_padding=padding.symmetric(4, 10),
                        dense=True)
                    self.cells.append(t)
                    cell = Row([
                        Text(f'{i*10+j}'),
                        t
                    ], spacing=0)
                    columns.append(cell)
                row = Column(columns, spacing=1)
                rows.append(row)

            self.cells[0].disabled = True
            self.cells[99].disabled = True

            return rows

        self.memory_row = Row(generate_memory())

        # Controls Container
        self.interface_container = Container(
            width=self.left_container.width,
            expand=2,
            padding=8,
            border_radius=20,
            border=border.all(1, colors.GREY_600)
        )
        self.interface_col = Column()

        # Status Container and Row content
        self.status_container = Container(
            width=self.interface_container.width,
            expand=1,
        )

        #     items
        self.flag_text = Text(f'Flag: {self.cardiac.flag}', size=24)
        self.accumulator_text = Text(f'Accumulator: {self.cardiac.accumulator}', size=24)
        self.step_text = Text(f'Step: {self.cardiac.step}', size=24)

        self.status_row = Row(
            controls=[
                self.flag_text,
                self.accumulator_text,
                self.step_text,
            ],
            alignment=MainAxisAlignment.SPACE_AROUND,
            vertical_alignment=CrossAxisAlignment.START,
        )
        self.status_container.content = self.status_row

        # Medium container and Row content
        self.medium_container = Container(
            width=self.interface_container.width,
            expand=1,
        )


        self.target_textbox = TextField(
            label='Target',
            value=0, 
            width=80, 
            height=40,
            on_change=self.target_changed
        )

        self.medium_row = Row(
            controls=[
                self.target_textbox
            ],
            alignment=MainAxisAlignment.SPACE_AROUND,
            vertical_alignment=CrossAxisAlignment.CENTER,
        )
        self.medium_container.content = self.medium_row

        # Controls Container and Row content
        self.controls_container = Container(
            width=self.interface_container.width,
            expand=1,
        )

        #     items
        self.run_button = ElevatedButton('Run', on_click=self.run_clicked)
        self.step_button = ElevatedButton('Step', on_click=self.step_clicked)
        self.reset_button = ElevatedButton('Reset', on_click=self.reset_clicked)

        self.controls_row = Row(
            controls=[
                self.run_button,
                self.step_button,
                self.reset_button
            ],
            alignment=MainAxisAlignment.SPACE_EVENLY,
            vertical_alignment=CrossAxisAlignment.CENTER,
        )

        self.controls_container.content = self.controls_row

        # Input and output Containers
        self.input_container = Container(
            expand=1,
            padding=10,
        )
        self.output_container = Container(
            expand=1,
            padding=10,        
        )

        #    Elements input col
        self.input_lv = ListView(
            expand=1, spacing=10, item_extent=50, padding=10, auto_scroll=True
        )
        self.input_lv_bg = Container(
            expand=True,
            bgcolor='blue',
            content=self.input_lv,
            border_radius=20,
        )
        self.add_input_textbox = TextField(
            height=40,
            border_radius=20,
            content_padding=padding.symmetric(1, 10),
            hint_text='Number',            
        )
        self.add_input_button = ElevatedButton(
            'Add', width=100, on_click=self.add_input_clicked
        )

        #    Elements output col
        self.output_lv = ListView(
            expand=1, spacing=10, item_extent=50, padding=10, auto_scroll=True
        )
        self.output_lv_bg = Container(
            expand=True,
            bgcolor='blue',
            content=self.output_lv,
            border_radius=20,
        )
        self.clear_output_button = ElevatedButton(
            'Clear', width=100, on_click=self.clear_output_clicked
        )

        #    Input and output cols
        self.input_col = Column([
            self.input_lv_bg, self.add_input_textbox, self.add_input_button
        ])
        self.output_col = Column([self.output_lv_bg, self.clear_output_button])

        self.input_container.content = self.input_col
        self.output_container.content = self.output_col

        #
        self.interface_col.controls.append(self.status_container) # or use extend
        self.interface_col.controls.append(self.medium_container)
        self.interface_col.controls.append(self.controls_container)
        
        self.interface_container.content = self.interface_col

        #
        self.memory_container.content = self.memory_row

        #
        self.right_row.controls.append(self.input_container)
        self.right_row.controls.append(self.output_container)

        self.right_container.content = self.right_row

        #
        self.left_col.controls.append(self.memory_container) # or use extend
        self.left_col.controls.append(self.interface_container) 

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

    def update_all(self):
        # Flag text
        value = '+' if self.cardiac.flag else '-'
        self.flag_text.value = f'Flag: {value}'
        self.flag_text.update()
        # step text
        self.step_text.value = f'Step: {self.cardiac.step}'
        self.step_text.update()
        # target textbox
        self.target_textbox.value = self.cardiac.target
        self.target_textbox.update()
        # Accumulator
        self.accumulator_text.value = f'Accumulator: {self.cardiac.accumulator}'
        self.accumulator_text.update()
        # Memory
        self.update_memory()
        # Output card-deck
        self.output_lv.controls = []
        for num in self.cardiac.output_card:
            self.output_lv.controls.append(Text(str(num).zfill(3)))
        self.output_lv.update()
        # Input card-deck
        self.input_lv.controls = []
        for num in self.cardiac.input_card:
            self.input_lv.controls.append(Text(str(num).zfill(3)))
        self.input_lv.update()

    def update_memory(self):
        for i, cell in enumerate(self.cells):
            # Update cell target
            if i == self.cardiac.target:
                cell.bgcolor = 'blue'
            else:
                cell.bgcolor = 'none'

            # Update cell value
            if self.cardiac.memory[i]:
                cell.value = str(self.cardiac.memory[i]).zfill(3)

            if cell.value:
                if self.cardiac.memory[i] != int(cell.value):
                    self.cardiac.memory[i] = int(cell.value)

            cell.update()

    def step_clicked(self, e):
        self.update_memory() # Fix
        self.cardiac.step_program()
        print(self.cardiac)
        self.update_all()

    def run_clicked(self, e):
        self.cardiac.run_program()
        self.update_all()

    def reset_clicked(self, e):
        self.cardiac.target = 0
        self.cardiac.step = 0
        self.cardiac.flag = True
        self.update_all()

    def target_changed(self, e):
        try:
            self.cardiac.target = int(e.control.value)
            self.update_all()
        except:
            return

    def clear_output_clicked(self, e):
        self.cardiac.output_card = []
        self.update_all()

    def add_input_clicked(self, e):
        value = self.add_input_textbox.value
    
        if 0 < len(value) <= 3:
            try:
                value = int(value)
                self.cardiac.input_card.append(value)
            except:
                pass
        self.add_input_textbox.value = None

        self.add_input_textbox.update()
        self.update_all()
                
def main(page: Page):
    page.title = "Cardiac"
    page.window_width = SCREEN_WIDTH
    page.window_height = SCREEN_HEIGHT
    page.padding = 0

    app = CardiacApp(page)
    page.add(app)
    app.update_memory()

    page.update()

flet.app(target=main)