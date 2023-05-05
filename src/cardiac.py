
class Cardiac:
    '''Emulator of the CARDIAC cardboard computer.'''

    def __init__(self):
        self.reset()
        self.output_card = []

    def run_program(self):
        '''Execute the program loaded into the emulator memory.'''        
        self.run = True
        while self.run:
            self.step_program()

    def step_program(self):
        if not (0 <= self.target <= 99):
            return

        instruction = self.memory[self.target]
        self.target += 1
        self.step += 1
        opcode = instruction // 100
        address = instruction % 100

        match opcode:

            case 0:
                if address:
                    value = self.input_card.pop() if self.input_card else 0
                    self.write_memory(address, value)

            case 1:
                self.accumulator = self.read_memory(address)

            case 2:
                self.accumulator += self.read_memory(address)

            case 3:
                if not self.flag:
                    self.target = address

            case 4:
                value = str(self.accumulator)
                x = address // 10
                y = address % 10

                value += '0' * x
                if len(value) > 3:
                    value = value[-3:]

                value = '0' * y + value
                if len(value) > 3:
                    value = value[:3]

                self.accumulator = int(value)

            case 5:
                self.output_card.append(self.read_memory(address))

            case 6:
                self.write_memory(address, self.accumulator)

            case 7:
                self.accumulator -= self.read_memory(address)

            case 8:
                if address != 99:
                    self.memory[99] = int('8' + str(self.target).zfill(2))
                if self.target-1 == 99:
                    self.memory[99] = 800
                self.target = address

            case 9:
                self.target = address # Temporal
                self.run = False

        if not self.target:
            self.run = False

        self.update_flag()

    def reset(self):
        self.flag = True
        self.accumulator = 0
        self.memory = [0] * 100
        self.memory[0] = 1
        self.memory[99] = 800
        self.step = 0
        self.target = 0
        self.input_card = []

    def read_memory(self, address):
        '''Reads a value from the emulator memory at a given address.'''
        if not (0 <= address <= 99):
            raise ValueError("Memory address out of range")
        return self.memory[address]

    def write_memory(self, address, value):
        '''Writes a value to the emulator memory at a given address.'''
        if not (0 <= address <= 99):
            raise ValueError("Memory address out of range")
        if not (0 <= value <= 999):
            raise ValueError("Value out of range")
        self.memory[address] = value

    def update_flag(self):
        if self.accumulator < 0:
            self.flag = False
        else:
            self.flag = True
